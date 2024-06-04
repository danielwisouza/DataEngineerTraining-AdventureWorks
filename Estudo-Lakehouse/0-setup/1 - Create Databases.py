# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE if NOT EXISTS adventure_works_bronze
# MAGIC LOCATION '/mnt/dlsestudoprod/bronze/adventure_works_bronze'
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE if NOT EXISTS adventure_works_prata
# MAGIC LOCATION '/mnt/dlsestudoprod/prata/adventure_works_prata'

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE if NOT EXISTS  adventure_works_ouro
# MAGIC LOCATION '/mnt/dlsestudoprod/ouro/adventure_works_ouro'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop database adventure_works_bronze  CASCADE;
# MAGIC --drop database adventure_works_prata;
# MAGIC --drop database adventure_works_ouro;
