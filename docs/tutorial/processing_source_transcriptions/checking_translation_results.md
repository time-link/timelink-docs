# Checking translation results

Every translation writes a report file (`.rpt`) next to the source,
with one entry per error or warning found in the `.cli` file. Reading
these reports is the fastest feedback loop while transcribing.

## In notebooks

`TimelinkNotebook` wraps the whole loop:

```python
from timelink.notebooks import TimelinkNotebook

tlnb = TimelinkNotebook()

status = tlnb.get_import_status()   # one row per file:
#   import_status, translation_status, errors, warnings
#   V=valid, W=warnings, E=errors; I=imported, N=new, U=needs reimport

tlnb.get_translation_report(file_spec="b1685")  # the .rpt contents for one file
```

Files with translation errors are never imported, so a red `E` in the
status table is always worth a look at the report.

## In VS Code

The Timelink extension translates on save and shows errors and
warnings inline in the `.cli` file — the quickest way to fix a
structure mismatch (a group the structure does not know, a positional
element out of order, an id typo). The `.rpt` file is also written
next to the source, so it can be opened directly.

## In the web

The web interface shows per-file status and the translation report of
each source of the project.

## Common errors and what they mean

| Report entry | Meaning | Fix |
|---|---|---|
| unknown group | a group class the structure does not define | check the class name; if the source type needs it, extend the structure (see [Defining new source types](../defining_new_source_types/defining_new_source_types.md)) |
| element out of position | a positional element where the structure expects another | count the `/` slots against the structure definition |
| missing mandatory element | a `guaranteed` element is absent | fill it, or use `?` if the source does not give it |
| duplicate id | the same `id=` used twice in the file | ids must be unique within the file |

Once files translate without errors, import them — see
[Importing into the database](importing_into_the_database.md).
