# Location of source schema files

The Kleio server has a builtin generic schema / structure file.

Individual projects can define their own schema files using [Kleio Schema Syntax](kleio_schema_syntax.md)

## Rules for associating structure files to kleio files

The `Kleio` processor locates the relevant structure file for a given source (kleio) file as follows:

1. If the kleio file start with `kleio$PATH-TO-FILE` the path is used to locate the structure file (more information on paths bellow)
2. If a file exists with the same base name and "-structure.yaml" suffix , e.g., for file `mysource.cli`  a file `mysource-structure.yaml` if it exists will be used
3. In the containing directory or its parents a file with the same name as the directory and `DIRNAME-structure.yaml`, e.g., for a file in `my_sources/a_source.cli` a file `my_sources/mysources-structure.yaml` will be used, also if the yaml file is in an upper directory (then the name should match the enclosing directory).
4. A file named `sources-structure.yaml` in the same directory or parent directories.

## Including structure files in other structure files

A given structure file can include other structure files by using the `include` key, e.g.

```
- file: 
	- name: mystru.yaml
	- description: my own structure file
- include: structures.pt-groups.yaml
```

The path in `include`uses the following conventions:
- `structures` at the beginning refers to the directory with the same name at the same level as the `sources` directory that contains the kleio files.
- `system` refers to the builtin structures distributed with kleio server.
- `.` refers to the directory of the structure file that contains the `include`directive.


## Best practices

If no specific structure file is needed then `kleio` server will use the default file.

1. In small projects create a `sources-structure.yaml` and place it at the root of the `sources` directory.
2. For more complex projects create sub directories inside `sources` and place files named `DIR_NAME-structure.yaml` at the root of each directory. 
3. If the same set of structure files are used across different projects and need to be maintained in sync, then it is better to keep them in the `structures` directory of the repository and refer to them with `include` in minimal structure files associated by the rules above.

