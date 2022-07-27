# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    delivery_date = fields.Date(string='Delivery date', required=False)

    @api.multi
    def button_confirm(self):
        for order in self:
            if order.delivery_date == False:
                raise exceptions.UserError(_("To confirm the order you have to indicate the delivery date."))
            else:
                super(PurchaseOrder,self).button_confirm()
    
    @api.multi
    def write(self, vals):
        if vals['delivery_date']:
            date_order = fields.Date.from_string(self.date_order)
            delivery_date = fields.Date.from_string(vals['delivery_date'])

            if (delivery_date > date_order) == False:
                raise exceptions.UserError(_("A delivery date prior to or equal to the order date cannot be entered."))
            _logger.debug(delivery_date > date_order)
        
        res = super(PurchaseOrder, self).write(vals)
        return res