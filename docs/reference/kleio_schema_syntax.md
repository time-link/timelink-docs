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
- **position**: List of elements that appear after the group name. Values of elements can be specified
- **also**: Additional fields that are part of the group.
- **guaranteed**: Fields that are mandatory for the group.
- **contains**: List of other groups that can be included in the current group ("part" and "arbitrary" were variants of "contains" currently deprecated; use "contains")
- **idprefix**: A prefix used for IDs in the group.


---

### Example Structure

Here is an example of a `group` definition:

```yaml
- group:
    name: historical-act
    description: >
        Represents an historical act, i.e. a record of an event ,
        something that happened at a moment and place in time.
        This form is used for records such as parish records notarial acts.
    source: event
    position: [id, type, date]
    guaranteed: [id, type, date]
    also: [loc, ref, obs, day, month, year]
    contains: [person, object, geoentity, abstraction, ls, atr, rel, cevent, end]
    idprefix: hac
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