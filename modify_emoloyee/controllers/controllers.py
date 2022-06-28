# -*- coding: utf-8 -*-
# from odoo import http


# class ModifyEmoloyee(http.Controller):
#     @http.route('/scuh_emoloyee/scuh_emoloyee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scuh_emoloyee/scuh_emoloyee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scuh_emoloyee.listing', {
#             'root': '/scuh_emoloyee/scuh_emoloyee',
#             'objects': http.request.env['scuh_emoloyee.scuh_emoloyee'].search([]),
#         })

#     @http.route('/scuh_emoloyee/scuh_emoloyee/objects/<model("scuh_emoloyee.scuh_emoloyee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scuh_emoloyee.object', {
#             'object': obj
#         })
