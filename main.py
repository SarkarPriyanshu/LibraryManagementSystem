from Library import Library
from LibraryManagement import LibraryManagement

session = Library()
manage = LibraryManagement()
Authors = [
    (7,'Aldous Huxley','He is a great author'),
    (8,'William Golding','He is a great author'),
    (9,'Gabriel Garcia Marquez','He is a great author'),
    (10,'Kurt Vonnegut','He is a great author')
]

# print(manage.insertbooks((6,'1984','George Orwell','Science Fiction',1949,True)))
print(manage.insertauthors(Authors))
print(session.getauthorslist())