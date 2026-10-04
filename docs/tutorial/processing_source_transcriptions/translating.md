# Translating source files

_Translation_ is the process that reads a transcription of a
historical source in Kleio notation and produces the normalized data
that will be imported into the database. It is performed by the
**Kleio server** — a SWI-Prolog service, normally running in Docker —
which reads the `.cli` file together with the applicable
[structure files](../../reference/kleio_schema_files_location.md) and
writes an XML file and a report (`.rpt`) next to the source. See
[How Timelink works](../../introduction/system_overview.md) for the
pipeline.

## What translation does

### Mapping _groups_ in the source to _entities_ in the database

Each Kleio group class is mapped by the structure to a database class:
`n`, `pai`, `pad`… become `person` entities; `bap` becomes an `act`;
`ls` becomes an attribute row of the enclosing person. The mapping
vocabulary is described in
[Timelink data concepts and models](../../reference/source_db_mappings_semantics.md).

### Inferences: how implicit information is produced

The structures can also declare inferences — information the
translator derives that is not literally in the source: the sex of
`pad$`/`mad$` groups (godfather male, godmother female), the
`function-in-act` relations that connect each person to the act
(baptized, father, godfather…), kinship relations between the `n`
person and its kin groups. Inferences are part of the structure files,
so they are consistent across all files of the same type.

## Managing translation

Translation is triggered automatically whenever the database is
updated from sources, so in normal work you do not think about it —
you call update (notebook, web or agent) and translation of stale
files happens first. The explicit triggers:

1. **With the VS Code extension** — translate on save: keeping the
   Kleio file open, every save re-translates and shows errors inline.
   Recommended while transcribing.
2. **With notebooks** — `TimelinkNotebook().update_from_sources()`
   translates what is stale and imports what is new in one call (see
   [Importing into the database](importing_into_the_database.md)).
3. **With a Python call** — start or attach a server and translate:

   ```python
   from timelink.kleio.kleio_server import KleioServer

   ks = KleioServer.start(kleio_home="path/to/timelink-home")  # or .attach(url, token)
   ks.translate_sources(path="sources/reference_sources")      # server-relative path
   ```

4. **In the web interface** — the update action of the project page
   runs the same pipeline.
5. **With AI agents** — the MCP server exposes the pipeline as
   `translate_sources` → `wait_for_translations` →
   `import_from_sources` tools (see
   [AI agents](../../ai_agents/index.md)).

Docker must be running for the Kleio server to start. Whatever the
trigger, results are checked the same way — see
[Checking translation results](checking_translation_results.md).
