# Defining new historical source types

The base Kleio vocabulary (`gacto2`) fits parish-type sources well.
When your source is different — a chronology, a membership list, a
bibliographic repertoire — you define a **new source type** by writing
a structure (schema) file. This page is the hands-on walkthrough; the
complete syntax is in
[Kleio schema files syntax](../../reference/kleio_schema_syntax.md),
and the location/naming rules in
[Schema file location](../../reference/kleio_schema_files_location.md).

## What you need to define

Before writing YAML, answer five questions about the source:

1. **What are the groups?** — the kinds of "line" the source has (the
   unit, the events, the people mentioned, the attributes…).
2. **Which existing groups can I reuse?** — a person is a person:
   inherit from the core groups instead of redefining them.
3. **What are the positional elements** of each group, in the order
   they appear in the source?
4. **What can contain what?** — which groups may be nested inside
   which (the *meronomy* of the source).
5. **What should be inferred?** — e.g. sex from kin-group names,
   person-to-act relations.

## Structure of schema files

A structure file is a YAML list of `group` (and `element`)
definitions, inheriting through the `source` key:

```yaml
- group:
    name: historical-act
    description: >
        Represents an historical act, i.e. a record of an event,
        something that happened at a moment and place in time.
    source: event
    position: [id, type, date]
    guaranteed: [id, type, date]
    also: [loc, ref, obs, day, month, year]
    contains: [person, object, geoentity, abstraction, ls, atr, rel, cevent, end]
    idprefix: hac
```

* `position` — elements given after the group name, separated by `/`
  (the positional slots used in
  [Kleio notation](../../reference/kleio_notation_reference.md)).
* `also` — additional, named elements (`name=value`).
* `guaranteed` — mandatory elements; the translator reports their
  absence as errors.
* `contains` — the groups that may be nested inside (older files use
  the deprecated `part`/`arbitrary` keys with the same meaning).
* `idprefix` — prefix for generated ids of this group's instances.

Put the file in the project's `structures/` tree, next to the sources
it governs; the
[location rules](../../reference/kleio_schema_files_location.md)
associate it with your source files. Use `include` to build on other
structures.

## Defining new sources by extending base ones

The usual path: start from the base structure, add the groups your
source needs, inherit the rest. The chronology type that ships with
Timelink (`structures/reference_sources/cronologias/sources.str.yaml`)
does exactly this — a `historical-source` unit containing
`historical-act` events, each with persons, places and topics. Its
transcription is documented in
[Chronologies](../../existing_source_schemes/Chronologies.md), a good
example of structure and transcription side by side.

## Most common components (groups) of source files

Reuse before defining: `fonte`/source unit, act groups, `n` and kin
groups for persons, `ls`/`attr` for attributes, `rel` for relations,
`link`/`property` for
[linked data](../../reference/linked_data_providers.md) annotations.
Most "new" source types need only a new act-like group and maybe a
new attribute vocabulary — not new database tables (tables are needed
only when a group stores information no core group stores; then see
[Defining source to database mappings](defining_new_database_mappings.md)).

## Special source types

* **Event lists** (chronologies, itineraries) — acts with dates and
  places, persons and topics attached; see the Chronologies example.
* **VIP lists / authority registers** — one group per real-world
  person, used to consolidate the same person across sources; see
  [Identification lists](../../reference/identification_lists.md).

Once the structure exists, transcribe against it
([Adding your own files](../processing_source_transcriptions/add_your_own_files.md))
— the translation report ([Checking translation
results](../processing_source_transcriptions/checking_translation_results.md))
tells you immediately when a line does not conform.
