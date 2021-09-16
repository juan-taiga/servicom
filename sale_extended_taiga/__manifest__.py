# -*- coding: utf-8 -*-
{
    'name': "Sale Extended Taiga",

    'summary': """
        Sale Extended Taiga""",

    'description': """
        Sale Extended Taiga
    """,
    'author': "Taiga Consulting S.A.",
    'website': "https://www.taiga-conmsulting.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        #'security/ir.model.access.csv',
        'views/sale_extended_view.xml',
        'views/sale_report_extended_view.xml',
    ],
}
