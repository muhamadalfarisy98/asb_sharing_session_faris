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
            base_url = 'http://192.168.1.7:8069/'
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
                'image' : self.get_image_url(product.id),
                'price' : product.list_price,
                'qty_available': int(product.qty_available)
                } for product in product_ids ]
        else :
            product_ids = self.search([])
            return [
                {
                'id' : product.id,
                'name' : product.name, 
                'image' : self.get_image_url(product.id),
                'price' : product.list_price,
                'qty_available': int(product.qty_available)
                } for product in product_ids ]

    def api_edit_product(self, product_id, body):
        product_id = self.search([('id','=',product_id)])
        if not product_id:
                return [{'error': {
                        'code': 401, 'message': 'ID tidak ditemukan!'
                        }}]
        vals = body.get('data', False)
        product_id.write(vals)
        message = "product %s was successfully edited" % (
            product_id.name)
        return {'message' : message}

    def api_post_product(self, body):
        new_product = body.get('data', False)
        if new_product:
            try:
                product_id = self.create(new_product)
            except Exception:
                raise RestException(
                    400, "Invalid parameters to Create New Teacher")
        return {
            "product_id": product_id.id,
            "name" : product_id.name,
            "type" : product_id.type,
            "categ" : product_id.categ_id.name,
            "price" : product_id.list_price
        }

    def api_delete_product(self, product_id):
        product_id = self.search([('id', '=', product_id)])
        if not product_id:
                return [{'error': {
                        'code': 401, 'message': 'ID tidak ditemukan!'
                        }}]
        product_name = product_id.name
        product_id.unlink()
        message = "Product %s was successfully deleted" % (
            product_name)
        return {'message' : message}