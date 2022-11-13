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

def view_user():
    c.execute('select * from users')
    return c.fetchall()
def view():
    c.execute('select * from pages')
    return c.fetchall()

def delete_record(Page_ID):
    c.execute(f'delete from pages where Page_ID = "{Page_ID}"')
    mydb.commit()

def update(Page_ID,Page_bio,Page_Content_no_followers_n_following):
    c.execute(f'update pages SET Page_bio = "{Page_bio}" , Page_Content_no_followers_n_following = "{Page_Content_no_followers_n_following}" where Page_ID = {Page_ID}')
    mydb.commit()
    
def add_data(table_name,Page_user_id,Page_bio,Page_Content_no_followers_n_following):
    c.execute(f'INSERT INTO {table_name} (Page_user_id,Page_bio,Page_Content_no_followers_n_following) VALUES ("{Page_user_id}","{Page_bio}","{Page_Content_no_followers_n_following}")')
    mydb.commit()

def get_post(page_id):
    c.execute(f'select * from pages where Page_ID = "{page_id}"')
    return c.fetchall()  

def create():
    # User_ID = st.text_input("User_ID: ")
    data = view_user()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
    user_ids = [i[0] for i in data]
    Page_user_id = st.selectbox('Select the User who wishes to add the Page', user_ids)
    Page_bio = st.text_input("Page_Bio:")
    # Phone_Number = int(phone_no_str)
    Page_Content_no_followers_n_following = st.text_input("Page_Content")
    if st.button("Add Post"):
        add_data("pages",Page_user_id,Page_bio,Page_Content_no_followers_n_following)
        st.success("Successfully added record!")
        
# def view():
#     c.execute('select * from users')
#     return c.fetchall()

# def delete_record(User_id):
    # c.execute(f'delete from users where User_ID = "{User_id}"')
    
# def update(user_id, updated_email, updated_Phone_Number, updated_First_Name, updated_Last_Name, updated_City,updated_PinCode):
    # c.execute(f'update train SET Email_ID = "{updated_email}", Phone_Number = "{updated_Phone_Number}", First_name = "{updated_First_Name}", Last_name = "{updated_Last_Name}", City = "{updated_City}" , PinCode ="{updated_PinCode}" where User_ID = {user_id}')

def delete():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Page_ID','Page_user_id','Page_bio','Page_Content_no_followers_n_following']))
    Page_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Page to be delete', Page_ids)
    if st.button('Delete Record'):
        delete_record(choice)
        st.success("Deleted!")
        # st.experimental_rerun()
     
# def get_user(user_id):
#     c.execute(f'select * from train where Train_no = "{user_id}"')
#     return c.fetchall()   
        
def edit():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Page_ID','Page_user_id','Page_bio','Page_Content_no_followers_n_following']))
    page_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Page to be Updated',page_ids)
    data = get_post(choice)
    if data:
        Page_Content = st.text_input("Enter new Content")
        Page_bio = st.text_input("Enter the new bio")
        if Page_Content == '':
            Page_Content = data[0][3]
        if Page_bio == '':
            Page_bio = data[0][2]
        if st.button("Update"):
            update(choice, Page_bio,Page_Content)
            st.success("Updated!")
        # st.experimental_rerun()



def main():
    st.title("Page Table")
    menu = ["Add", "View", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == 'Add':
        st.subheader("Enter details")
        try:
            create()
        except Exception as e:
            st.error("Error!"+' '+str(e))
    elif choice == 'View':
        st.subheader("Information in Table")
        try:
            data = view()
        except:
            st.error("Error!")
        df = pd.DataFrame(data, columns = ['Page_ID','Page_user_id','Page_bio','Page_Content_no_followers_n_following'])
        st.dataframe(df)
    
    elif choice == 'Delete':
        st.subheader('Select row to delete')
        delete()
    elif choice == 'Update':
        st.subheader('Select row to update')
        edit()


# if __name__ == '__main__':
#     db = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = '',
#         database = 'instagram_database'
#     )
#     cursor = db.cursor()

main()

