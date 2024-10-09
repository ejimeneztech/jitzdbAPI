from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import CORS

pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app)


# Database configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ejimenez90:Skynet9000%21@ejimenez90.mysql.pythonanywhere-services.com/ejimenez90$jitzdbAPI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#create data model0. Update line 17-25 if columns are modified
class Tech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    steps = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name,"title": self.title, "steps": self.steps }

# Create the database tables
with app.app_context():
    db.create_all()


#list of techs
@app.route('/techs', methods=['GET'])
def get_techs():
    techs = Tech.query.all()
    return jsonify([tech.to_dict() for tech in techs])


# get data for each tech
@app.route('/techs/<int:id>', methods=['GET'])
def get_tech_id(id):
    tech = Tech.query.get(id)
    if tech:
        return jsonify(tech.to_dict())
    else:
        return jsonify({"error": "Technique not found"}), 404



#create a tech
@app.route('/create', methods=['POST'])
def create_tech():
    new_tech = request.get_json()
    # Ensure all required fields are present
    if 'name' not in new_tech or 'title' not in new_tech:
        return jsonify({"error": "Name and title are required"}), 400
    tech = Tech(name=new_tech['name'], title=new_tech['title'], steps=new_tech['steps'])
    db.session.add(tech)
    db.session.commit()
    return jsonify(tech.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)