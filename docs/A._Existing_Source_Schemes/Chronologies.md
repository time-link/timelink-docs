
Chronologies are similar to events. They describe something took place at a given date in a given location. Their main elements are *date*, *loc* (for location), and *description*.

Optionally they can have an *obs* element that can store long texts.

They can include people, places and topics.

The sequence is:
		
		crono$DATE/LOC/DESCRIPTION

The *loc* element is used to record the scope of the chronology. In this example,
taken from Dehergne, *Répertoire des Jésuites de Chine...*  loc is used to record
either "En Chine" or "Hors de Chine", in the portuguese version.

Note that dates can take the extended notation https://github.com/time-link/timelink-kleio/issues/1 except for the *after* and *before* (">", "<") notation.

Dates with dashes for legibility and ranges separated by ":" are acceptable.

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

  
