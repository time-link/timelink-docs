# Location of source schema files

The Kleio server has a builtin generic schema / structure file.

Individual projects can define their own schema files using [Kleio Schema Syntax](kleio_schema_syntax.md)

## Rules for associating structure files to kleio files

The `Kleio` processor locates the relevant structure file for a given source (kleio) file as follows:

1. If the kleio file start with `kleio$PATH-TO-FILE` the path is used to locate the structure file (more information on paths bellow)
2. If a file exists with the same base name and "-structure.yaml" suffix , e.g., for file `mysource.cli`  a file `mysource-structure.yaml` if it exists will be used
3. Look for a file that ends in “-structure.yaml.”  It must have the same name as the folder it sits in.  If the folder is called “my_sources,” the file should be named “my_sources-structure.yaml.”  This file can live in that folder or any folder above it.
4. A file named `sources-structure.yaml` in the same directory or parent directories.
5. The default structure of the current installation of Kleio Server, determined as follows
	- If the environment variable `KLEIO_DEFAULT_STRU`exists and contains a path to an existing file this will be considered the default structure.
	- A file named either 'sources-structure.yaml' or 'gacto2.str' will be searched, in order
		- Env variable KLEIO_STRU_DIR`.
		- Env variable `KLEIO_CONF_DIR` / `str`
		- `structures` directory of the `timelink-home` (see [web_timelink_home_layout](web_timelink_home_layout.md))
		- `str` directory in the Kleio Server working directory (normally inside a Docker container)
		- the Kleio Server working directory.

## Including structure files in other structure files

A given structure file can include other structure files by using the `include` key, e.g.

```
- file: 
	- name: mystru.yaml
	- description: my own structure file
- include: structures.pt-system-structure.yaml
```

The path in `include`uses the following conventions:
- `structures` at the beginning refers to the directory with the same name at the same level as the `sources` directory that contains the kleio files.
- `system` refers to the builtin structures distributed with kleio server.
- `.` refers to the directory of the structure file that contains the `include`directive.


## Best practices

1. In small projects create a `sources-structure.yaml` and place it at the root of the `sources` directory.
2. For more complex projects create sub directories inside `sources` and place files named `DIR_NAME-structure.yaml` at the root of each directory. 
3. If the same set of structure files are used across different projects and need to be maintained in sync, then it is better to keep them in the `structures` directory of the repository and refer to them with `include` in minimal structure files associated by the rules above.

