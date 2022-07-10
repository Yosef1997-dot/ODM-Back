from flask import Flask, Response, request, json
from bson import ObjectId
import controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['GET'])
def get_all_employees():
    users = controller.read()
    return Response(response=json.dumps(users))

@app.route('/add_user', methods=['POST'])
def upload_employee():
    output = controller.create(request.json)
    return Response(response=json.dumps(output))

@app.route('/update/<user_id>', methods=['PUT'])
def update_employee(user_id):
    filt = {'_id':ObjectId(user_id)}
    output = controller.update(filt,request.json )
    return Response(response=json.dumps(output))

@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_employee(user_id):
    filt = {'_id':ObjectId(user_id)}
    output = controller.delete(filt)
    return output

@app.route('/<user_id>', methods=['GET'])
@app.route('/edit/<user_id>', methods=['GET'])
def get_employee(user_id):
    filt = {'_id':ObjectId(user_id)}
    users = controller.read_one(filt)
    return Response(response=json.dumps(users))

@app.route('/<user_id_1>/<user_id_2>', methods=['GET'])
def compare_between_enployees(user_id_1, user_id_2):
    filt = [ObjectId(user_id_1),ObjectId(user_id_2)]
    output = controller.compare_between_two_employees(filt)
    return Response(response=json.dumps(output))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
