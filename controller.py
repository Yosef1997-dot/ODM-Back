from dbConnection import employeesCollection


def read():
    employees = employeesCollection.find()
    output = [{'id':str(employee['_id']), 'name':employee['name']}
              for employee in employees]
    return output


def create(new_employee):
    response = employeesCollection.insert_one(new_employee)
    output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
    return output


def update(filt, updated_employee):
    response = employeesCollection.update_one(filt, {"$set": updated_employee})
    output = {'Status': 'Successfully Updated' if response.modified_count >
                  0 else "Nothing was updated."}
    return output


def delete(filt):
    response = employeesCollection.delete_one(filt)
    output = {'Status': 'Successfully Deleted' if response.deleted_count >
                0 else "Document not found."}
    return output


def read_one(filt):
    employee = employeesCollection.find_one(filt)
    output = {item: employee[item] for item in employee if item != '_id' and item !='salary'}
          
    return output


def get_percentage_diff(a, b):
    try:
        percentage = 100 - abs(a - b)/max(a, b) * 100 
    except ZeroDivisionError:
        percentage = float('inf')
    return percentage
    
def compare_between_two_employees(filt):

    output = []

    for employee_id in filt:
        output.append(employeesCollection.find_one({'_id':employee_id}))

    output = [{'id':str(item['_id']), 'name':item['name'],'salary':item['salary']}
              for item in output]
    
    output[0]['difference'] = output[0]['salary']  - output[1]['salary']
    output[1]['difference'] = output[1]['salary']  - output[0]['salary']
    
    per_diff = 100 - get_percentage_diff(output[0]['salary'],output[1]['salary'])

    if  output[0]['salary'] > output[1]['salary'] :
        output[1]['percentage'] = str(per_diff) + '%'
    elif output[1]['salary'] > output[0]['salary']:
        output[0]['percentage'] = str(per_diff) + '%'

    
    return output






