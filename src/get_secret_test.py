import boto3
import json
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "demo/rdwh/Vinit"   # 👈 MUST MATCH AWS
    region_name = "ap-south-1"

    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    # Secret comes as STRING
    secret_dict = json.loads(response["SecretString"])

    # Extract values
    username = secret_dict["username"]
    password = secret_dict["password"]
    dbname   = secret_dict["dbname"]
    host     = secret_dict["host"]
    port     = secret_dict["port"]

    # Print for validation
    print("Username :", username)
    print("Password :", password)
    print("DB Name  :", dbname)
    print("Host     :", host)
    print("Port     :", port)

    return username, password, dbname, host, port


if __name__ == "__main__":
    get_secret()
