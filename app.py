from flask import Flask, jsonify, request

app = Flask(__name__)

#connect to database
techs = [
    {"id" : 1, "Armbar": "step 1", "completed": False },
    {"id": 2, "title": "Task 2", "completed": True},
]

#list of techs
@app.route('/techs', methods=['GET'])
def get_tasks():
    return jsonify(techs)


# get data for each tech
@app.route('/techs/<int:tech_id>', methods=['GET'])
def get_tech(tech_id):
    tech = next((tech for tech in techs if tech["id"] == tech_id), None)
    return jsonify(tech) if tech else ('', 404)

#create a tech
@app.route('/techs', methods=['POST'])
def create_tech():
    new_tech = request.get_json()
    techs.append({"id": len(techs) + 1, **new_tech})
    return jsonify(new_tech), 201

if __name__ == '__main__':
    app.run(debug=True)