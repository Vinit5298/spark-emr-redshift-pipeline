# Amazon Redshift Serverless Setup

## Steps Performed

1. Created a Redshift Serverless namespace.
2. Created a Redshift Serverless workgroup.
3. Opened Redshift Query Editor v2.
4. Executed the following SQL commands:

```sql
CREATE DATABASE Regexdb;

CREATE USER Vinit WITH PASSWORD '******';

GRANT ALL PRIVILEGES ON DATABASE Regexdb TO Vinit;
