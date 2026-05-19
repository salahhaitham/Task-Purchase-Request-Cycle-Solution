{
    'name': 'Purchase Request',
    'version': '1.0',
    'summary': ' custom module',
    'description': """
        هذا الموديول مثال لتعلم كيفية عمل Module في Odoo.
        يمكنك إضافة Models و Views هنا.
    """,
    'author': 'Salah',
    'category': 'Tools',
    'depends': ['base','account','analytic','product'],
    'assets': {

    },
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/purchase_request_view.xml',
        'views/sequence.xml',




    ],
    'images': [],
    'demo': [

    ],

    'application': True,
'installable': True,
}
