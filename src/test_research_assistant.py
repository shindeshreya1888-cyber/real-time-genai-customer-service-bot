
from src.research_assistant import search_research_papers

papers = search_research_papers("machine learning", max_results=3)

if not papers:
    print("No papers returned. Check your internet connection or try again later.")
else:
    for number, paper in enumerate(papers, start=1):
        print(f"\nPaper {number}: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Published: {paper['published']}")
        print(f"Abstract: {paper['abstract'][:300]}...")
        print(f"Link: {paper['link']}")
