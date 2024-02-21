from odoo import api, models, fields, _

class CustomContact(models.Model):
    _inherit = 'res.partner'

    @api.constrains('cni', 'niu')
    def _check_format(self):
        for record in self:
            if record.cni and len(record.cni) != 11:
                raise ValidationError(_("Le numéro CNI doit comporter 11 caractères."))
            if record.niu and len(record.niu) != 14:
                raise ValidationError(_("Le numéro NUI doit comporter 14 caractères."))
