import datetime
from DataBase import DatabaseConnection
from CustomExcepttion import CustomError
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
                return result
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
                query = 'SELECT * FROM PATRONS WHERE Name = %s'
                data = (Name,)

                result = self.execute_select_query(query,data)
                return result
            else:
                return {'Error':'Please provide valid data to insert.'}

    def CheckoutTransaction(self,NameofPaton,TitleofBook,TransactionID) -> Dict:
        '''
            CheckoutTransaction:
                This Method is to use book and patron details methodsand then update the Transaction Table

            Parameters:
                Title (str) : example : 'To Kill a Mockingbird'
                Name (str): example : 'Lil wayne'    
        '''
        self.connection.start_transaction()
        try:
            patrondetails = self.FindPatronID(Name=NameofPaton)
            if not patrondetails:
                raise CustomError('Patron details are not available in db.')
        
            bookdetails = self.FindBookISBN(Name=TitleofBook)
            if not bookdetails:
                raise CustomError('Books details are not available in db.')
            
            patrondetailsID =patrondetails[0][0]
            bookdetailsID= bookdetails[0][0]

            query = '''INSERT INTO TRANSACTIONS(TransactionID,BookISBN,PatronID,TransactionType,DateAndTime)
                        VALUES (%s,%s,%s,%s,%s)
                    '''
            data = (TransactionID,bookdetailsID,patrondetailsID,'Checkout',datetime.datetime.now())

            result =  self.execute_manipulation_query(query=query,data=data)
            
            if not result:
                raise CustomError('Failed to do Transactions')
            else:
               query = '''UPDATE BOOKS SET AvailabiltyStatus = False WHERE ISBN = %s'''
               data = (bookdetailsID,)
               result =  self.execute_manipulation_query(query=query,data=data) 
               
               if result:
                    return {'Info','Transaction Successfull'} 
               
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def ReturnTransaction(self,NameofPaton,TitleofBook,TransactionID) -> Dict:
        '''
            ReturnTransaction:
                This Method is to use book and patron details methodsand then update the Transaction Table

            Parameters:
                Title (str) : example : 'To Kill a Mockingbird'
                Name (str): example : 'Lil wayne'    
        '''
        self.connection.start_transaction()
        try:
            patrondetails = self.FindPatronID(Name=NameofPaton)
            if not patrondetails:
                raise CustomError('Patron details are not available in db.')
        
            bookdetails = self.FindBookISBN(Name=TitleofBook)
            if not bookdetails:
                raise CustomError('Books details are not available in db.')
            
            patrondetailsID =patrondetails[0][0]
            bookdetailsID= bookdetails[0][0]

            query = '''INSERT INTO TRANSACTIONS(TransactionID,BookISBN,PatronID,TransactionType,DateAndTime)
                        VALUES (%s,%s,%s,%s,%s)
                    '''
            data = (TransactionID,bookdetailsID,patrondetailsID,'Return',datetime.datetime.now())

            result =  self.execute_manipulation_query(query=query,data=data)
            
            if not result:
                raise CustomError('Failed to do Transactions')
            else:
               query = '''UPDATE BOOKS SET AvailabiltyStatus = True WHERE ISBN = %s'''
               data = (bookdetailsID,)
               result =  self.execute_manipulation_query(query=query,data=data) 
               
               if result:
                    return {'Info','Transaction Successfull'} 
               
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()        
                        