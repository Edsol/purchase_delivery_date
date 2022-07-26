# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    delivery_date = fields.Date(string='Delivery date', required=False)

    @api.multi
    def button_confirm(self):
        for order in self:
            if order.delivery_date == False:
                raise exceptions.Warning(_("To confirm the order you have to indicate the delivery date."))
            else:
                super(PurchaseOrder,self).button_confirm()