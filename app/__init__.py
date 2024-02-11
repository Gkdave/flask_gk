from app.blueprints import web, user 
from flask import Flask ,request
from app.extentions import db 


app = Flask(__name__)
from flask import Flask




app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

app.register_blueprint(web.bp)
app.register_blueprint(user.bp)




with app.app_context():
    db.create_all()
