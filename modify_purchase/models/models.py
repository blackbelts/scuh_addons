# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modify_purchase(models.Model):
    # _inherit = 'purchase.order'
    _name = 'modify_purchase.modify_purchase'
    _description = 'modify_purchase.modify_purchasee'

    tender_no = fields.Char(string="Tender No:")
    state = fields.Selection([
        ('pending', 'Draft'),
        ('first', 'Approved'),
    ], default='pending')

    Type = fields.Selection([
        ('Blank', 'Blank Order'),
        ('Tendor', 'Tendor'),
    ],string="Blank Order / Tender Date")
    order_deadline =fields.Date(string="Order Deadline")
    vendorr =fields.Many2one('res.partner' ,string="Approved Offer")

    offer_line= fields.One2many('offer.line','offer_id',string="Financial Proposal")
    Technical_Proposal = fields.One2many('offer.line', 'offer_id', string="Technical Proposal")
    namee = fields.One2many('offer.line', 'offer_id', string="name")

    def offer_line_report(self):
        for rec in self:
            print("fjjdjdjd")
            print(rec.offer_line.vendor_1)

    # value = fields.Integer()

    def generate_reportttt(self):
        datas = {'ids': [self.id]}
        counter = []
        return self.env.ref('modify_purchase.vendor_report').report_action(self)

    def generate_vendor_report(self):
        datas = {'ids': [self.id]}
        counter = []
        return self.env.ref('modify_purchase.vendor_report_report').report_action(self)

    def generate_product_report(self):
        datas = {'ids': [self.id]}
        counter = []
        return self.env.ref('modify_purchase.product_report').report_action(self)

    def generate_inventory_report(self):
        datas = {'ids': [self.id]}
        counter = []
        return self.env.ref('modify_purchase.inventory_report').report_action(self)

    def get_dataa(self):
        data = [{

            'tender_no': self.tender_no,
        }]
        return data



    def emp_cancel(self):
        self.write({
            'state': 'first'
        })

    def emp_approved(self):
        self.write({
            'state': 'pending'
        })

    def get_first_table(self):
        data=[]
        # <field name="Product"  />
        #                                         <field name="vendor_1"  />
        #                                         <field name="vendor_2"  />
        #                                         <field name="vendor_3"  />
        #                                         <field name="vendor_4"  />
        #                                         <field name="vendor_5"  />
        total_vendor_1,total_vendor_2,total_vendor_3,total_vendor_4,total_vendor_5 = 0,0,0,0,0
        for rec in self:
            for ven in rec.Technical_Proposal:
                for pro in ven.Product:
                    data.append({'product':pro.name,
                                 'vendor_1': ven.vendor_1,
                                 'vendor_2': ven.vendor_2,
                                 'vendor_3': ven.vendor_3,
                                 'vendor_4': ven.vendor_4,
                                 'vendor_5': ven.vendor_5,
                                     # 'hospital_size': hospitals_record.num_beds,
                                     # 'icu_n ame': unit_list
                                 }
                                )
                    total_vendor_1 += ven.vendor_1
                    total_vendor_2 +=ven.vendor_2
                    total_vendor_3 +=ven.vendor_3
                    total_vendor_4 +=ven.vendor_4
                    total_vendor_5 +=ven.vendor_5
            totals = [{'name': 'Total','total_vendor_1': total_vendor_1,
                 'total_vendor_2': total_vendor_2,
             'total_vendor_3': total_vendor_3,
             'total_vendor_4': total_vendor_4,
             'total_vendor_5': total_vendor_5,
                       }]

        return [{'data': data, 'total': totals}]


    def get_second_table(self):
        data=[]
        # <field name="Product"  />
        #                                         <field name="vendor_1"  />
        #                                         <field name="vendor_2"  />
        #                                         <field name="vendor_3"  />
        #                                         <field name="vendor_4"  />
        #                                         <field name="vendor_5"  />
        total_vendor_1, total_vendor_2, total_vendor_3, total_vendor_4, total_vendor_5 = 0, 0, 0, 0, 0
        for rec in self:
            for ven in rec.Technical_Proposal:
                for pro in ven.Product:
                    data.append({'product':ven.Criteria_Rating,
                                 'vendor_1': ven.vendor_11,
                                 'vendor_2': ven.vendor_22,
                                 'vendor_3': ven.vendor_33,
                                 'vendor_4': ven.vendor_44,
                                 'vendor_5': ven.vendor_55,
                                     # 'hospital_size': hospitals_record.num_beds,
                                     # 'icu_n ame': unit_list
                                 }
                                )
                    total_vendor_1 += ven.vendor_11
                    total_vendor_2 += ven.vendor_22
                    total_vendor_3 += ven.vendor_33
                    total_vendor_4 += ven.vendor_44
                    total_vendor_5 += ven.vendor_55
                totals = [{'name': 'Total', 'total_vendor_1': total_vendor_1,
                           'total_vendor_2': total_vendor_2,
                           'total_vendor_3': total_vendor_3,
                           'total_vendor_4': total_vendor_4,
                           'total_vendor_5': total_vendor_5,
                           }]

            return [{'data': data, 'total': totals}]




    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class OfferLine(models.Model):
    _name = 'offer.line'
    _rec_name = 'vendor_name'


    Vendor =fields.Many2one('res.partner', string='Vendor', )
    vendor_name = fields.Char(string="name")

    vendor_1=fields.Float(string="Vendor 1")
    vendor_2 = fields.Float(string="Vendor 2")
    vendor_3 = fields.Float(string="Vendor 3")
    vendor_4 = fields.Float(string="Vendor 4")
    vendor_5 = fields.Float(string="Vendor 5")

    vendor_11 = fields.Float(string="Vendor 1")
    vendor_22 = fields.Float(string="Vendor 2")
    vendor_33 = fields.Float(string="Vendor 3")
    vendor_44 = fields.Float(string="Vendor 4")
    vendor_55 = fields.Float(string="Vendor 5")

    Product = fields.Many2one('product.product','Criteria (price)')

    Criteria_Rating= fields.Char(string="Criteria (Rating)")

    Price = fields.Char(string="Price")
    offer_id= fields.Many2one('modify_purchase.modify_purchase')
