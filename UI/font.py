import streamlit as st

# Custom CSS to apply a color palette to each word in the title
st.markdown("""
    <style>
    .title {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
    }
    .word1 {
        color: #1e3a8a;  /* Dark blue */
    }
    .word2 {
        color: #3b82f6;  /* Medium blue */
    }
    .word3 {
        color: #93c5fd;  /* Light blue */
    }
    </style>
    <h1 class="title">
        <span class="word1">Travel</span> 
        <span class="word2">Agent</span> 
        <span class="word3">AI</span>
    </h1>
""", unsafe_allow_html=True)
