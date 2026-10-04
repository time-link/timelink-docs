# Getting started

The 10-minute path from zero to a queried database. Each step links
to the detailed page.

## 1. Install

```bash
pip install timelink-py
```

[Docker](https://www.docker.com/) must be installed and running — the
Kleio server (translation) runs in a Docker container. Details and
options: [Installing](introduction/installing_timelink.md).

## 2. Create a project

The quickest path is the project template on GitHub: create a
repository from the *timelink-project-template*, clone it, and open it
in VS Code. This gives you the standard directories (`sources/`,
`structures/`, `database/`, `notebooks/`) and a ready notebook
environment. Details:
[Create a new project](tutorial/setting_up_a_project/create_a_new_project.md)
and [Timelink home](reference/timelink_home.md) for the layouts.

## 3. Understand the pipeline (2 minutes)

Read [How Timelink works](introduction/system_overview.md): you
transcribe sources in [Kleio
notation](reference/kleio_notation_reference.md); the Kleio server
translates them to XML; the importer loads them into a relational
database; you explore with notebooks, the web app, or AI agents.

## 4. Add a source and transcribe it

Copy a reference file of your source type into `sources/` and adapt
it, or transcribe from scratch — the guided walkthrough is
[Transcribing a source](tutorial/processing_source_transcriptions/transcribing_a_source.md).

## 5. Translate and import

One call does both:

```python
from timelink.notebooks import TimelinkNotebook

tlnb = TimelinkNotebook()
tlnb.update_from_sources()
tlnb.get_import_status()   # per file: translation and import status
```

Errors, if any, come with reports —
[Checking translation results](tutorial/processing_source_transcriptions/checking_translation_results.md),
[Importing into the database](tutorial/processing_source_transcriptions/importing_into_the_database.md).

## 6. Explore

```python
from timelink.pandas.entities_with_attribute import entities_with_attribute

df = entities_with_attribute(the_type="residencia", db=tlnb.db)
df.head(20)
```

More: [Working with pandas](tutorial/working_with_notebooks/working_with_pandas.md).

## Where to go next

* New source type? [Defining new source types](tutorial/defining_new_source_types/defining_new_source_types.md)
* Prefer the web? `timelink start` (see [Launching the web interface](admin/launching_web_app.md))
* Working with AI agents? [Timelink and AI agents](ai_agents/index.md)
