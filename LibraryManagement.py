from DataBase import DatabaseConnection
from typing import Union,Dict,Tuple,List
from Library import Library

class LibraryManagement(DatabaseConnection):
    '''
        LibraryManagement:
            This class is for managing the library assets like Genres, Authors and Books
            We can Update, Delete or Create new entires of Genres, Author and Books
        
        Steps:
            As we are using relational database MySQL We have Three main Tables one for Genres, One for Authors and one for Books.
            So its necessary to Have Genre and Author available before adding Book entity into BOOKS Table
            1) Enter The Genre if the Genre is not present in GENRES Table.
            2) Enter Author if the Author is not present in AUTHORS Table.    
            3) Enter Book 
    '''

    def insertgenres(self, data:Union[Tuple,List]) -> Dict:
        '''
            insertauthors:
                This method will insert a single genre entry or you can insert multiple genres entries.
            
            Parameter:
                data (Tuple): (GenreID ,GenreName,Descp)
                    GenreID : Unique genre Id
                    GenreName : Unique genre Name
                    Descp : Biography about genre.

                data (List): [
                    (GenreID ,GenreName,Descp),
                    (GenreID ,GenreName,Descp),
                    (GenreID ,GenreName,Descp)
                ]    
        '''        
        if not data:
            return {'Error':'Please provide valid data to insert.'}
        else:
            if isinstance(data,tuple):
                # Insert Single Author Entry into db
                query = '''INSERT INTO GENRES (GenreID, GenreName, Descp)
           VALUES (%s, %s, %s)'''
                data = (data[0], data[1], data[2])
    
                result = self.execute_manipulation_query(query,data)
                return result
            
            elif isinstance(data,list):
                # Insert Multiple Author Entries into db
                query = '''INSERT INTO GENRES (GenreID, GenreName, Descp)
           VALUES (%s, %s, %s)'''
                
                for _ in data:
                    result = self.execute_manipulation_query(query,_)    
                return result
            
            else:   
                return {'Error':'Please provide valid data to insert.'}        


    def updategenres(self, data: Tuple, id: int) -> dict:
        '''
        updategenres:
            This method is used to update a genre entry from GENRES Table.

        Parameter:
            data (Tuple): (GenreName, Descp)
                        Note: If you don't want an attribute to change, just put None.
                        Example: ('Fantasy', 'fantasy, dystopian, and steampunk.')
        '''
        if not data or not id:
            return {'Error': 'Please provide valid data to update.'}
        else:
            query = ''' 
                UPDATE GENRES 
                SET 
                    GenreName = CASE WHEN %s IS NOT NULL THEN %s ELSE GenreName END,
                    Descp = CASE WHEN %s IS NOT NULL THEN %s ELSE Descp END
                WHERE GenreID = %s;
            '''
            data = (data[0], data[0], data[1], data[1], id)

            result = self.execute_manipulation_query(query, data)
            return result


    def deletegenres(self,id:int) -> Dict:
        '''
        updategenres:
            This method is used to delete a genre entry from GENRES Table.

        Parameter:
            id (int): 
        '''        
        if not id:
            return {'Error':'Please provide valid id to delete an entry.'}
        else:
            query = ''' DELETE FROM GENRES
                        WHERE GenreID = %s
                    '''    
            data = (id,)
            result = self.execute_manipulation_query(query,data)
            return result

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

    
    def updateauthors(self, data: Tuple, id: int) -> dict:
        '''
        updateauthors:
            This method is used to update a author entry from AUTHORS Table.

        Parameter:
            data (Tuple): (AuthorName, Biography)
                        Note: If you don't want an attribute to change, just put None.
                        Example: ('Arthur Conan Doyle', 'Arthur Conan Doyle, dystopian, and steampunk.')
        '''
        if not data or not id:
            return {'Error': 'Please provide valid data to update.'}
        else:
            query = ''' 
                UPDATE AUTHORS 
                SET 
                    AuthorName = CASE WHEN %s IS NOT NULL THEN %s ELSE AuthorName END,
                    Biography = CASE WHEN %s IS NOT NULL THEN %s ELSE Biography END
                WHERE AuthorID = %s;
            '''
            data = (data[0], data[0], data[1], data[1], id)

            result = self.execute_manipulation_query(query, data)
            return result


    def deleteauthors(self,id:int) -> Dict:
        '''
        deleteuthors:
            This method is used to delete a author entry from AUTHORS Table.

        Parameter:
            id (int): 
        '''        
        if not id:
            return {'Error':'Please provide valid id to delete an entry.'}
        else:
            query = ''' DELETE FROM AUTHORS
                        WHERE AuthorID = %s
                    '''    
            data = (id,)
            result = self.execute_manipulation_query(query,data)
            return result
             
    
     
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
            