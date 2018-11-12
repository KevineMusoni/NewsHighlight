from flask import render_template
from . import main
# 404 Page
@main.app_errorhandler(404)
def four_Ow_four(error):
    return render_template("fourOwfour.html"),404
    