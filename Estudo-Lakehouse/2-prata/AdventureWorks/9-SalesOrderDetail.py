# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE or replace TABLE adventure_works_prata.salesorderdetail as
# MAGIC select * from adventure_works_bronze.salesorderdetail
# MAGIC
