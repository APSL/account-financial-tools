# Copyright 2024 APSL - Nagarro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Move Product",
    "summary": """Shows product field on the Journal Entry""",
    "version": "16.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "author": "APSL-Nagarro, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-financial-tools",
    "depends": ["account"],
    "data": [
        "views/account_move.xml",
    ],
    "installable": True,
    "maintainers": ["mpascuall"],
}
