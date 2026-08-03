from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich import print

load_dotenv()

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic. Returns text snippets."""
    try:
        # No external package needed, uses pure requests
        url = f"https://duckduckgo.com{query}"
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        
        out = []
        for result in soup.find_all('a', class_='result__snippet')[:4]:
            out.append(result.get_text(strip=True))
            
        if not out:
            return "No recent results found. Try rephrasing the topic."
            
        return "\n---\n".join(out)
    except Exception as e:
        return f"Search failed: {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
