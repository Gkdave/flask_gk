from flask import Blueprint, request ,render_template

bp = Blueprint("web",__name__)


@bp .route("/")
def index():
    return "<h1>hello User !</h1>"
    #return render_template("user/show.html")