# -*- encoding: utf-8 -*-
# Copyright (C) 2009-Today Tech Receptives(http://techreceptives.com).
# Parthiv Pate, Tech Receptives, Open Source For Ideas
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class LetterClass(models.Model):
    """ Class to define the classification of letter like : classified,
    confidential, personal, etc. """
    _name = 'letter.class'
    _description = "Letter Classification"
    name = fields.Char('Type', required=True)
