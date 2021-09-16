# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare


class ProductTemplate(models.Model):
    _inherit = "product.template"


    product_no_recurrente = fields.Boolean(string='Producto No recurrente Separa Total PDF', default=False)


class ProductProduct(models.Model):
    _inherit = "product.product"


    product_no_recurrente = fields.Boolean(string='Producto No recurrente Separa Total PDF', default=False)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        #Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = amount_recurrent = amount_not_recurrent = 0.0
            for line in order.order_line:
                if(line.product_id.product_no_recurrente == False):
                    amount_recurrent += line.price_subtotal

                if(line.product_id.product_no_recurrente == True):
                    amount_not_recurrent += line.price_subtotal

                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax

            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
                'amount_recurrent': amount_recurrent,
                'amount_recurrent_total': amount_recurrent + amount_tax,
                'amount_not_recurrent': amount_not_recurrent,
                'amount_not_recurrent_total': amount_not_recurrent,
            })

    show_col_taxes = fields.Boolean(string='Mostar Columna de Impuestos', default=True)
    show_label_notify = fields.Boolean(string='Mostar Etiqueta Recuerrente', default=True)
    amount_recurrent = fields.Monetary(string='Recurrent Amount', store=True, readonly=True, compute='_amount_all', tracking=5)
    amount_recurrent_total = fields.Monetary(string='Recurrent Amount', store=True, readonly=True, compute='_amount_all', tracking=5)
    amount_not_recurrent = fields.Monetary(string='Not Recurrent Amount', store=True, readonly=True, compute='_amount_all', tracking=5)
    amount_not_recurrent_total = fields.Monetary(string='Not Recurrent Amount', store=True, readonly=True, compute='_amount_all', tracking=5)



class SaleOrder(models.Model):
    _inherit = "sale.order.line"

   

    section_not_recurrent = fields.Boolean(string='Agrupar en PDF Fuera del Subtototal', default=False)

    