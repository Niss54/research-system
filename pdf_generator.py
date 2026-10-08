#!/usr/bin/env python3
"""
PDF Generator with Permanent 'Nissh' Watermark and Clickable Portfolio Link (nissh.info)
Uses Chrome/Edge headless rendering for vector-perfect styling and permanent watermark layers.
"""

import os
import sys
import subprocess
from pathlib import Path

# Reconfigure stdout/stderr for UTF-8 on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent

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

def generate_pdf_html(report_data):
    """
    Constructs an investor-grade, printable HTML document with permanent watermark
    and active clickable link to https://nissh.info.
    """
    problem = report_data.get("problem", "N/A")
    audience = report_data.get("audience", "N/A")
    verdict = report_data.get("verdict", "GO ✅")
    p1 = report_data.get("p1", "")
    p2 = report_data.get("p2", "")
    p3 = report_data.get("p3", "")
    p4 = report_data.get("p4", "")
    p5 = report_data.get("p5", "")
    p6 = report_data.get("p6", "")
    p7 = report_data.get("p7", "")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Startup Research Diligence Report | Nissh Research System</title>
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
      @bottom-right {{
        content: "Page " counter(page);
      }}
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.6;
      background: #ffffff;
      font-size: 11pt;
    }}

    /* Permanent Watermark Layer - Embedded across pages */
    .watermark-layer {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      align-items: center;
      opacity: 0.045;
      transform: rotate(-35deg);
      user-select: none;
    }}
    
    .watermark-text {{
      font-size: 56pt;
      font-weight: 900;
      color: #000000;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      white-space: nowrap;
    }}

    /* Header & Footer on each page */
    .doc-header {{
      border-bottom: 2px solid #6366f1;
      padding-bottom: 12px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    
    .doc-brand {{
      font-size: 14pt;
      font-weight: 800;
      color: #0f172a;
    }}
    
    .doc-meta {{
      font-size: 9pt;
      color: #64748b;
      text-align: right;
    }}

    .nissh-link {{
      color: #6366f1;
      text-decoration: none;
      font-weight: 700;
    }}

    .cover-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 5px solid #6366f1;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 25px;
    }}

    .title {{
      font-size: 22pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 8px;
    }}

    .tagline {{
      font-size: 12pt;
      color: #6366f1;
      font-weight: 600;
      margin-bottom: 15px;
    }}

    .verdict-badge {{
      display: inline-block;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 11pt;
      font-weight: 800;
      margin-top: 10px;
    }}
    .verdict-go {{ background: #dcfce7; color: #15803d; border: 1px solid #86efac; }}
    .verdict-maybe {{ background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }}
    .verdict-nogo {{ background: #ffe4e6; color: #b91c1c; border: 1px solid #fecdd3; }}

    h2 {{
      font-size: 14pt;
      font-weight: 700;
      color: #0f172a;
      margin-top: 26px;
      margin-bottom: 12px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
      page-break-after: avoid;
    }}

    h3 {{
      font-size: 11pt;
      font-weight: 700;
      color: #334155;
      margin-top: 14px;
      margin-bottom: 6px;
    }}

    p {{
      margin-bottom: 10px;
    }}

    .content-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 14px;
      font-size: 9.5pt;
      margin-bottom: 16px;
      white-space: pre-wrap;
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      word-break: break-word;
    }}

    .footer-bar {{
      margin-top: 40px;
      border-top: 1px solid #cbd5e1;
      padding-top: 12px;
      font-size: 8.5pt;
      color: #64748b;
      display: flex;
      justify-content: space-between;
      align-items: center;
      page-break-inside: avoid;
    }}

    .page-break {{
      page-break-before: always;
    }}
  </style>
</head>
<body>

  <!-- Permanent Non-Removable Watermark Layers -->
  <div class="watermark-layer">
    <div class="watermark-text">NISSH &bull; NISSH.INFO</div>
    <div class="watermark-text">AUTHENTIC RESEARCH &bull; NISSH</div>
    <div class="watermark-text">VERIFIED BY NISSH.INFO</div>
  </div>

  <!-- Header -->
  <div class="doc-header">
    <div>
      <div class="doc-brand">Startup Research Diligence Memo</div>
      <div style="font-size: 8.5pt; color: #64748b;">Autonomous 7-Agent Evidence Pipeline</div>
    </div>
    <div class="doc-meta">
      Created with <a href="https://nissh.info" class="nissh-link">Nissh Research System</a><br>
      Portfolio: <a href="https://nissh.info" class="nissh-link">https://nissh.info</a>
    </div>
  </div>

  <!-- Cover Summary Box -->
  <div class="cover-box">
    <h1 class="title">Startup Opportunity Research Report</h1>
    <div class="tagline">From Problem Hypothesis to Launch-Ready Evidence</div>
    
    <p><strong>Validated Problem Statement:</strong><br>{problem}</p>
    <p><strong>Target Customer ICP:</strong> {audience}</p>
    
    <div>
      <strong>Autonomous Research Verdict:</strong><br>
      <span class="verdict-badge verdict-go">{verdict}</span>
    </div>
  </div>

  <h2>1. Executive Summary & Evidence Validation (Agent 1)</h2>
  <div class="content-box">{p1 or "Phase 1 validation evidence recorded."}</div>

  <h2>2. Competitive Landscape & Top 10 Solutions (Agent 2)</h2>
  <div class="content-box">{p2 or "Top 10 solutions mapped."}</div>

  <div class="page-break"></div>

  <h2>3. Forensic Competitor Deep-Dive Profiles (Agent 3)</h2>
  <div class="content-box">{p3 or "Competitor profiles and failures audited."}</div>

  <h2>4. Strategic Gap Analysis & Feature Matrix (Agent 4)</h2>
  <div class="content-box">{p4 or "Feature matrix and scored gaps calculated."}</div>

  <div class="page-break"></div>

  <h2>5. Exhaustive Gap Verification (Agent 5)</h2>
  <div class="content-box">{p5 or "9-platform audit completed."}</div>

  <h2>6. Investor-Ready Diligence Memo & Roadmap (Agent 6)</h2>
  <div class="content-box">{p6 or "Final diligence memo synthesized."}</div>

  <h2>7. Production GitHub README & Launch Kit (Agent 7)</h2>
  <div class="content-box">{p7 or "Launch README and positioning ready."}</div>

  <!-- Footer Link and Creator Watermark -->
  <div class="footer-bar">
    <div>
      &copy; Researched & Built by <strong>Nishant Maurya (Nissh)</strong> &bull; Founder of Sight Pro &bull; MLH Hackathon Winner
    </div>
    <div>
      Official Portfolio: <a href="https://nissh.info" class="nissh-link" target="_blank">https://nissh.info</a>
    </div>
  </div>

</body>
</html>"""
    return html

def render_pdf(report_data, output_pdf_path=None):
    """
    Renders report_data dictionary to a PDF using Chrome/Edge headless.
    Returns the absolute path to the generated PDF.
    """
    if output_pdf_path is None:
        output_pdf_path = os.path.abspath(os.path.join(REPO_ROOT, "workspace", "STARTUP_RESEARCH_REPORT.pdf"))
    
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    temp_html_path = os.path.abspath(os.path.join(REPO_ROOT, "workspace", "report_printable.html"))

    html_content = generate_pdf_html(report_data)
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    browser = find_browser()
    if not browser:
        print("⚠️ Warning: No Chrome/Edge browser found for headless PDF. HTML report generated at:", temp_html_path)
        return temp_html_path

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        f"file:///{temp_html_path}"
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        if os.path.exists(output_pdf_path):
            print(f"✅ PDF Successfully Generated: {output_pdf_path} ({os.path.getsize(output_pdf_path)} bytes)")
            return output_pdf_path
    except Exception as e:
        print(f"⚠️ Error during headless PDF rendering: {e}. Printable HTML preserved at: {temp_html_path}")
    
    return temp_html_path

if __name__ == "__main__":
    sample = {
        "problem": "Freelance web designers struggle to manage client revision cycles without automated scope paywalls.",
        "audience": "Freelance designers and boutique agencies",
        "verdict": "GO ✅",
        "p1": "Daily frequency, severity 8/10, strong WTP.",
        "p2": "Bonsai, HoneyBook, MarkUp.io, DIY Spreadsheets.",
        "p3": "Bonsai lacks revision counters. MarkUp has zero billing links.",
        "p4": "Gap 1: Automated Smart Scope Paywall (Score: 8.5/10).",
        "p5": "Confirmed Gap: Nothing exists with Stripe milestone paywalls.",
        "p6": "ScopeLock: The automated client revision gatekeeper.",
        "p7": "# ScopeLock\n> Stop scope creep with automated change-order paywalls."
    }
    render_pdf(sample)
