"""
Nissh Research System v2 - Evidence Vault & Provenance Ledger
=============================================================
Hyperresearch-inspired persistent evidence vault:
- Records structured claims with source provenance, dates, exact quotations, and verification tiers.
- Captures automated real-browser PNG screenshots using headless Chrome into evidence/screenshots/.
- Archives clean HTML text snapshots into evidence/snapshots/.
- Generates an auditable EVIDENCE_LEDGER.md for investors and founders.
"""

import os
import sys
import json
import subprocess
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EVIDENCE_DIR = REPO_ROOT / "evidence"
SCREENSHOTS_DIR = EVIDENCE_DIR / "screenshots"
SNAPSHOTS_DIR = EVIDENCE_DIR / "snapshots"
LEDGER_FILE = EVIDENCE_DIR / "ledger.json"

def find_browser():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "google-chrome",
        "chromium",
        "chrome"
    ]
    for b in candidates:
        if os.path.exists(b):
            return b
    return None

class EvidenceVault:
    def __init__(self, evidence_dir: Path = EVIDENCE_DIR):
        self.evidence_dir = evidence_dir
        self.screenshots_dir = evidence_dir / "screenshots"
        self.snapshots_dir = evidence_dir / "snapshots"
        self.ledger_file = evidence_dir / "ledger.json"
        self._init_dirs()
        self.ledger = self._load_ledger()
        self.browser_path = find_browser()

    def _init_dirs(self):
        self.evidence_dir.mkdir(parents=True, exist_ok=True)
        self.screenshots_dir.mkdir(parents=True, exist_ok=True)
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)

    def _load_ledger(self) -> List[Dict[str, Any]]:
        if self.ledger_file.exists():
            try:
                with open(self.ledger_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return []

    def _save_ledger(self):
        with open(self.ledger_file, "w", encoding="utf-8") as f:
            json.dump(self.ledger, f, indent=2, ensure_ascii=False)
        self._write_markdown_ledger()

    def record_evidence(
        self,
        claim: str,
        source_url: str,
        source_title: str = "",
        exact_passage: str = "",
        published_date: str = "Unknown",
        source_tier: str = "Secondary",  # Primary (official filing/press), Secondary (news/articles), Community (Reddit/G2)
        verification_status: str = "VERIFIED",  # VERIFIED, PARTIAL, UNVERIFIED, CONTRADICTED
        confidence: str = "High",  # High, Medium, Low
        limitation: str = "",
        capture_media: bool = True
    ) -> Dict[str, Any]:
        """
        Records an auditable evidence item, downloads page snapshot,
        and triggers a headless screenshot.
        """
        claim_hash = hashlib.md5(f"{source_url}{claim[:40]}".encode("utf-8")).hexdigest()[:8]
        timestamp = datetime.now().isoformat()
        
        screenshot_rel_path = ""
        snapshot_rel_path = ""

        if capture_media and source_url.startswith("http"):
            # 1. Capture HTML text snapshot
            snapshot_filename = f"snapshot_{claim_hash}.txt"
            snapshot_file = self.snapshots_dir / snapshot_filename
            try:
                res = requests.get(source_url, timeout=6, headers={"User-Agent": "Mozilla/5.0"})
                if res.status_code == 200:
                    snapshot_file.write_text(res.text[:15000], encoding="utf-8", errors="ignore")
                    snapshot_rel_path = f"evidence/snapshots/{snapshot_filename}"
            except Exception as e:
                print(f"[Evidence Vault] Snapshot download failed for {source_url}: {e}")

            # 2. Capture Chrome headless screenshot
            if self.browser_path:
                ss_filename = f"screenshot_{claim_hash}.png"
                ss_file = self.screenshots_dir / ss_filename
                try:
                    cmd = [
                        self.browser_path,
                        "--headless",
                        "--disable-gpu",
                        "--no-first-run",
                        "--no-default-browser-check",
                        f"--screenshot={str(ss_file)}",
                        "--window-size=1280,800",
                        source_url
                    ]
                    subprocess.run(cmd, timeout=12, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    if ss_file.exists():
                        screenshot_rel_path = f"evidence/screenshots/{ss_filename}"
                except Exception as e:
                    print(f"[Evidence Vault] Screenshot failed for {source_url}: {e}")

        record = {
            "id": f"EV-{len(self.ledger) + 1:03d}",
            "claim": claim,
            "source_title": source_title or source_url,
            "source_url": source_url,
            "published_date": published_date,
            "retrieved_date": datetime.now().strftime("%Y-%m-%d"),
            "exact_passage": exact_passage,
            "source_tier": source_tier,
            "verification_status": verification_status,
            "confidence": confidence,
            "limitation": limitation or "None noted",
            "screenshot_path": screenshot_rel_path,
            "snapshot_path": snapshot_rel_path,
            "timestamp": timestamp
        }

        self.ledger.append(record)
        self._save_ledger()
        return record

    def _write_markdown_ledger(self):
        """Generates an investor-grade EVIDENCE_LEDGER.md in the evidence/ folder"""
        rows = []
        for item in self.ledger:
            ss_link = f"[Screenshot]({item['screenshot_path']})" if item.get('screenshot_path') else "N/A"
            rows.append(
                f"| `{item['id']}` | **{item['claim']}** | [{item['source_title']}]({item['source_url']}) | "
                f"`{item['source_tier']}` | `{item['verification_status']}` | `{item['confidence']}` | {ss_link} |"
            )

        md = f"""# 🏛️ Immutable Startup Evidence Ledger
> **Managed by Nissh Research System v2 Provenance Engine**
> Total Evidence Items Logged: **{len(self.ledger)}**

| ID | Claim | Source | Tier | Status | Confidence | Media Proof |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
{chr(10).join(rows) if rows else "| - | No claims recorded yet | - | - | - | - | - |"}

---

### Detailed Provenance & Limitation Audit
"""
        for item in self.ledger:
            md += f"""
#### [{item['id']}] {item['claim']}
- **Source:** [{item['source_title']}]({item['source_url']}) (Retrieved: {item['retrieved_date']})
- **Exact Cited Passage:** > *"{item['exact_passage']}"*
- **Verification Verdict:** `{item['verification_status']}` | **Confidence:** `{item['confidence']}`
- **Source Limitation:** {item['limitation']}
- **Artifacts:** Snapshot: `{item.get('snapshot_path', 'None')}` | Screenshot: `{item.get('screenshot_path', 'None')}`
"""
        (self.evidence_dir / "EVIDENCE_LEDGER.md").write_text(md, encoding="utf-8")
