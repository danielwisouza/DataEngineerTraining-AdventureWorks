# Databricks notebook source
# MAGIC %md
# MAGIC # Só executar esse caderno todo

# COMMAND ----------

storage_account_name = "dlsestudoprod" 
client_id            = "" #usar secrets
tenant_id            = "" #usar secrets
client_secret        = "" #usar 
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": f"{client_id}",
          "fs.azure.account.oauth2.client.secret": f"{client_secret}",
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
def mount_adls(container_name):
    dbutils.fs.mount(
      source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
      mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls 'mnt/dlsestudoprod/landing-zone/AdventureWorksLT/'

# COMMAND ----------

display(dbutils.fs.ls('mnt//dlsestudoprod/landing-zone/AdventureWorksLT'))
