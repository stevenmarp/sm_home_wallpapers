# -*- coding: utf-8 -*-
{
    'name': 'Home Screen Wallpaper',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Customize the Odoo home screen with random background wallpapers',
    'description': """
Home Screen Wallpaper
=====================

Customize your Odoo home screen with beautiful background wallpapers.
Upload multiple images and a random one is displayed each time you visit the
home screen. Fully configurable from Settings.
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/browse?repo_maintainer_id=512936',
    'license': 'OPL-1',
    'depends': ['base', 'base_setup', 'web'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sm_home_wallpaper/static/src/js/home_wallpaper.js',
        ],
    },
    'images': ['static/description/banner.gif', 'static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 1.00,
    'currency': 'USD',
}
