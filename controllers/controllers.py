# -*- coding: utf-8 -*-
from odoo import http

class IPython(http.Controller):
    @http.route('/ipython-report/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/exper/exper/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exper.listing', {
#             'root': '/exper/exper',
#             'objects': http.request.env['exper.exper'].search([]),
#         })

#     @http.route('/exper/exper/objects/<model("exper.exper"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exper.object', {
#             'object': obj
#         })