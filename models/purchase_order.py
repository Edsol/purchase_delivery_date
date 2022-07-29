# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    delivery_date = fields.Date(string='Delivery date', required=False)

    @api.multi
    def button_confirm(self):
        order_lines = self.env['purchase.order.line'].search_read([('order_id','=',self.id)], order="delivery_date asc")
        for order_line in order_lines:
            if order_line['delivery_date'] == False:
                raise exceptions.UserError(_("All order lines must have a delivery date"))
            
            date_order = fields.Date.from_string(self.date_order)
            delivery_date = fields.Date.from_string(order_line['delivery_date'])
            if (delivery_date >= date_order) == False:
                raise exceptions.UserError(_("It is not possible to enter a delivery date earlier than the order date."))

        last_line = order_lines[-1]
        self.write({'delivery_date':last_line['delivery_date']})
        super(PurchaseOrder, self).button_confirm()

    @api.multi
    def button_cancel(self):
        self.write({'delivery_date':False})
        super(PurchaseOrder, self).button_cancel()
