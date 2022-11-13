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
    c.execute('select * from posts')
    return c.fetchall()

def delete_record(Post_id):
    c.execute(f'delete from posts where Post_ID = "{Post_id}"')
    mydb.commit()

def update(post_id,Post_Content):
    c.execute(f'update posts SET Post_Content = "{Post_Content}" where Post_ID = {post_id}')
    mydb.commit()
    
def add_data(table_name,Post_User_ID,Post_Date,Post_Content):
    c.execute(f'INSERT INTO {table_name} (Posted_User_ID,Post_Date,Post_Content) VALUES ("{Post_User_ID}",DATE "{Post_Date}","{Post_Content}")')
    mydb.commit()

def get_post(post_id):
    c.execute(f'select * from posts where Post_ID = "{post_id}"')
    return c.fetchall()  

def create():
    # User_ID = st.text_input("User_ID: ")
    data = view_user()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
    user_ids = [i[0] for i in data]
    Post_User_ID = st.selectbox('Select the User who wishes to add the post', user_ids)
    # Post_User_ID = st.text_input("Post_User_ID: ")
    Post_Date = st.text_input("Post_Date:")
    # Phone_Number = int(phone_no_str)
    Post_Content = st.text_input("Post_Content")
    if st.button("Add Post"):
        add_data("posts",Post_User_ID,Post_Date,Post_Content)
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
    st.dataframe(pd.DataFrame(data, columns = ['Post_ID', 'Post_User_ID', 'Post_Date', 'Post_Content']))
    post_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Post to be delete', post_ids)
    if st.button('Delete Record'):
        delete_record(choice)
        st.success("Deleted!")
        # st.experimental_rerun()
     
# def get_user(user_id):
#     c.execute(f'select * from train where Train_no = "{user_id}"')
#     return c.fetchall()   
        
def edit():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Post_ID', 'Post_User_ID', 'Post_Date', 'Post_Content']))
    post_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Post to be Updated',post_ids)
    data = get_post(choice)
    if data:
        updated_Content = st.text_input("Enter new Content")
        # updated_Phone_Number_str = st.text_input("Enter the New Mobile Number")
        # # updated_Phone_Number = int(updated_Phone_Number_str)
        # updated_First_Name = st.text_input("Enter New First_Name")
        # updated_Last_Name = st.text_input("Enter New Last_Name")
        # updated_City = st.text_input("Enter New City")
        # updated_Pin = st.text_input("Enter New PinCode")
        # updated_PinCode = int(updated_Pin)
        if updated_Content == '':
            updated_Content = data[0][3]
        # if updated_Phone_Number_str == '':
        #     updated_Phone_Number_str = data[0][2]
        # if updated_First_Name == '':
        #     updated_First_Name = data[0][4]
        # if updated_Last_Name == '':
        #     updated_Last_Name = data[0][5]
        # if updated_City == '':
        #     updated_City = data[0][6]
        # if updated_Pin == '':
        #     updated_Pin = data[0][7]
        if st.button("Update"):
            update(choice, updated_Content)
            st.success("Updated!")
        # st.experimental_rerun()



def main():
    st.title("Posts Table")
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
        df = pd.DataFrame(data, columns = ['Post_ID', 'Post_User_ID', 'Post_Date', 'Post_Content'])
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

