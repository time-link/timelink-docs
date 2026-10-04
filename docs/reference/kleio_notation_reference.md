# Kleio notation for historical sources

`Kleio` is a notation for the transcription of historical sources
developed by Manfred Thaller. Its aim is to transcribe the relevant
information from a historical source in a form close to the original
in terms of the sequence and structure of the information: a Kleio
transcription is *readable*, can preserve original orthography when
needed, and can include comments by the transcriber.

This page is the syntax reference. For the conceptual model
(groups/elements vs entities/relations) see
[Basic concepts](../introduction/basic_concepts.md); for a guided first
transcription see
[Transcribing a source](../tutorial/processing_source_transcriptions/transcribing_a_source.md).

## The three building blocks

* **Group** — one line, one fact with an identity: a source, an act, a
  person mentioned in an act, an attribute, a relation. Written
  `name$class …`.
* **Element** — a component of a group: either *positional* (values
  separated by `/`, meaning defined by the structure) or *named*
  (`name=value`).
* **Aspect** — extra information attached to the preceding element:
  `%original` marks the spelling as in the source, `#note` adds an
  observation, `?` marks uncertainty.

## Anatomy of a line

From a real parish baptism register (`b1685.cli`):

```
fonte$b1685/tipo=reg paroquiais/localizacao=fol. 30-34/data=16850000

   bap$b1685.1/8/7/1685/?/manuel cordeiro

      n$maria/f/id=b1685.1-per1

         pai$manuel madeira/m/id=b1685.1-per1-per2
            ls$residencia/alencarce
```

Piece by piece:

| Fragment | Meaning |
|---|---|
| `fonte$b1685` | group named by the source unit, class `fonte`, positional element `b1685` (the source id) |
| `tipo=reg paroquiais` | named element `tipo` (source type) |
| `bap$b1685.1/8/7/1685/?/manuel cordeiro` | a baptism act: positional elements are id, day, month, year, place (`?` = not filled), celebrant — the order is defined by the `bap` structure |
| `n$maria/f` | the baptized person: name `maria`, sex `f` |
| `id=b1685.1-per1` | explicit id (see [ids](#ids) below) |
| `pai$manuel madeira/m` | the father as a person group |
| `ls$residencia/alencarce` | an attribute inside the father: type `residencia`, value `alencarce` |

## Core syntax rules

**Nesting is indentation.** A group indented under another is *inside*
it: the `pai` group is inside the `n` group, which is inside the act,
which is inside the source. Inside-ness becomes provenance in the
database (the `inside` column) and defines what belongs to what.

**`name=value`** — named element. Values may contain spaces. Several
named elements follow one another, separated by `/`:

```
rel$sociabilidade/esteve com/Matteo Ricci/bio-matteo-ricci/data=15580000/obs=Em Lisboa
```

**`?`** — marks the preceding value as uncertain, in the transcriber's
judgement (`maria donana?`).

**`%text`** — aspect giving the **original spelling/wording** of the
preceding value, when the transcription normalizes it:

```
ls$residencia/cumieira, freguesia de Penela%termo de penela
ls$freguesia/penela%termo de penela
```

**`#text`** — aspect attaching a comment to the preceding element.

**Dates** — written `yyyymmdd` (partial allowed: `16850000`,
`16851200`). Inside positional slots of act groups the day/month/year
may be separate elements, as in `bap`; in named elements and attribute
groups a single `data=` element holds the full date string.

## Common group classes (gacto2 base)

The base structure `gacto2` provides the vocabulary used by most
source transcriptions:

| Class | Used for | Typical positional elements |
|---|---|---|
| `fonte` | the source unit (top of the file) | id; then `tipo=`, `data=`, `localizacao=`, `obs=` |
| `bap`, `cas`, `obito` (and other act groups) | acts: baptism, marriage, death… | id, day, month, year, place, celebrant |
| `n` | a person mentioned in an act | name, sex |
| `pai`, `mae`, `pad`, `mad`, `pmad`… | kin of the `n` person (father, mother, godfather…) | name, sex |
| `ls` | attribute of the enclosing person group | type, value (`ls$ec/s` = estado civil, solteiro) |
| `attr` | attribute with a date/evidence | type, value, date |
| `rel` | relation between two persons | type, value, destination-name, destination-id |
| `link`, `property` | linked-data annotations | see [Linked data providers](linked_data_providers.md) |

Projects extend this vocabulary with their own structures — see
[Defining new source types](../tutorial/defining_new_source_types/defining_new_source_types.md)
and the [schema syntax reference](kleio_schema_syntax.md).

## Ids

Every group can carry an explicit id with the named element `id=`. If
omitted, the translator **generates a stable id** from the file name,
line number and position — an id that survives re-translations of the
same file, which is what makes
[re-importing updated sources](processing_new_versions_of_sources.md)
safe. Good practice:

* give explicit ids to entities you will refer to elsewhere
  (`id=b1685.1-per1`), following the source hierarchy
  (`source-act-person`);
* let automatic ids happen for ephemeral groups (attributes,
  observations).

## The first line of a file

```
kleio$gacto2.str/translations=125
```

declares the base structure of the file (`gacto2.str`) plus how many
translations of it are in use. It is maintained by the tools — do not
edit it by hand.

## Where files live and how they are found

Kleio files live under the project's `sources/` directory; the
structures that govern them under `structures/`. Which structure
applies to which file is decided by the
[schema file location rules](kleio_schema_files_location.md).
