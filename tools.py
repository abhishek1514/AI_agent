from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
# Tavily हटाकर मुफ़्त DuckDuckGo सर्च इम्पोर्ट किया
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from rich import print

load_dotenv()

# मुफ़्त सर्च टूल का सेटअप (इसके लिए कोई API Key नहीं चाहिए)
ddg_search = DuckDuckGoSearchRun()

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and snippets."""
    try:
        # यह इंटरनेट पर लाइव सर्च करेगा
        results = ddg_search.run(query)
        return results
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