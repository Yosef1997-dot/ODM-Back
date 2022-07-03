
from bson import ObjectId
from dbConnection import usersCollection


def read():
    users = usersCollection.find()
    output = [{'id':str(data['_id']), 'name':data['name']}
              for data in users]
    return output


def create(new_user):
    response = usersCollection.insert_one(new_user)
    output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
    return output


def update(filt, updated_user):
    response = usersCollection.update_one(filt, {"$set": updated_user})
    output = {'Status': 'Successfully Updated' if response.modified_count >
                  0 else "Nothing was updated."}
    return output


def delete(filt):
    response = usersCollection.delete_one(filt)
    output = {'Status': 'Successfully Deleted' if response.deleted_count >
                0 else "Document not found."}
    return output


def read_one(filt):
    user = usersCollection.find_one(filt)
    output = {item: user[item] for item in user if item != '_id' and item !='salary'}
          
    return output


def get_percentage_diff(a, b):
    try:
        percentage = 100 - abs(a - b)/max(a, b) * 100 
    except ZeroDivisionError:
        percentage = float('inf')
    return percentage
    
def compare_between_two_employees(filt):

    output = []

    for user_id in filt:
        output.append(usersCollection.find_one({'_id':user_id}))

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






