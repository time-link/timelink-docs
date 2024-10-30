
### Purpose

Chronologies are similar to events. 

They describe that something took place at a given date in a given location. 

### Elements

The main elements of cronologies are *date*, *loc* (for location), and *description*.

Optionally they can have an *obs* element that can store long texts.

The sequence is:
		
		crono$DATE/LOC/DESCRIPTION/obs=OBS

The *loc* element is used to record the scope of the chronology. 

In the example bellow,taken from Dehergne, *Répertoire des Jésuites de Chine...*,  loc is used to record
either "En Chine" or "Hors de Chine", ("China" or "Fora da China" in the Portuguese version)

Note that dates can take the [extended date notation](https://github.com/time-link/timelink-kleio/issues/1) except for the *after* and *before* (">", "<") characters.

Dates with dashes for legibility and ranges separated by ":" are acceptable.

### Enclosed groups

They can include people, places and topics.

### Example

Example (using portuguese group names):


	kleio$
		fonte$deh-crono/tipo=cronologia/data=1552:1758
		
			crono$1522-01-28/China/Kia-Tsing imperador
				referido$Jiajing%Kia-Tsing# @wikidata:Q10011
				
			crono$1542:1543/Fora da China/Chegada dos Portugueses a Japão 
						(e, em 1549, chegada de S. Francisco Xavier)
				referido$Francisco Xavier/xmesmo_que=francisco-xavier
				lugar$Japão
					
			crono$1563/Fora da China/Fim do Concílio de Trento
				topico$Concílio de Trento


### Schema 

The base group for chronologies is `cevent` , representing a chronology event. 

A `crono` synonym is defined for legibility in Portuguese sources
	
	note ============================================
	note doc group cevento Chronology event,
	note           can be used inside source
	note TODO: change to cevent source event, check mappings
	part name=cevento; source=evento;
	    position=data,loc,description;
	    guaranteed=data,loc,description;
	    also=id,obs, same_as, xsame_as;
	    part=person,topic,place
	
	part name=topic; source=abstraction;
		position=name,description;
		guaranteed=name;
		also=obs,id
	
	part name=place; source=geoentity
	
	note doc group crono Synonym for cevento
	
	part name=crono; source=cevento;
	    part=referido,referida,lugar,topico
	
	part name=topico; source=topic
	
	part name=lugar; source=place
  
