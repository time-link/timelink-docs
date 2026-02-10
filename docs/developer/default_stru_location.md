# Default structure (schema) location

Each Kleio source file is associated with a schema definition. `Timelink` provides different methods for associating source files and schemas, by placing schema files in conventional locations (see [Kleio schema files location](reference/kleio_schema_files_location.md)).

If the user provides no information about the schema file to use the `kleio server` selects a default file, that can be set using environment variables. 

As last ressort the `kleio server`will use the builtin schema file, derived from the legacy `gacto2.str` file of the `Timelink-mhk` version.

Here are the details of the process of determining the default schema, in the case that the user did not provide one.

1. if the environment variable `KLEIO_DEFAULT_STRU`exists and contains a path to an existing file will be used.
2. A file named 'sources-structure.yaml' or , alternatively, 'gacto2.str' if it exists in the following directories:
	1. Directory path in the environment variable KLEIO_STRU_DIR`.
	2. `structures` directory of the `timelink-home` for single project layouts (see [web_timelink_home_layout](web_timelink_home_layout.md))
	3. Directory `stru` in the directory path in`KLEIO_CONF_DIR` (usually `kleio_home/system/conf/stru`, but can be `.kleio/conf` in single project layouts).
	4. `system/structures`in `timelink_home` for multi project layouts  (see [web_timelink_home_layout](web_timelink_home_layout.md))
	5. `str` directory in the Kleio Server working directory (normally inside a Docker container)
	6. The Kleio Server working directory.

Note that if a `gacto2.str` file is processed a `yaml` copy named `gacto2-structure.yaml` is generated with the same content, which can be renamed `sources-structure.yaml` for  default usage in subsequent runs.

## Best practices

## Setting the default schema for a given `Kleio` home

1. `timelink_home/system/conf/kleio/sources-structure.yaml` for multi project layouts (one `kleio server` serving multiple projects)
2. `timelink_home/structures/sources-structure.yaml`
3. 



