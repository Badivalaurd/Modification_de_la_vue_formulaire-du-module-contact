# -*- coding: utf-8 -*-
# from odoo import http


# class ContactCustom(http.Controller):
#     @http.route('/contact_custom/contact_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_custom/contact_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_custom.listing', {
#             'root': '/contact_custom/contact_custom',
#             'objects': http.request.env['contact_custom.contact_custom'].search([]),
#         })

#     @http.route('/contact_custom/contact_custom/objects/<model("contact_custom.contact_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_custom.object', {
#             'object': obj
#         })
