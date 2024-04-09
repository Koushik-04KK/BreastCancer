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
            background-image: url("https://img.freepik.com/premium-photo/melanoma-skin-cancer-vaccine-injury-awareness-month-rest-peace-concepts-black-ribbon-grey-background_42256-3737.jpg");
            background-size: 100vw 100vh;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """

st.markdown(background_style, unsafe_allow_html=True)

st.title("Skin Cancer Detection")
st.header("Identification and Classification of Skin Cancer based on Images")
st.write("""
**Skin cancer** is the abnormal growth of skin cells, most often developed on skin exposed to the sun. 
Early detection and proper management are essential for improving outcomes. 
Here, you can upload an image for classification.
""")
st.subheader("**Insights on Skin Cancer:**")
st.markdown("""
- **Skin cancer** is the most common type of cancer globally.
- **Exposure to ultraviolet (UV) radiation** from the sun or tanning beds is a major risk factor for developing skin cancer.
- **Skin cancer** can occur on any part of the body but is most commonly found on areas exposed to the sun, such as the face, neck, hands, and arms.
- **Regular skin checks**, including self-examinations and dermatological screenings, can aid in early detection.
- **Types of skin cancer** include basal cell carcinoma, squamous cell carcinoma, and melanoma, each with distinct characteristics and treatment approaches.
- **Treatment options** for skin cancer may include surgery, radiation therapy, chemotherapy, immunotherapy, and targeted therapy, depending on the type and stage of cancer.
- **Preventive measures** such as wearing sunscreen, protective clothing, and avoiding excessive sun exposure can reduce the risk of developing skin cancer.
""")
st.subheader("Upload your image")
uploaded_file = st.file_uploader("Choose an image ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("**Classifying...**")
    label = teachable_machine_classification(image, '/content/SkinCancer.h5')
    if label == 0:
        st.error("Your scan displays features of cancer.")
        st.subheader("Managing Skin Cancer:")
        st.markdown("""
          1. **Consult healthcare professionals** for diagnosis and treatment options.
          2. **Understand the diagnosis** and characteristics of the cancer.
          3. **Discuss treatment options** and develop a personalized plan.
          4. **Regular monitoring** and follow-up appointments.
          5. **Maintain a healthy lifestyle** and sun-safe practices.
          6. **Seek emotional support** from loved ones and support groups.
          7. **Stay informed** about advancements in skin cancer research and treatment.
          8. **Advocate for awareness** and sun protection.
          """)
    else:
        st.write("**Your image is normal. Take care of your skin and practice sun safety measures.**")
