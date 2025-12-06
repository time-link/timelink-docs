# Kleio Schema files syntax (YAML)

This document describes the structure of the YAML files used in the `timelink-kleio` project.

## General Structure

The YAML files define groups, elements, and their relationships for historical data processing. 

A “group” corresponds to the concept of an entity in a database or a class in programming languages.  Groups contain “elements” that correspond to fields in databases or attributes in programming language classes. 

Both element and groups can inherit from other higher level elements and groups, keeping some of their characteristics and changing others. 

This creates a hierarchy of groups and elements that is also used for data typing or triggering default semantic effects. 

Below is a breakdown of the key components used to define groups and elements. 
### Top-Level Keys

- **file**: Metadata about the YAML file itself.
  - `name`: The name of the file.
  - `description`: A description of the file's purpose.
- **include**: References to other YAML files to include.
- **group**: Defines a group. 
- **element**: Defines an element. 

---

### `group` Key

Each `group` represents a logical collection of related data. Below are the common fields:

- **name**: The name of the group.
- **description**: A textual description of the group.
- **source**: The source or parent group this group is derived from. This defines an inheritance hierarchy. 
- **position**: list of elements that appear after the group name. These elements have 
- **also**: Additional fields that are part of the group.
- **guaranteed**: Fields that are mandatory for the group.
- **arbitrary**: Other groups that can be included in the current group 
- part: Same as "arbitrary"
- **idprefix**: A prefix used for IDs in the group.
- **part**: Sub-elements or components of the group.
- **prefix**: A prefix for the group (if applicable).
- **suffix**: A suffix for the group (if applicable).

---

### Example Structure

Here is an example of a `group` definition:

```yaml
- group:
    name: acto
    description: >
      Actos genericos, servem para vereacoes etc. Compostos por items
    position: [id, tipo, dia, mes, ano, loc, obs]
    also:
    - ref
    - loc
    - obs
    - presente
    - presente-f
    - referido
    - referida
    - item
    - ls
    - atr
    - rel
    counter: 0
    guaranteed:
    - id
    - dia
    - mes
    - ano
    idprefix: his
    prefix: non
    source: pt-acto
    suffix: non
```

### `element` Key

Each `element` represents an individual data field. Below are the common fields:

- **name**: The name of the element.
- **description**: A textual description of the element.
- **identification**: Identification type (e.g., `non` for none).
- **source**: The source of the element's value.
- **prefix**: A prefix for the element (if applicable).
- **suffix**: A suffix for the element (if applicable).

---

### Notes

- The `include` key allows modularity by referencing other YAML files.
- The `part` field in groups specifies sub-elements or components.
- Fields like `also`, `arbitrary`, and `guaranteed` define the flexibility and constraints of the group.

For more details, refer to the specific YAML files in the `tests/kleio-home/structures` directory.