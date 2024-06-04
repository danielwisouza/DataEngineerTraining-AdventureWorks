# Databricks notebook source
# MAGIC %md
# MAGIC Vamos ler os arquivos parquet do ADLS

# COMMAND ----------

table = 'address'
database = 'adventure_works_bronze'

# COMMAND ----------

folder_path= "/mnt/dlsestudoprod/landing-zone/AdventureWorksLT/"

# COMMAND ----------

df = spark.read.parquet(f"{folder_path}/{table}.parquet")

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("overwriteschema", True)\
    .saveAsTable(f"{database}.{table}")

# COMMAND ----------


