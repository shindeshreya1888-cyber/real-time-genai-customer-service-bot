
import requests
import xml.etree.ElementTree as ET


ARXIV_API_URL = "https://export.arxiv.org/api/query"

ATOM_NAMESPACE = {
    "atom": "http://www.w3.org/2005/Atom"
}


def search_research_papers(query, max_results=5):
    """
    Search arXiv for research papers matching a query.
    Returns paper titles, authors, abstracts, and links.
    """

    if not query or not query.strip():
        return []

    params = {
        "search_query": f"all:{query.strip()}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }

    try:
        response = requests.get(
            ARXIV_API_URL,
            params=params,
            timeout=20
        )
        response.raise_for_status()

        root = ET.fromstring(response.content)
        papers = []

        for entry in root.findall("atom:entry", ATOM_NAMESPACE):
            title = entry.findtext(
                "atom:title", default="No title",
                namespaces=ATOM_NAMESPACE
            ).strip()

            abstract = entry.findtext(
                "atom:summary", default="No abstract available",
                namespaces=ATOM_NAMESPACE
            ).strip()

            published = entry.findtext(
                "atom:published", default="Unknown",
                namespaces=ATOM_NAMESPACE
            ).strip()

            authors = [
                author.findtext(
                    "atom:name",
                    default="Unknown",
                    namespaces=ATOM_NAMESPACE
                )
                for author in entry.findall(
                    "atom:author", ATOM_NAMESPACE
                )
            ]

            link_element = entry.find(
                "atom:id", ATOM_NAMESPACE
            )
            paper_link = (
                link_element.text.strip()
                if link_element is not None
                else ""
            )

            papers.append({
                "title": " ".join(title.split()),
                "authors": authors,
                "abstract": " ".join(abstract.split()),
                "published": published[:10],
                "link": paper_link
            })

        return papers

    except requests.RequestException as error:
        print(f"Research paper search failed: {error}")
        return []

    except ET.ParseError as error:
        print(f"Could not read research results: {error}")
        return []
