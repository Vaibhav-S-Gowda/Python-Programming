import xml.etree.ElementTree as xml
books=[
    {'Title':"Pride and Prejustice",
     "Author":'Jane Austen',
     'Price':240,
     'Category':'Fiction'},
    {'Title':"The Diary of young girl",
     "Author":'Anne Frank',
     'Price':500,
     'Category':'Non-Fiction'},
    {'Title':"Five on a Treasure Island",
     "Author":'Enid Blyton0',
     'Price':250,
     'Category':'Fiction'}]

root=xml.Element("Books")
# print(type(root))
for book in books:
    b_element=xml.Element('Book')
    root.append(b_element)
    b_element.set('Category',book['Category'])
    '''First parameter - attribute name'''
    '''Second parameter - attribute value'''
    title = xml.SubElement(b_element, 'Title')
    '''First parameter - parent node'''
    '''Second parameter - name of the child node'''
    title.text = book['Title']
    author = xml.SubElement(b_element, 'Author')
    author.text = book['Author']
    price = xml.SubElement(b_element, 'Price')
    price.text = str(book['Price'])
tree = xml.ElementTree(root)

with open('Book.xml', 'wb') as fh:
    tree.write(fh)

# print('Books.xml file has been created')

# print(type(b_element),'\n',type(title),'\n',type(author), '\n',type(price))

# print(title)
# print(title.text)

tree = xml.ElementTree(file = 'Book.xml')
root = tree.getroot()
books = []
# print(type(tree), type(root), type(books))

for book in root.findall('Book'):
    b_data = {}
    b_data['Category'] = book.get('Category')
    '''Get the attribute and its value'''
    for d in book:
        '''Get each child element for every parent'''
        b_data[d.tag] = d.text
    books.append(b_data)
# print(type(b_data),'\n',type(d),'\n',type(book))
print(books)

# -------------------------------------------
#         Modification of a XML file
# -------------------------------------------

tree = xml.ElementTree(file='Book.xml')
root=tree.getroot()

# Iterate over prce
for p_ele in root.iter('Price'):
    p = int(p_ele.text)
    '''Convert the string value into an integer'''
    p+=20
    p_ele.text = str(p)
    '''Convert the element's value to a string'''
    '''Since all values are stored as strings in XML'''

# Write the new data back into an XML file
with open('Book.xml','wb') as f:
    tree.write(f)

print('Prices Updated')