# Transcribing a source

This page walks through the first real task in Timelink: transcribing
a historical source into
[Kleio notation](../../reference/kleio_notation_reference.md). We use
a parish baptism register, the classic case; other source types differ
in vocabulary, not in method.

## Before you start

* A project exists (see [Create a new project](../setting_up_a_project/create_a_new_project.md))
  with `sources/` and `structures/` directories.
* You know which **structure** (schema) your source type uses —
  parish registers use the `gacto2` base vocabulary (`fonte`, `bap`,
  `n`, `pai`, `ls`…); other types may need their own, see
  [Defining new source types](../defining_new_source_types/defining_new_source_types.md).
* An existing file of the same type is the best template: copy its
  first line and the shape of its groups.

## The source

Book of baptisms, Contenda parish, 1685 (fol. 30-34):

> *Aos oito dias do mês de julho de mil seiscentos e oitenta e cinco,
> batizei eu, padre Manuel Cordeiro, a Maria, filha de Manuel Madeira
> e de sua mulher Domingas João, moradores no Alencarce; foi padrinho
> António Jorge, madrinha Maria, solteira, do Alencarce.*

## Transcription, step by step

**1. The source unit.** One file per source unit (a book, a year, a
 coherent dossier). The top group declares it:

```
fonte$b1685/tipo=reg paroquiais/localizacao=fol. 30-34/data=16850000/obs=existem baptismos anteriores mas em muito mau estado
```

**2. The act.** One group per act, in the order of the source. The
positional elements of `bap` are id, day, month, year, place,
celebrant — fill with `?` what the source does not give:

```
bap$b1685.1/8/7/1685/?/manuel cordeiro
```

**3. The people.** Indented under the act, one group per person. The
baptized child first (`n`), then the kin groups the structure provides
(`pai`, `mae`, `pad`, `mad`…). Give each an explicit id built from the
act id, so other files can refer to them:

```
n$maria/f/id=b1685.1-per1

   pai$manuel madeira/m/id=b1685.1-per1-per2
      ls$residencia/alencarce

   mae$domingas joao/f/id=b1685.1-per1-per3

   pad$antonio jorge/m/id=b1685.1-per4
      ls$residencia/alencarce

   mad$maria/f/id=b1685.1-per5
      ls$ec/s
      ls$residencia/alencarce
```

Note the details the source gives, attached where they belong: the
family's residence as `ls$residencia` inside the father, the
godmother's marital status as `ls$ec/s` (estado civil: solteira).

**4. Doubts and original wording.** Keep the source's voice with
aspects: `maria donana?` (uncertain reading),
`ls$residencia/cumieira, freguesia de Penela%termo de penela`
(normalized value, original wording after `%`), `#` for comments.

The full file for this example ships with Timelink as
`b1685.cli` in the reference sources.

## Working habits

* **Follow the source order.** The transcription should read like the
  source; the database does not care about order, the historian does.
* **Do not infer.** If the source says "moradores no Alencarce" for
  the couple, the residence is attached where the source puts it (the
  father); generalizations ("therefore the mother also lived there")
  are for the *inference* stage, not for the transcription.
* **Re-transcribe freely.** Ids keep the database in sync when the
  file changes (see
  [Processing new versions of sources](../../reference/processing_new_versions_of_sources.md));
  correcting a transcription is never a reason to fear re-importing.
* **Save and translate often.** The next step —
  [Translating](translating.md) — checks the file against its
  structure and reports errors while the source is still open in
  front of you.
