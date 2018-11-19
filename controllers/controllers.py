# -*- coding: utf-8 -*-
from odoo import http
import requests
from werkzeug.wrappers import Response
from urllib.parse import urlencode
from odoo.http import request
import json

BASE_URL = '/ipython_report'
API_URL = '%s/api' % (BASE_URL, )

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

    @http.route([BASE_URL, '%s/' % (BASE_URL,)], auth='public')
    def index(self, debug=False, **kw):
        # if user not logged in, log him in
        return request.render('ipython_report.index', qcontext={})

    @http.route('%s/config/notebook' % (API_URL, ), auth='public', method='GET')
    def config_notebook(self, debug=False, **kw):
        return json.dumps({})

    @http.route('%s/config/common' % (API_URL, ), auth='public', method='GET')
    def config_common(self, debug=False, **kw):
        return json.dumps({})

    @http.route('%s/kernelspecs' % (API_URL, ), auth='public', method='GET')
    def kernelspecs(self, debug=False, **kw):
        sample = {
            "default": "python3",
            "kernelspecs": {
                "python3": {
                    "name": "python3",
                    "spec": {
                        "argv": ["python", "-m", "ipykernel_launcher", "-f", "{connection_file}"],
                        "env": {},
                        "display_name": "Python 3",
                        "language": "python",
                        "interrupt_mode": "signal",
                        "metadata": {}
                    },
                    "resources": {
                        "logo-32x32": "/kernelspecs/python3/logo-32x32.png",
                        "logo-64x64": "/kernelspecs/python3/logo-64x64.png"
                    }
                }
            }
        }
        return json.dumps(sample)

    @http.route('%s/contents/<notebook_name>' % API_URL, auth='public', method='GET')
    def contents(self, notebook_name, debug=False, **kw):
        notebook_path = '/home/tamvm/Data/notebook/guardian_gaza.ipynb'
        with open(notebook_path, 'r') as f:
            content = json.loads(f.read())
        return json.dumps(dict(
            content=content,
            created='2018-11-12T07:55:01.296009Z',
            format='json',
            last_modified='2018-11-12T07:55:01.296009Z',
            name='guardian_gaza.ipynb',
            path='guardian_gaza.ipynb',
            size=9285,
            type='notebook',
            writable=True
        ))

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