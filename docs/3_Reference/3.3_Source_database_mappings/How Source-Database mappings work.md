
# Timelink data concepts and models


The uniqueness of Timelink resides in its capability of processing rich
textual transcriptions and insert information in a structured relational
database, that can be explored with modern data science tools.

This document explains at a technical level how the mapping between the source
transcription and the database works. For more information about the `kleio` notation used 
for source transcriptions see: [3.1 Kleio Notation Reference](05%20Timelink/timelink-docs/docs/3_Reference/3.1_Kleio_Notation_Reference/index.md)

## Summary

Timelink uses a dual model to represent historical information.

-   A *source-oriented text-oriented data model* is used to transcribe
    sources with little loss of information.
-   A *person-oriented relational database model*, consolidates biographical data,
    handles inference of networks and reversible record linking

The ``Kleio`` notation (Manfred Thaller) is used for source-oriented
data input.

A relational database structure is used to store person-oriented data, 
keeping the original source context.

A special software, *the Kleio translator* processes text transcriptions
of the sources in ``kleio`` notation and generates data for the
the person-oriented database.

This solves the inevitable tension between a source-oriented model, 
that aims to preserve the rich complexity of the data source
and an analytical mode that requires a formal representation of
data and the expression of complex queries.

## The Source Oriented Model

Uses a containment structure of ``source->act/events->persons`` and ``objects``.

The *source oriented model* uses a number of key terms in a formal way:
``source``, ``act``, ``person``, ``object``, ``function``, ``attribute``
and ``relation``.

-   A historical ``source`` contains one or more ``acts``.
-   An ``act`` is a records of events described in the sources
    (a baptism, a marriage, a sale contact, a rental contract, ...)
-   An ``act`` contains actors (``persons``) and ``objects``
    (things, properties, institutions, ...).
-   ``persons`` and ``objects`` appear in ``acts`` with specific ``functions``
    (father in a baptism, owner in a sale contract, house in a rental contract).
-   ``Actors`` and ``objects`` are described by ``attributes``
    (name, age, gender, price, area, ...).
-   ``Actors`` and ``objects`` are linked by ``relations``. Relations are described
    by a type (kin, economical, professional), and a value
    (brother, lender, apprentice).
-   Every ``act``, ``function``, ``attribute`` and ``relation`` has a date
    and a link to the point in the original source where it appeared.

## Example of the Kleio notation

A baptism:

    baptism$17/9/1685/parish church
        n$manuel/m
            father$jose luis
                attr$residence/casal da corujeira
            mother$domingas jorge
            gfather$francisco rodrigues/id=b1685.9.17.gf
                attr$residence/moinhos do paleao
            gmother$maria pereira
                rel$kin/wife/francisco rodrigues/b1685.9.17.gf

This example shows an ``act`` (a baptism) that contains five ``persons``:
child ("n"), father, mother, god father and god mother. Two of the people,
the father and the god father have the ``atribute`` *residence*, and the god
mother has a *kin* ``relation`` with the god father.

## The Person Oriented Model

The `Person Oriented Model` represents a biography through 3 domains:

-   Functions (the roles of the person in acts)
-   Attributes
-   Relations

The `Person Oriented Model` is an alternative view on the information recorded
in the sources, in a way that facilitates statistical analysis, network analysis
and prosopographies.

The previous baptism generates information as follows (*italics* show
information inferred by Timelink).

## Entities

| Id             | Class       | Inside           |
|----------------|-------------|------------------|
| bapt1685-1700  | source      | ---              |
| *b1*           | act         | bapt1685-1700    |
| *b1-per1*      | person      | *b1*             |
| b1685.9.17.gf  | person      | *b1*             |
| *b1-per2*      | person      | *b1*             |
| *b1-per3*      | person      | *b1*             |

Note that each *entity* has an unique
identifier: ``id``. Such identifier is necessary to refer unambiguosly
to a ``person``, ``object``, ``act`` or ``source``.

Most ``ids`` are generated automatically by the *Kleio translator* 
when processing the source transcripts,
but in some circunstances they need to be explicitly given, when a link
between two entities needs to be recorded in an non ambiguous way, such as
the relation between godmother and godfather in the example above.

## Persons

