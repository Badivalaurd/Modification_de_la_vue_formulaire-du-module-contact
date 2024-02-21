{
    'name': 'Custom Contact',
    'version': '1.0',
    'category': 'Custom',
    'author': 'BAHENG DIEUDONNE',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'summary': 'Ajoute des champs CNI et NUI au module contact.',
    'depends': ['contacts'],
    'data': [
        'views/custom_contact_form.xml',
    ],
    'installable': True,
    'application': False,
}
