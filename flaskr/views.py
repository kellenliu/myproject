from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('views', __name__)


@bp.route('/')
def views():
    db = get_db()
    viewconts = db.execute(
        'SELECT age_section, num, flag '
        ' FROM carry_for_age'
        ' ORDER BY age_section '
    ).fetchall()
    return render_template('views/pie.html', viewconts=viewconts)


@bp.route('/lib')
def jstmp():
    return render_template('views/lib/echarts.custom.min.js')


