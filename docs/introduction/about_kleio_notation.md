# Kleio notation for historical sources

`Kleio` is a notation for the transcription of historical sources
developed by Manfred Thaller. Its aim is to transcribe the relevant
information from a historical source in a form close to the original
in terms of the sequence and structure of the information: a Kleio
transcription is *readable*, can preserve original orthography when
needed, can include comments by the transcriber, and is at the same
time formal enough to be processed by software into a relational
database.

The notation is based on the following components: **groups**,
**elements** and **aspects**. A first taste, from a parish baptism
register:

```
bap$b1685.1/8/7/1685/?/manuel cordeiro

   n$maria/f/id=b1685.1-per1

      pai$manuel madeira/m/id=b1685.1-per1-per2
         ls$residencia/alencarce
```

Read: a baptism act on 8/7/1685 celebrated by Manuel Cordeiro; the
baptized, Maria, female; her father, Manuel Madeira, living in
Alencarce.

To go further:

* [Basic concepts](basic_concepts.md) — how the source-oriented model
  of Kleio relates to the person-oriented model of the database;
* [Kleio notation reference](../reference/kleio_notation_reference.md)
  — the complete syntax, group by group;
* [Transcribing a source](../tutorial/processing_source_transcriptions/transcribing_a_source.md)
  — a guided first transcription.
