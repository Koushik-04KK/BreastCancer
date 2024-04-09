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
      background-image: url("https://cdn.wallpapersafari.com/40/18/yg7M4l.jpg");
      background-size: 100vw 100vh;
      background-position: center;
      background-repeat: no-repeat;
    }
  </style>
  """

st.markdown(background_style, unsafe_allow_html=True)

st.title("Breast Cancer Detection")
st.header("Identification and Classification of Breast Cancer Based on Ultrasound Scan")
st.write("""
**Breast cancer** is the most common cancer among women worldwide. 
**Early detection** and proper management are crucial for improving outcomes. 
Here, you can upload an ultrasound scan for classification.
""")
st.subheader("**Insights on Breast Cancer:**")
st.markdown("""
- **Breast cancer** can occur in both men and women, but it is far more common in women.
- **Age, genetics, family history**, and lifestyle factors can influence the risk of developing breast cancer.
- **Regular breast screenings**, including mammograms and self-examinations, can aid in early detection.
- **Symptoms** of breast cancer may include a lump or mass in the breast, changes in breast size or shape, nipple discharge, or skin changes.
- Various **treatment options** for breast cancer include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy.
- Each case of breast cancer is unique, and **treatment plans** are tailored to individual needs.
- **Support networks**, counseling, and advocacy groups can provide valuable emotional support for individuals affected by breast cancer.
""")
st.subheader("Upload your Mammogram")
uploaded_file = st.file_uploader("Choose a scan ...", type="png")
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded Scan.', use_column_width=True)
  st.write("")
  st.write("**Classifying...**")
  label = teachable_machine_classification(image, '/content/Breastcancer.h5')
  if label == 0:
    st.write("**Your scan is normal. Take care of your body.**")
  else:
    st.write("""**Your scan displays features of cancer.**

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
