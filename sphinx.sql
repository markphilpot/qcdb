create or replace view web_catalog as
select
	c.id as dialog_id,
	a.title,
	b.id as character_id,
	b.name,
	c.text,
	a.id as comic_id
from
	web_comic as a, web_character as b, web_dialog as c, web_comic_characters as a_b, web_dialog_characters as b_c, web_comic_dialog as a_c 
where
	a.id = a_b.comic_id and
	b.id = a_b.character_id and
	a.id = a_c.comic_id and
	c.id = a_c.dialog_id and
	b.id = b_c.character_id and
	c.id = b_c.dialog_id;

	