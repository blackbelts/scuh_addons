import datetime
import numpy as np
from odoo import api, models, fields,modules
from datetime import date
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime,date
import base64
import base64
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
import io
import xlsxwriter
import xlrd
from datetime import datetime
import datetime
from tempfile import TemporaryFile
import time

from datetime import date

from odoo.exceptions import UserError, ValidationError
import io
from datetime import datetime
from xlrd import open_workbook
import base64


class UploadSheet(models.Model):
    _inherit = 'hr.attendance'
    # related="employee_id.pin"
    pin = fields.Char( string="Employee Code",)
    # 'hr.department', string="Department", related="employee_id.department_id",
    #                                     readonly=True

    department_id = fields.Char(string="Department")

class UploadSheet(models.TransientModel):
    _name = 'hr.attendancee'
    # _inherit = 'hr.attendance'
    upload_file= fields.Binary(string="Upload File")
    file = fields.Char(string="Upload File")

    def read_excel(self):
        wb = open_workbook(file_contents=base64.decodestring(self.upload_file))
        sheet = wb.sheets()[0]
        for s in wb.sheets():

            values = []

            for row in range(s.nrows):

                col_value = []

                for col in range(s.ncols):

                    value = (s.cell(row, col).value)

                    try:
                        value = str(int(value))

                    except:
                        pass

                    col_value.append(value)
                values.append(col_value)
                values.append((0, 0, {
                    'employee_id': col_value[0],
                    'ckeck_in': col_value[1],
                    'ckeck_out': col_value[2],
                    'worked_hours': col_value[3],

                }))
                print("vnnv")
                print(values)


    def generate_xls(self):
        # workbook = xlrd.open_workbook(r"/home/eslam/Downloads/Book111.xlsx")
        workbook = xlrd.open_workbook(file_contents=base64.decodestring(self.upload_file))
        print("cvjjvv")
        print(workbook)
        sheet = workbook.sheet_by_name("Sheet1")
        sheet_1 = workbook.sheet_by_index(0)
        for sh in workbook.sheets():
            i = 1
            start_time = time.time()
            values = []
            print(sh.name)
        row_count = sheet.nrows
        col_count = sheet.ncols
        for cur_row in range(1, row_count):
            vals = []
            col_value = []
            for cur_col in range(0, col_count):
                cell = (sheet.cell(cur_row, cur_col).value)
                if cell:
                    try:
                        cell = str(int(cell))
                    except:
                        pass
                col_value.append(cell)
                print("fjjgg")
                print(col_value)
            #
            # mport
            # datetime
            # datetime.datetime.strptime(obj.start_date, '%Y-%m-%d').strftime('%d-%m-%Y')
            vals = {
                'employee_id': int(col_value[0]),
                'pin': col_value[1],
                'department_id': col_value[2],

                'check_in': datetime.strptime(col_value[3], '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'),
                'check_out':datetime.strptime(col_value[4], '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'),
            }
            print("vnnncn")
            print(vals)
            self.env['hr.attendance'].create(vals)
            # self.table_header = vals
            i += 1
        header = sheet.row_values(0, start_colx=0, end_colx=None)
        for sh in workbook.sheets():
            print(sh.name)
    def action_test_connection(self):
        id_created = self.env['hr.attendance'].create({'employee_id':10,
                                                       'check_in':"2022-06-27 12:36:51",
                                                        'check_out': "2022-06-28 15:36:51",
                                                       'pin':1002
            # 'worked_hours': "14:36:51",
                                                       })
        self.env.cr.commit()

