The data model is based on the concept that a historical source contains information on a sequence of nested entities. 

Although there is an infinite variety of historical sources, here we focus on those that contain information about people and objects, or abstractions (like institutions or ideas) and events in which those people participate. 

Typical case is parish registers or notarial records. In those cases the source is a written registration of an event.



```mermaid
---
title: Timelink ontology Source Model
---
classDiagram
    Kleio *-- Source: contained in
    Source *-- Act: contained in
    Source *-- Event: contained in
    Act *-- Person: function in
    Act *-- Object:  in
    Endurant *-- Attribute: dated attribute of
    Endurant *-- Relation: date relation of
    Endurant <|-- Person: is type of
    Endurant <|-- Object: is type of
    Perdurant <|-- Act: is type of
    Perdurant <|-- Event: is type of
    Perdurant <|-- Attribute: is type of
    Perdurant <|-- Relation: is type of
    
	class Source{
		+str id
		+str description
		+date date}
	class Act{
		+str id
		+date date
		+str loc
		+str ref}
	class Endurant{
		+str id}
	class Person{
		+str name
		+char sex
		+str obs
		+same_as(person_id)}
    class Object{
        +str description
        +str type
        +str obs
        +same_as(object_id)
        
    }
    class Attribute{
        +str id
        +str type
        +str value
        +date date
        +str obs
    }
    class Relation{
        +str id
        +str type
        +str value
        +date date
        +str date
        +str origin()
    }
	Person <|-- Male_actor
	Person <|-- Female_actor
	Person <|-- Neutral_actor
	class Male_actor{
		-str sex(m)
	}
	class Female_actor{
		-str sex(f)
	}
	Male_actor <|-- PT_Male_actor
	Male_actor <|-- EN_Male_actor
	
	
	
```
