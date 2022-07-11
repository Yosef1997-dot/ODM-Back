from flask import Flask, Response, request, json
from bson import ObjectId
import controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = controller.read()
    return Response(response=json.dumps(employees))

@app.route('/add_employee', methods=['POST'])
def upload_employee():
    output = controller.create(request.json)
    return Response(response=json.dumps(output))

@app.route('/update/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    filt = {'_id':ObjectId(employee_id)}
    output = controller.update(filt,request.json )
    return Response(response=json.dumps(output))

@app.route('/delete/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    filt = {'_id':ObjectId(employee_id)}
    output = controller.delete(filt)
    return output

@app.route('/edit/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    filt = {'_id':ObjectId(employee_id)}
    employees = controller.read_one(filt)
    return Response(response=json.dumps(employees))

@app.route('/<employee_id_1>/<employee_id_2>', methods=['GET'])
def compare_between_enployees(employee_id_1, employee_id_2):
    filt = [ObjectId(employee_id_1),ObjectId(employee_id_2)]
    output = controller.compare_between_two_employees(filt)
    return Response(response=json.dumps(output))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
