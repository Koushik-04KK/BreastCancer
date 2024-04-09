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
    # Image resizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    return np.argmax(prediction)  # Return position of the highest probability

# Custom CSS for background
background_style = """
  <style>
    [data-testid="stAppViewContainer"]> .main {
      background-image: url("https://bodyvisionmedical.com/assets/65428c4fd053280012a6d6b3/iStock-1448941404.jpg");
      background-size: 100vw 100vh;
      background-position: center;
      background-repeat: no-repeat;
    }
  </style>
  """

st.markdown(background_style, unsafe_allow_html=True)




st.title("Lung Cancer Detection")
st.header("Identification and Classification of Lung Cancer based on MRI Scans")

# General Information
st.subheader("General Information:")
st.markdown("""
Lung cancer is one of the most common cancers worldwide and is a leading cause of cancer-related deaths. It occurs when abnormal cells grow uncontrollably in one or both lungs, usually in the cells lining the air passages.

**Risk Factors:**
- Smoking: The primary cause of lung cancer, accounting for the majority of cases.
- Exposure to Radon: A naturally occurring radioactive gas that can accumulate in homes and buildings.
- Exposure to Asbestos and Other Carcinogens: Found in certain workplaces and environments.
- Family History: Genetic predisposition can increase the risk of developing lung cancer.
- Air Pollution: Prolonged exposure to pollutants in the air may contribute to lung cancer risk.

**Symptoms:**
- Persistent Cough
- Chest Pain
- Shortness of Breath
- Unintended Weight Loss
- Fatigue
- Hoarseness

**Diagnosis and Treatment:**
- Diagnosis typically involves imaging tests (such as MRI, CT scans) and tissue biopsy.
- Treatment options may include surgery, chemotherapy, radiation therapy, targeted therapy, or immunotherapy, depending on the type and stage of cancer.

Early detection and prompt treatment significantly improve outcomes for individuals with lung cancer.
""")

st.subheader("Upload your MRI Scan")
uploaded_file = st.file_uploader("Choose a scan ...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Scan', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Classify the uploaded scan
    label = teachable_machine_classification(image, '/content/LungCancer.h5')

    if label == 0:
        st.error("Your scan displays features of cancer.")
        st.subheader("Managing Lung Cancer:")
        st.markdown("""
            1. **Consult Specialists:** Seek guidance from healthcare professionals specializing in cancer.
            2. **Understand Diagnosis:** Educate yourself about your diagnosis and its implications.
            3. **Discuss Treatment Options:** Explore various treatment options with your healthcare team.
            4. **Personalized Treatment Plan:** Develop a treatment plan tailored to your needs and preferences.
            5. **Open Communication:** Maintain open communication with your healthcare providers throughout the treatment process.
            6. **Manage Side Effects:** Take measures to manage and cope with the side effects of treatment.
            7. **Seek Support:** Seek emotional and psychological support from loved ones, support groups, or therapists.
            8. **Healthy Lifestyle:** Adopt a healthy lifestyle with a balanced diet and regular exercise.
            9. **Regular Follow-up:** Attend follow-up appointments as scheduled to monitor your progress and address any concerns.
            10. **Stay Informed:** Stay updated on the latest research and resources related to lung cancer.
        """)
    else:
        st.success("**Your scan is normal. Take care of your body.**")
