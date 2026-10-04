# Working with pandas

After [importing](../processing_source_transcriptions/importing_into_the_database.md),
the database is explored most comfortably from notebooks, with the
pandas helpers of the `timelink` package. This page is the starter
kit; the tutorial notebooks that ship with Timelink
(`02-tutorial.ipynb`, `A2-database-explore.ipynb`) walk the same
ground with more examples.

## Setting up

```python
from timelink.notebooks import TimelinkNotebook

tlnb = TimelinkNotebook()   # finds the project database, attaches the Kleio server
tlnb.print_info()           # database type, tables, row counts
```

`TimelinkNotebook` is a convenience wrapper around
`TimelinkDatabase`; for direct access use
`TimelinkDatabase("my_project", "sqlite")` and pass `db=` to the
functions below.

## `entities_with_attribute`

Fetches entities that have certain attributes, producing a data frame
where entities are rows and attributes are columns. Parameters limit
by attribute type and value (wildcards allowed), by date range, by
Kleio group name, and by list of entity ids; several attributes can be
aggregated into one column:

```python
from timelink.pandas.entities_with_attribute import entities_with_attribute

# people with a residence in 1685, residence and status as columns
df = entities_with_attribute(
    the_type="residencia",
    the_value="alencarce%",
    column_name="Residência",
    dates_in=(None, "16851231"),
    db=tlnb.db,
)
df.info()
df.head(20)

# several attributes in one column
faculdade = entities_with_attribute(
    the_type=["faculdade", "grau"],       # list = exact match on each
    column_name="Formação",
    db=tlnb.db,
)
```

Empty columns (nobody has that attribute) can be dropped with
`df.dropna(axis=1, how="all")` before display.

## `attribute_values`

Before filtering on values, **list the vocabulary** — attribute
values are data-dependent, and a wrong value silently returns
nothing:

```python
from timelink.pandas.attribute_values import attribute_values

values = attribute_values("residencia", db=tlnb.db)
values  # value, count, first and last date seen
```

The same function counts attributes from an existing data frame
(`df=`), and `group_attributes` shows all attributes of one entity or
group of entities.

## Searching by name

```python
from timelink.pandas import pname_to_df

people = pname_to_df("manuel cordeiro", db=tlnb.db)   # particles (de, da...) handled
```

Remember: the same historical person appears once per source with
different ids ([About timelink databases](../../introduction/timelink_database.md)) —
counting persons means counting mentions unless identifications were
made.

## From data frame to Kleio notation

To inspect an entity in full — its groups, attributes and relations,
rendered back in Kleio notation with provenance — fetch it in a
session and call `to_kleio()`:

```python
from timelink.api.models import Person

with tlnb.db.session() as session:
    person = session.get(Person, df.iloc[0]["id"])
    print(person.to_kleio())
```

Every row can thus be traced back to the source line it came from.
