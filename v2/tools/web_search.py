"""
Nissh Research System v2 - Live Web Search Tool
===============================================
Multi-provider web search engine with auto-fallback:
1. Tavily Search API (deep research mode)
2. Serper / Google API
3. Zero-key DuckDuckGo fallback (ensures search always works without paid keys)
"""

import os
import json
import urllib.parse
import re
from typing import List, Dict, Any, Optional
import requests

class WebSearchEngine:
    def __init__(self, tavily_key: Optional[str] = None, serper_key: Optional[str] = None):
        self.tavily_key = tavily_key or os.environ.get("TAVILY_API_KEY", "")
        self.serper_key = serper_key or os.environ.get("SERPER_API_KEY", "")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Executes web search with automatic fallback across providers.
        Returns list of dicts: [{"title": ..., "url": ..., "snippet": ..., "provider": ...}]
        """
        # 1. Try Tavily
        if self.tavily_key:
            try:
                results = self._search_tavily(query, max_results)
                if results:
                    return results
            except Exception as e:
                print(f"[Search Engine] Tavily search failed: {e}. Falling back...")

        # 2. Try Serper
        if self.serper_key:
            try:
                results = self._search_serper(query, max_results)
                if results:
                    return results
            except Exception as e:
                print(f"[Search Engine] Serper search failed: {e}. Falling back...")

        # 3. Zero-key fallback (DuckDuckGo HTML Lite)
        try:
            return self._search_duckduckgo(query, max_results)
        except Exception as e:
            print(f"[Search Engine] DuckDuckGo fallback failed: {e}")
            return []

    def _search_tavily(self, query: str, max_results: int) -> List[Dict[str, str]]:
        url = "https://api.tavily.com/search"
        payload = {
            "api_key": self.tavily_key,
            "query": query,
            "search_depth": "basic",
            "max_results": max_results
        }
        res = self.session.post(url, json=payload, timeout=12)
        if res.status_code == 200:
            data = res.json()
            out = []
            for r in data.get("results", []):
                out.append({
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "snippet": r.get("content", ""),
                    "provider": "tavily"
                })
            return out
        raise Exception(f"HTTP {res.status_code}: {res.text[:100]}")

    def _search_serper(self, query: str, max_results: int) -> List[Dict[str, str]]:
        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": self.serper_key, "Content-Type": "application/json"}
        payload = {"q": query, "num": max_results}
        res = self.session.post(url, headers=headers, json=payload, timeout=12)
        if res.status_code == 200:
            data = res.json()
            out = []
            for r in data.get("organic", [])[:max_results]:
                out.append({
                    "title": r.get("title", ""),
                    "url": r.get("link", ""),
                    "snippet": r.get("snippet", ""),
                    "provider": "serper"
                })
            return out
        raise Exception(f"HTTP {res.status_code}: {res.text[:100]}")

    def _search_duckduckgo(self, query: str, max_results: int) -> List[Dict[str, str]]:
        """Zero-key free fallback using DuckDuckGo HTML Lite"""
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        res = self.session.get(url, timeout=10)
        out = []
        if res.status_code == 200:
            # Simple regex parser for DDG HTML results
            # Result links usually look like: <a class="result__url" href="..."> or <a class="result__snippet" ...>
            blocks = re.findall(r'<div class="result__body">(.*?)</div>', res.text, re.DOTALL)
            for block in blocks[:max_results]:
                # Extract URL
                url_m = re.search(r'href="([^"]+)"', block)
                raw_url = url_m.group(1) if url_m else ""
                # DDG wrapper decode: //duckduckgo.com/l/?uddg=URL
                if "uddg=" in raw_url:
                    actual_url_match = re.search(r'uddg=([^&]+)', raw_url)
                    clean_url = urllib.parse.unquote(actual_url_match.group(1)) if actual_url_match else raw_url
                else:
                    clean_url = raw_url

                # Extract title
                title_m = re.search(r'<a class="result__snippet"[^>]*>(.*?)</a>', block, re.DOTALL)
                if not title_m:
                    title_m = re.search(r'<a[^>]+class="result__url"[^>]*>(.*?)</a>', block, re.DOTALL)
                title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else query

                # Extract snippet
                snippet_m = re.search(r'<a class="result__snippet"[^>]*>(.*?)</a>', block, re.DOTALL)
                snippet = re.sub(r'<[^>]+>', '', snippet_m.group(1)).strip() if snippet_m else ""

                if clean_url and clean_url.startswith("http"):
                    out.append({
                        "title": title or "Search Result",
                        "url": clean_url,
                        "snippet": snippet,
                        "provider": "duckduckgo_lite"
                    })
        return out
