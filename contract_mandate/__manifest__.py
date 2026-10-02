# Copyright 2017 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Vendored from OCA/contract 16.0 and ported to 19.0 by BSO: OCA dropped this
# module at 19.0 with no open migration PR, so BSO carries it in local-src.

{
    "name": "Contract Mandate",
    "summary": "Mandate in contracts and their invoices",
    "version": "19.0.1.0.0",
    "author": "Odoo Community Association (OCA), Tecnativa",
    "website": "https://github.com/OCA/contract",
    "depends": ["contract_payment_mode", "account_banking_mandate"],
    "category": "Sales Management",
    "license": "AGPL-3",
    "data": ["views/contract_view.xml"],
    "installable": True,
    "auto_install": True,
}
