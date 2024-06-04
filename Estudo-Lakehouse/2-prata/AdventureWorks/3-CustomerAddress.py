# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE or replace TABLE adventure_works_prata.customeraddress as
# MAGIC select * from adventure_works_bronze.customeraddress
# MAGIC
