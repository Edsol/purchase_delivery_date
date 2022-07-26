# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Purchase delivery date",
    'summary': "Purchase delivery date in Purchase order",
    'description': "This module adds delivery date field in purchase order.",
    'version': "0.1",
    'author': "Edoardo Soloperto",
    'category': "Purchases",
    'depends': ["purchase"],
    'data': [
        "views/purchase_order_view.xml"
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}