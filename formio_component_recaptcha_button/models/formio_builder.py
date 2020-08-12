# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from odoo import fields, models


class Builder(models.Model):
    _inherit = 'formio.builder'

    component_recaptcha_button_site_key = fields.Char(string='(odoo) reCAPTCHA Site Key', compute='_compute_recaptcha_button')
    component_recaptcha_button_secret_key = fields.Char(string='(odoo) reCAPTCHA Secret Key', compute='_compute_recaptcha_button')

    def _compute_recaptcha_button(self):
        Config = self.env['ir.config_parameter'].sudo()
        site_key = Config.get_param('formio_recaptcha_button.site_key')
        secret_key = Config.get_param('formio_recaptcha_button.secret_key')
        self.component_recaptcha_button_site_key = site_key
        self.component_recaptcha_button_secret_key = secret_key
