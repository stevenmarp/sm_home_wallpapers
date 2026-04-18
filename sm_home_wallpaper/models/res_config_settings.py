# -*- coding: utf-8 -*-
import ast
import random

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sm_wallpaper_ids = fields.Many2many(
        'ir.attachment',
        string='Home Screen Wallpapers',
        help='Upload images to use as random home screen backgrounds. '
             'A random image is shown each time the home screen loads.',
    )

    @api.model
    def sm_get_random_wallpaper(self):
        """Return a random wallpaper attachment ID, or False if none set."""
        ICP = self.env['ir.config_parameter'].sudo()
        raw = ICP.get_param('sm_home_wallpaper.wallpaper_ids', '[]')
        try:
            ids = ast.literal_eval(raw)
        except (ValueError, SyntaxError):
            ids = []
        if not ids:
            return False
        # Filter to only existing attachments
        valid = self.env['ir.attachment'].sudo().browse(ids).exists().ids
        if not valid:
            return False
        return random.choice(valid)

    @api.model
    def get_values(self):
        res = super().get_values()
        ICP = self.env['ir.config_parameter'].sudo()
        raw = ICP.get_param('sm_home_wallpaper.wallpaper_ids', '[]')
        try:
            ids = ast.literal_eval(raw)
        except (ValueError, SyntaxError):
            ids = []
        if ids:
            res['sm_wallpaper_ids'] = [(6, 0, ids)]
        return res

    def set_values(self):
        super().set_values()
        ICP = self.env['ir.config_parameter'].sudo()
        ICP.set_param('sm_home_wallpaper.wallpaper_ids', str(self.sm_wallpaper_ids.ids))
