#import packages 
import snowflake.connector
import pandas as pd
from simple_salesforce import Salesforce, format_soql

#connect to Snowflake
con = snowflake.connector.connect(
    user='SNOWFLAKE_USER',
    password='SNOWFLAKE_PASSWORD',
    account='SNOWFLAKE_ACCOUNT',
    warehouse='WAREHOUSE',
    database='DATABASE',
    schema= 'SCHEMA',
  	role= 'ROLE',
    session_parameters={'QUERY_TAG': 'SnowflakeToSalesforce'})

#query view from Snowflake
cur = con.cursor()
sql = "select * from SOME_SNOWFLAKE_VIEW"
cur.execute(sql)
df = cur.fetch_pandas_all()

#connect to Salesforce
Username = 'SALESFORCE_USERNAME'
Password = 'SALESFORCE_PASSWORD'
Securitytoken = 'SALESFORCE_SECURITYTOKEN'
sf = Salesforce(username=Username, password=Password, security_token=Securitytoken)
sessionID = sf.session_id
instance = sf.sf_instance

#create list of dictionaries that will be inserted into the Custom object
data = [{'Custom_Field1__c': str(df.COLUMN_NAME1[i]),
        'Custom_Field2__c':str(df.COLUMN_NAME2[i]),
        'Custom_Field3__c':str(df.COLUMN_NAME3[i]),
        'Custom_Field4__c':str(df.COLUMN_NAME4[i])} for i in df.index]    
 
#insert into Custom Object
sf.bulk.Custom_Object__c.insert(data)
