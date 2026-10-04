# Timelink projects and project discovery

A "project" in Timelink is the association of a set of Kleio sources
with a database (see [Timelink home](timelink_home.md) for the concept
and the home layouts). Most of the time a project lives in a directory
of the filesystem, and that is what project discovery works on.

## Detecting projects: `get_timelink_projects`

Since timelink 1.2.0 the Python package can list the projects of a
home directory, independently of databases:

```python
from timelink.api.database import get_timelink_projects

for project in get_timelink_projects("/path/to/timelink-home"):
    print(project["name"], project["relative_path"], project["has_database"])
```

A directory below the given root is a **project** when it has any of:

* a `.timelink-project` marker file, or
* a `database/` subdirectory, or
* a `structures/` subdirectory, or
* a `sources/` subdirectory (sources not imported yet — the project
  exists even if no database was ever created).

Detection is structural, not database-driven: a project whose sources
were never imported has no database file to find, but it is listed
anyway, with `has_database: False`. All the home layouts of
[Timelink home](timelink_home.md) are covered, including the legacy
MHK layout (`sources/<project>`) and git-submodule subprojects, which
are reported nested, with `inside` set to the enclosing project.

Each entry carries:

| Field | Meaning |
|---|---|
| `name`, `path`, `relative_path` | identity of the project directory |
| `marker` | has a `.timelink-project` marker |
| `has_database`, `has_structures`, `has_sources` | layout flags |
| `inside` | relative path of the enclosing project (subprojects), else `None` |

### Marker files

* `.timelink-project` marks a project directory. Use it when a project
  has none of the layout subdirectories yet, or to make the project
  explicit.
* `.timelink-home` marks a multi-project home container. It is never a
  project itself; projects under it are discovered normally.

### Project of a path

`project_for(path, root)` returns the name of the nearest enclosing
project of any path — the rule used to annotate databases listed by
`get_sqlite_databases`-based tools.

## The Timelink MCP server

Also since 1.2.0, the package ships an
[MCP](https://modelcontextprotocol.io) server that exposes Timelink to
AI agents (Claude, ZCode and compatible clients) over stdio:

```bash
pip install "timelink[mcp]"
timelink-mcp
```

Configuration is through `TIMELINK_MCP_*` environment variables, of
which `TIMELINK_MCP_HOME` (the timelink home to serve) is the main
one; `TIMELINK_MCP_KLEIO_URL`/`TIMELINK_MCP_KLEIO_TOKEN` attach to an
already running Kleio server.

The server exposes 18 tools in four groups:

* **Discovery**: `list_projects` (structural project discovery, the
  tool version of `get_timelink_projects`), `list_databases`,
  `db_info`, `db_schema`.
* **Attribute search**: `attribute_values` (check a vocabulary before
  filtering), `find_entities_by_attribute`, `find_persons_by_name`,
  `entity_attributes`, `entity_details`.
* **Relations**: `find_relations`, `entity_relations`.
* **Sources and updating**: the split update pipeline
  `translate_sources` → `wait_for_translations` →
  `import_from_sources`, with `get_import_status`,
  `get_import_report`, `get_translation_report` and
  `kleio_server_info` for inspection.

Tabular tools page with `row_limit`/`offset`, and a packaged database
structure reference is served as the `timelink://schema/{database}`
resource.
