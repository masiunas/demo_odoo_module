from odoo


class Book(models.Model):
    inherit = 'library.book'
    is_available = fields.Boolean('Is Available?')
    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
    publisher_id = fields.Many2one(index=True)
