# -*- coding: utf-8 -*-
from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    invoice_partner_id = fields.Many2one('res.partner', string='Invoice Partner')