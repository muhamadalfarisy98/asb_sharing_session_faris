from odoo import http
from odoo.http import request, route

from ..jwt.login import token_required

class ApiProduct(http.Controller):

    @route(route=['/api/v1/product/',
                  '/api/v1/product/<int:product_id>'],
           methods=['GET'], type='json', auth='public', csrf=False)
    # @token_required()
    def get_product(self, product_id=False, debug=False, **kwargs):
        product = request.env['product.product'].with_user(
            kwargs.get('uid', 1)).api_get_product(product_id = product_id)
        result = {}
        result['result'] = product
        return result

    # @route('/api/v1/parent/<int:parent_id>', methods=['PUT'], type='json', auth='public', csrf=False)
    # @token_required()
    # def edit_parent(self, parent_id, **kwargs):
    #     body = request.jsonrequest
    #     result = request.env['parent.parent'].with_user(
    #         kwargs.get('uid', 1)).api_edit_parent(
    #         parent_id, body)
    #     code = 201
    #     if type(result) == list:
    #         code = 401
    #     return {'result': result, 'code': code}

    # @route('/api/v1/parent', methods=['POST'], type='json', auth='public', csrf=False)
    # @token_required()
    # def post_parent(self, **kwargs):
    #     body = request.jsonrequest
    #     result = request.env['parent.parent'].with_user(
    #         kwargs.get('uid', 1)).api_post_parent(body)
    #     return {'result': result, 'code': 201}

    # @route('/api/v1/parent/<int:parent_id>', methods=['DELETE'], type='json', auth='public', csrf=False)
    # @token_required()
    # def delete_parent(self, parent_id, **kwargs):
    #     result = request.env['parent.parent'].with_user(
    #         kwargs.get('uid', 1)).api_delete_parent(
    #         parent_id)
    #     code = 201
    #     if type(result) == list:
    #         code = 401
    #     return {'result': result, 'code': code}