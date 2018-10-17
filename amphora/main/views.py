from flask import render_template, request, Blueprint, abort


main = Blueprint('main', __name__)

@main.route('/'):
