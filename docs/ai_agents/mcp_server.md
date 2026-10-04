# The Timelink MCP server

The MCP server (`timelink-mcp`) exposes a Timelink home to AI agents
over the
[Model Context Protocol](https://modelcontextprotocol.io): the agent
discovers your projects, queries the databases and runs the update
pipeline, while you keep control of what happens.

## Install and run

```bash
pip install "timelink[mcp]"
timelink-mcp        # speaks MCP over stdio
```

The server is configured through `TIMELINK_MCP_*` environment
variables:

| Variable | Purpose | Default |
|---|---|---|
| `TIMELINK_MCP_HOME` | the timelink home to serve (searched recursively for projects and databases) | `~/.timelink` |
| `TIMELINK_MCP_SQLITE_ROOT` | override the database search root | the home |
| `TIMELINK_MCP_DB_TYPE` | default engine: `sqlite` or `postgres` | `sqlite` |
| `TIMELINK_MCP_KLEIO_URL` | attach to a running Kleio server (with token) instead of starting one | none |
| `TIMELINK_MCP_KLEIO_TOKEN` | admin token for that server | none |
| `TIMELINK_MCP_MAX_ROWS` | hard cap on rows returned per page | `500` |

One deployment per home: point `TIMELINK_MCP_HOME` at your timelink
home (e.g. `~/mhk-home`) and every project under it is reachable.

## Connecting a client

In the client's MCP configuration (Claude Desktop, ZCode, or any
MCP client), add a stdio server along these lines:

```json
{
  "mcpServers": {
    "timelink": {
      "command": "timelink-mcp",
      "env": { "TIMELINK_MCP_HOME": "/Users/you/mhk-home" }
    }
  }
}
```

## The tools

18 tools in four groups (names unprefixed; the server namespaces them
as `timelink` in clients):

**Discovery**

| Tool | What it does |
|---|---|
| `list_projects` | projects of the home, detected structurally — including projects with no database yet |
| `list_databases` | databases of all projects, each annotated with its project |
| `db_info` | contents of one database: row counts, entity classes, views, version |
| `db_schema` | columns of a table/class/view; Kleio-group → ORM-class mapping |

**Search** — `attribute_values` (list a vocabulary before filtering),
`find_entities_by_attribute` (the workhorse), `find_persons_by_name`,
`entity_attributes`, `entity_details` (an entity rendered in Kleio
notation).

**Relations** — `find_relations` (population level),
`entity_relations` (one entity, in/out).

**Sources and updating** — the pipeline split so the agent
orchestrates: `translate_sources` → `wait_for_translations` →
`import_from_sources`, with `get_import_status` for polling and
`get_import_report` / `get_translation_report` / `kleio_server_info`
for diagnosis. With no path argument these operate on the database's
own project sources only.

A packaged reference of the database structure — conceptual model,
conventions (dates as `yyyymmdd` strings compared lexically, LIKE
wildcards, ids as strings), and query recipes — is served as the
`timelink://schema/{database}` resource that agents read before heavy
querying.

## What an agent session looks like

> **You:** what projects do I have, and which have no database yet?
>
> **Agent:** `list_projects` → "15 projects; `COMMEMORtis_SB`,
> `COMMEMORtis_ST`, `soure-fontes` and `jesuitas-franco-imagem-virtude`
> have sources and structures but no imported database."
>
> **You:** in `dehergne`, who was in Macau before 1645?
>
> **Agent:** `attribute_values("chegada")` to check the vocabulary,
> then `find_entities_by_attribute(the_type="chegada",
> dates_in=[...])`, then `entity_details` on the interesting ids —
> answers with names, dates and the source lines they came from.
>
> **You:** update the `dehergne` database from its sources.
>
> **Agent:** `get_import_status` → `translate_sources` →
> `wait_for_translations` (re-invoked while files are pending) →
> `import_from_sources` → `get_import_status` again, reporting
> per-file counts and any errors with their reports.

## Safety notes

* The server is **read-plus-update**, not arbitrary write: the only
  mutations are the translate/import pipeline on your own source
  files.
* Connecting never creates databases: a database name that does not
  resolve to an existing file raises, so typos cannot materialize
  empty databases.
* Tokens are never returned by tools (`kleio_server_info` shows url,
  version and health only).
