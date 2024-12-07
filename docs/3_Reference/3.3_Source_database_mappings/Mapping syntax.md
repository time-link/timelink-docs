  
Currently mappings between source groups and database tables are defined with a notation baed of `prolog` clauses with special operators.

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
  

The statement:`mapping person to class person` 	means that the Kleio group `person` will be stored in the database as an entity of class `person`.

The statement: `class person super entity table persons` means that database entity class `person` is a specialization of `entity`, and is stored in a table named `persons`.


The subsequent lines after `with attributes` specify the mapping between the database entity attributes, store as columns in tables and group elements.

For each attribute the following is specified:
- id : name of the attribute in the database entity class
- column id: name of the column in the database for this element
- baseclass id: the kleio reference class for this attribute
- coltype, colsize, colprecision: information used to create the column in the database
precision only applies if coltype is "DECIMAL"
- pkey: integer,if this attribute is part of the primary key of the table, this is the order

  
The `baseclass` refers to certain attribute names that have special meaning .

For instance,day,month,year,id,obs, same_as are names of elements that have special meaning in the translation of sources and mapping of data into the database.

#### An example: transcripts of meetings

In order to process transcript of meetings it is necessary to define both the groups  that will be used in the transcription of the sources and the tables that will store the information in the database.

In the mapping for portuguese act called "acta" (minutes, or transcript, normally of a meeting) the groups used are defined in a `str` file:


```kleio-structure
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
	position=id,dia,mes,ano;
	guaranteed=id,dia,mes,ano;
	arbitrary=celebrante,actorm,
		actorf,object,abstraction,ls,rel;
	also=ref,loc,obs

element name=dia; source=day
element name=mes; source=month
element name=ano; source=year
element name=data; source=date

part name=amz; source=pt-acto;
	repeat=eleito,eleitor,referido;
	guaranteed=id,dia,mes,ano,fol;
	position=id,dia,mes,ano,fol;
	also=resumo,obs

```

And now the mappings to database tables:

```prolog
mapping 'historical-act' to class act.
class act super entity table acts with attributes
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
class acta super act table actas with attributes
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


The attributes names in Portuguese (dia,mes,ano) are mapped to standard classes (day,month,year) and conform column names that do not conflict with reserved words in database systems (the_day, the_month, the_year).

With this information `timelink` is able to process a transcription such as:
```kleio
amz$amz1/3/10/1683/fol=2
	/resumo=nomeacao de capelao que se fez na casa desta
	 vila de soure por morte do padre simao homem de oliveira
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
<core><![CDATA[3]]></core> </ELEMENT>
<ELEMENT NAME="mes" CLASS="month">
<core><![CDATA[10]]></core> </ELEMENT>
<ELEMENT NAME="ano" CLASS="year">
<core><![CDATA[1683]]></core> </ELEMENT>
<ELEMENT NAME="fol" CLASS="fol">
<core><![CDATA[2]]></core> </ELEMENT>
<ELEMENT NAME="resumo" CLASS="resumo">
<core><![CDATA[nomeacao de capelao que se fez na casa desta vila de soure por morte do padre simao homem de oliveira]]></core>
</ELEMENT>
<ELEMENT NAME="date" CLASS="date">
<core><![CDATA[16831003]]></core> </ELEMENT>
<ELEMENT NAME="type" CLASS="type">
<core><![CDATA[amz]]></core> </ELEMENT>
</GROUP>
```


Note that the elements of the group are exported in XML with class derived from the elements source parameter:

```
element name=dia; source=day
element name=mes; source=month
element name=ano; source=year
```
  

Which generates the `CLASS` attribute in XML
```xml
<ELEMENT NAME="dia" CLASS="day">

<core><![CDATA[3]]></core> </ELEMENT>

<ELEMENT NAME="mes" CLASS="month">

<core><![CDATA[10]]></core> </ELEMENT>

<ELEMENT NAME="ano" CLASS="year">
```

  
During import Timelink will determine the mapping information to be used for the incoming Kleio group, from the group XML information:

```xml
<GROUP ID="amz1" NAME="amz" CLASS="acta" ORDER="2" LEVEL="2" LINE="6">
```
  
  
It will then go through each of the attributes of database class `acta` and fetch the group element with CLASS equal to the attribute baseclass. The value of the element is used to set the corresponding column in the table `actas`.


Note that the mapping allows for the usage of a Kleio group with a evocative name "amz" while using a more generic table name `actas`.
