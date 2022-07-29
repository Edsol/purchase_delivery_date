# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    delivery_date = fields.Date(string='Delivery date', required=False)

    @api.multi
    def write(self, vals):
        if 'delivery_date' in vals and vals['delivery_date']:
            date_order = fields.Date.from_string(self.date_order)
            delivery_date = fields.Date.from_string(vals['delivery_date'])
            if (delivery_date >= date_order) == False:
                raise exceptions.UserError(_("It is not possible to enter a delivery date earlier than the order date."))
        
        res = super(PurchaseOrderLine, self).write(vals)
        return res