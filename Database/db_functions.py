import sqlite3 as sql
import csv

def sql_connect(db_name=":memory:"):
    """
    Establishes a connection to an SQLite database.

    Args:
        db_name (str): The name of the database file. Defaults to ":memory:" for an in-memory database.
                      If a file-based database is desired, the file name should be provided (without the .db extension).

    Returns:
        tuple:
            - (bool): True if connection is successful, False if it fails.
            - (sqlite3.Connection or None): The connection object if successful, or None if it fails.
            - (sqlite3.Cursor or None): The cursor object if successful, or None if it fails.
            - (str): The database name used in the connection (with .db appended for file-based DBs).

    Raises:
        sqlite3.Error: If the connection or cursor creation fails.
    """
    try:
        # Establish connection
        connection = sql.connect(db_name)
        cursor = connection.cursor()
        # Print/log the error
        print(f"Database connection successful: {db_name}")
        # Return success
        return {'Connected': True, 'Connection': connection, 'Cursor': cursor, 'DB_Name': db_name}
    except sql.Error as e:
        # Print/log the error
        print(f"Database connection failed: {e}")
        return False, None, None, db_name


def create_table(conn, cursor, table_name, table_keys):
    """
    Creates a table in the SQLite database with an auto-incrementing primary key 'id'.

    :param conn: sqlite3.Connection - The SQLite connection object
    :param cursor: sqlite3.Cursor - The SQLite cursor object
    :param table_name: str - The name of the table to be created
    :param table_keys: list - A list of tuples, where each tuple contains the column name and data type
    """
    # Adding 'id' as the primary key and auto-incrementing column
    id_column = "id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT"

    # Constructing the SQL command for creating a table with additional user-provided keys
    keys_str = ", ".join([f"{col} {dtype}" for col, dtype in table_keys])

    # Final SQL statement includes the id column
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({id_column}, {keys_str});"

    try:
        # Executing the SQL command
        cursor.execute(create_table_query)
        conn.commit()

    except sql.Error as e:
        return f"Error creating table: {e}"

    return f"Table '{table_name}' created successfully with auto-incrementing 'id'."


def return_data(conn, cursor, table_name, items=None):
    if items:
        columns = ', '.join(items)
    else:
        columns = '*'

    query = f"SELECT {columns} FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def return_data_by_id(conn, cursor, table_name, pk):
    query = f"SELECT * FROM {table_name} WHERE id = {pk}"
    cursor.execute(query)
    return cursor.fetchall()

def insert_csv_to_sqlite(conn, cursor, table_name, csv_file):
    """
    Inserts data from a CSV file into an existing SQLite3 table.

    :param conn: sqlite3.Connection - The SQLite connection object
    :param cursor: sqlite3.Cursor - The SQLite cursor object
    :param db_name: Name of the SQLite3 database file.
    :param table_name: Name of the table in the SQLite3 database.
    :param csv_file: Path to the CSV file containing the data to be inserted.
    """
    try:
        # Open the CSV file
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)

            # Read the header (column names)
            headers = next(reader)

            # Create a placeholder string for the SQL INSERT statement (e.g., "?, ?, ?")
            placeholders = ', '.join(['?'] * len(headers))

            # Prepare the SQL insert statement
            insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

            # Insert each row of data into the SQLite table
            for row in reader:
                cursor.execute(insert_query, row)

            # Commit the transaction
            conn.commit()
    except sql.Error as e:
        return f"SQLite error: {e}"
    except Exception as e:
        return f"Error: {e}"
    return "Data successfully inserted into the table."


def insert_data(conn, cursor, table_name, data_dict):
    """
    Inserts data from a dictionary into an existing SQLite3 table with specific column names.

    :param conn: sqlite3.Connection - The SQLite connection object
    :param cursor: sqlite3.Cursor - The SQLite cursor object
    :param table_name: Name of the table in the SQLite3 database.
    :param data_dict: A dictionary where keys represent 'Load Combo' and values represent 'Load'.
    """
    try:
        # Prepare the SQL insert statement with placeholders
        insert_query = f"INSERT INTO {table_name} ('FirstName', 'LastName') VALUES (\"{data_dict['FirstName']}\", \"{data_dict['LastName']}\")"
        print(insert_query)
        cursor.execute(insert_query)
        # Commit the transaction
        conn.commit()

    except sql.Error as e:
        return f"SQLite error: {e}"
    except Exception as e:
        return f"Error: {e}"
    return "Data successfully inserted into the table."

def update_data(conn, cursor, table_name, data_dict):
    query = f"UPDATE {table_name} SET FirstName = \"{data_dict['FirstName']}\", LastName = \"{data_dict['LastName']}\" WHERE ID = {data_dict['ID']}"
    cursor.execute(query)
    conn.commit()
