from DataBase import DatabaseConnection
from typing import Union,Dict,Tuple,List
from Library import Library

class LibraryManagement(DatabaseConnection):
    def insertbooks(self, data:Union[Tuple,List]) -> Dict:
        '''
            insertbooks:
                This method will insert a single book entry or you can insert multiple books entries.
            
            Parameter:
                data (Tuple): (ISBN ,BookName,AuthorName,PublishYear,Genre,AvailabilityStatus)
                    ISBN : Unique Book Id
                    BookName : Unique Book Name
                    AuthorName : Unique Author Name
                    PublishYear : Year 
                    Genre : Genre of Book
                    Availability : Does Book available in library.

                data (List): [
                    (ISBN ,BookName,AuthorName,PublishYear,Genre,AvailabilityStatus),
                    (ISBN ,BookName,AuthorName,PublishYear,Genre,AvailabilityStatus),
                    (ISBN ,BookName,AuthorName,PublishYear,Genre,AvailabilityStatus)
                ]    
        '''
        if not data:
            return {'Error':'Please provide valid data to insert.'}
        else:
            if isinstance(data, tuple):
                
                # Check if the author available in AUTHORS table.
                author_name = data[2]
                query = f"SELECT AuthorID FROM AUTHORS WHERE AuthorName = '{author_name}'"
                AuthorID = self.execute_select_query(query)
                if not AuthorID[0][0]:
                    return {'Error':'Author is not available in AUTHORS table.'}
                
                
                # Check if the genre avilable in GENRE table
                genre_name = data[3]
                query = f"SELECT GenreID FROM GENRES WHERE GenreName = '{genre_name}'"
                GenreID = self.execute_select_query(query)
                if not GenreID[0][0]:
                    return {'Error':'Genre is not available in GENRES table.'}
                
                
                query = '''INSERT INTO BOOKS (ISBN, Title, Author, PublicationYear, Genre, AvailabiltyStatus)
           VALUES (%s, %s, %s, %s, %s, %s)'''
                data = (data[0], data[1], AuthorID[0][0], data[4], GenreID[0][0], data[-1])
    
                result = self.execute_manipulation_query(query,data)
                return result
            
            elif isinstance(data, list):  
                # Check if the author available in AUTHORS table.
                # Check if the genre avilable in GENRE table
                return {'Info':'Data is of list type'}
            else:
                return {'Error':'Please provide valid data to insert.'}    
            
    def insertauthors(self, data:Union[Tuple,List]) -> Dict:
        '''
            insertauthors:
                This method will insert a single author entry or you can insert multiple authors entries.
            
            Parameter:
                data (Tuple): (AuthorID ,AuthorName,Biography)
                    AuthorID : Unique author Id
                    AuthorName : Unique author Name
                    Biography : Biography about author.

                data (List): [
                    (AuthorID ,AuthorName,Biography),
                    (AuthorID ,AuthorName,Biography),
                    (AuthorID ,AuthorName,Biography)
                ]    
        '''        
        if not data:
            return {'Error':'Please provide valid data to insert.'}
        else:
            if isinstance(data,tuple):
                # Insert Single Author Entry into db
                query = '''INSERT INTO AUTHORS (AuthorID, AuthorName, Biography)
           VALUES (%s, %s, %s)'''
                data = (data[0], data[1], data[2])
    
                result = self.execute_manipulation_query(query,data)
                return result
            
            elif isinstance(data,list):
                # Insert Multiple Author Entries into db
                query = '''INSERT INTO AUTHORS (AuthorID, AuthorName, Biography)
           VALUES (%s, %s, %s)'''
                
                for _ in data:
                    result = self.execute_manipulation_query(query,_)    
                return result
            
            else:   
                return {'Error':'Please provide valid data to insert.'}         
