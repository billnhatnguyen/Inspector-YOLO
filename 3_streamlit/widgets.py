import streamlit as st
import os as os

st.title ('Input Widgets')

#Button
button = st.button("Button")
if button: 
    st.write("You pressed me, yipeee! ")
else:
    st.write("I am offed")

#Checkbox
checkbox = st.checkbox("Do you agree?")
if checkbox:
    st.write("Yipee!")
else: 
    st.write("Not Yipee :(")

#Fav Country
option = ("India", "US", "Canada")
radio = st.radio("fav country?", option, index=0)
st.write("Ans:", radio)

#Select box
options = ('Email', "Phone", "WhatsApp")
select = st.selectbox("How would you live to contact?", options)
st.write("Ans :",select, index=1)

#Slider 
slider_range = st.slider('How old are you?', min_value=1, max_value=100, step=1, value =20)
st.write('You age is', slider_range)

#Text 
name = st.text_input('What is your name?')
st.write('Hello', name)

age = st.number_input('What is your age?', min_value=1, max_value=100, step=1, value =20)
st.write('Your age is:', age)

#Uploading File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success("Successful Upload")
    details = {'filename': uploaded_file.name, 
               'filetype': uploaded_file.type,
               'filesize': uploaded_file.size,
             }
    st.json(details)

    #saving the file
    path = os.path.join('./upload', uploaded_file.name)
    with open(path, mode="wb") as f: 
        f.write(uploaded_file.getbuffer())
        st.success('File Saved Successfully!')