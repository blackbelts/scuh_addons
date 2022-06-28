# -*- coding: utf-8 -*-
# from odoo import http


# class ModifyPurchase(http.Controller):
#     @http.route('/scuh_purchase/scuh_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scuh_purchase/scuh_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scuh_purchase.listing', {
#             'root': '/scuh_purchase/scuh_purchase',
#             'objects': http.request.env['scuh_purchase.scuh_purchase'].search([]),
#         })

#     @http.route('/scuh_purchase/scuh_purchase/objects/<model("scuh_purchase.scuh_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scuh_purchase.object', {
#             'object': obj
#         })
