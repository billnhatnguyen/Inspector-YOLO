import streamlit as st

st.write("Hello World")

st.header("HEADER")
st.subheader("SUBHEADER")

st.markdown("""
# This is title
## This is header
### subheader
this is *italics*
this is **BOLD**
""")

# status elements
# success
st.success("This will be in green background")
#warning
st.warning("This will be yellow background")
#error
st.error("This will be red background")

#Displaying Media
st.subheader("Display Image")
st.image('./media/mountains.webp', caption="mountains", width=300)

#Displaying Videos
st.subheader("Display Video")
video_file = open('./media/star.mp4', mode='rb').read()
st.video(video_file)