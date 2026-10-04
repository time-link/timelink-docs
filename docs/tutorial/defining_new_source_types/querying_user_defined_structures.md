# Querying user defined structures

When a structure defines new database classes/tables (see
[Defining source to database mappings](defining_new_database_mappings.md)),
they appear in the database like any other entity class — and can be
introspected and queried the same way.

## Introspecting the database

`TimelinkDatabase` knows what it contains:

```python
from timelink.api.database import TimelinkDatabase

db = TimelinkDatabase("my_project", "sqlite")

db.table_row_count()   # [('persons', 1204), ('acts', 356), ...]
db.get_models_ids()    # entity classes: ['person', 'act', 'source', ...]
db.describe(None)      # group → table → ORM model mapping
db.get_columns("persons")  # columns and types of one table
db.view_names()        # database views
```

**Never assume the class list** — classes are dynamic, stored in the
database itself (`classes` and `class_attributes` tables); a project
can define new Kleio groups that map to new tables created at import
time.

## Building queries with `SQLAlchemy`

Query through the ORM with the session context manager; entity rows
join to their specialization tables by id:

```python
from timelink.api.models import Entity, Person

with db.session() as session:
    # people with a name starting with "manuel"
    query = session.query(Person).filter(Person.name.like("manuel%"))
    for person in query.all():
        print(person.id, person.name, person.sex)
```

Class-specific tables are reached through the entity's class
(`entities.class` says which specialization table completes a row);
generic cross-class queries go through `Entity` and the
attributes/relations tables, for which the pandas helpers below are
usually faster.

## With pandas helpers

The functions of [Working with pandas](../working_with_notebooks/working_with_pandas.md)
work for user-defined classes too, because they query attributes and
relations generically:

```python
from timelink.pandas.entities_with_attribute import entities_with_attribute

df = entities_with_attribute(
    the_type="residencia",     # any attribute type, from any structure
    column_name="Residência",
    db=db,
)
```

Attribute vocabularies are data-dependent: list the existing values
first (`attribute_values(the_type=..., db=db)`) before filtering on
them. The tutorial notebooks that ship with Timelink
(`A2-database-explore.ipynb`, `DEV-01-using-orm.ipynb`) go deeper into
both styles.
