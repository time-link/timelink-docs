
## How to keep text sources and databases in sync

One of the challenges of the data model of Timelink is to ensure that successive versions of the same  source are imported without compromising the integrity of the database.

This is difficult because relations between entities need to be preserved. Since historical entities do not have, usually, attributes that can be used as unique identifiers, every entity in the database needs to get an unique id so that it can be referred to as the data collection progresses.

Changes related to entities that require some type of unique ids are:

1. Relations between entities such as those recorded with "relation" groups, which can be changed in successive versions of the source, as reading improves, errors are corrected or conventions for "type" and "value" of relations are refined. Note that many relations between entities are generated automatically by the translator.
2. Signaling that two entities in different points of the source, or in different sources, are the same, through "same_as" or "xsame_as" elements.
3. Changes in the elements of the entities, like names, or comments and original wording registered with "#" and "%".
4. Changes in time attributes registered with "ls" or "attr" .
5. Changes in the order of the entities in the source.
6. Addition of new entities to the source, possibly in the middle of already imported entities.
7. Removal of entities from the source, after they were already imported in the database.

Successive versions of a given source transcription must allow for these changes seamlessly, without the risk of loosing information or making changes in the wrong places.

The only way to ensure that the changes are done without errors is to attribute an unique id to each entity as it enters the database and register that id back to the original source transcription so that next time the source is imported the entity is matched with its previous context.

The alternative is to require the user to assign an unique id to each entity in the source during transcription, which would slow down the process enourmously and would be difficult, in terms of ensuring uniqueness.

The solution is to allow the user to transcribe the source without needing to provide an unique id to each entity. Unique ids must be provided by the user only for sources, certain types of acts and a few types of entities. For most of the content of historical sources, mainly people and objects, explicit ids are required only when the person or the object must be referred to unambiguosly in a relation group, or a "same as"  element, further in the source. All the entities registered without explicit ids receive an explicit id during translation and a copy of the source is generated with the explicit ids appended to each entity.

For each new version of a source, the previous information in the database is  erased and replaced with the new information.

The process is the following:

1. During translation the kleio translator generates an unique id for each entity that does not have an user defined id. User defined ids are normally registered with "/id=xxxx" .
2. The translation generates a new version of the kleio file with the ids explicitly registered with "/id=" tags. More information on the process of generating the unique ids bellow.
3. The source is then imported in the database with  all the ids explicit.
4. The user then continues working in the file with the explicit ids, adding information to existing entities, changing  their elements, deleting and adding entities at will in any position in the file where it is allowed by the structure format. Again, the user might provide or not unique ids to the added information. If the user moves entities already imported to other places in the source file and keeps the id (either explicitly or automatically generated), then the association to the same entity in the database is preserved.
5. The next translation will generate unique ids for those new entities that need them, because they are new and the user did not provide an explicit id.
6. On the second and subsequent imports the existing source in the database and all its contained entities are erased and replaced by the new ones. Those entities that were previously in the database return to the database with the same ids, so inter source relations like identifications are preserved.

## keeping cross references between sources. 