| Id             | Nome                | Gender |
|----------------|---------------------|--------|
| *b1-per1*      | manuel              | f      |
| *b1-per2*      | jose luis           | *m*    |
| *b1-per3*      | domingas jorge      | *f*    |
| b1985.9.17.gf  | francisco rodrigues | *m*    |
| *b1.per5*      | maria pereira       | *f*    |

## Attributes

| Entity          | Type      | Value              | Date        |
|-----------------|-----------|--------------------|-------------|
| *b1-per1i*      | residence | Casal da Corujeira | *17/9/1685* |
| *b1985.9.17.gf* | residence | Moinhos do Paleao  | *17/9/1685* |

## Relations

| Origin        | Destination   | Type    | Value     | Date          |
|---------------|---------------|---------|-----------|---------------|
| *b1-per2*     | *b1-per3*     | *kin*   | *husband* | *17/9/1685*   |
| *b1-per5*     | b1985.9.17.gf | kin     | wife      | *17/9/1685*   |
| *b1-per2*     | *b1-per1*     | *kin*   | *father*  | *17/9/1685*   |

## Functions

Functions of people (father,mother, ...) in acts are a special case
of relations linking people to acts, with the type 'function-in-act'.
The same applies to objects, when they appear in acts.

| Origin        | Destination   | Type             | Value     | Date          |
|---------------|---------------|------------------|-----------|---------------|
| b1985.9.17.gf | *b1*          | function-in-act  | gfather   | *17/9/1685*   |
| *b1.per5*     | *b1*          | function-in-act  | gmother   | *17/9/1685*   |

## How translation between SOM and POM works

Timelink contains a set of basic entities: *sources*, *acts*, *persons*,
*objects*, *attributes* and *relations*. For an example such as the previous
one to work, Timelink needs to know the correspondence between the Kleio
notation and the relational database tables, as well as how to infer values
like gender and kin relations.

### Terminology note

When describing both the Source Oriented Model and the Person Oriented Model
different terms are used to describe concepts that are similar.

In both the Source Oriented Model (SOM) and the Person Oriented Model (POM),
we have concepts for entities that existed, such as *sources*, *transcriptions of acts*, *people*, and *objects*.

These entities have *attributes* that provide information about them, such as names, dates, and archival locations.

Additionally, both models include the concept of *relations*, which describe the connections between entities.

For example, with relations, we can specify that person X is the father of person Y or that person Z bought property W.

Since Timelink bridges different types of data models, which have their own literature and terminology, it is sometimes confusing to what exactly terms like "attribute", "entity", "relation" refer to.



In the context of a database, entities such as *persons*, *objects*, *acts*, and *sources* are represented as rows in different database tables. Each table column corresponds to an attribute of the entities of the same type, storing information such as names, dates, and other relevant data.

At a higher level, when describing the structure of information, we will
use the terminology defined by the `Entity-Relationship-Model
<https://en.wikipedia.org/wiki/Entity–relationship_model>`_ (ER Model)

*   Entity: something that existed in the real world:
    sources, acts, people, also "abstractions" like institutions and
    events like baptisms or marriages.
*   Relation: relations between entities
    like kinship relations between
    people, ownership relations between people and properties, roles
    of people participating in acts
*   Attribute: items of information that describe entities and relations
    (names, dates, kinship terms, prices of transactions)
*   Entity-class or entity-type: a category of Entities described by the same attributes
    `person` is a entity class, `building` is
    another entity class and so is `acts`; each is described by different attributes.
*   Entity instance: a specific entity of a specific class
    (the person named Galileo Galillei, the building named 'Tower of Pisa',
    the baptism that occurred in 8/7/1685 in the church of Soure, Portugal ).

We refer to the concepts above to introduce the terminology specific
to the SOM and POM models.

For the SOM the main terms are Group,Element and Aspect used by Manfred Thaller
in the Kleio notation.

-   Group: corresponds to *entities*.
-   Element: corresponds to *attributes*.
-   Aspect: represent extra information about attributes.
    The Kleio notation allows to register not only the core value of an
    attribute but also a comment and the original wording in the document.

In Timelink Kleio groups are used also to record attributes of entities
that vary with time, like residence or profession.

These attributes have
not just a value ("Abbey Road", "Musician") but also have associated a
date. So they have their own attributes (dates for one), like entities.
In the ER Model this type of information is called a "weak entity": they
have their own attributes like entities, but they do not correspond to
something that exists on its own in the real world, they depend on a main
entity.

