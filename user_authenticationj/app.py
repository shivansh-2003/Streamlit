import streamlit as st
from pymongo import MongoClient
import bcrypt

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://shivansh:sgnedba@cluster0.xdp6wa8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
users = db["users"]


def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        login_user(username, password)


def login_user(username, password):
    user = users.find_one({'username': username})

    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            st.success('Logged in successfully!')
        else:
            st.error('Invalid username or password')
    else:
        st.error('Invalid username or password')


login()


def register():
    st.title('Register')
    new_username = st.text_input('New Username')
    new_password = st.text_input('New Password', type='password')

    if st.button('Register'):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({'username': new_username, 'password': hashed_password})
        st.success('Registered successfully!')


register()
