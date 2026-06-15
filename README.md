# ⚖️ Google Scholar Case Law API: US Court Opinions in Clean JSON

> The efficient, reliable, and developer-friendly way to use the Google Scholar Case Law API.

**Actor page:** [apify.com/johnvc/google-scholar-case-law](https://apify.com/johnvc/google-scholar-case-law?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-scholar-case-law/input-schema](https://apify.com/johnvc/google-scholar-case-law/input-schema?fpr=9n7kx3)

The Google Scholar Case Law API searches US case law (state and federal courts) on Google Scholar and returns clean, structured JSON: case title, court and citation summary, cited-by count, `case_id`, and a link per result. Filter by court, year range, and sort order, and optionally pull full case details (parties, court, citations, and cited cases). Built for legal research, citation analysis, docket tooling, and AI agent workflows.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Scholar-Case-Law-API.git
   cd Apify-Google-Scholar-Case-Law-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-scholar-case-law-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-scholar-case-law-api-example.py
```

## Why Use This Google Scholar Case Law API?

**Search every US court.** Query state and federal case law, or scope to specific jurisdictions with court codes (for example `158` for the Supreme Court).

**Citation context.** Each result includes the reporter and court summary plus a cited-by count, so you can gauge a case's weight at a glance.

**Full details on demand.** Set `fetchCaseDetailsForResults`, or pass `caseIds`, to pull parties, court, citations, and cited cases for each opinion.

**Precise filtering.** Restrict by `yearFrom` and `yearTo`, sort by date, and exclude bare citation entries to keep only full opinions.

**Predictable, pay-per-use pricing.** Billing is per search result, with full case details billed separately only when requested.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can run legal searches for you on demand.

## Features

### Core Capabilities
- Case-law search across US state and federal courts
- Court-code filtering for specific jurisdictions
- Year-range filtering and date sorting
- Optional full case details (parties, court, citations, cited cases)
- Search by `query`, by `caseIds`, or both

### Data Quality
- One row per case, each with a stable `case_id` and `result_id`
- Reporter and court summary plus cited-by count
- Direct Google Scholar opinion link on every result
- Search metadata echoed on every row

## Usage Examples

### Search case law
```json
{
  "query": "patent infringement",
  "maxResults": 10
}
```

### Supreme Court only, recent years
```json
{
  "query": "First Amendment school speech",
  "courts": ["158"],
  "yearFrom": 2000,
  "sortByDate": true
}
```

### Full details for specific cases
```json
{
  "caseIds": ["10285146068541901213"]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | one of | - | Case-law search query. Either `query` or `caseIds` is required. |
| `caseIds` | `array` | one of | - | Google Scholar case IDs to pull full detail for. |
| `maxResults` | `int` | no | `20` | Maximum search results (max 100). Each result is billed. |
| `yearFrom` / `yearTo` | `int` | no | - | Earliest / latest decision year (inclusive). |
| `courts` | `array` | no | (all) | Court codes, e.g. `158` SCOTUS, `159` Federal Circuit, `33` NY state. |
| `language` | `str` | no | `en` | Interface language code. |
| `sortByDate` | `bool` | no | `false` | Sort by decision date (newest first) instead of relevance. |
| `excludeCitations` | `bool` | no | `false` | Return only full opinions, not bare citation entries. |
| `fetchCaseDetailsForResults` | `bool` | no | `false` | Fetch full detail for every result (one detail charge each). |

## Output Format

A real search for `patent infringement` returns one row per case.

```json
{
  "result_type": "search_result",
  "position": 1,
  "title": "Markman v. Westview Instruments, Inc.",
  "case_id": "10285146068541901213",
  "result_id": "nQlyNtstvI4J",
  "link": "https://scholar.google.com/scholar_case?case=10285146068541901213",
  "publication_info": {
    "summary": "52 F. 3d 967 - Court of Appeals, Federal Circuit, 1995 - Google Scholar"
  },
  "inline_links": {
    "cited_by": { "total": 7023, "link": "https://scholar.google.com/scholar?cites=10285146068541901213" }
  },
  "fetched_at": "2026-05-30T13:16:21Z"
}
```

Each case row also carries a `snippet` from the opinion and `publication_info.authors` (the deciding judges when available). When `fetchCaseDetailsForResults` is enabled or `caseIds` are supplied, detail items add the parties, court, full citations, and the list of cited cases.

---

## Use as an MCP tool

You can load the Google Scholar Case Law API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Scholar Case Law API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Scholar Case Law API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Scholar Case Law API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-scholar-case-law`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law`, using OAuth when prompted.
5. Ask Claude to run the Google Scholar Case Law API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Scholar Case Law API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-scholar-case-law`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Scholar Case Law API to power legal research, citation analysis, and docket tooling with reliable, structured results.*

Last Updated: 2026.06.15
