import json as j

p = '{"name":"Alpha","age":30}'
p_dict = j.loads(p)
print(type(p), type(p_dict))

# with open('Json file1.json','r') as f:
#     p_json = j.load(f)
#     print(type(p_json))
#     print(p_json)

# with open('Json file2.json','r') as f:
#     p2_json = j.load(f)
#     print(type(p2_json))
#     print(p2_json)

# print(p2_json[0]["name"])
# for r in p2_json:
    # print(r['name'])

print("Json file3")
with open('Json file3.json','r') as f:
    p3_json = j.load(f)
    print(type(p3_json))
    print(p3_json)
    print(p3_json['alpha']['city'])
    for r in p3_json:
        print(f'Name : {r}')
        print(f"Age: {p3_json[r]['age']}")
        print(f"City: {p3_json[r]['city']}")

# ----------- Writing the JSON objects------------

n_dict = {'name':'Delta','age':25}
n_json = j.dumps(n_dict)
print(type(n_dict),type(n_json))
print(n_dict)
print(n_json)

with open('Json file4.json','w') as f:
    j.dump(n_dict, f)

with open('Json file4.json','a') as f:
    j.dump(n_dict,f)

with open('Json file4.txt','w') as f:
    j.dump(n_dict, f)