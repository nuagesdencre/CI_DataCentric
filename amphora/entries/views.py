from flask import render_template, url_for, flash, Blueprint, redirect, request
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being
from amphora.entries.forms import Entry