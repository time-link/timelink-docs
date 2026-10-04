# About `timelink` databases

When Kleio sources are translated and imported (see
[How Timelink works](system_overview.md)), the information lands in a
relational database — SQLite (a file, zero administration) or
PostgreSQL — with a fixed core model. This page describes that model;
see also [Timelink data concepts and models](../reference/source_db_mappings_semantics.md)
for how source groups map onto it.

## Everything is an entity

Every person, act, source, object, attribute and relation gets one row
in the `entities` table with a unique string `id`. Class-specific data
lives in specialization tables (`persons`, `acts`, `sources`, …) that
share the same id (joined-table inheritance). The entity's class — in
`entities.class` — determines which specialization table completes it.

## Attributes and relations

* **Attributes** are data about one entity: a `the_type` /
  `the_value` / `the_date` triple plus provenance — a *property with
  citation*. Example: type `residencia`, value `alencarce`, date
  `16850708` for the father in a baptism of 1685.
* **Relations** connect two entities: origin → destination with a
  type, value and date. Participation in an act is a relation of type
  `function-in-act` (origin = person, destination = act, value = the
  person's role in it). Identity assertions — "these two rows are the
  same historical person" — are relations of type `identification`.

## Provenance is everywhere

Each imported row records the `source` id it came from, its position
in the source (`the_line`, `the_level`, `the_order`), its containing
group (`inside`) and the Kleio group name that produced it
(`groupname`). Any query result can therefore be traced back to the
exact line of the transcription — the database is a derived,
rebuildable index of the sources.

## Ids

Ids are strings, stable across re-imports: the same source file
translated twice produces the same ids (explicit `id=` elements when
the transcriber gave them, generated from file/line/position
otherwise). The **same historical person appears once per source**,
with different ids — a baptism's father and a marriage's groom are two
rows, consolidated later through `identification` relations, never by
merging.

## Dates

Dates are stored as strings in `yyyymmdd` format, with partial dates
allowed (`1685`, `168507`, `16850700` when the day is unknown). They
compare correctly as strings and are never cast to SQL date types.

## Exploring

* [Working with pandas](../tutorial/working_with_notebooks/working_with_pandas.md)
  — data frames from attributes and names;
* [Querying user defined structures](../tutorial/defining_new_source_types/querying_user_defined_structures.md)
  — inspecting the schema and querying with the ORM;
* The [web interface](https://time-link.github.io/timelink-docs/) and
  [AI agents](../ai_agents/index.md) sit on the same database.
