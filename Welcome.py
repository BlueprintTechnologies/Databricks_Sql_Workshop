# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC <img src = 'https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/header.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## 1 Lakehouse Architecture & Familiarity with the Web UI (15 Minutes)
# MAGIC 
# MAGIC * Today: 
# MAGIC   * Review a Lakehouse Architecture <a href="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/refarch2.png">here</a>
# MAGIC   * Explore the SQL Workspace UI
# MAGIC   * View the Data Explorer UI
# MAGIC   * Delta enabling
# MAGIC * Note:
# MAGIC   * Blueprint's Focus on Cost Transparency | Lakehouse Monitor <a href="https://bpcs.com/databricks/data-optimization">here</a>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## 2 SQL Data Warehouse Clustering (15 Minutes)
# MAGIC * Clusters: Create & Understand the role of sizing. 
# MAGIC * Discuss the new Serverless option for Cluster.
# MAGIC   * Classic / Pro - Non_Serverless
# MAGIC   * Serverless - Benefits
# MAGIC * Permissions & Access

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 Hands-on Lab Objectives (90 Minutes)
# MAGIC * Keep this page open in a tab

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1 - Datasets for Exploration
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/tables-Enhanced.jpg" />  | <b>NYC taxi: Yellow taxi trips + Lat/Long (835M rows)</b><br><br>  &bullet; Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page<br><br><b>Bureau of Transportation - On Time Flight Performance (79M rows)</b><br><br>  &bullet; Source: https://www.transtats.bts.gov/ontime/<br><br><b>Iowa State Liquor Sales - All state liquore store sales from 2012 to present</b><br><br>  &bullet; Source: https://data.iowa.gov/stories/s/Iowa-Liquor-Sales-Explorer/mke2-7r5k &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 3 - Data Lineage
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/lineage1-Enhanced.jpg'/>|Navigate to the <b> Data </b> tab, select your table and view <b>Lineage</b> to see interdependencies. <br><br> &bullet; Upstream/Downstream Tables <br><br> &bullet;  Notebook Relationships <br><br> &bullet; Dashboards | 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4 - Data Exploration w/ SQL Queries
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/querysearch-Enhanced.jpg" /> | <b>Create Queries</b><br><br> &bullet; Navigate to <b>Queries</b> or <b>Search</b> in the top toolbar for queries by #tag or description. <br><br> &bullet; Or, create a few queries on your own! When you <b>Save</b>, they will be added to your <b>home workspace</b>. | 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 5 - Data Visualizations
# MAGIC 
# MAGIC |   |   | 
# MAGIC |---|---|
# MAGIC | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/viz-Enhanced.jpg" />  | <b> Databricks SQL - Turn queries into visuals by opening the viz tab. </b> <br><br> &bullet; Visualize SQL Queries <br><br> &bullet; Pin visuals to dashboards <br><br> &bullet; Set update schedules | 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 6 - Dashboards
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/dash-Enhanced.jpg' />  | <b> Dashboards - Visuals with Filter and Cross Filter Capabilities for interaction. &emsp;&emsp;&emsp;&emsp;&emsp; </b> <br><br> &bullet; Quick Insights feature <br><br> &bullet; Pinning visuals <br><br> &bullet; Schedules   | 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### 7 - Data Alerts
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/alerts1-Enhanced.jpg' />  | <b> Create alerts Slack, Teams, PagerDuty as a scheduled run. Get insights in the right context. </b> <br><br> &bullet; Ideal for data quality alerts <br><br> &bullet; Alert to any webhook <br><br> &bullet; Integrate with Incident Mgmt. Systems  | 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### 8 - Query Performance & History
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/queryperf-Enhanced.jpg"/>| <b> Explore Query Performance the Execution Plan </b> <br><br> &bullet; Cached queries <br><br> &bullet; Full execution plan for optimization <br><br> &bullet; Query history for analysis &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; |  

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/bar.png' >
