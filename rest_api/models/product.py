from odoo import models, SUPERUSER_ID
from ..exceptions import RestException
import base64
from odoo.http import request, route
from odoo import http

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_image_url(self, product_id):
        product = self.search([('id','=',product_id)])
        base_url = self.env['ir.config_parameter'].with_user(SUPERUSER_ID).get_param('web.base.url')\
                        or request.httprequest.host_url
        if base_url[-1] != '/':
            base_url = base_url + '/'

        if not product.image_1920:
            image_url = ""
        else:
            try:
                image_url = base_url + 'web/image?model=' + self._name + '&id=' + str(
                    product.id) + '&field=' + 'image_1920' + '&session_id=' + http.request.session.sid
            except Exception as e:
                image_url = base_url + 'web/image?model=' + \
                    self._name + '&id=' + str(product.id) + '&field=' + 'image_1920'
        return image_url

    def api_get_product(self, product_id=False):
        if product_id :
            product_ids = self.search([('id', '=', product_id)])
            if not product_ids:
                return [{'error': {
                        'code': 401, 'message': 'ID tidak ditemukan!'
                        }}]
            return [
                {
                'id' : product.id,
                'name' : product.name, 
                'image' : self.get_image_url(product.id)
                
                } for product in product_ids ]
        else :
            product_ids = self.search([])
            return [
                {
                'id' : product.id,
                'name' : product.name, 
                'image' : self.get_image_url(product.id)
                } for product in product_ids ]

    # def api_edit_parent(self, parent_id, body):
    #     parent_id = self.search([('id','=',parent_id)])
    #     if not parent_id:
    #             return [{'error': {
    #                     'code': 401, 'message': 'ID tidak ditemukan!'
    #                     }}]
    #     vals = body.get('data', False)
    #     parent_id.write(vals)
    #     message = "Parent %s was successfully edited" % (
    #         parent_id.name)
    #     return {'message' : message}

    # def api_post_parent(self, body):
    #     new_parent = body.get('data', False)
    #     if new_parent:
    #         try:
    #             parent_id = self.create(new_parent)
    #         except Exception:
    #             raise RestException(
    #                 400, "Invalid parameters to Create New Teacher")
    #     return {
    #         "parent_id": parent_id.id,
    #         "name" : parent_id.name,
    #         "gender" : parent_id.gender,
    #         "email" : parent_id.email,
    #         "phone" : parent_id.phone
    #     }

    # def api_delete_parent(self, parent_id):
    #     parent_id = self.search([('id', '=', parent_id)])
    #     if not parent_id:
    #             return [{'error': {
    #                     'code': 401, 'message': 'ID tidak ditemukan!'
    #                     }}]
    #     parent_name = parent_id.name
    #     parent_id.unlink()
    #     message = "Teacher %s was successfully deleted" % (
    #         parent_name)
    #     return {'message' : message}