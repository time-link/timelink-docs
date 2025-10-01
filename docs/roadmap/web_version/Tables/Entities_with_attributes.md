Select all the entities with a given attribute. 
Filter by attribute value, dates, or a given group of people or objects.

{Interface to` timelink.pandas.entities_with_attributes`}



3. Select entity type  (must)
	1. [pop up - only one] {select distinct the_type from entities}
4. Select columns of entity to show: 
	1. [[multiple selection]]  {TimeinkDatabase.get_columns(Entity_type)}
5. Select attribute type  (must) 
	1. [multiple selection]  {select distinct the_type from attributes
	2. in column named [text field] default selected type if only one
6. select value  (optionally)
	1. multiple selection.  {select distinct the_value from attributes where the_type=selected attribute type} Note: if list more than 32 (parametrized) show textbox and user type values in rows.}
7. Other attributes to show in columns
	1. [multiple selection]  {select distinct the_type from attributes}
8. date range (optionally):
	1. After [Date1] Before [Date2]
9. Show only from list (optionally)
	1. List of ids of name of saved list of ids [Text field]

Output de `timelink.pandas.entities_with_attributes` DataFrame 
Button [Save as]  Format: one of Excel, Csv, JSON (user stand widget for this)
Button: [Save ids]  Saves ids with a name, user.