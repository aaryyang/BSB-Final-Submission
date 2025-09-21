import os
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv
from urllib.parse import urlparse
import re
from datetime import datetime

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def format_citation(title, url, domain, credibility_level, style="APA"):
    """Format a source into proper academic citation"""
    # Extract domain name for publisher
    publisher = domain.replace('www.', '').replace('.com', '').replace('.org', '').replace('.edu', '').replace('.gov', '')
    publisher = publisher.split('.')[0].title()
    
    # Get current date for access date
    access_date = datetime.now().strftime("%B %d, %Y")
    
    if style == "APA":
        # APA Style: Author/Organization. (Year). Title. URL
        citation = f"{publisher}. (2024). {title}. Retrieved {access_date}, from {url}"
    elif style == "MLA":
        # MLA Style: "Title." Publisher, Date, URL.
        citation = f'"{title}." {publisher}, {access_date}, {url}.'
    else:  # Simple format
        citation = f"{title}. {publisher}. Retrieved {access_date}. {url}"
    
    return citation

def create_source_reference_map(unique_results):
    """Create a mapping of sources for inline citations"""
    source_map = {}
    for i, result in enumerate(unique_results, 1):
        # Create short reference key
        domain = result['credibility']['domain']
        publisher = domain.replace('www.', '').split('.')[0].title()
        key = f"{publisher}_{i}"
        
        source_map[result['url']] = {
            'key': key,
            'short_cite': f"({publisher}, 2024)",
            'full_citation': format_citation(
                result['title'], 
                result['url'], 
                domain,
                result['credibility']['level']
            ),
            'credibility': result['credibility']['level']
        }
    return source_map

def analyze_fact_consistency(unique_results):
    """Analyze consistency of facts across multiple sources"""
    fact_check_prompt = f"""
    Analyze the following sources for factual consistency and potential contradictions:
    
    Sources:
    {chr(10).join([f"- {r['title']}: {r['content'][:200]}..." for r in unique_results[:8]])}
    
    Identify:
    1. Claims that appear in multiple sources (consistent facts)
    2. Contradictory information between sources
    3. Claims that appear in only one source (needs verification)
    
    Format as:
    CONSISTENT: [fact] (appears in X sources)
    CONTRADICTORY: [conflicting claims]
    SINGLE-SOURCE: [unverified claims]
    """
    
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": fact_check_prompt}],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Fact-checking analysis unavailable: {e}"
from urllib.parse import urlparse
import re
from datetime import datetime

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def analyze_source_credibility(url, title, content):
    """Analyze the credibility of a source based on URL, title, and content"""
    domain = urlparse(url).netloc.lower()
    
    # High credibility domains
    high_credibility = [
        'wikipedia.org', 'britannica.com', 'reuters.com', 'bbc.com', 'npr.org',
        'gov', 'edu', 'org', 'nytimes.com', 'wsj.com', 'theguardian.com',
        'forbes.com', 'bloomberg.com', 'cnn.com', 'nbcnews.com', 'cbsnews.com'
    ]
    
    # Medium credibility domains
    medium_credibility = [
        'techcrunch.com', 'wired.com', 'arstechnica.com', 'engadget.com',
        'motortrend.com', 'caranddriver.com', 'consumerreports.org',
        'trustpilot.com', 'glassdoor.com', 'yelp.com'
    ]
    
    # Low credibility indicators
    low_credibility_indicators = [
        'buy', 'sale', 'shop', 'store', 'purchase', 'deal', 'discount',
        'cheap', 'best-price', 'for-sale', 'wheels', 'parts'
    ]
    
    credibility_score = 50  # Start with neutral
    credibility_level = "Medium"
    
    # Domain analysis
    if any(hc in domain for hc in high_credibility):
        credibility_score += 30
        credibility_level = "High"
    elif any(mc in domain for mc in medium_credibility):
        credibility_score += 15
        credibility_level = "Medium"
    elif any(lc in domain.lower() or lc in url.lower() for lc in low_credibility_indicators):
        credibility_score -= 25
        credibility_level = "Low"
    
    # Official company domains get higher credibility
    if any(indicator in domain for indicator in ['.com', '.co.uk']) and not any(lc in domain for lc in low_credibility_indicators):
        if 'official' in title.lower() or 'company' in title.lower():
            credibility_score += 10
    
    # Content quality indicators
    if len(content) > 200:  # Substantial content
        credibility_score += 5
    if re.search(r'\d{4}', content):  # Contains dates/years
        credibility_score += 5
    
    # Final credibility classification
    if credibility_score >= 70:
        credibility_level = "High"
    elif credibility_score >= 45:
        credibility_level = "Medium"
    else:
        credibility_level = "Low"
    
    return {
        'score': credibility_score,
        'level': credibility_level,
        'domain': domain
    }

def format_citation(title, url, domain, credibility_level, style="APA"):
    """Format a source into proper academic citation"""
    # Extract domain name for publisher
    publisher = domain.replace('www.', '').replace('.com', '').replace('.org', '').replace('.edu', '').replace('.gov', '')
    publisher = publisher.split('.')[0].title()
    
    # Get current date for access date
    access_date = datetime.now().strftime("%B %d, %Y")
    
    if style == "APA":
        # APA Style: Author/Organization. (Year). Title. Publisher. URL
        citation = f"{publisher}. (2024). {title}. Retrieved {access_date}, from {url}"
    elif style == "MLA":
        # MLA Style: "Title." Publisher, Date, URL.
        citation = f'"{title}." {publisher}, {access_date}, {url}.'
    else:  # Simple format
        citation = f"{title}. {publisher}. Retrieved {access_date}. {url}"
    
    return citation

