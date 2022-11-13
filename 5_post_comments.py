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
def view():
    c.execute('select * from post_comments')
    return c.fetchall()
def view_user():
    c.execute('select * from users')
    return c.fetchall()
def view_posts():
    c.execute('select * from posts')
    return c.fetchall()

def delete_record(Comment_id):
    c.execute(f'delete from post_comments where Comment_ID = "{Comment_id}"')
    mydb.commit()

def update(Comment_ID,Comment_Content):
    c.execute(f'select CURDATE()')
    Date = c.fetchall()
    formatted_date = Date[0][0].strftime('%Y-%m-%d %H:%M:%S')
    Date = formatted_date.split(' ')[0]
    c.execute(f'update post_Comments SET Comment_Content = "{Comment_Content}" , Commented_Date = DATE "{Date}" where Comment_ID = {Comment_ID}')
    mydb.commit()
    
def add_data(table_name,Post_ID,Comment_Content,User_ID):
    c.execute(f'select CURDATE()')
    Date = c.fetchall()
    formatted_date = Date[0][0].strftime('%Y-%m-%d %H:%M:%S')
    Date = formatted_date.split(' ')[0]
    c.execute(f'INSERT INTO {table_name} (Post_ID,Commented_Date,Comment_Content,Commented_User_ID) VALUES ("{Post_ID}",DATE"{Date}","{Comment_Content}","{User_ID}")')
    mydb.commit()

def get_post(Comment_id):
    c.execute(f'select * from post_comments where Comment_ID = "{Comment_id}"')
    return c.fetchall()  

def create():
    data = view_user()
    user_ids = [i[0] for i in data]
    User_ID = st.selectbox('Select the user who wants to comment ', user_ids)
    data_ = view_posts()
    post_ids = [i[0] for i in data_]
    Post_ID = st.selectbox('Select the Post on which the user wants to comment ', post_ids)
    Comment_Content = st.text_input("Comment_content:")
    if st.button("Add Comment ?"):
        add_data("post_comments",Post_ID,Comment_Content,User_ID)
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
    st.dataframe(pd.DataFrame(data, columns = ['Comment_ID','Post_ID', 'Comment_Date', 'Comment_Content', 'Commented_User_ID']))
    Comment_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Comment to be delete', Comment_ids)
    if st.button('Delete Record'):
        delete_record(choice)
        st.success("Deleted!")
        # st.experimental_rerun()
     
# def get_user(user_id):
#     c.execute(f'select * from train where Train_no = "{user_id}"')
#     return c.fetchall()   
        
def edit():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Comment_ID','Post_ID', 'Commented_Date', 'Comment_Content', 'Commented_User_ID']))
    Comment_ids = [i[0] for i in data]
    choice = st.selectbox('Select the Comment to be Updated',Comment_ids)
    data = get_post(choice)
    if data:
        updated_Comment = st.text_input("Enter new Comment")
        # updated_Phone_Number_str = st.text_input("Enter the New Mobile Number")
        # # updated_Phone_Number = int(updated_Phone_Number_str)
        # updated_First_Name = st.text_input("Enter New First_Name")
        # updated_Last_Name = st.text_input("Enter New Last_Name")
        # updated_City = st.text_input("Enter New City")
        # updated_Pin = st.text_input("Enter New PinCode")
        # updated_PinCode = int(updated_Pin)
        if updated_Comment == '':
            updated_Comment = data[0][3]
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
            update(choice, updated_Comment)
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
        df = pd.DataFrame(data, columns = ['Comment_ID','Post_ID', 'Comment_Date', 'Comment_Content', 'Commented_User_ID'])
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

