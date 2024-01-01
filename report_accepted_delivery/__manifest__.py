# Copyright 2023 Rosen Vladimirov, BioPrint Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Report Accepted Delivery',
    'summary': """
        Accepted delivery documents.""",
    'version': '16.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Rosen Vladimirov, BioPrint Ltd.,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/stock-logistics-reporting',
    'depends': [
        'stock',
    ],
    'data': [
        'report/report_accepted_deliveryslip.xml',
        'report/stock_report_views.xml'
    ],
    'demo': [
    ],
}
