{
    'name': 'Odoo Rest API',
    'version': '14.0.0',
    'author': 'PT. Arkana Solusi Bisnis',
    'category': 'Backend',
    'website': 'https://www.arkana.co.id/',
    'summary': 'ASB Sharing Session',
    'description': '''
        Sharing session
    ''',
    'external_dependencies': {
         #'python': ['pyjwt','simplejson'],
    },
    'depends': ['web','base','product', 'asb_sharing_session_faris'],
    'data': [
            'security/ir.model.access.csv',
            'views/refresh_token.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
