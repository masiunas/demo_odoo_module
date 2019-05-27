# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'description': "Manage library book catalogue and lending.",
    'author': "Evgenii Masiunas",
    "licence": "By default considered to be LGPL",
    'category': "Management",
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
    ],
}
