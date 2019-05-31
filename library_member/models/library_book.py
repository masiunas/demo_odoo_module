from Odoo import fields, models


class Book(models.Model):
    inherit = 'library.book'
    is_available = fields.Boolean('Is Available?')



