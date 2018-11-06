# -*- coding: utf-8 -*-
from odoo import http
import requests

class IPython(http.Controller):
    @http.route(['/ipython-report', '/ipython-report/<path:path>'], auth='public')
    def index(self, *path, **kw):
        print(kw)
        print(path)
        print(self)
        print(http.request)
        print(http.request.env)

        r = requests.get('http://localhost:8888/notebooks/guardian_gaza.ipynb?token=e4fafee6f8b80c9a5d591d1b541b162ca78a021169070387')        
        return r.text

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