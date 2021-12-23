# -*- coding: utf-8 -*-
# from odoo import http


# class AsbProductPricing(http.Controller):
#     @http.route('/asb_product_pricing/asb_product_pricing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asb_product_pricing/asb_product_pricing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asb_product_pricing.listing', {
#             'root': '/asb_product_pricing/asb_product_pricing',
#             'objects': http.request.env['asb_product_pricing.asb_product_pricing'].search([]),
#         })

#     @http.route('/asb_product_pricing/asb_product_pricing/objects/<model("asb_product_pricing.asb_product_pricing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asb_product_pricing.object', {
#             'object': obj
#         })
