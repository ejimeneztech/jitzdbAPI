from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ejimenez90:Skynet9000!@ejimenez90.mysql.pythonanywhere-services.com/ejimenez90$jitzdbAPI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#create data model
class Tech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# Create the database tables
with app.app_context():
    db.create_all()


#list of techs
@app.route('/techs', methods=['GET'])
def get_tasks():
    techs = Tech.query.all()
    return jsonify([tech.to_dict() for tech in techs])


# get data for each tech


#create a tech
@app.route('/techs', methods=['POST'])
def create_tech():
    new_tech = request.get_json()
    tech = Tech(name=new_tech['name'])
    db.session.add(tech)
    db.session.commit()
    return jsonify(tech.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)