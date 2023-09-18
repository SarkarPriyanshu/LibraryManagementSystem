from DataBase import DatabaseConnection
import pandas as pd

class Library(DatabaseConnection):
    def getbookslist(self): 
        """
        Retrieves and prints the list of books in the library.
        """
        try:
            # Fetch results
            results = self.execute_select_query('SELECT * FROM BOOKS')
            return pd.DataFrame(results,columns=['ISBN','Title','Author','PublicationYear','Genre','AvailabiltyStatus'])
        
        except Exception as e:
            return {'Error':'Failed to fetch BOOKS table'}
    
    def getgenreslist(self): 
        """
        Retrieves and prints the list of genres available in the library.
        """
        try:
            # Fetch results
            results = self.execute_select_query('SELECT * FROM GENRES')
            return pd.DataFrame(results,columns=['GenreID','GenreName','Descp'])    
           
        except Exception as e:
            return {'Error':'Failed to fetch GENRES table'}

    def getpatronslist(self): 
        """
        Retrieves and prints the list of library patrons.
        """
        try:
            # Fetch results
            results = self.execute_select_query('SELECT * FROM PATRONS')
            return pd.DataFrame(results,columns=['PatronID','Name','ContactNumber','MembershipStatus'])
        
        except Exception as e:
            return {'Error':'Failed to fetch PATRONS table'}     

    def getauthorslist(self): 
        """
        Retrieves and prints the list of authors in the library.
        """
        try:
            # Fetch results
            results = self.execute_select_query('SELECT * FROM AUTHORS')
            return pd.DataFrame(results,columns=['AuthorID','AuthorName','Biography'])
        
        except Exception as e:
            return {'Error':'Failed to fetch AUTHORS table'}        

    def showfullbookdetails(self):
        """
        Retrieves and displays detailed information about books in the library, including author, genre, and availability status.
        """
        try:
            # Fetch results
            results = self.execute_select_query('''SELECT BOOKS.ISBN,BOOKS.Title,AUTHORS.AuthorName,AUTHORS.Biography,BOOKS.PublicationYear,GENRES.GenreName,GENRES.Descp,BOOKS.AvailabiltyStatus FROM BOOKS 
                                JOIN AUTHORS ON BOOKS.Author = AUTHORS.AuthorID
                                JOIN GENRES ON BOOKS.Genre = GENRES.GenreID
                                ''')
            return pd.DataFrame(results,columns=['ISBN','Title','AuthorName','Biography','PublicationYear','GenreName','Descp','AvailabiltyStatus'])   
        
        except Exception as e:
            return {'Error':'Failed to fetch BOOKS table'}