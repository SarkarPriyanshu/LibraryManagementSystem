from Library import Library
from LibraryManagement import LibraryManagement
from TransactionManagements import TransactionManagements

session = Library()
manage = LibraryManagement()
transaction = TransactionManagements()

print(session.getpatronslist())
# print(transaction.FindPatronID('Divesh Sharma'))
print(transaction.ReturnTransaction('Divesh Sharma','To Kill a Mockingbird',2))