In the SOM model Kleio groups are also used to record relations.

In the POM we use the terminology of databases: tables and columns.

-   Table: corresponds to entities
-   Columns: corresponds to attributes

In the Person Oriented Model tables are also used to represent relationships
between entities and time varying attributes.

## Mapping Kleio Groups to Database tables

### Overview

The correspondence between the Kleio groups, elements and aspects, on one side,
and tables and columns in a relational database is defined by conventions and
configuration files in Timelink.

Basic correspondence is provided by Timelink for basic entity types
like sources, acts, people, objects. This allows Timelink to process generic
Kleio transcriptions into generic tables as demonstrated in the example of
the baptism above. 

In most cases a transcription closer to the source is desired, either because
of readability (we rather read `baptism$` than  `act$` and `father$` than  `person$ )
or because the source describes entities with specific attributes (for instance
a land property being sold is an `object` which can have special attributes such as
area and a typology like rural/urban).

To be able to use Kleio to record in a format closer to the source we need
to provide Timelink with mapping information between the terminology used in the 
source and the core groups and elements.  

### Mapping scenarios

The mapping configuration process addresses several scenarios of different complexity: 

1. Define new  names for the base groups so that the vocabulary of the transcription is closer to the original source
	- e.g. `baptims` instead of `act`, `father` and `mother` instead of `person` or `land` instead of `object`
2. Define which groups can appear inside other groups.
	- e.g the group "baptism" can only contain groups named `child, father, mother, godfather, godmother`. 
	- This is what is known as a [Meronomy or partonomy](https://en.wikipedia.org/wiki/Meronomy)
3. Define new names for the builtin elements of the groups
	- e.g. `nome` instead of `name` and `dia, mês, ano` instead of `day, month, year`.
4.  Define new groups that extend the existing groups by adding different elements, and so require also new database tables to store that information
	- e.g. a group "baptism" extends "act" adding the element "date-of-birth".

5. If there is information to be inferred from the transcription (attributes or relations), what are the rules to be used for inference
    -   e.g. the element `sex` can be inferred if groups such as `father`
        and `mother` are used instead of `person`

### Configuration of mappings

Currently three types of configuration files are used to provide this information:

structure (str) files
:   define new groups and their relation with core groups, any extra elements that 
	 new groups might include, and the order by which the groups may appear; 
	 str files define the way sources can be transcribed.

mappings files
:   Describe how new groups map to existing database tables and
	    can define new database table. 

inference files
:   contain rules for inference of attributes and relations
    from the groups in the transcriptions

Here we describe the content of a mapping file.

Here is an example of a mapping, in the current notation:

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

The statement:

    mapping person to class person.

means that the Kleio group `person` will be stored in the database as an
entity of class `person`.

The statement:

    class person super entity table persons

means that database entity class `person` is a specialization of `entity`,
and is stored in a table named `persons`.

The subsequent lines after `with attributes` specify the mapping between the
database entity attributes, stored as columns in tables and group elements.

For each attribute the following is specified:

-    name of the attribute in the group.
-   column: name of the column in the database for this element; normally it is the same and id, but it can happen that the name of the attribute in entity class is a reserved word for database columns (for instance "value" or "type"). This  information
-   baseclass: the kleio element class for this attribute
-   coltype, colsize, colprecision: information used to create the column in the database
    precision only applies if coltype is "DECIMAL"
-   pkey: integer,if this attribute is part of the primary key of the table, this is the order


The `baseclass` refers to certain attribute names that have special meaning.

For instance,day,month,year,id,obs, same_as are names of elements that have special
meaning in the translation of sources and mapping of data into the database.

In the mapping for portuguese act called "acta" (minutes, or
transcript, normally of a meeting):

    part name=historical-act;
         guaranteed=id,type,date;
         position=id,type,date;
         also=loc,ref,obs,day,month,year;
         arbitrary=person,object,geoentity,abstraction,ls,atr,rel

    element name=day; type=number
    element name=month; type=number
    element name=year; type=number
    element name=date;type=number

    part name=pt-acto; source=historical-act;
         arbitrary=celebrante,actorm,
             actorf,object,abstraction,ls,rel;
         position=id,dia,mes,ano;
         guaranteed=id,dia,mes,ano;
         also=ref,loc,obs

    element name=dia; source=day
    element name=mes; source=month
    element name=ano; source=year
    element name=data; source=date

    part name=amz;
     source=pt-acto;
     repeat=eleito,eleitor,referido;
     guaranteed=id,dia,mes,ano,fol;
     position=id,dia,mes,ano,fol;
     also=resumo,obs
 
```prolog
mapping 'historical-act' to class act.
class act super entity table acts
    with attributes
    id column id baseclass id coltype varchar colsize 64 colprecision 0 pkey 1
         and
    date column the_date baseclass date coltype varchar colsize 24 colprecision 0 pkey 0
         and
    type column the_type baseclass type coltype varchar colsize 32 colprecision 0 pkey 0
         and
    loc column loc baseclass loc coltype varchar colsize 64 colprecision 0 pkey 0
         and
    ref column ref baseclass ref coltype varchar colsize 64 colprecision 0 pkey 0
         and
    obs column obs baseclass obs coltype varchar colsize 16654 colprecision 0 pkey 0 .

mapping amz to class acta.

class acta super act table actas
    with attributes
    id column id baseclass id coltype varchar colsize 64 colprecision 0 pkey 1
         and
    dia column the_day baseclass day coltype numeric colsize 2 colprecision 0 pkey 0
         and
    mes column the_month baseclass month coltype numeric colsize 2 colprecision 0 pkey 0
         and
    ano column the_year baseclass year coltype numeric colsize 4 colprecision 0 pkey 0
         and
    fol column fol baseclass fol coltype varchar colsize 64 colprecision 0 pkey 0
         and
    resumo column resumo baseclass resumo coltype varchar colsize 1024 colprecision 0 pkey 0
         and
	obs column obs baseclass obs coltype varchar colsize 16654 colprecision 0 pkey 0 .
```


The attributes names in Portuguese (dia,mes,ano) are mapped to standard
classes (day,month,year) and conform column names
that do not conflict with reserved words in database systems
(the_day, the_month, the_year).
```
    amz$amz1/3/10/1683/fol=2
        /resumo=nomeacao de capelao que se fez na casa desta
                vila de soure por morte do padre simao homem de oliveira

```
The `Kleio` translator processes the transcription and generates a xml file that includes the mapping information and the groups data.

```xml
<CLASS NAME="acta" SUPER="act" TABLE="actas" GROUP="amz">
	<ATTRIBUTE NAME="id" COLUMN="id" CLASS="id" TYPE="varchar" SIZE="64" PRECISION="0" PKEY="1" ></ATTRIBUTE>
	<ATTRIBUTE NAME="dia" COLUMN="the_day" CLASS="day" TYPE="numeric" SIZE="2" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="mes" COLUMN="the_month" CLASS="month" TYPE="numeric" SIZE="2" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="ano" COLUMN="the_year" CLASS="year" TYPE="numeric" SIZE="4" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="fol" COLUMN="fol" CLASS="fol" TYPE="varchar" SIZE="64" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="resumo" COLUMN="resumo" CLASS="resumo" TYPE="varchar" SIZE="1024" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="obs" COLUMN="obs" CLASS="obs" TYPE="varchar" SIZE="16654" PRECISION="0" PKEY="0" ></ATTRIBUTE>

</CLASS>
```


This is the way the above transcription is exported by the translator

```xml
    <GROUP ID="amz1" NAME="amz" CLASS="acta" ORDER="2" LEVEL="2" LINE="6">
        <ELEMENT NAME="line" CLASS="line"><core>6</core></ELEMENT>
        <ELEMENT NAME="id" CLASS="id"><core>amz1</core></ELEMENT>
        <ELEMENT NAME="groupname" CLASS="groupname"><core>amz</core></ELEMENT>
        <ELEMENT NAME="inside" CLASS="inside"><core>mis-mesa-1</core></ELEMENT>
        <ELEMENT NAME="class" CLASS="class"><core>acta</core></ELEMENT>
        <ELEMENT NAME="order" CLASS="order"><core>2</core></ELEMENT>
        <ELEMENT NAME="level" CLASS="level"><core>2</core></ELEMENT>
        <ELEMENT NAME="dia" CLASS="day">
        <core><![CDATA[3]]></core>   </ELEMENT>
        <ELEMENT NAME="mes" CLASS="month">
        <core><![CDATA[10]]></core>   </ELEMENT>
        <ELEMENT NAME="ano" CLASS="year">
        <core><![CDATA[1683]]></core>   </ELEMENT>
        <ELEMENT NAME="fol" CLASS="fol">
        <core><![CDATA[2]]></core>   </ELEMENT>
        <ELEMENT NAME="resumo" CLASS="resumo">
        <core><![CDATA[nomeacao de capelao que se fez na casa desta vila de soure por morte do padre simao homem de oliveira]]></core>
        </ELEMENT>
        <ELEMENT NAME="date" CLASS="date">
        <core><![CDATA[16831003]]></core>   </ELEMENT>
        <ELEMENT NAME="type" CLASS="type">
        <core><![CDATA[amz]]></core>   </ELEMENT>
    </GROUP>
```

Note that the elements of the group are exported in XML with class derived
from the elements source parameter:

    element name=dia; source=day
    element name=mes; source=month
    element name=ano; source=year

Which generates the `CLASS` attribute in XML

```xml
<ELEMENT NAME="dia" CLASS="day">
	 <core><![CDATA[3]]></core>   </ELEMENT>
<ELEMENT NAME="mes" CLASS="month">
	 <core><![CDATA[10]]></core>   </ELEMENT>
<ELEMENT NAME="ano" CLASS="year">

```
### Translator logic for group to class mapping.

####  Mapping Group to Database class

The determination of the database class `a_class` associated with a group `a_group` is based on the following reasoning:

1. In the mappings configuration there is a clause `mapping a_agroup to class a_class` 
2. if not there is a clause `mapping s_agroup to class a_class`  and `s_group` can be found in the `source` parameter of `a_group`, recursively.  In other words `a_group` descends from `s_group` .


> [!NOTE] Mapping of Group to Class depends on local mappings and structure files
> Since it is possible that different Kleio files are processed with specific structure files associated, and in the future also different mappings file, and since several Kleio files can feed a single database, it is possible that groups with the same name will map diferently to database tables.

#### Mapping of element to columns in tables

When processing an element of a group for export the Kleio translator determines the class of each element as follows:

1. The class associated with the group  has an attribute with the same name as the element in the group: then the class of the element is obtained from the `baseclass` value of the class attribute.
2. There element extends, through the parameter `source`, recursively, an element whose name appears as the name of an attribute in the class associated to the group of the element.
3. The class associated with the group extends another class with has an attribute with the same name as the element.


### Importer login for the group to database table mapping

1. Each group must correspond to a database entity type.
2. Each database entity type is stored in a hierarchical table structure , with the Class Entity associated to table "entities" at the top.
3. Each database entity type has associated a PomSomMapper class.
4. The PomSomMapper class stores the definitiond the database structure as follows:
	1. The name of the entity class
	2. The name of the super class
	3. The name of the associated table
	4. A set of column definitions. Each column definition contains:
		1. Generic name of the column/attribute/element
		2. The column name in the database
		3. The class of the column in the Kleio SOM model
		4. The specific of the data type of column (type, size, precision)
		5. If the column is a primary key.
5. The information necessary to instantiate a PomSomMapper is part of the export file. It is not needed for built in models, but is used to generate tables and Python ORM classes during import.

The correspondence between group and database entities is imported 
1. The PomSomMapper also keeps track of the correspondence between groups and database classes.
	1. This correspondence is part of the import file: each group in the import file contains the name of the  class it is associated with. 
	2. Also, each element of the group contain the baseclass it corresponds to.  
	3. It is common for multiple groups to map to the same class, and that different elements names are used to record the information of columns with the same name. 
	4. This will not generate different PomSomMappers, but the PomSomMapper associated with each class keeps track of the groups associated with its class, and also of the mapping of group elements to database columns.



During import Timelink will determine the mapping information to be used
for the incoming Kleio group, from the group XML information:

```xml
    <GROUP ID="amz1" NAME="amz" CLASS="acta" ORDER="2" LEVEL="2" LINE="6">
```


It will then go through each of the attributes of database class `acta`
and fetch the group element with CLASS equal to the attribute baseclass. The
value of the element is used to set the corresponding column in the table
`actas`.

So from:


```xml
<GROUP ID="amz1" NAME="amz" CLASS="acta" ORDER="2" LEVEL="2" LINE="6">
	<ELEMENT NAME="dia" CLASS="day">
		 <core><![CDATA[3]]></core>   </ELEMENT>
```

and

```xml
<CLASS NAME="acta" SUPER="act" TABLE="actas" GROUP="amz">
	<ATTRIBUTE NAME="dia" COLUMN="the_day" CLASS="day" TYPE="numeric" SIZE="2" PRECISION="0" PKEY="0" ></ATTRIBUTE>
```

The importer determines that the information of group element "dia" should be stored in column "the_day"

Note that the mapping allows for the usage of a Kleio group with a evocative
name "amz" while using a more generic table name `actas`.

## The importer logic

When the XML files created by the `kleio` translator is imported with the `timelink-py` package the mapping information is used to store the source data in the corresponding database columns.

This import process is at the heart of the Timelink model of data management, and here we describe it in some detail.

### Process CLASS mappings embedded in the XML export

The kleio translator embeds the class mappings in the XML export.
```xml
<CLASS NAME="acta" SUPER="act" TABLE="actas" GROUP="amz">
	<ATTRIBUTE NAME="id" COLUMN="id" CLASS="id" TYPE="varchar" SIZE="64" PRECISION="0" PKEY="1" ></ATTRIBUTE>
	<ATTRIBUTE NAME="dia" COLUMN="the_day" CLASS="day" TYPE="numeric" SIZE="2" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="mes" COLUMN="the_month" CLASS="month" TYPE="numeric" SIZE="2" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="ano" COLUMN="the_year" CLASS="year" TYPE="numeric" SIZE="4" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="fol" COLUMN="fol" CLASS="fol" TYPE="varchar" SIZE="64" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="resumo" COLUMN="resumo" CLASS="resumo" TYPE="varchar" SIZE="1024" PRECISION="0" PKEY="0" ></ATTRIBUTE>
	<ATTRIBUTE NAME="obs" COLUMN="obs" CLASS="obs" TYPE="varchar" SIZE="16654" PRECISION="0" PKEY="0" ></ATTRIBUTE>

</CLASS>
```

With this information the importer is able to dynamically create new database tables as necessary. Note that the XML file also includes the class mappings of the built in models (entity, source, act, person, object, geo entity, attribute, relation), but these are ignored by the import process, which uses the most updated versions of the mappings in the timelink-py package.

When a CLASS section is detected in the XML file, if it refers to a builtin, it is ignored. If not, a new table is created along with a SQLAlchemy model for access in Jupiter notebooks and Python applications.

#### Process a GROUP element in the XML export

When a GROUP element is encountered in the XML import file the following logic is executed:

1. Find the PomSomMapper corresponding to the GROUP, using the CLASS attribute of the GROUP XML Element as the id of PomSomMapper.

	 <GROUP ID="amz1" NAME="amz" CLASS=**"acta"** ORDER="2" LEVEL="2" LINE="6">

this is done with ```pom_class=PomSomMapper.get_pom_class_from_group(group,...)```python 
	
2. Get The ORM model associated with this PomSomMapper. This ORM class must exist at this point. it is either a builtin model in `timelink.models.api` or it was created dynamically from a database class definition such as above by the method PomSomMapper.ensure_mapping().

```orm_model = pom_class.orm_class```

3. Get the name of the columns mapped to the attributes of the ORM model. The list of columns mapped to the ORM attributes is obtained by `sqlalchemy.inspect(orm_model_class).columns`
4. For each column associated to the ORM model, get the corresponding entry in the CLASS attributes, using `PomSomMaper.column_to_class_attribute(column_name,...)` 
5. in the class attribute corresponding to the ORM column name, get the CLASS (baseclass) and  ELEMENT in GROUP section
6. Store the core value of the element in the corresponding column of the ORM model
7. Store the extra information about the element in the extra_info columns of the ORM model. The extra info can be: the original name of the element in the group, comment text and original wording text.
	
Several Groups can map to the same table/entitiy (father, mother, grandfather, godfather, child all map to the person Entitiy and persons table)

### Summary


1. KleioHandler  -> PomSomMapper.storeGroup(a_group)
2. PomSomMapper -> pom_class = PomSomMapper.get_pom_class_from_group(a_group, session)
3. orm_mapper = pom_class.orm_class
4. orm_mapper 
		



