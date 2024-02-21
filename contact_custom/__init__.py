from odoo import api, models, fields

class CustomContact(models.Model):
    _inherit = 'res.partner'

    # Champs personnalisés
    cni = fields.Char(string="Numéro CNI", size=11, required=False)
    niu = fields.Char(string="Numéro NUI", size=14, required=False)
