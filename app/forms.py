# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import SelectMultipleField, validators

import Sort


class SortsForm(Form):
    kinds = SelectMultipleField(choices=[(sort, sort.replace('_', ' ')) for sort in Sort.__all__],
                                validators=[validators.DataRequired()])