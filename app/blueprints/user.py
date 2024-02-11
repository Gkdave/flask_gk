from flask import Blueprint,redirect, request ,render_template , url_for 
from app.models.user import User as UserModel

bp = Blueprint("user",__name__)

from flask import Flask
from app.extentions import db 



@bp .route("/user/")
def index():
    users = UserModel.query.all()
    return render_template("user/index.html", users=users)
    
       

@bp .route("/user/",methods=["POST"]) 
def store():
    newUser = UserModel(
        name=request.form["name"],
        email=request.form["email"]
    )
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("user.index"))

        

@bp .route("/user/create")
def create():
    #return url_for("user.user")
    return render_template("user/create.html")


@bp .route("/user/<int:id>", methods=["DELETE","PUT"])
def user_id(id):
    if request.method == "DELETE":
        user = UserModel.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "Deleted"   
    elif request.method == "PUT":
        return "<h1> Update users </h1>"
    
@bp .route("/user/<int:id>")
def about(id):
    return render_template("user/show.html",id=id)