from odoo import api, fields, models
import json
import requests

class TokoBuku(models.Model):
    _name = 'toko.buku'
    _description = 'Toko Buku'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', copy=False)
    alamat = fields.Char(string='Alamat')
    contact = fields.Char(string='Kontak')
    pemilik = fields.Many2one(comodel_name='res.partner', string='Pemilik')
    pajak = fields.Integer(string='Pajak')
    discount = fields.Integer(string='Diskon')
    
    # o2m 
    buku_line = fields.One2many(comodel_name='buku.buku', inverse_name='toko_id', 
        string='')
    
    def get_buku(self) :
        query_param = {}
        base_url = 'http://localhost:8080/books'
        response = requests.get(base_url, params = query_param)
        return response.json()

    def get_parsing_buku(self):
        data = self.get_buku()
        # deklarasi object
        buku_obj = self.env['buku.buku']
        toko_obj = self.env['toko.buku']
        for line in data:
            toko = toko_obj.browse(line['toko_id'])
            vals = {
                'name' : line['title'], 
                'description' : line['description'],
                'release_year' : line['release_year'],
                'price' : line['price'],
                'total_page' : line['total_page'],
                'thickness' : line['thickness'],
                'toko_id' : line['toko_id'],
                'price_taxed' : self.get_price_taxed(line['price'], toko.pajak, toko.discount),
                'price_discount' : self.get_price_discount(line['price'], toko.pajak, toko.discount)
            }
            buku_obj.create(vals)

    def get_price_taxed(self, price, pajak, discount):
        query_param = {}
        base_url = 'http://localhost:8080/books/price'
        query_param['hitung'] = "pajak"
        query_param['price'] = price
        query_param['tax'] = pajak
        query_param['discount'] = discount
        response = requests.get(base_url, params = query_param)
        return response.json()

    def get_price_discount(self, price, pajak, discount):
        query_param = {}
        base_url = 'http://localhost:8080/books/price'
        query_param['hitung'] = "discount"
        query_param['price'] = price
        query_param['tax'] = pajak
        query_param['discount'] = discount
        response = requests.get(base_url, params = query_param)
        return response.json()

class BukuBuku(models.Model):
    _name = 'buku.buku'
    _description = 'List Buku'

    name = fields.Char(string='Title', copy=False)
    description = fields.Char(string='Deskripsi')
    release_year = fields.Integer(string='Release Year')
    price = fields.Char(string='Price')
    total_page = fields.Integer(string='Total Page')
    thickness = fields.Char(string='Thickness')
    price_taxed = fields.Integer(string='Price Taxed')
    price_discount = fields.Integer(string='Price Discount')
    
    # m2o 
    toko_id = fields.Many2one(comodel_name='toko.buku', string='Toko Buku')