# Adding your own files

Where your Kleio files go, and how to start one.

## Where files live

Kleio files live in the project's `sources/` directory, organized in
subdirectories as you find useful (by source type, by archive, by
year). The
[schema location rules](../../reference/kleio_schema_files_location.md)
find the applicable structure through the same tree, so keep files of
one source type together in one subtree.

## Starting a file from an existing one

The best template is an existing file of the same source type: copy
it, delete its acts, keep the `fonte` group and the first line, and
change the ids to the new source unit. The reference sources that ship
with Timelink (parish baptisms `b1685.cli`, the Dehergne repertoire
`dehergne-a.cli`, chronologies, and others) cover the common cases.

Minimum skeleton for a parish-type source:

```
kleio$gacto2.str

   fonte$b1686/tipo=reg paroquiais/localizacao=fol. 35-40/data=16860000
```

Then add acts and people following
[Transcribing a source](transcribing_a_source.md).

## Starting a file for a new source type

If no existing structure fits, you are defining a new source type —
see [Defining new source types](../defining_new_source_types/defining_new_source_types.md):
first write the structure (YAML) in `structures/`, then transcribe
against it.
