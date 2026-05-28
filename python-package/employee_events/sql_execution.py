from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Points to the .db file sitting next to this .py file in the package
db_path = Path(__file__).parent / 'employee_events.db'


class QueryMixin:

    def pandas_query(self, sql_query):
        connection = connect(db_path)
        df = pd.read_sql(sql_query, connection)
        connection.close()
        return df

    def query(self, sql_query):
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(sql_query).fetchall()
        connection.close()
        return result


# Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """
    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result

    return run_query