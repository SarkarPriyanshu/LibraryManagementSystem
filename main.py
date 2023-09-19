from Library import Library
from LibraryManagement import LibraryManagement
from TransactionManagements import TransactionManagements

session = Library()
manage = LibraryManagement()
transaction = TransactionManagements()

print(session.getpatronslist())
print(transaction.FindBookISBN('To Kill a Mockingbird'))