def generate_search_queries(original_query: str):
    """Generate multiple related search queries for comprehensive research"""
    prompt = f"""
    Generate 4 related search queries for comprehensive research on: "{original_query}"
    
    Include:
    1. An informational query about the brand/topic (add "brand overview history" or "company information" to avoid commercial results)
    2. A query about problems/criticisms/disadvantages/issues
    3. A query about benefits/advantages/features/positive aspects
    4. A comparative query (vs competitors or alternatives)
    
    Make sure the first query focuses on getting informational content, not commercial/sales pages.
    
    Return only the queries, one per line, no numbering or formatting.
    """
    
    completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    
    queries = [q.strip() for q in completion.choices[0].message.content.strip().split('\n') if q.strip()]
    return queries[:4]  # Ensure max 4 queries

def research(query: str, citation_style="APA"):
    # Step 1: Generate multiple search queries
    search_queries = generate_search_queries(query)
    print(f"Searching with queries: {search_queries}")
    
    # Step 2: Search web with multiple queries
    all_results = []
    for search_query in search_queries:
        try:
            results = tavily.search(query=search_query, max_results=3)  # Reduced per query to manage total
            all_results.extend(results['results'])
        except Exception as e:
            print(f"Search failed for query '{search_query}': {e}")
            continue
    
    # Remove duplicates based on URL and analyze credibility
    seen_urls = set()
    unique_results = []
    for result in all_results:
        if result['url'] not in seen_urls:
            seen_urls.add(result['url'])
            # Add credibility analysis
            credibility = analyze_source_credibility(result['url'], result['title'], result['content'])
            result['credibility'] = credibility
            unique_results.append(result)
    
    # Sort by credibility score (highest first)
    unique_results.sort(key=lambda x: x['credibility']['score'], reverse=True)
    
    # Step 3: Perform fact-checking analysis
    fact_check_analysis = analyze_fact_consistency(unique_results)
    
    # Create source reference map for inline citations
    source_map = create_source_reference_map(unique_results)
    
    # Step 4: Format results for analysis with credibility indicators
    snippets = "\n".join([f"- {r['title']} [Credibility: {r['credibility']['level']}]: {r['url']}\n  {r['content']}" for r in unique_results[:12]])  # Limit total results
    
    # Step 4: Organize sources by search query for better citation with credibility
    sources_by_query = {}
    result_index = 0
    for i, search_query in enumerate(search_queries):
        sources_by_query[search_query] = []
        # Get results for this specific query (approximate based on order)
        query_results = unique_results[result_index:result_index+3]
        for result in query_results:
            credibility_icon = {"High": "🟢", "Medium": "🟡", "Low": "🔴"}[result['credibility']['level']]
            # Create proper citation
            citation = format_citation(
                result['title'], 
                result['url'], 
                result['credibility']['domain'],
                result['credibility']['level'],
                citation_style
            )
            sources_by_query[search_query].append(
                f"- {credibility_icon} {citation}"
            )
        result_index += len(query_results)
    
    # Format sources section
    sources_section = "\n\n**SOURCES BY SEARCH PERSPECTIVE:**\n"
    for i, (search_query, sources) in enumerate(sources_by_query.items(), 1):
        sources_section += f"\nSearch Perspective {i}: {search_query}\n"
        sources_section += "\n".join(sources) + "\n"

    # Step 5: Enhanced summarization with Groq
    prompt = f"""
    You are an expert research assistant conducting comprehensive analysis with fact-checking capabilities.
    Task: Create a detailed, balanced research report from multiple search perspectives.

    Original Query: {query}
    Search Queries Used: {', '.join(search_queries)}

    Results from Multiple Searches (with credibility ratings):
    {snippets}

    FACT-CHECKING ANALYSIS:
    {fact_check_analysis}

    Create a comprehensive report with:
    - Executive Summary (2-3 sentences)
    - Key Findings (main facts and insights - prioritize CONSISTENT facts from High credibility sources)
    - Advantages/Benefits
    - Disadvantages/Criticisms/Concerns
    - Different Perspectives (if applicable)
    - Market Position/Comparisons (if applicable)
    - Future Outlook/Trends
    - Fact-Check Alerts (highlight any contradictory or single-source claims that need verification)
    - Open Questions/Areas for Further Research

    IMPORTANT INSTRUCTIONS:
    1. Prioritize information that appears in multiple sources (marked as CONSISTENT in fact-check analysis)
    2. Flag contradictory information with a warning
    3. Mark single-source claims as "needs verification"
    4. Give more weight to High credibility sources
    5. Do NOT include a sources section - I will add properly formatted sources afterward
    6. Do NOT use inline URLs or "Credit:" citations - reference sources by publisher name only when needed
    """

    completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",  # production model on Groq
        messages=[{"role": "user", "content": prompt}],
    )

    # Combine the AI report with properly formatted sources
    report = completion.choices[0].message.content + sources_section
    return report

if __name__ == "__main__":
    user_query = input("Enter a research topic: ")
    print("Citation style options: APA, MLA, Simple")
    citation_style = input("Choose citation style (press Enter for APA): ").strip() or "APA"
    
    report = research(user_query, citation_style)
    print(f"\n=== Research Report ({citation_style} Citations) ===\n")
    print(report)
