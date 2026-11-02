"""
Nissh Research System v2 - Link & URL Validator Tool
====================================================
Forensically verifies that competitor URLs are live (HTTP 200),
detects dead/404 links, and extracts domain title & meta descriptions.
"""

import re
from typing import Dict, Any
import requests

class LinkValidator:
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def validate_url(self, url: str) -> Dict[str, Any]:
        """
        Validates URL and extracts live title/meta tags.
        Returns: {
            "is_live": bool,
            "status_code": int,
            "title": str,
            "description": str,
            "final_url": str
        }
        """
        if not url or not url.startswith("http"):
            return {
                "is_live": False,
                "status_code": 0,
                "title": "",
                "description": "",
                "final_url": url,
                "error": "Invalid URL protocol"
            }

        try:
            res = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            is_live = 200 <= res.status_code < 400

            # Extract title
            title = ""
            title_match = re.search(r'<title[^>]*>(.*?)</title>', res.text, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = re.sub(r'\s+', ' ', title_match.group(1)).strip()

            # Extract meta description
            desc = ""
            desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', res.text, re.IGNORECASE)
            if not desc_match:
                desc_match = re.search(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']', res.text, re.IGNORECASE)
            if desc_match:
                desc = desc_match.group(1).strip()

            return {
                "is_live": is_live,
                "status_code": res.status_code,
                "title": title[:100],
                "description": desc[:200],
                "final_url": res.url
            }
        except Exception as e:
            return {
                "is_live": False,
                "status_code": 0,
                "title": "",
                "description": "",
                "final_url": url,
                "error": str(e)[:100]
            }
