# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo14Enterprise/odoo-customAddons/saleExtendedTaiga(http.Controller):
#     @http.route('//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga.listing', {
#             'root': '//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga',
#             'objects': http.request.env['/opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga./opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga'].search([]),
#         })

#     @http.route('//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga//opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga/objects/<model("/opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga./opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo14_enterprise/odoo-custom_addons/sale_extended_taiga.object', {
#             'object': obj
#         })
