
from flask import Flask, render_template
import os
import pymongo
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client.thirty_days_of_python
# db.students.insert_one({'name': 'Paulin', 'country':'Togo', 'city': 'ville', 'age': 21})
# print(client.list_database_names())
# app = Flask(__name__)
# if __name__ == '__main__':
#      port = int(os.environ.get("PORT", 5000))
#      app.run(debug=True, host='0.0.0.0', port=port)

# MONGODB_URI = 'mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client.thirty_days_of_python
# students = [
# {'name':'David','country':'UK','city':'London','age':34},
# {'name':'John','country':'Sweden','city':'Stockholm','age':28},
# {'name':'Sami','country':'Finland','city':'Helsinki','age':25},]
# for student in students:
#     db.students.insert_one(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

#
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# student = db.students.find_one()
# print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# ##
# from bson.objectid import ObjectId # id object
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
# print(student)
# app = Flask(__name__)
# if __name__ == '__main__':
# # for deployment we use the environ
# # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# ##
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython''

# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# students = db.students.find()
# for student in students:
#     print(student)
# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
#  ##
# from flask import Flask, render_template
# import os
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] 
# query = {
# "country":"Finland"
# }
# students = db.students.find(query)
# for student in students:
#     print(student)
# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# #
# from flask import Flask, render_template
# import os
# import pymongo
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python']
# query = {
# "city":"Helsinki"
# }
# students = db.students.find(query)
# for student in students:
# print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython''
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python']
# query = {
# "country":"Finland",
# "city":"Helsinki"
# }
# students = db.students.find(query)
# for student in students:
#     print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


# #
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# students = db.students.find().sort('name')
# for student in students:
#     print(student)

# students = db.students.find().sort('name',-1)
# for student in students:
#     print(student)
# students = db.students.find().sort('age')
# for student in students:
#     print(student)
# students = db.students.find().sort('age',-1)
# for student in students:
#     print(student)
# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
#     #
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# query = {'age':250}
# new_value = {'$set':{'age':38}}
# db.students.update_one(query, new_value)
# # lets check the result if the age is modified
# for student in db.students.find():
#     print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
# MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python'] # accessing the database
# query = {'name':'John'}
# db.students.delete_one(query)
# for student in db.students.find():
#     print(student)
# # lets check the result if the age is modified
# for student in db.students.find():
#     print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
# # for deployment we use the environ
# # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
# #
MONGODB_URI ='mongodb+srv://koutoatipaulin:devpaulingameli11@30daysofpython.lhjmfyf.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']
db.students.drop()