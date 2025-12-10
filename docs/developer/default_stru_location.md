# Default structure (schema) location

Each Kleio source file is associated with a schema definition. `Timelink` provides different methods for associating source files and schemas, by placing schema files in conventional locations (see [Kleio schema files location](reference/kleio_schema_files_location.md)).

If the user provides no information about the schema file to use the `kleio server` selects a default file, that can be set using environment variables. 

As last ressort the `kleio server`will use the builtin schema file, derived from the legacy `gacto2.str` file of the `Timelink-mhk` version.

Here are the details of the process of determining the default schema, in the case that the user did not provide one.

The default structure of the current installation of Kleio Server, determined as follows
	- If the environment variable `KLEIO_DEFAULT_STRU`exists and contains a path to an existing file this will be considered the default structure.
	- A file named either 'sources-structure.yaml' or 'gacto2.str' will be searched, in order
		- Env variable KLEIO_STRU_DIR`.
		- Env variable `KLEIO_CONF_DIR` / `str`
		- `structures` directory of the `timelink-home` (see [web_timelink_home_layout](web_timelink_home_layout.md))
		- `str` directory in the Kleio Server working directory (normally inside a Docker container)
		- the Kleio Server working directory.

Note that if a `gacto2.str` is processed a `yaml` copy names `gacto2-structure.yaml` is generated which can be renamed `sources-structure.yaml` for  default usage in subsequent runs.