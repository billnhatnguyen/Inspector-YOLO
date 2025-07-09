import streamlit as st
st.title("Streamlit Layout") #displaying the title format
st.set_page_config(page_title="STREAMLIT LAYOUT", layout='wide')

#Sidebar 
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('This is a header in my sidebar')

col1, col2, col3 = st.columns(3)

with col1: 
    st.write('Column 1')
    st.image('./media/cat.jpg')

with col2: 
    st.write('Column 2')
    st.image('./media/dog.jpg')

with col3: 
    st.write('Column 3')
    st.image('./media/owl.jpg')
