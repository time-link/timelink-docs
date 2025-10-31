# Web: Timelink home directory structure
## What is a _Timelink home_

"Timelink home" represents the base directory of a specific `timelink` web site.  The `timelink` web application will serve information from that base directory.

The `timelink` webapp can be used in two modes:

1. single-user, single-project mode
2. multi-user, multi-project mode.

In both cases the webapp is associated with a base directory, called `timelink_home`.  The internal layout of the `timelink_home` is different in both cases, as explained bellow.

Note that in a given machine it is possible to have multiple `timelink_home` directories, each one serving a different port and different projects.

## What is a "project"

A "project" in `timelink` is the association of a set of `kleio` files with a database.

Normally, the information about a project is kept in a directory in the filesystem, from where `timelink` obtains the necessary information.

But it is possible that the webapp runs in a machine,  publishing a project with files in another machine and the database in yet another.

This is possible because `timelink` manages files through a Kleio Server and the database through a SQLAlchemy url, which can reference a remote database server (e.g. postgres).


## Single-user, single project timelink-home

In a single-user instalation the web app will serve one project, and timelink-home is a project directory, with a standard structure:


	├── single-project   <-- timelink-home
	│ ├── database
	│ ├── extras
	│ ├── inferences
	│ ├── notebooks
	│ ├── sources
	│ └── structures
	│ .timelink-project # place holder file to indicate this is a timelink project directory
## Multi-user, multi-project timelink-home

In a multi-project installation the web app will serve multiple projects and users, and timelink_home is a directory that contains a `projects` with mujltiple subdirectories, and other support directories.

	├── multiproject-dir  <-timelink-home
		├── projects
		│   ├── test-project
		│   │   ├── database
		│   │   │   └── sqlite  <-- each project its database
		│   │   ├── identifications
		│   │   ├── inferences
		│   │   ├── notebooks
		│   │   ├── sources
		│   │   ├── structures
		│   └── web-tests
		│       ├── database
		│       │   └── sqlite
		│       ├── extras
		│       ├── identifications
		│       ├── inferences
		│       ├── notebooks
		│       └── sources
		└── system
			├── db
			│   └── sqlite
			└── structures
		.timelink-home # place holder file to indicate this is a timelink home directory


> Same directory can be served as a single project or as part of a multi-project site
>
> A project directory inside a mutiproject dir can be accessed both as stand alone single user or as part of a web interface for multiple projects and multiple users. It depends on the base directory given to the start command. Multiple variants can exist in the same machine, serving different ports.
>

## Special cases

### Single project, multiple subprojects

In some complex projects, there can be more than one project directory for different types of sources, managed by different researchers and a too level project that aggregates all of them.

This is implemented  with git [submodules] (https://git-scm.com/book/en/v2/Git-Tools-Submodules).

This type of structure is treated as a single-project

In this case the structure is:

	| toplevel-project  <-- timelink-home
	├── database
	│   └── sqlite   <-- joint database all subprojects
	├── extras
	├── identifications
	├── inferences
	├── notebooks
	├── sources   <-- sources directory contain other project directories
	│   ├── china-coimbra-biografias  <-- sub-project, git submodule
	│   │   ├── database   <-- project database
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   └── structures
	│   ├── china-cronologia    <-- sub-project, git submodule
	│   │   ├── database   <-- project database
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   └── structures
	│   ├── dehergne-repertoire   <-- sub-project, git submodule
	│   │   ├── database  <-- project database
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   ├── structures
	│   └── jesuitas-franco-imagem-virtude   <-- sub-project, git submodule
	│       ├── database <-- project database
	│       ├── extras
	│       ├── identifications
	│       ├── inferences
	│       ├── notebooks
	│       ├── sources
	│ .timelink-project # place holder file to indicate this is a timelink project directory


### Legacy mhk-home layouts

These are directory structures used in the previous version of `timelink` known as `MHK`.

It is basically a multi-project layout, where the toplevel directory sources contains the equivalent of projects.

	├── app
	│   ├── java
	│   │   ├── lib
	│   │   └── pt
	│   └── scripts
	│       ├── container
	│       └── host
	├── sources  <- projects directory
	│   ├── COMMEMORtis_SB  <-- project
	│   │   ├── database
	│   │   ├── etc
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   ├── structures
	│   │   └── system
	│   ├── china-coimbra  <-- project
	│   │   ├── database
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   ├── structures
	│   │   └── system
	│   ├── china-coimbra-biografias   <-- project
	│   │   ├── database
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   └── structures
	│   ├── dehergne   <-- project
	│   │   ├── database
	│   │   ├── etc
	│   │   ├── extras
	│   │   ├── identifications
	│   │   ├── inferences
	│   │   ├── notebooks
	│   │   ├── sources
	│   │   ├── structures
	│   │   └── templates
	├── system  <-- MHK stuff
	│   ├── caddy
	│   │   └── site
	│   ├── conf
	│   │   ├── caddy
	│   │   ├── kleio
	│   │   └── mysql
	│   ├── db
	│   │   ├── mhk
	│   │   └── mysql
	│   ├── logs
	│   │   ├── kleio
	│   │   └── tomcat
	│   └── vscode
	└── users  <-- MHK user configuration
	    ├── china_coimbra
	    │   └── conf
	    ├── commersb
	    │   └── conf
	    ├── commerst
	    │   └── conf
	    ├── dehergne
	    │   └── conf
	    ├── dehergne-locations
	    │   └── conf
	    ├── demo
	    │   └── conf
	    ├── fauc
	    │   └── conf
	    └── mhk
	        └── conf