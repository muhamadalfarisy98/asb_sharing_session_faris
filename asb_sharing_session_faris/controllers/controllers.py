# -*- coding: utf-8 -*-
# from odoo import http


# class AsbSharingSessionFaris(http.Controller):
#     @http.route('/asb_sharing_session_faris/asb_sharing_session_faris/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asb_sharing_session_faris/asb_sharing_session_faris/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asb_sharing_session_faris.listing', {
#             'root': '/asb_sharing_session_faris/asb_sharing_session_faris',
#             'objects': http.request.env['asb_sharing_session_faris.asb_sharing_session_faris'].search([]),
#         })

#     @http.route('/asb_sharing_session_faris/asb_sharing_session_faris/objects/<model("asb_sharing_session_faris.asb_sharing_session_faris"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asb_sharing_session_faris.object', {
#             'object': obj
#         })
