import pymysql
import config_parser

class DBUtil:
    def __init__(self,host, user, password, database, logger) -> None:
        """
        Initialize the DBUtil with a database.

        Args:
            host (str): The host for the database.
            user (str): The user for the database.
            password (str): The password for the database.
            database (str): The database to connect to.
            logger (Logger): A Logger instance.

        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.logger = logger
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """
        Connect to the database.

        Raises:
            Exception: If the connection fails.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            self.logger.info(f"Connected to {self.database} database")
        except Exception as e:
            self.logger.error(f"Failed to connect to {self.database} database")
            raise e
    
    def disconnect(self):
        """
        Disconnect from the database.

        Raises:
            Exception: If the disconnection fails.
        """
        try:
            self.connection.close()
            self.logger.info(f"Disconnected from {self.database} database")
        except Exception as e:
            self.logger.error(f"Failed to disconnect from {self.database} database")
            raise e
    
    def execute_query(self, query):
        """
        Execute a query.

        Args:
            query (str): The query to execute.

        Returns:
            A cursor for the executed query.

        """
        if not self.connection:
            self.connect()
        self.logger.info(f"Executing query: {query}")
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            self.logger.error(f"Failed to execute query: {query}")
            raise e
        return self.cursor
    
    def fetch_one(self, query):
        """
        Fetch one row from a query.

        Args:
            query (str): The query to execute.

        Returns:
            A tuple of the row data.

        """
        if not self.connection:
            self.connect()
        
        self.logger.info(f"Fetching one row from query: {query}")
        try:
            self.cursor.execute(query)
            row = self.cursor.fetchone()
        except Exception as e:
            self.logger.error(f"Failed to fetch one row from query: {query}")
            raise e
        return row
    
    def fetch_all(self, query):
        """
        Fetch all rows from a query.

        Args:
            query (str): The query to execute.

        Returns:
            A list of tuples of the row data.

        """
        if not self.connection:
            self.connect()
        
        self.logger.info(f"Fetching all rows from query: {query}")
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Failed to fetch all rows from query: {query}")
            raise e
        return rows