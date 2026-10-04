# Importing into the database

Import reads the XML produced by
[translation](translating.md) and loads it into the relational
database: one [entity](../../introduction/timelink_database.md) per
group, with attributes, relations and provenance. Files with
translation errors are skipped; files already imported and unchanged
are not imported again.

## Triggering the import

The normal trigger is one call that does both stages — translate what
is stale, import what is new:

### In notebooks

```python
from timelink.notebooks import TimelinkNotebook

tlnb = TimelinkNotebook()
tlnb.update_from_sources(path="sources/reference_sources")
```

`path` is optional; without it the whole project sources tree is
processed. Only files that changed since the last import are
re-imported (see
[Processing new versions of sources](../../reference/processing_new_versions_of_sources.md)
for how ids keep this safe).

### In the web interface

The project's update action runs the same pipeline.

### With a Python call

```python
from timelink.api.database import TimelinkDatabase

db = TimelinkDatabase("my_project", "sqlite")   # or "postgres"
db.update_from_sources(path="sources/reference_sources")
```

### With AI agents

The MCP server splits the pipeline into
`translate_sources` → `wait_for_translations` → `import_from_sources`,
with `get_import_status` as the polling view — see
[AI agents](../../ai_agents/index.md).

## Checking for errors

Import problems (as opposed to translation problems) are rare — the
XML was already validated by translation — but each file's outcome is
recorded:

```python
status = tlnb.get_import_status(status="E")   # files imported with errors
rpt = tlnb.get_import_rpt(file_spec="b1685")  # the import report of one file
```

Status letters for import: `N` new (not yet imported), `U` updated
source needs re-import, `I` imported, `W`/`E` imported with
warnings/errors. A typical `E` is a structural surprise in the data
itself (e.g. a relation pointing to an id that does not exist in any
imported file — postponed relations are stored and resolved when the
target file arrives).

After importing, the data is ready to explore — see
[Working with pandas](../working_with_notebooks/working_with_pandas.md).
