from pyspark.sql import SparkSession
from get_secret_test import get_secret


def main():
    spark = (
        SparkSession.builder
        .appName("SparkWriteRedshiftStage")
        .getOrCreate()
    )

    username, password, dbname, host, port = get_secret()

    jdbc_url = f"jdbc:redshift://{host}:{port}/{dbname}"

    data = [
        (101, "Amit", "Delhi"),
        (102, "Neha", "Pune"),
        (103, "Rahul", "Bangalore")
    ]

    columns = ["user_id", "user_name", "city"]
    df = spark.createDataFrame(data, columns)

    df.show()

    (
        df.write
        .format("io.github.spark_redshift_community.spark.redshift")
        .option("url", jdbc_url)
        .option("user", username)
        .option("password", password)
        .option("dbtable", "public.users_stage")
        .option("tempdir", "s3a://regex-spark-redshift-temp/spark-temp/")
        .option("forward_spark_s3_credentials", "true")
        .mode("append")
        .save()
    )

    print("Data written to users_stage successfully")

    spark.stop()


if __name__ == "__main__":
    main()
