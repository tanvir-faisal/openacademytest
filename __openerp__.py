{
    'name' : 'openacademytest',
    'summary': """Manage Trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Tanvir",
    'website': "http://www.BayIT.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/alert_wizard_view.xml',
        'views/openacademy_menu.xml',
        'views/openacademy_course.xml',
        'views/openacademy_session.xml',
        'wizards/confirmation_wizard_view.xml',
        'workflows/session_workflow_server_action.xml',
        #'workflows/session_workflow.xml',
        'reports/session_report_of_openacademy.xml',
    ],
}