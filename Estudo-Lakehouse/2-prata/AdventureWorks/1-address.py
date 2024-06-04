# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE or replace TABLE adventure_works_prata.address as
# MAGIC select * from adventure_works_bronze.address
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from adventure_works_prata.address
