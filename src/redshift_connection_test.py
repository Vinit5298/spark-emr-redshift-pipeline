import psycopg
from .get_secret_test import get_secret


def test_redshift_connection():
    """
    Connect to Amazon Redshift Serverless using credentials
    fetched from AWS Secrets Manager and run a test query.
    """

    # Fetch credentials
    username, password, dbname, host, port = get_secret()

    # Connect to Redshift (SSL + UTF8 enforced)
    conn = psycopg.connect(
        host=host,
        port=int(port),
        dbname=dbname,
        user=username,
        password=password,
        sslmode="require",
        connect_timeout=10,
        options="-c client_encoding=UTF8"
    )

    print("Connected to Redshift successfully")

    # Test query
    with conn.cursor() as cur:
        cur.execute("SELECT current_database(), current_user;")
        result = cur.fetchone()
        print("Query Result:", result)

    conn.close()
    print("Connection closed")


if __name__ == "__main__":
    test_redshift_connection()

