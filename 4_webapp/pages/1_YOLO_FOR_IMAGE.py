import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

st.set_page_config(page_title='YOLO Object Detection',
                   layout='wide',
                   page_icon ='images/object.png')

st.title('Welcome to YOLO for Image')
st.write('Please upload images for detection')

with st.spinner('Wait while our model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx',
                    data_yaml='./models/data.yaml')


def upload_image():
    image_file = st.file_uploader(label = 'upload image')
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        file_details = { "filename":image_file.name,
                        "filetype":image_file.type,
                        "filesize": "{:,.2f} MB".format(size_mb)
                        }
        
        #st.json(file_details)

        if file_details['filetype'] in ('image/png', 'image/jpeg'):
            st.success('GOOD we are valid')
            return {"file":image_file, 
                    "details":file_details
                    }
        else:
            st.error('The file that you have uploaded is not accepted, please upload files which are either pngs or jpegs!')
            return None
        

def main():
    object = upload_image()
    
    if object:
        prediction = False
        image_obj = Image.open(object['file'])       
        
        col1 , col2 = st.columns(2)
        
        with col1:
            st.info('Preview of Image')
            st.image(image_obj)
            
        with col2:
            st.subheader('Check below for file details')
            st.json(object['details'])
            button = st.button('Get Detection from YOLO')
            if button:
                with st.spinner("""
                Geting Objets from image. please wait
                                """):
                    # below command will convert
                    # obj to array
                    image_array = np.array(image_obj)
                    pred_img = yolo.predictions(image_array)
                    pred_img_obj = Image.fromarray(pred_img)
                    prediction = True
                
        if prediction:
            st.subheader("Predicted Image")
            st.caption("Object detection from YOLO V5 model")
            st.image(pred_img_obj)

if __name__ == "__main__":

    main()