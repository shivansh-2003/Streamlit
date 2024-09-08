import streamlit as st

# Set the page configuration for responsive view on mobile and larger screens
st.set_page_config(
    page_title="Responsive Streamlit App",
    layout="wide",  # wide layout adapts to larger screens
)

# Custom CSS for responsive font sizes
st.markdown("""
    <style>
    @media only screen and (max-width: 600px) {
        h1 {font-size: 24px;}
        p {font-size: 16px;}
        .element-container {margin-top: 5px;}
    }
    @media only screen and (min-width: 601px) {
        h1 {font-size: 48px;}
        p {font-size: 20px;}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Responsive Webpage Example with Equal Column Width")

# Create two equal-width columns using a [1, 1] ratio
col1, col2 = st.columns([1, 1])  # Both columns will occupy 50% of the available width

# Content in the first column
with col1:
    st.header("Column 1")
    st.write("""
        This is the first column. Both columns occupy the same amount of space,
        and the layout is responsive to screen size.
    """)

# Content in the second column
with col2:
    st.header("Column 2")
    st.write("""
        This is the second column. Resize the browser or view this on different devices
        to see how both columns adjust dynamically with equal width.
    """)

# Add a button for user interaction
st.button("Click Me")

# Additional content below
st.write("This page adapts to different screen sizes automatically.")
