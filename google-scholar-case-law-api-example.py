"""
Example: call the Google Scholar Case Law API Apify Actor from Python.

Searches US case law (state and federal courts) on Google Scholar and returns
clean, structured JSON: case title, court and citation summary, cited-by count,
case_id, and a link. Optionally pull full case details (parties, court,
citations, cited cases) for each result.

This example runs a search with a small result cap to keep the first run
inexpensive (each search result is billed; full details cost extra). Provide
`caseIds` to fetch details for specific cases instead.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

run_input = {
    "query": "patent infringement",
    "maxResults": 5,
    # "courts": ["158"],   # 158 = US Supreme Court; omit to search all courts
    # "yearFrom": 1990,
    # "fetchCaseDetailsForResults": True,  # pull full details per result (billed extra)
}

print(f"Searching US case law for: {run_input['query']}")
run = client.actor("johnvc/google-scholar-case-law").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("result_type") != "search_result":
        # When details are fetched, detail items appear with a different result_type.
        print(f"[{item.get('result_type')}] {item.get('title')}")
        continue

    info = item.get("publication_info") or {}
    cited_by = (item.get("inline_links") or {}).get("cited_by") or {}

    print(f"{item.get('position')}. {item.get('title')}")
    print(f"   {info.get('summary', '')}")
    print(f"   Cited by: {cited_by.get('total', 0)}")
    print(f"   case_id={item.get('case_id')}")
    print(f"   {item.get('link')}")
    print()
