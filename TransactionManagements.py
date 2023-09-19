from DataBase import DatabaseConnection
from typing import Union,Dict,Tuple,List

class TransactionManagements(DatabaseConnection):
    '''
        TransactionManagements:
            This class is mainly focus on finding relavent information about books, patrons and storing there transation type.

        Key features:
             Find booksISBN using book name
             Find PatronID using Name 
             Storing Transations like

                Checkout Transaction : Patrons borrow library materials (e.g., books) for a specified duration.
                Check-in Transaction : Patrons return borrowed items to the library.
                Renewal Transaction  : Patrons may request to extend the borrowing period of checked-out items.
    '''

    def FindBookISBN(self,Name:str)->Dict:
        '''
            FindBookISBN:
                This Method is to find book details using book Name

            Parameters:
                Name (str):
                    example : 'To Kill a Mockingbird'    
        '''

        if not Name:
            return {'Error':'Please provide valid data to insert.'}
        else:
            if isinstance(Name,str):
                query = 'SELECT * FROM BOOKS WHERE TITLE LIKE %s'
                data = (Name,)

                result = self.execute_select_query(query,data)
                return result[0]
            else:
                return {'Error':'Please provide valid data to insert.'}

    def FindPatronID(self,Name:str)->Dict:
        '''
            FindPatronID:
                This Method is to find Patron details using Patron Name

            Parameters:
                Name (str):
                    example : 'Nicky Minaj'    
        '''

        if not Name:
            return {'Error':'Please provide valid data to insert.'}
        else:
            if isinstance(Name,str):
                query = 'SELECT * FROM PATRONS WHERE TITLE LIKE %s'
                data = (Name,)

                result = self.execute_select_query(query,data)
                return result[0]
            else:
                return {'Error':'Please provide valid data to insert.'}

    def InsertTransaction(self):
        pass
    
    def updateTransaction(self):
        pass

    def CheckoutTransaction(self,Name,Title) -> Dict:
        '''
            CheckoutTransaction:
                This Method is to use book and patron details methodsand then update the Transaction Table

            Parameters:
                Title (str) : example : 'To Kill a Mockingbird'
                Name (str): example : 'Lil wayne'    
        '''

        patrondetails = self.FindPatronID(Name=Name)
        if not patrondetails:
            return {'Error', 'Patron details are not available in db.'}
        
        bookdetails = self.FindBookISBN(Name=Title)
        if not bookdetails:
            return {'Error', 'Books details are not available in db.'}
        
        # Insert the transaction in TRANSACTIONS Table

        # update the book status avilability to False