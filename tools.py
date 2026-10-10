from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime


# Save research output to a text file
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)


# DuckDuckGo search tool
search = DuckDuckGoSearchRun()

def safe_search(query: str) -> str:
    """Search the web and handle errors gracefully."""
    try:
        result = search.run(query)

        if not result:
            return "No search results found."

        return result

    except Exception as e:
        print(f"DuckDuckGo search error: {e}")
        return (
            f"Web search is temporarily unavailable. "
            f"Error: {type(e).__name__}: {e}"
        )


search_tool = Tool(
    name="search",
    func=safe_search,
    description=(
        "Search the web for information about a topic. "
        "If the search fails, returns an error message."
    ),
)


# Wikipedia tool
def safe_wikipedia_search(query: str) -> str:
    """Search Wikipedia and handle errors gracefully."""
    try:
        api_wrapper = WikipediaAPIWrapper(
            top_k_results=1,
            doc_content_chars_max=2000,
        )

        wiki_tool = WikipediaQueryRun(
            api_wrapper=api_wrapper,
        )

        result = wiki_tool.run(query)

        if not result:
            return "No information found on Wikipedia."

        return result

    except Exception as e:
        print(f"Wikipedia search error: {e}")
        return f"Wikipedia search failed: {type(e).__name__}: {e}"


wiki_tool = Tool(
    name="wikipedia_search",
    func=safe_wikipedia_search,
    description="Search Wikipedia for information about a topic. Returns an error message if the search fails.",
)
