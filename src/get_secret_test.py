import boto3
import json
from botocore.exceptions import ClientError


def get_secret():
    """
    Fetch Amazon Redshift credentials securely from AWS Secrets Manager.

    Returns:
        tuple: (username, password, dbname, host, port)
    """

    secret_name = "demo/rdwh/Regex"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise RuntimeError("Failed to fetch secret from Secrets Manager") from e

    # Secret is returned as a JSON string
    secret_dict = json.loads(response["SecretString"])

    # Extract values
    username = secret_dict["username"]
    password = secret_dict["password"]   # Used later for DB connection
    dbname   = secret_dict["dbname"]
    host     = secret_dict["host"]
    port     = secret_dict["port"]

    # SAFE validation logs (NO sensitive data)
    print("Secrets fetched successfully from AWS Secrets Manager")
    print("Username :", username)
    print("Database :", dbname)
    print("Host     :", host)
    print("Port     :", port)
    print("Password : ****** (hidden)")

    return username, password, dbname, host, port


if __name__ == "__main__":
    get_secret()
