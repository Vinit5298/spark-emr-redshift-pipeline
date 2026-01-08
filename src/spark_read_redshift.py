from pyspark.sql import SparkSession
from get_secret_test import get_secret

def main():
    spark = (
        SparkSession.builder
        .appName("SparkReadRedshift")
        .getOrCreate()
    )

    username, password, dbname, host, port = get_secret()

    jdbc_url = f"jdbc:redshift://{host}:{port}/{dbname}"

    df = (
        spark.read
        .format("io.github.spark_redshift_community.spark.redshift")
        .option("url", jdbc_url)
        .option("user", username)
        .option("password", password)
        .option("dbtable", "public.users_test")
        .option("tempdir", "s3a://regex-spark-redshift-temp/tmp/")
        .option("forward_spark_s3_credentials", "true")
        .load()
    )

    df.printSchema()
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()

