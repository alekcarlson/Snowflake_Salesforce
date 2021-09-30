# Snowflake_Salesforce
File to extract data from a Snowflake view and upload to a custom Salesforce object


This queries some view in Snowflake and inserts that data into some custom object in Salesforce

The script first connects to Snowflake. 
Then it queries the view in Snowflake and stores the results in a Pandas DF. 
Then it connects to Salesforce. 
Then it creates a list of dictionaries containing the different columns from the Pandas DF. 
It then inserts this list of dictionaries into the custom object in Salesforce.
