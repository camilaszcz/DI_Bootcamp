# info = {
#     'first_name': 'Camila',
#     'last_name': 'Szczerbacki',
#     'phone': '0503317818',
# }

# print(info)


# print('Keys:', info.keys())
# print('Values:', info.values())

# print('Items:', info.items())


#Class Exercise

from ast import comprehension


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

      
# Delete set of keys from Python Dictionary

# keys_to_remove = ["name", "salary"]

# Expected output:  {'city': 'New york', 'age': 25}

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

del sample_dict['name']
print(sample_dict)

del sample_dict['salary']
print(sample_dict)

keys_to_remove = ['name', 'salary']

for key_rmv in keys_to_remove:
   
   if key_rmv in sample_dict:
      del sample_dict[key_rmv]
      
      print(sample_dict)
      
      
# comprehension

a_list=[]

for num in range(0,100,10):
   a_list.append(num)
   
print(a_list)

