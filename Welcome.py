# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC <img src = 'https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/header.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## 1 Lakehouse Architecture & Familiarity with the Web UI (15 Minutes)
# MAGIC 
# MAGIC 
# MAGIC * Reference Architecture (here)
# MAGIC * Blueprint's Focus on Cost Transparency | Lakehouse Monitor (here)
# MAGIC * Explore the SQL Workspace UI
# MAGIC * View the Data Explorer UI

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## 2 SQL Data Warehouse Clustering (15 Minutes)
# MAGIC * Clusters: Create & Understand the role of sizing. 
# MAGIC * Discuss the new Serverless option for Cluster.
# MAGIC * Permissions & Access

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 Hands-on Lab Objectives (90 Minutes)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sample Datasets & Tables
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC | <b>NYC taxi: Yellow taxi trips + Lat/Long (835M rows)</b><br><br>  &bullet; Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page<br><br><b>Bureau of Transportation - On Time Flight Performance (79M rows)</b><br><br>  &bullet; Source: https://www.transtats.bts.gov/ontime/<br><br><b>Iowa State Liquor Sales - All state liquore store sales from 2012 to present</b><br><br>  &bullet; Source: https://data.iowa.gov/stories/s/Iowa-Liquor-Sales-Explorer/mke2-7r5k |  <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/tables.png" /> |

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### Create SQL Warehouse
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b> Endpoint for queries </b> <br><br> &bullet; Serverless - Fully managed, elastic, best value <br><br> &bullet; Pro - Self managed, advanced SKU, compute in your account  | <img align="left" width=800  src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/cluster.png' />  |

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Exploration w/ SQL Queries
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b>Create Queries</b><br><br> &bullet; Navigate to your HOME SQL Workspace for sample queries. <br><br> &bullet; Try your own using the query editor. | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/query_shared_folder.png" alt="Picture" width="800" height="600" style="display: block; margin: 0 auto" /> |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Data Lineage
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |Shows you the connectedness of tables and others objects. <br><br> &bullet; Upstream/Downstream Tables <br><br> &bullet;  Notebook Relationships <br><br> &bullet; Dashboards | <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/lineage.png' />  |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Data Visualization 

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### Data Alerts
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b> Create alerts Slack, Teams, PagerDuty! </b> <br><br> &bullet; Ideal for data quality alerts <br><br> &bullet; Alert to any webhook <br><br> &bullet; Integrate with Incident Mgmt. Systems  | <img align="left" width=800  src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/alerts.png' />  |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Dashboards
