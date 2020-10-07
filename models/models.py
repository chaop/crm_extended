# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    linkedin = fields.Char(string='linkedin')
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')
    twitter = fields.Char(string='Twitter')


class LeadInherit(models.Model):
    _name = 'crm.lead'
    _inherit = 'crm.lead'

    linkedin = fields.Char(string='linkedin')
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')
    twitter = fields.Char(string='Twitter')

    def handle_partner_assignment(self, force_partner_id=False, create_missing=True):
        super(LeadInherit, self).handle_partner_assignment(force_partner_id, create_missing)
        Partner = self.env['res.partner']
        for lead in self:
            partner = Partner.search([('id', '=', lead.partner_id.id)])
            partner.write({
                'facebook': lead.facebook,
                'linkedin': lead.linkedin,
                'instagram': lead.instagram,
                'twitter': lead.twitter
            })