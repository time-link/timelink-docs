
The result of "record linking" or "Entity Resolution" can be exported in `kleio` format. This was a feature of the `MHK` system. 

Here is how an exported file looks like:

	
	kleio$gacto2.str/authorities/Generated from database toliveira_china by user toliveira, file date: +2021-06-18 Timestamp:2021-06-18T02:43:33.674Z/translations=13
	
	   identifications$real-entities-toliveira/Real entities, including real persons and real objects/dbase=toliveira_china/user=toliveira/date=20210618/mode=backup

	      rperson$rp-46/Agostinho de Barros/m/status=N
	
	         occ$deh-joao-de-barros-ref1/id=rp-46-occ
	
	         occ$deh-agostinho-de-barros/id=rp-46-occ2



The  `str` definition for `identifications` is:

	note ===========================================================
	note doc group authority-register a register of authority-records
	note    authority records are used to identify people, objects
	note    and to normalize vocabularies and other authority information.
	note    authority-registers must have an unique id, but a given community
	note    can have as many authority-registers as needed
	note
	
	part name=authority-register;
	    position=id,name;
	    guaranteed=id,name,date,user,dbase;
	    also=date,user,dbase;
	    part=authority-record
	
	note ===========================================================
	note identifications: a authority-register for identifications
	note doc group identifications 
	     Identifications are authority-registers for record linking.
	     They contain real-entity records (people or objects) that aggregate
	     occurrences in the source pertaining to the same person or entity.
	     To keep imported records separate from local ones use a different user.
	part name=identifications;
	    source=authority-register;
	    position=id,name;
	    guaranteed=id,name,date,user,dbase,mode;
	    also=obs;
	    part=rentity,rperson,robject
	    
	note ===========================================================
	note rentity: a authority-record for a real entity
	note doc group rentity
	        Rentity contains information about a real entity.
	        Defines the standart name for the entity and what are the occurences,
	        in `occ` subgroups.
	part name=rentity;
	     position=id,description,type;
	     guaranteed=id,description,type;
	     also=status,user,obs;
	     part=occ
	     
	note ===========================================================
	note rperson: a authority-record for a real person
	note doc group rperson contains information about a real person.
	note     Defines the standart name for the person, the sex, and what are the occurrences
	note    Note that real entities can have attributes and relations
	part name=rperson;
	     position=id,sname,sex;
	     guaranteed=id,sname,sex;
	     also=status,user,obs;
	     part=occ,ls,atr,rel
	
	note ===========================================================
	note robject: a authority-record for a real object
	note doc group robject contains information about a real object.
	note     Defines the standart name for the object, the type, and what are the occurrences
	note    Note that real entities can have attributes and relations
	part name=robject;
	     position=id,sname,type;
	     guaranteed=id,sname,type;
	     also=status,user,obs;
	     part=occ,ls,atr,rel
	
	note ===========================================================
	note occ: an occurrence of a real entity
	note doc group occ contains the ids of the occurrences of a real entity
	note     Defines the id of the occ and optionally the name of the occurence
	note     the id_act of the act where it occurs, the type of act and the fucntion
	note     note that these optional information are just for documentation because they
	note    derive automatically from the occurrence id.
	part name=occ;
	     position=occurrence,atype,func,date,name;
	     guaranteed=occurrence;
	     also=name,atype,func,date,id,obs
