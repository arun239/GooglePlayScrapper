# def lambda_handler(event, context):
#     #print("Received event: " + json.dumps(event, indent=2))
#     print("value1 = " + event['key1'])
#     print("value2 = " + event['key2'])
#     print("value3 = " + event['key3'])
#     return event['key1']  # Echo back the first key value
#     #raise Exception('Something went wrong')
    
from __future__ import print_function
    
import sys
# import logging
# import rds_config
import pymysql
import json
#rds settings
rds_host  = "playstorescrapper-db.cwuauy846jbz.us-east-1.rds.amazonaws.com"
name = "admin" # rds_config.db_username
password = "password" # rds_config.db_password
db_name = "PlayStoreScrapperDB" #rds_config.db_name
port = 3306

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

server_address = (rds_host, port)
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5, cursorclass=pymysql.cursors.DictCursor)
except:
    # logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    print ("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

# logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
print ("SUCCESS: Connection to RDS mysql instance succeeded")
def lambda_handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0
    result = None
    with conn.cursor() as cur:
        # cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")  
        # cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
        # cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
        # cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
        # conn.commit()
        try: 
            cur.execute('insert into Packages values ("'+ event["package_name"] + '","' + event["app_name"] + '")')
            result = "Inserted Package Name successfully."
            conn.commit()
        except Exception, e: 
            print ("Error executing insert sql command for Package name")
            print (e)
            result = e
            conn.rollback()
        
    

    # return "Added %d items from RDS MySQL table" %(item_count)    
    return result
    

if __name__ == "__main__":
    event = {}
    event["package_name"] = "com.martinmagni.mekorama"
    event["app_name"] = "Mekorama"
    result = lambda_handler(event, None) 
    print (result)


    