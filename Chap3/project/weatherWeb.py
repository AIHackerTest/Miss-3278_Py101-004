#! /urs/bin/env python
# coding=utf-8

from flask import Flask, render_template, redirect, session, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from weatherAPI import weather


app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

history = []


class NameForm(FlaskForm):
    name = StringField("请输入城市名称：", validators=[Required()])
    submit = SubmitField("查询")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    

@app.route('/help')
def help(): 
    return render_template('help.html')
    
@app.route('/history')
def history():
    global history
    form = NameForm()
    if form.validate_on_submit():
        city = form.name.data
        result = weather(city)
        if result != "查询失败！":
            history.append(result) 
    return render_template('history.html', history = history)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        city = form.name.data
        result = weather(city)
        flash(result)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

    
    
if __name__ == '__main__':
    manager.run()
        
    
