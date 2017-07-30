from openerp import models, fields, api

class book(models.Model):
	_name = "book.book"
	_description = "Book List"
	
	name = fields.Char(string='Name', size=30, required=True)
	description = fields.Text()
	author = fields.Char(string='Author', size=30, required=True)
	