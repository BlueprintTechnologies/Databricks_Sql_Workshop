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
# MAGIC * Reference Architecture <a href="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/refarch.png">here</a>
# MAGIC * Blueprint's Focus on Cost Transparency | Lakehouse Monitor <a href="https://bpcs.com/databricks/data-optimization">here</a>
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
# MAGIC ### 1 - Datasets for Exploration (3)
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC | <b>NYC taxi: Yellow taxi trips + Lat/Long (835M rows)</b><br><br>  &bullet; Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page<br><br><b>Bureau of Transportation - On Time Flight Performance (79M rows)</b><br><br>  &bullet; Source: https://www.transtats.bts.gov/ontime/<br><br><b>Iowa State Liquor Sales - All state liquore store sales from 2012 to present</b><br><br>  &bullet; Source: https://data.iowa.gov/stories/s/Iowa-Liquor-Sales-Explorer/mke2-7r5k |  <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/tables.png" /> |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 3 - Data Lineage
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |Navigate to the <b> Data </b> tab, select your table and view <b>Lineage</b> to see interdependencies. <br><br> &bullet; Upstream/Downstream Tables <br><br> &bullet;  Notebook Relationships <br><br> &bullet; Dashboards | <img align="left" width=100%  src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/lineage.png' />  |

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4 - Data Exploration w/ SQL Queries
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b>Create Queries</b><br><br> &bullet; Navigate to <b>Queries</b> or <b>Search</b> in the top toolbar for queries by #tag or description. <br><br> &bullet; Or, create a few queries on your own! When you <b>Save</b>, they will be added to your <b>home workspace</b>. | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/querysearch.png" alt="Picture" width="100%" height="600" style="display: block; margin: 0 auto" /> |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 5 - Data Visualizations
# MAGIC 
# MAGIC |   |   | 
# MAGIC |---|---|
# MAGIC | <b> Databricks SQL - Turn queries into vizuals by opening the viz tab. </b> <br><br> &bullet; Visualize SQL Queries <br><br> &bullet; Pin visuals to dashboards <br><br> &bullet; Set update schedules | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/viz.png" width=100% style="display: block; margin: 0 auto" /> |

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 6 - Dashboards
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b> Dashboards - Visuals with Filter and Cross Filter Capabilities </b> <br><br> &bullet; Quick Insights feature <br><br> &bullet; Pinning visuals <br><br> &bullet; Schedules | <img src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/dash.png' /> |

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### 7 - Data Alerts
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b> Create alerts Slack, Teams, PagerDuty as a scheduled run. Get insights in the right context. </b> <br><br> &bullet; Ideal for data quality alerts <br><br> &bullet; Alert to any webhook <br><br> &bullet; Integrate with Incident Mgmt. Systems  | <img align="left" width=100%  src='https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/alerts1.png' />  |

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### 8 - Query Performance & History
# MAGIC 
# MAGIC |   |   |
# MAGIC |---|---|
# MAGIC |<b> Explore Query Performance the Execution Plan </b> <br><br> &bullet; Cached queries <br><br> &bullet; Full execution plan for optimization <br><br> &bullet; Query history for analysis  | <img src="https://raw.githubusercontent.com/BlueprintTechnologies/Databricks_Sql_Workshop/main/img_artifacts/queryperf.png" alt="Picture" width="800" height="600" style="display: block; margin: 0 auto" /> |
