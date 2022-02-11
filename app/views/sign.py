from flask import Blueprint, redirect, request, flash, session, url_for, render_template, session, g
from app import db
from app.models import UserSignUpInfo
from app.forms import SignUpForm, SignInForm
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('sign', __name__, url_prefix='/sign/')

@bp.route("/up", methods=["GET", "POST"])
def SignUp():
    form = SignUpForm()

    if request.method == "POST" and form.validate_on_submit():
        user = UserSignUpInfo.query.filter_by(username=form.username.data).first()
        if not user:
            user = UserSignUpInfo(username=form.username.data,
                                  email=form.email.data,
                                  password=generate_password_hash(form.password1.data))

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.index"))

        else:
            flash("이미 존재하는 사용자입니다.")

    return render_template('signup.html', form=form)

@bp.route("/in/", methods=["GET", "POST"])
def SignIn():
    form = SignInForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = UserSignUpInfo.query.filter_by(username=form.username.data).first()

        if not user:
            error = "존재하지 않는 사용자입니다."

        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))

        flash(error)
    return render_template('signin.html', form=form)

@bp.route('/out/')
def SignOut():
    session.clear()
    return redirect(url_for('main.index'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = UserSignUpInfo.query.get(user_id)