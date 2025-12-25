import xml.etree.ElementTree as xml
employees=[
    {'Name':"Shannu",
     "Age": 23,
     'Salary':240000},
     {'Name':"Keerthi",
     "Age": 23,
     'Salary':24000},
     {'Name':"Mindri",
     "Age": 2,
     'Salary':0}
     ]

root=xml.Element("employees")
# print(employees)

for emp in employees:
    b_element=xml.Element('Employees')
    root.append(b_element)
    b_element.set('Employees',employees['Employee'])
    name = xml.SubElement(b_element, 'Name')
    name.text = employees['Name']
    age = xml.SubElement(b_element, 'Age')
    age.text = employees['Age']
    sal = xml.SubElement(b_element, 'Salary')
    sal.text = float(employees['Salary'])
tree = xml.ElementTree(root)

with open('Employees.xml', 'wb') as fh:
    tree.write(fh)