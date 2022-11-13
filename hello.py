import streamlit as st

st.set_page_config(
    page_title="Instagram",
    page_icon="👋",
)

st.write("# Welcome to Instagram Admin portal! 👋")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    Instagram Admin portal is mainly designed to manage and secure the Instagram User Database.
    **👈 Select a page from the sidebar** to perform CRUD operations on the tables in the database. This is done as part of the DBMS Project.
    
    **NOTE : This is only for educational purpose**
    
    ### Link to Our Actual Login Page!!!
    - Check out [instagram](https://www.instagram.com/accounts/login/)
"""
)