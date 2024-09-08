The Kleio server has a builtin generic schema / structure file.
Individual projects can define their own schema.

The standard source repository has a `sources` directory at the same level of a `structures` directory.

#### Files in the `structures` directory
For a given source file to be translated with path `sources/SUBPATH/file.cli` the default stru would be, in order:

* `structures/SUBPATH/file.str`  
* `structures/SUBPATH2/gacto2.str`
	 where `SUBPATH2` is a parent path of SUBPATH
* `structures/DIRNAME.str`  where DIRNAME, is the name of a dir in SUBPATH
* `structures/gacto2.str` can be replaced by `sources.str`  for clarity in all patterns.

This allows for a source repository to have formats specific to a single file, a sub directory of files or to all the sources in the repository:

*  `structures/baptisms/baptism-index.str` format specific for `sources/baptisms/baptism-index.cli` 
* `structures/baptisms/gacto2.str` or `structures/baptisms/sources.str` for all sources inside `sources/baptisms` and sub directories
* `structures/baptisms.str`  for all sources in `sources/baptisms` (not sure about this one, the advantage is to manage more easily different structure files with different names)
* `structures/gacto2.str` or `structures/sources.str` default str for all sources.

See source code for this at [file apiTranslations.pl](https://github.com/time-link/timelink-kleio/blob/51ac4e3821c39475837f30443400c8d05e07d916/src/apiTranslations.pl#L316-L366)
