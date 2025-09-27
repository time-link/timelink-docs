
Questões em aberto:
- Isto é ontologia do Source Model ou a Ontologia *tout-court* ? 
- Onde estão as real-entities?
- Onde estão as geo-entities?
- Porque estão aqui os male-actor, female-actor, etc... isso não é ontologia, é artefacto para a transcrição de fonte. Esta parte está mal conceptualizada. 

### Bibliografia a ler

- [ ] Spyns, P., Meersman, R., & Jarrar, M. (2002). Data modelling versus ontology engineering. _ACM SIGMOD Record_, _31_(4), 12–17. [https://doi.org/10.1145/637411.637413](https://doi.org/10.1145/637411.637413)
- [ ] Johansson, I. (2005). _Qualities, Quantities, and the Endurant-Perdurant Distinction in Top-Level Ontologies._ (p. 550). PDF Zotero
- [ ] Krieger, H.-U., & Declerck, T. (sem data). _An OWL Ontology for Biographical Knowledge. Representing Time-Dependent Factual Knowledge_. PDF Zotero
- [ ] Huang, C.-R. (sem data). _Endurant vs Perdurant: Ontological Motivation for Language Variations_. 11.
- [ ] Poveda Villalón, M. (2016). _Ontology Evaluation: A pitfall-based approach to ontology diagnosis_ [PhD Thesis, Universidad Politécnica de Madrid]. [https://doi.org/10.20868/UPM.thesis.39448](https://doi.org/10.20868/UPM.thesis.39448)
- [ ] _Geonames ontology in OWL - GSWB_. (2008, fevereiro 12). [https://web.archive.org/web/20080212144050/http://www.geospatialsemanticweb.com/2006/10/14/geonames-ontology-in-owl](https://web.archive.org/web/20080212144050/http://www.geospatialsemanticweb.com/2006/10/14/geonames-ontology-in-owl)
- [ ] Niles, I., & Pease, A. (2001). _Towards a standard upper ontology_. _2001_, 2–9. [https://doi.org/10.1145/505168.505170](https://doi.org/10.1145/505168.505170)





```mermaid
---
title: Timelink ontology Source Model
---
classDiagram
    Root <|-- Event: something happened
    Root <|-- Entity: something existed
    Root <|-- TimeBasedInformation: information that varies with time
    Event <|-- Source: is a record of
    Event <|-- Act: is a type of
    TimeBasedInformation <|-- Attribute: is a type of
    TimeBasedInformation <|-- Relation: is a type of
    
    class Entity{
	    <<Abstract>>
	    +str id
	    +link same_as
	    }
	class TimeBasedInformation{
		<<abstract>>
		str: id
		date: date
		}
	class Event{
		str: description
		location: location
		date: date
	    }
	class Source{
		str: ref_in_archive
		}
	class Act{
		+str id
		+str ref_in_source}
	class Person{
		+str name
		+char sex
		+str obs
	}
    class Object{
        +str description
        +str type
        +str obs
    }
    class Attribute{
        +str type
        +str value
        +str obs
    }
    class Relation{
        +str type
        +str value
        +link origin
        +link destination
    }
    Entity <|-- Person: is a type of
    Entity <|-- Object: is a type of
	Person <|-- Male_actor: is a type of
	Person <|-- Female_actor: is a type of
	Person <|-- Neutral_actor: is a type of
	class Male_actor{
		-str sex(m)
	}
	class Female_actor{
		-str sex(f)
	}
	Male_actor <|-- PT_Male_actor: is a type of
	Male_actor <|-- EN_Male_actor: is a type of
	Female_actor <|-- PT_Female_actor: is a type of
	Neutral_actor <|-- PT_Neutral_actor: is a type of
	PT_Male_actor <|-- Pai: is a type of
	PT_Female_actor <|-- Mãe: is a type of
```

## Containment hierarchy (not an ontology)

```mermaid
---
title: Timelink Source containment hierarchy
---
classDiagram
	
    Kleio *-- Source: contained in
    Source *-- Act: contained in
    Source *-- Event: contained in
    Act *-- Object: has function in
    Event *-- Person: has function in
    Act *-- Person: has function in
    Event *-- Object: has function in
    Person *-- Attribute
    Person *-- Relation
    Object *-- Attribute
	Object *-- Relation
	
	
	
	
	
```
