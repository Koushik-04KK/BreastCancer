
import streamlit as st

def main():
    # Set page title and background
    st.set_page_config(page_title="Oncoscan - Multi Cancer Detection", page_icon="🔬", layout="wide")
    background_style = """
       <style>
          [data-testid="stAppViewContainer"]> .main {
            background-image: url("https://i.pinimg.com/564x/32/c3/ea/32c3eaaed26fa73510851bc7ffdbf0fa.jpg");
            background-size: 100vw 100vh;
            background-position: center;
            background-repeat: no-repeat;
          }
        </style>
    """

    st.markdown(background_style, unsafe_allow_html=True)

  
    # Header
    st.title("Oncoscan - Multi Cancer Detection")
    st.write("Welcome to Oncoscan! Your one-stop solution for multi-cancer detection.")

    # General Information about cancer
    st.header("General Information about Cancer")
    st.markdown("""
    Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. 
    It can affect any part of the body and has various types, each with its own symptoms, risk factors, and treatments.
    Early detection plays a crucial role in improving outcomes and survival rates.
    """)

    # Cancer Statistics
    st.header("Cancer Statistics")
    st.markdown("""
    - According to the World Health Organization (WHO), cancer is the second leading cause of death globally, 
      accounting for an estimated 9.6 million deaths in 2018.
    - The most common cancers worldwide are lung, breast, colorectal, prostate, and stomach cancers.
    - Approximately 70% of deaths from cancer occur in low- and middle-income countries.
    """)

    # Cancer Prevention Tips
    st.header("Cancer Prevention Tips")
    st.markdown("""
    While not all cancers are preventable, there are steps you can take to reduce your risk:
    1. **Quit Smoking:** Smoking is a leading cause of many cancers, including lung, throat, and mouth cancer.
    2. **Maintain a Healthy Diet:** Eat plenty of fruits, vegetables, and whole grains, and limit processed foods.
    3. **Exercise Regularly:** Aim for at least 30 minutes of moderate exercise most days of the week.
    4. **Limit Alcohol Consumption:** Excessive alcohol consumption is linked to an increased risk of several cancers.
    5. **Protect Yourself from the Sun:** Use sunscreen, wear protective clothing, and avoid tanning beds.
    6. **Stay Vaccinated:** Vaccines can help prevent certain cancers, such as hepatitis B and human papillomavirus (HPV).
    """)

    # Cancer Screening Guidelines
    st.header("Cancer Screening Guidelines")
    st.markdown("""
    Regular screenings can help detect cancer early when treatment is most effective. 
    Talk to your doctor about the appropriate screening tests for your age and risk factors. 
    Some common cancer screening tests include:
    - Mammograms for breast cancer
    - Pap smears for cervical cancer
    - Colonoscopies for colorectal cancer
    - PSA tests for prostate cancer
    - CT scans and X-rays for lung cancer
    """)

    # Sidebar with top hospitals and doctors in Chennai
    st.sidebar.title("Top Hospitals for Cancer in Chennai")
    st.sidebar.markdown("""
    1. Apollo Hospitals, Greams Road
    2. Adyar Cancer Institute
    3. Fortis Malar Hospital, Adyar
    4. MIOT International
    5. Cancer Institute (WIA), Adayar
    """)

    st.sidebar.title("Top Doctors for Cancer in Chennai")
    st.sidebar.markdown("""
    1. Dr. V. Shanta - Adyar Cancer Institute
    2. Dr. Prathap C. Reddy - Apollo Hospitals
    3. Dr. Mohan Kameswaran - MIOT International
    4. Dr. Arun Kumar V - Fortis Malar Hospital
    5. Dr. R. Pallivikashan - Cancer Institute (WIA)
    """)

if __name__ == "__main__":
    main()
