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
    c.execute('select * from friends')
    return c.fetchall()

def view_user():
    c.execute('select * from users')
    return c.fetchall()
def view_post_comments():
    c.execute('select * from post_comments')
    return c.fetchall()

def delete_record(User_ID,Friend_ID):
    c.execute(f'delete from friends where User_ID = "{User_ID}" and Friend_ID ="{Friend_ID}" ')
    mydb.commit()

def update(choice,Friend_ID,choice1):
    c.execute(f'update friends SET Friend_ID = "{Friend_ID}" where User_ID = {choice} and Friend_ID="{choice1}"')
    mydb.commit()
    
def add_data(table_name,User_ID,Friend_ID):
    c.execute(f'INSERT INTO {table_name} (User_ID,Friend_ID) VALUES ("{User_ID}","{Friend_ID}")')
    mydb.commit()

def get_post(user_id,friend_id):
    c.execute(f'select * from friends where User_ID = "{user_id}" and Friend_ID="{friend_id}"')
    return c.fetchall()  

def create():
    data = view_user()
    user_ids = list(set([i[0] for i in data]))
    User_ID = st.selectbox('Select the User who wishes to make friends', user_ids)
    Friend_ID = st.selectbox('Select the user who wishes to Like the comment', user_ids)
    if(User_ID==Friend_ID):
        st.error("Not possible")
    else:
        if st.button("Send Friend Request?"):
            add_data("friends",User_ID,Friend_ID)
            st.success("Successfully added record!")
 
def delete():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['User_ID','Friend_ID']))
    User_ids = list(set([i[0] for i in data]))
    User_ID= st.selectbox('Select the User who wishes to unfollow his friend', User_ids)
    Friends_ids = list(set([i[1] for i in data]))
    Friends_ID= st.selectbox('Select the Friend to be unfollwed', Friends_ids)
    if st.button('Delete Record'):
        delete_record(User_ID,Friends_ID)
        st.success("Deleted!")
        # st.experimental_rerun()
     
# def get_user(user_id):
#     c.execute(f'select * from train where Train_no = "{user_id}"')
#     return c.fetchall()   
        
def edit():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['User_ID','Friend_ID']))
    User_ids = list(set([i[0] for i in data]))
    friend_ids = list(set([i[1] for i in data]))
    choice = st.selectbox('Select the user who wishes to edit his friends list ',User_ids)
    choice1 = st.selectbox('Select the friend whom the user wishes to unfollow',friend_ids)
    data = get_post(choice,choice1)
    if data:
        data_ = view_user()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
        user_ids = [i[0] for i in data_]
        User_ID = st.selectbox('Select a user to whom you want to send a request', user_ids)
        if User_ID == '':
            User_ID = data[0][0]
        if(User_ID==choice):
            st.error("NOT POSSIBLE!!")
        else:    
            if st.button("Update"):
                update(choice,User_ID,choice1)
                st.success("Updated!")
        # st.experimental_rerun()



def main():
    st.title("Friends Table")
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
        df = pd.DataFrame(data, columns = ['User_ID','Friend_ID'])
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

