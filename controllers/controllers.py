# -*- coding: utf-8 -*-
from odoo import http
import requests
from werkzeug.wrappers import Response
from urllib.parse import urlencode
from odoo.http import request

class IPython(http.Controller):
    # notebook_api = 'http://localhost:8888'
    # notebook_token = '29a1d85f11d9a45b529849a9a11f9aa1aaa7a2ec3ec1db5c'
    #
    # @http.route(['/ipython-report/static/<path:path>', '/ipython-report/custom/<path:path>'], auth='public')
    # def static_resource(self, path, **kw):
    #     # print('static_url = %s' % (path, ))
    #     fwd_url = '%s/%s'
    #     if http.request.httprequest.full_path.startswith('/ipython-report/static'):
    #         fwd_url = '%s/static/%s'
    #     elif http.request.httprequest.full_path.startswith('/ipython-report/custom'):
    #         fwd_url = '%s/custom/%s'
    #     fwd_url = fwd_url % (self.notebook_api, path)
    #     if 'v' in http.request.params:
    #         fwd_url = '%s?v=%s' % (fwd_url, http.request.params['v'])
    #     r = requests.get(fwd_url, stream=True)
    #     return Response(r.raw,
    #         status=r.status_code,
    #         mimetype=r.headers['content-type'])
    #
    # @http.route(['/ipython-report/api/<path:path>'], auth='public', methods=['GET', 'PUT'])
    # def api_resource(self, path, **kw):
    #     # print('static_url = %s' % (path, ))
    #     fwd_url = '%s/api/%s'
    #     fwd_url = fwd_url % (self.notebook_api, path)
    #     params = {}
    #     params.update(http.request.params)
    #     params['token'] = self.notebook_token
    #     # if 'v' in http.request.params:
    #     fwd_url = '%s?%s' % (fwd_url, urlencode(params))
    #     print('fwd to url ', fwd_url)
    #     r = requests.get(fwd_url)
    #     return Response(r.content,
    #                     status=r.status_code,
    #                     content_type=r.headers['content-type'])
    #
    # @http.route(['/ipython-report/api/<path:path>'], auth='public', methods=['POST'], type='json')
    # def api_post_resource(self, path, **kw):
    #     # print('static_url = %s' % (path, ))
    #     fwd_url = '%s/api/%s'
    #     fwd_url = fwd_url % (self.notebook_api, path)
    #     params = {}
    #     params.update(http.request.params)
    #     params['token'] = self.notebook_token
    #     # if 'v' in http.request.params:
    #     fwd_url = '%s?%s' % (fwd_url, urlencode(params))
    #     print ('original data = ', http.request.httprequest.get_data())
    #     print('fwd to url ', fwd_url)
    #     r = requests.post(fwd_url, data=http.request.httprequest.get_data() )
    #     print('post response ', r.text)
    #     return r.json()
    #     # return Response(r.text,
    #     #                 status=r.status_code,
    #     #                 content_type=r.headers['content-type'])
    #
    # @http.route(['/ipython-report', '/ipython-report/'], auth='public')
    # def index(self, **kw):
    #     r = requests.get('%s/notebooks/guardian_gaza.ipynb?token=%s' % (self.notebook_api, self.notebook_token))
    #     return r.text

    @http.route(['/ipython_report', '/ipython_report/'], auth='public')
    def index2(self, debug=False, **kw):
        # if user not logged in, log him in
        return request.render('ipython_report.index', qcontext={})

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