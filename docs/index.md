## 1 Introduction

### [[1.1_What_is_Timelink|1.1 What is Timelink]]

### [[1.2_About_Kleio_notation|1.2 The Kleio Notation for Historical Sources]]

### [[1.3_Timelink_Database|1.3 The Timelink Database]]


## 2 Tutorial


### [[2.1_Setting_up_a_Timelink_project]]

#### [[2.1.1 Creating a repository for your project]]
#### [[2.1.2. Cloning the repository in your computer]]
#### [[2.1.3. Adding sample files]]
#### [[2.1.4. Adding your own files]]

	2. [[Using VSCode to transcribe historical sources]]
		1. The Timelink VSCode extension
		3. Using one of the existing source formats
	3. [[Updating the database with new source transcriptions]]
	4. [[Exploring the database]]
		1. Database status
		2. Listing entities
		3. Creating tables from attributes
		4. Fetching entities
		5. Exploring relations
		6. Infering networls
3. Reference
	1. Kleio Notation Reference
		1. Groups, elements and aspects
		2. Unique identification of entities (ids)
			1. Groups that require explicit ids
			2. Automatically generated ids
			3. Identifying two entities as the same
		3. Linking to external information (linked data)
		4. List of predefined kleio groups
			1. Persons (person, actorm, actorf)
				1. Using groups to register kinship (pn, mn, marido, mulher, ...)
			2. Objects and abstractions
			3. Attributes
				1. Using ls\$ or atr\$, attr\$ groups.
			4. Relations
			5. Acts
				1. Generic acts
				2. Generic lists
				3. Pre-defined acts:
					1. Parish registers: bap, b, cas, o, obito
					2. Notarial records: escritura, perdao, ....
				4. Special types of acts
					1. Cartas
					2. Devassas
		5. Defining new source formats
		6. Defining new database tables
		7. Defining new inference rules
	2. Database reference
		1. Tables
			1. Entities
			2. Classes
			3. Persons
			4. Objects
			5. Attributes
			6. Relations
			7. Links
		2. Views
	3. Projects
		1. Structure of a Timelink project
			1. Sources
			2. Structures
			3. Notebooks
			4. Inferences
			5. Mappings
	4. Timelink in Jupyter notebooks and Python applications
		2. `TimelinkNotebook` class
			1. Setting up
			2. Updating the database
			3. Showing database status
			4. Inspecting Kleio files
		4. `TimelinkDatabase` class
			1. Access to the Timelink tables and ORM classes
			2. Querying the Timelink database
		5. `TimelinkKleioServer` class
		6. Timelink with Pandas
		7. Generating Kleio sources from Python code
			1. Python representation of Kleio groups, elements and aspects
4. Timelink WebApp
5. Timelink Command Line Interface
6. Developer reference
	1. timelink-py Python Library
	3. Kleio Server API
	5. Timelink Server API 
	6. Source code repositories
		1. Timelink.py
		2. Kleio-server
		3. Timelink-project-template
		4. Timelink-tutorial-project
		5. Timelink-sample-data