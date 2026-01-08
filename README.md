\# Spark EMR – Redshift Serverless Data Pipeline



This project demonstrates an end-to-end data engineering pipeline using:



\- Amazon EMR (Apache Spark)

\- Amazon Redshift Serverless

\- AWS Secrets Manager

\- Amazon S3

\- IAM Roles



The pipeline securely reads data from Redshift, processes it in Spark, and writes it back using staging and merge logic.



---



\## Architecture Overview



1\. Credentials stored securely in AWS Secrets Manager

2\. EMR cluster accesses Redshift Serverless using IAM roles

3\. Spark reads data from Redshift using Spark-Redshift connector

4\. Spark writes data to Redshift staging tables via S3

5\. SQL-based merge logic loads final tables



---



\## Project Phases



\### Phase 1: Redshift \& Secrets Manager Setup

\- Created Redshift Serverless namespace and workgroup

\- Stored DB credentials in AWS Secrets Manager



📄 Docs:

\- `docs/redshift\_setup.md`

\- `docs/secrets\_manager\_setup.md`



---



\### Phase 2: EMR Cluster Setup

\- Created EMR cluster with required IAM roles

\- Enabled S3 and Redshift access



---



\### Phase 3: EMR → Redshift Connectivity Test

\- Used `psycopg` with Secrets Manager

\- Validated Redshift connection from EMR



📄 Script:

\- `src/redshift\_connection\_test.py`



---



\### Phase 4: Spark Read \& Write with Redshift

\- Read Redshift tables using Spark

\- Wrote Spark DataFrame back to Redshift using S3 temp directory



📄 Scripts:

\- `src/spark\_read\_redshift.py`

\- `src/spark\_write\_redshift.py`



---



\### Phase 5: Staging and Merge Logic

\- Spark writes data to staging table

\- SQL merge logic loads data into final table



📄 Scripts:

\- `src/redshift\_merge\_users.sql`



---



\### Phase 6: Transactions, Validation \& Documentation

\- Used BEGIN / COMMIT transactions

\- Validated final data correctness

\- Documented entire pipeline



---



\## How to Run



1\. Create EMR cluster

2\. Configure IAM roles

3\. Run Spark jobs using:



```bash

spark-submit src/spark\_read\_redshift.py

spark-submit src/spark\_write\_redshift.py



