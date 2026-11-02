"""
Nissh Research System v2 - GitHub Repository Verifier Tool
==========================================================
Searches GitHub's public API to verify whether open-source implementations
already solve a candidate market gap, preventing false gaps from surviving.
"""

import urllib.parse
from typing import List, Dict, Any
import requests

class GitHubVerifier:
    def __init__(self, token: str = None):
        self.token = token
        self.session = requests.Session()
        headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "Nissh-Research-System/2.0"}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        self.session.headers.update(headers)

    def search_repositories(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Searches GitHub repositories by query.
        Returns top matching repositories sorted by stars.
        """
        encoded = urllib.parse.quote_plus(query)
        url = f"https://api.github.com/search/repositories?q={encoded}&sort=stars&order=desc&per_page={limit}"
        try:
            res = self.session.get(url, timeout=8)
            if res.status_code == 200:
                data = res.json()
                items = data.get("items", [])
                out = []
                for item in items:
                    out.append({
                        "name": item.get("full_name", ""),
                        "url": item.get("html_url", ""),
                        "stars": item.get("stargazers_count", 0),
                        "description": item.get("description", "") or "",
                        "updated_at": item.get("updated_at", "")
                    })
                return out
            else:
                return []
        except Exception as e:
            print(f"[GitHub Verifier] Search error: {e}")
            return []
