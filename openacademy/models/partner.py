# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
    level = fields.Integer(compute="_get_level", string="Teacher", store=True)

    wizard_ids = fields.Many2many('openacademy.wizard')

    @api.depends('category_id', 'category_id.name')
    def _get_level(self):
        for partner in self:
            level = []
            for categ in partner.category_id:
                if "Chain Level" in categ.name:
                    level.append(int(categ.name.split(' ')[-1]))
            partner.level = max(level) if level else 0


class PartnerSessionWizard(models.TransientModel):
    _name = "openacademy.wizard"

    session = fields.Many2one('openacademy.session', string="Session")

    def _default_partners(self):
        return self.env['res.partner'].browse(self._context.get('active_ids'))

    partners = fields.Many2many('res.partner', string="Participants", default=_default_partners)

    
    @api.multi
    def subscribe(self):
        for partner in self.partners:
            self.session.attendee_ids |= partner
        return {}

