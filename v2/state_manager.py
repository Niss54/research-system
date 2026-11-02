"""
Nissh Research System v2 - State Manager & SQLite Persistence
=============================================================
Manages multi-run research sessions, phase outputs, event logs,
and Human-in-the-Loop (HITL) pause/resume checkpoints.
"""

import sqlite3
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

DB_PATH = Path(__file__).resolve().parent.parent / "research_system_v2.db"

class StateManager:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    raw_idea TEXT NOT NULL,
                    audience TEXT,
                    status TEXT NOT NULL, -- running, paused_hitl, completed, failed
                    current_agent INTEGER DEFAULT 1,
                    current_agent_name TEXT DEFAULT 'Idle',
                    execution_mode TEXT DEFAULT 'autonomous', -- autonomous, hitl
                    verdict TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS phase_data (
                    project_id TEXT NOT NULL,
                    phase_number INTEGER NOT NULL,
                    phase_name TEXT NOT NULL,
                    raw_markdown TEXT,
                    structured_json TEXT,
                    status TEXT NOT NULL, -- pending, completed, failed
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (project_id, phase_number),
                    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id TEXT NOT NULL,
                    agent_number INTEGER,
                    agent_name TEXT,
                    log_type TEXT, -- info, warning, error, fallback, tool
                    message TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
                )
            """)
            conn.commit()

    def create_project(self, raw_idea: str, audience: str = "", title: str = "", mode: str = "autonomous") -> str:
        project_id = f"proj_{uuid.uuid4().hex[:10]}"
        proj_title = title or (raw_idea[:50] + "..." if len(raw_idea) > 50 else raw_idea)
        with self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO projects (id, title, raw_idea, audience, status, execution_mode)
                VALUES (?, ?, ?, ?, 'running', ?)
                """,
                (project_id, proj_title, raw_idea, audience, mode)
            )
            # Initialize 7 phases
            phase_names = [
                "Problem Validator",
                "Landscape Hunter",
                "Competitor Forensic Auditor",
                "Strategic Gap Analyst",
                "9-Platform Gap Verifier",
                "Diligence Synthesizer",
                "Launch README Architect"
            ]
            for i, name in enumerate(phase_names, start=1):
                conn.execute(
                    """
                    INSERT INTO phase_data (project_id, phase_number, phase_name, status)
                    VALUES (?, ?, ?, 'pending')
                    """,
                    (project_id, i, name)
                )
            conn.commit()
        return project_id

    def update_project_status(self, project_id: str, status: str, current_agent: int = None, agent_name: str = None, verdict: str = None):
        with self._get_conn() as conn:
            updates = ["status = ?", "updated_at = CURRENT_TIMESTAMP"]
            params = [status]
            if current_agent is not None:
                updates.append("current_agent = ?")
                params.append(current_agent)
            if agent_name is not None:
                updates.append("current_agent_name = ?")
                params.append(agent_name)
            if verdict is not None:
                updates.append("verdict = ?")
                params.append(verdict)
            params.append(project_id)
            conn.execute(f"UPDATE projects SET {', '.join(updates)} WHERE id = ?", params)
            conn.commit()

    def save_phase_output(self, project_id: str, phase_number: int, markdown_text: str, structured_obj: Any = None):
        json_str = json.dumps(structured_obj if isinstance(structured_obj, dict) else (structured_obj.to_dict() if hasattr(structured_obj, "to_dict") else {}), ensure_ascii=False)
        with self._get_conn() as conn:
            conn.execute(
                """
                UPDATE phase_data
                SET raw_markdown = ?, structured_json = ?, status = 'completed', updated_at = CURRENT_TIMESTAMP
                WHERE project_id = ? AND phase_number = ?
                """,
                (markdown_text, json_str, project_id, phase_number)
            )
            conn.commit()

    def get_phase_output(self, project_id: str, phase_number: int) -> Optional[Dict[str, Any]]:
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM phase_data WHERE project_id = ? AND phase_number = ?",
                (project_id, phase_number)
            ).fetchone()
            if row:
                d = dict(row)
                if d.get("structured_json"):
                    try:
                        d["structured_data"] = json.loads(d["structured_json"])
                    except Exception:
                        d["structured_data"] = {}
                return d
            return None

    def add_log(self, project_id: str, message: str, agent_number: int = 0, agent_name: str = "", log_type: str = "info"):
        with self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO logs (project_id, agent_number, agent_name, log_type, message)
                VALUES (?, ?, ?, ?, ?)
                """,
                (project_id, agent_number, agent_name, log_type, message)
            )
            conn.commit()

    def get_project_state(self, project_id: str) -> Optional[Dict[str, Any]]:
        with self._get_conn() as conn:
            p_row = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
            if not p_row:
                return None
            project = dict(p_row)

            phases = {}
            for row in conn.execute("SELECT * FROM phase_data WHERE project_id = ? ORDER BY phase_number ASC", (project_id,)):
                pd = dict(row)
                if pd.get("structured_json"):
                    try:
                        pd["structured_data"] = json.loads(pd["structured_json"])
                    except Exception:
                        pd["structured_data"] = {}
                phases[str(pd["phase_number"])] = pd

            logs = []
            for row in conn.execute("SELECT * FROM logs WHERE project_id = ? ORDER BY id ASC", (project_id,)):
                logs.append(dict(row))

            project["phases"] = phases
            project["logs"] = logs
            return project

    def list_projects(self) -> List[Dict[str, Any]]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM projects ORDER BY created_at DESC").fetchall()
            return [dict(r) for r in rows]
