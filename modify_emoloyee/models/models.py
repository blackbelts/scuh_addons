

from odoo import models, fields, api


class modify_emoloyee(models.Model):
    # _name = 'scuh_emoloyee.scuh_emoloyee'
    _inherit = 'hr.employee'
    _description = 'scuh_emoloyee.scuh_emoloyee'
    identification_id = fields.Char(required=True)
    name = fields.Char(required=True)
    phone = fields.Char(required=True ,readonly=False)
    job_id = fields.Many2one(required=True)

class modify_payroll(models.Model):
    _inherit = 'hr.payslip.run'

    department_id = fields.Many2one('hr.department',
                                    string="Department", help="Employee")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
