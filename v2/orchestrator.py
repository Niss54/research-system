"""
Nissh Research System v2 - Pipeline Orchestrator
================================================
Coordinates execution across all 7 agents with support for:
- 100% Autonomous Mode (Zero-click end-to-end execution)
- Human-in-the-Loop (HITL) Guided Mode (Pause & review checkpoints)
- Real-time logging & thread safety
"""

import threading
from typing import Dict, Any, Optional
from .state_manager import StateManager
from .engine import ResearchEngineV2

class PipelineOrchestrator:
    def __init__(self, state_mgr: Optional[StateManager] = None, keys: Optional[Dict[str, str]] = None):
        self.state_mgr = state_mgr or StateManager()
        self.engine = ResearchEngineV2(self.state_mgr, keys)
        self._threads = {}

    def start_pipeline(self, raw_idea: str, audience_hint: str = "", mode: str = "autonomous") -> str:
        """
        Initializes a new research session and begins background execution.
        Returns: project_id
        """
        project_id = self.state_mgr.create_project(raw_idea, audience_hint, mode=mode)
        self.state_mgr.add_log(project_id, f"🚀 Research run initialized in {mode.upper()} mode.", 1, "Orchestrator", "info")

        worker = threading.Thread(
            target=self._run_worker,
            args=(project_id, raw_idea, audience_hint, mode),
            daemon=True
        )
        self._threads[project_id] = worker
        worker.start()
        return project_id

    def _run_worker(self, project_id: str, raw_idea: str, audience_hint: str, mode: str):
        try:
            # Phase 1
            p1 = self.engine.run_agent_1(project_id, raw_idea, audience_hint)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=1, agent_name="Problem Validator")
                self.state_mgr.add_log(project_id, "⏸️ HITL checkpoint: Waiting for founder review of Phase 1.", 1, "Orchestrator", "info")
                return

            # Phase 2
            p2 = self.engine.run_agent_2(project_id, p1)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=2, agent_name="Landscape Hunter")
                return

            # Phase 3
            p3 = self.engine.run_agent_3(project_id, p2)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=3, agent_name="Competitor Forensic Auditor")
                return

            # Phase 4
            p4 = self.engine.run_agent_4(project_id, p1, p3)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=4, agent_name="Strategic Gap Analyst")
                return

            # Phase 5
            p5 = self.engine.run_agent_5(project_id, p4)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=5, agent_name="9-Platform Gap Verifier")
                return

            # Phase 6
            p6 = self.engine.run_agent_6(project_id, p1, p5)
            if mode == "hitl":
                self.state_mgr.update_project_status(project_id, "paused_hitl", current_agent=6, agent_name="Diligence Synthesizer")
                return

            # Phase 7
            p7 = self.engine.run_agent_7(project_id, p6)

        except Exception as e:
            self.state_mgr.update_project_status(project_id, "failed")
            self.state_mgr.add_log(project_id, f"❌ Execution error: {str(e)}", 0, "Orchestrator", "error")
