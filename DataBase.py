import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector.errors import DatabaseError

# Load environment variables from .env file (optional)
load_dotenv()

# Access environment variables
host = os.getenv("HOST")
database_user = os.getenv("DATABASE_USER")
database_pass = os.getenv("DATABASE_PASS")
database_name = os.getenv("DATABASE_NAME")

class DatabaseConnection:
    """
        Initialize a database connection with the provided credentials.
    """
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=database_user,
                password=database_pass,
                database=database_name
            )
        except mysql.connector.Error as e:
            raise DatabaseError(f'Failed to connect to the database: {e}')

    def execute_select_query(self, query,data=None):
        """
        Execute a SELECT query and retrieve the results.

        Args:
            query (str): The SQL SELECT query to execute.

        Returns:
            List[Tuple]: A list of tuples representing the query results.
        
        Raises:
            DatabaseError: If an error occurs while executing the query.
        """
        try:
            result = None
            cursor = self.connection.cursor()

            if not data:
                cursor.execute(query)
                result = cursor.fetchall()
            else:
                cursor.execute(query, data)   
                result = cursor.fetchall()

            cursor.close()
            return result
        
        except mysql.connector.Error as e:
            raise DatabaseError(f'Selection query failed: {e}')
        

    def execute_manipulation_query(self, query,data):
        """
        Execute a data manipulation query (e.g., INSERT, UPDATE, DELETE) with optional data.

        Args:
            query (str): The SQL manipulation query to execute.
            data (Tuple): Optional data values to be inserted into the query.

        Raises:
            DatabaseError: If an error occurs while executing the query.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query,data)
            self.connection.commit()
            cursor.close()
            return {'Info':'Insertion successful'}
        except mysql.connector.Error as e:
            raise DatabaseError(f'Manipulation query failed: {e}')
    