# -*- coding: utf-8 -*-

from random import randint
from timeit import Timer
import pygal
from pygal.style import Style
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground='#53E89B',
  foreground_light='#53A0E8',
  foreground_dark='#630C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))


from flask import render_template, current_app, redirect, url_for, flash, jsonify

from forms import SortsForm
from . import app


@app.route('/')
def index():
    return render_template('index.html', form=SortsForm())


@app.route('/compare/', methods=['POST'])
def compare():
    form = SortsForm()

    if form.validate():

        line_chart = pygal.Line(style=custom_style)
        line_chart.title = 'Sort Algorithms Comparisons (ms)'

        line_chart.x_labels = [str(i) for i in current_app.config['RANGE']]
        rands = [[randint(0, 11000) for x in xrange(i)] for i in current_app.config['RANGE']]

        def campare_sort(sort):
            line_chart.add(sort .replace('_', ' '),
                           [Timer('%s(%s)' % (sort, rand), 'from Sort import %s' % sort).timeit(number=1) for rand in rands])

        for sort in form.kinds.data:
            campare_sort(sort)

        return render_template('compare.html', diagram=line_chart.render())

    return redirect(url_for('index'))