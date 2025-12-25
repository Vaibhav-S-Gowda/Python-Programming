import csv

with open('data1_8dec.csv','r') as f:
    read_dict = csv.DictReader(f)
    for r in read_dict:
        print(r)
# print(type(r))

# with open('data2_8dec.csv','r') as f:
#     read_dict = csv.DictReader(f, delimiter=';', skipinitialspace=True)
#     for r in read_dict:
#         print(r)

with open('data2_8dec.csv','r') as f:
    fnames = ['Name', 'Age', 'Profession']
    read_dict = csv.DictReader(f, fieldnames= fnames, delimiter=';', skipinitialspace=True)
    for r in read_dict:
        print(r)

print(type(read_dict))
print(type(r))