
from src.research_assistant import search_research_papers
from src.paper_summarizer import summarize_paper

papers = search_research_papers("machine learning", max_results=1)

if papers:
    paper = papers[0]

    print("\nPAPER TITLE:")
    print(paper["title"])

    print("\nSUMMARY:")
    print(summarize_paper(paper["abstract"]))

else:
    print("No paper found. Check your internet connection.")
