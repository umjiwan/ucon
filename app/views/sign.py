from flask import Blueprint, redirect, request, flash, url_for, render_template
from app import db
from app.models import UserSignUpInfo
from app.forms import SignUpForm
from werkzeug.security import generate_password_hash


bp = Blueprint('signin', __name__, url_prefix='/sign')

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