import streamlit as st

st.title("hello worldb")

st.header("header")

st.subheader("subheader")

st.text("like this video and subscribe ")

st.markdown("""
# h1 tag
## h2 tag   
### h3 tag    
:moon:<br>
:sunglasses:             
**bold**
_italics_                                          
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)
