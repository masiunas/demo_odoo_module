# -*- coding: utf-8 -*-
from odoo import http

# class DemoLibraryModule(http.Controller):
#     @http.route('/demo_library_module/demo_library_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_library_module/demo_library_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_library_module.listing', {
#             'root': '/demo_library_module/demo_library_module',
#             'objects': http.request.env['demo_library_module.demo_library_module'].search([]),
#         })

#     @http.route('/demo_library_module/demo_library_module/objects/<model("demo_library_module.demo_library_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_library_module.object', {
#             'object': obj
#         })