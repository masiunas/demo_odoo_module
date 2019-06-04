# -*- coding: utf-8 -*-
{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Evgenii _Masiunas',
    'depends': ['library_module'],
    'data': [
        'views/book_view.xml',
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/member_view.xml',
        'views/library_menu.xml',

    ],
    'application': False,
}
