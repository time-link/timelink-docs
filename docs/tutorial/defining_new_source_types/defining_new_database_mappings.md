# Defining source to database mappings

Once a new source type is defined it must be mapped to existing, or
new, database tables. This correspondence between the source and the
database is called a _mapping_. In practice **most structures need no
mapping file at all** — read on to know when you do.

## How `timelink` determines a mapping

Group classes form an inheritance hierarchy (the `source` key of
[structure files](defining_new_source_types.md)). The database mapping
travels along that hierarchy: a group that inherits from a core group
is stored exactly like its parent — new names for old groups, no new
tables. From the mapping scenarios:

1. *New names for base groups* (`baptism` instead of `act`,
   `father` instead of `person`) — no mapping needed, inheritance
   carries the mapping.
2. *Containment rules* — a structure concern, not a database one.
3. *New names for builtin elements* (`nome` for `name`) — inherited
   mapping again.
4. **New groups with new elements that store new information** — this
   is the case that requires a mapping: a new database class and
   table.
5. *Inference rules* — inference files, not mappings (see
   [Timelink data concepts and models](../../reference/source_db_mappings_semantics.md)).

## Structure of mapping files

A mapping file states, for a group, which database class stores it and
which columns hold its elements. Current notation:

```prolog
mapping person to class person.
class person super entity table persons
with attributes
    id column id baseclass id coltype varchar colsize 64 colprecision 0 pkey 1
 and
    name column name baseclass name coltype varchar colsize 128 colprecision 0 pkey 0
 and
    sex column sex baseclass sex coltype char colsize 1 colprecision 0 pkey 0
 and
    obs column obs baseclass obs coltype varchar colsize 16654 colprecision 0 pkey 0 .
```

* `mapping X to class Y.` — the Kleio group `X` is stored as entities
  of database class `Y`.
* `class Y super entity table T` — class `Y` specializes `entity`,
  stored in table `T` (joined-table inheritance: one row in
  `entities`, one in `T`, same id).
* the `with attributes` lines — element name, column name, base
  element class, column type/size, and whether it is part of the
  primary key (`pkey`, in order).

The full field-by-field semantics are in
[Timelink data concepts and models](../../reference/source_db_mappings_semantics.md);
the older Prolog-style syntax page is
[Source to database mapping syntax](../../reference/source_db_mapping_syntax.md)
(the notation is being refactored to YAML — new structures should
check the current form in the timelink-kleio repository).

## Example

A `baptism` group that adds `date-of-birth` to the `act` information:

1. Structure: `baptism` extends `act`, adding element `date-of-birth`.
2. Mapping: new class `baptism` super `act` table `baptisms`, with a
   column for `date-of-birth`; all other elements arrive through the
   `act` inheritance.
3. After the next update, the importer creates the `baptisms` table on
   first import of a source using the structure.

Then query it — see
[Querying user defined structures](querying_user_defined_structures.md).
