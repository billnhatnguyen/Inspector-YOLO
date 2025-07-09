import streamlit as st

st.set_page_config(page_title='Home',
                   layout='wide',
                   page_icon ='images/home.png')

st.title("Yolo V5 Object Detection App")
st.caption("This web application demonstrates Object detection")

st.markdown("""
### This App detects objects from Images
- Automatically detects 20 objects from image
- [Click Here for App](../YOLO_FOR_IMAGE/)
            
WE CAN DETECT OVER 20 OBJECTS MAN:
- person  
- car  
- chair  
- bottle  
- pottedplant  
- bird  
- dog  
- sofa  
- bicycle  
- horse  
- boat  
- motorbike  
- cat  
- tvmonitor  
- cow  
- sheep  
- aeroplane  
- train  
- diningtable  
- bus  
            """)