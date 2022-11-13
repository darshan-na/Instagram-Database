import mysql.connector
import streamlit as st
import pandas as pd


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="instagram_database"
)
c = mydb.cursor()

query = st.text_input("Enter the Query to be executed: ")
if(query!=''):
    try:
        c.execute(f'{query}')
        mydb.commit()
        print(c.fetchall())
        st.success("Query Executed Successfully")
        st.write("Please look into the database to see the changes")
    except Exception as e:
        print(e)
        st.error("Query Execution Failed")