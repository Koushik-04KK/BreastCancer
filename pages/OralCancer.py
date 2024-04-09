import keras
from PIL import Image, ImageOps
import numpy as np
import streamlit as st

def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability

background_style = """
    <style>
        [data-testid="stAppViewContainer"]> .main {
            background-image: url("https://img.freepik.com/premium-photo/red-ribbon-red-may-awareness-campaign-prevention-oral-cancer_499484-1463.jpg");
            background-size: 100vw 100vh;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """

st.markdown(background_style, unsafe_allow_html=True)

st.title("Oral Cancer Detection")
st.header("Identification and Classification of oral cancer based on the images")


# Information and Insights regarding Oral Cancer
st.write("### Information and Insights regarding Oral Cancer")
st.markdown("""
    Oral cancer is a type of cancer that can affect any part of the mouth. It includes cancers of the lips, tongue, gums, floor of the mouth, and roof of the mouth (palate). 
    It is important to be aware of the risk factors associated with oral cancer. These include:
""")
st.markdown("""
    - Tobacco use, including smoking and chewing tobacco
    - Heavy alcohol use
    - Human papillomavirus (HPV) infection
    - Poor diet lacking in fruits and vegetables
    - Chronic sun exposure (for lip cancer)
""")
st.markdown("""
    Early detection of oral cancer greatly improves the chances of successful treatment. If you notice any signs or symptoms such as persistent mouth sores, lumps, or changes in mouth or lip color, it's essential to consult a healthcare professional for evaluation.
""")
st.subheader("Upload your image")
uploaded_file = st.file_uploader("Choose a scan ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Scan.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, '/content/OralCancer.h5')
    if label == 0:
        st.warning("""**Your scan displays features of cancer.**

A concise guide for managing malignant breast conditions effectively:

1. **Consult specialists** for guidance.
2. **Understand your diagnosis**.
3. **Discuss treatment options**.
4. **Develop a personalized treatment plan**.
5. **Communicate openly** with your healthcare team.
6. **Manage treatment side effects**.
7. **Seek emotional support**.
8. **Maintain a healthy lifestyle**.
9. **Attend regular follow-up appointments**.
10. **Stay informed** about research and resources.
""")
    else:
        st.success("**Your scan is normal. Take care of your body.**")
