# app.py
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- Profile Info ---
NAME = "Gaurav Vijay Jadhav"
DESCRIPTION = "Data Scientist | Machine Learning Engineer | Analyst"
EMAIL = "gaurav.vjadhav01@gmail.com"
PHONE = "+91 9322493102"
GITHUB = "https://github.com/jadhavgaurav"
LINKEDIN = "https://linkedin.com/in/gauravjadhav007"
RESUME_LINK = "https://storage.googleapis.com/personal-portfolio-data/documents/resume/Jadhav_Gaurav_Resume.pdf"

# --- Page Configuration ---
st.set_page_config(page_title="Gaurav Jadhav Portfolio", page_icon="📊", layout="wide")

st.markdown(
    """
    <style>
    /* Enlarge tab labels */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        font-weight: 600;
        padding: 10px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Load Profile Image ---
profile_img_url = "https://storage.googleapis.com/personal-portfolio-data/images/gaurav_photo.jpg"  # Replace with your image URL
response = requests.get(profile_img_url)
img = Image.open(BytesIO(response.content))


# --- Sidebar ---
# st.sidebar.image(img, width=200)

with st.sidebar:
    st.markdown(
    f"""
    <div style='margin-bottom: 1rem;'>
        <img src="{profile_img_url}" 
             style="border-radius: 50%; 
                    width: 220px; 
                    height: 220px; 
                    object-fit: cover; 
                    display: block;
                    margin-left: 0; 
                    margin-right: auto;" />
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title(NAME)
st.sidebar.markdown(DESCRIPTION)
st.sidebar.markdown(f"📧 [{EMAIL}](mailto:{EMAIL})")
st.sidebar.markdown(f"📞 {PHONE}")

st.sidebar.markdown(
    f"""
    <div style='font-size: 16px; padding-top: 8px;'>
        <a href="{GITHUB}" target="_blank" style="text-decoration: none;">
            🐙 <strong>GitHub</strong>
        </a><br>
        <a href="{LINKEDIN}" target="_blank" style="text-decoration: none;">
            💼 <strong>LinkedIn</strong>
        </a>
        <br><br>
    </div>
    """,
    unsafe_allow_html=True
)


try:
    response = requests.get(RESUME_LINK)
    if response.status_code == 200:
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=response.content,
            file_name="Gaurav_Jadhav_Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("⚠️ Unable to fetch resume. Check file permissions or URL.")
except Exception as e:
    st.error(f"Error downloading resume: {e}")

# --- Tabs ---
tabs = st.tabs(["🏠 Home", "📂 Projects", "📜 Certifications", "🏆 Achievements"])

# --- Home Tab ---
with tabs[0]:
    st.markdown("## 👋 Hello, I'm Gaurav")
    
    st.markdown(
    """
    I'm a **Data Scientist and Machine Learning Engineer** with a strong foundation in statistics, algorithmic problem-solving, and full-cycle software development.

    I specialize in crafting end-to-end, data-driven solutions that address real-world business challenges using machine learning, AI, and intuitive, dashboard-driven storytelling.

    ---
    ### 🎯 Professional Summary
    - ✅ Proven experience in delivering full-stack data projects — from data cleaning, feature engineering, and model building to CI/CD integration and scalable deployment.
    - ✅ Hands-on expertise with **Data Anaysis**, **Machine Learnning**, **Artificial Neural Networks (ANN)**, **Convolutional Neural Networks (CNN)**, and **OpenCV**.
    - ✅ Applied **MLflow** and **DagsHub** for experiment tracking and reproducibility; integrated **DVC** for robust data and pipeline versioning.
    - ✅ Automated workflows using **GitHub Actions** and deployed scalable models on **Google Cloud Platform**.
    - ✅ Developed real-time applications and interactive dashboards that enhanced decision-making and business impact.
    - ✅ Strong communicator with a passion for ethical AI, continuous learning, and building impactful solutions across industries.
    
    
    ---

    ### 🎓 Education
    - 🧠 **Master’s in Data Science** *(Ongoing)*
    - 🎓 **B.E. in Computer Engineering**, University of Mumbai – 2024  *CGPA: 7.83/10*


    """)

#  --- Skills Section ---

    st.subheader("🛠️ Skills")
    st.markdown("### 🧰 Technical Proficiency")

    skills = [
        {"name": "Python", "icon": "🐍", "level": 85},
        {"name": "SQL", "icon": "🗄️", "level": 90},
        {"name": "Advanced Excel", "icon": "📊", "level": 95},
        {"name": "Machine Learning", "icon": "🤖", "level": 90},
        {"name": "TensorFlow - ANN / CNN", "icon": "🧠", "level": 85},
        {"name": "Power BI", "icon": "📊", "level": 70},
        {"name": "Streamlit", "icon": "🌐", "level": 90},
        {"name": "Google Cloud", "icon": "☁️", "level": 80},
        {"name": "Tableau", "icon": "📈", "level": 60},
        {"name": "HTML / CSS", "icon": "🌐", "level": 85},
        {"name": "Git, GitHub & GitHub Actions", "icon": "🧬", "level": 85},
    ]

    for skill in skills:
        color = "#00C853" if skill["level"] >= 90 else "#FFD600" if skill["level"] >= 80 else "#FF6D00"
        st.markdown(
            f"""
            <div style='margin-bottom: 14px;'>
                <strong style='font-size: 15px;'>{skill["icon"]} {skill["name"]}</strong>
                <div style='background-color: #e0e0e0; border-radius: 8px; height: 18px; width: 100%; overflow: hidden;'>
                    <div style='height: 100%; width: {skill["level"]}%; background-color: {color}; 
                                border-radius: 8px; text-align: right; padding-right: 8px; 
                                color: black; font-size: 13px; line-height: 18px; text-style: bold;,'>
                        {skill["level"]}%
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Projects Tab ---
with tabs[1]:
    st.header("📂 Projects")

    with st.expander("🧠 Kidney Disease Classification Using CNN"):
        st.write("""
         [GitHub Repo](https://github.com/jadhavgaurav/kidney_disease_classification) [Live Demo](https://kidney-disease-classification.streamlit.app/)  [Live Demo](https://website-phishing-detection.streamlit.app/) [View Experiments](https://dagshub.com/jadhavgaurav/Kidney_disease_classification_cnn.mlflow/#/experiments/0?viewStateShareKey=3894e7dac091113a949e1a0b144bdfbf23f857b1cfb2b6251e919052fe25b155&compareRunsMode=TABLE)
        -  📌 Tech Stack: Python, TensorFlow/Keras (CNN), OpenCV,MLFlow, DVC[GCP], AWS (EC2), GitHub Actions
        - Built a CNN model to classify kidney disease from CT scan images, achieving high accuracy through deep learning architecture optimization.
        - Utilized MLflow for experiment tracking  DagsHub and model performance logging across multiple training iterations.
        - Integrated DVC to version datasets and manage model pipelines, ensuring reproducibility and traceability.
        - Automated deployment with AWS-based CI/CD pipeline (GitHub Actions + AWS) for scalable cloud execution and continuous delivery.

        """)

    with st.expander("🔍 Phishing Website Detection Using Machine Learning"):
        st.write("""
        [GitHub Repo](https://github.com/jadhavgaurav/CodeB_Internship_Project)  
        - 📌 Tech Stack: Python, Scikit-learn, LIME, SHAP, Streamlit, GridSearchCV, GitHub Actions, CI/CD, DVC (GCP)
        - Developed a phishing detection model using structured URL-based features (85+ features, 11K+ records) with advanced feature selection techniques (f_classif, RFE, VIF) and feature engineering.
        - Optimized XGBoost using GridSearchCV, achieving 95.6% accuracy and 0.99 ROC-AUC on the test set.
        - Applied LIME and SHAP for model interpretability, enhancing transparency and trust in predictions.
        - Deployed the model via a Streamlit web app with real-time prediction capability, and automated CI/CD workflows using GitHub Actions and DVC pipeline with Google Cloud Storage for version control.

        """)

    with st.expander("📊 Insurance Premium Estimation Using Machine Learning "):
        st.write("""
        [GitHub Repo](https://github.com/jadhavgaurav/Insurance-premium-prediction-using-MachineLearning) [Live Demo](https://insurance-premium-regression-gj.streamlit.app/)
        - 📌 Tech Stack: Python (Pandas, NumPy, Seaborn, Matplotlib), Machine Learning (Scikit-Learn), Streamlit, GitHub Actions 
        - Developed an SVR-based predictive model for insurance premium forecasting, analysing 1,000+ records with a testing R² score of 0.88.
        - Applied hyperparameter tuning, feature engineering, and 5-fold cross-validation to enhance model accuracy and robustness.
        - Built a Streamlit-based interactive web app for real-time predictions, dataset uploads, and instant result downloads.
        - Implemented a CI/CD pipeline using GitHub Actions to automate model training, testing, and deployment, ensuring seamless integration and continuous updates.
        - Improved pricing accuracy, risk assessment, and customer segmentation, driving better profitability for insurers.

        """)

    with st.expander("🏗️ Cement Composite Strength Prediction"):
        st.write("""
        [GitHub Repo](https://github.com/jadhavgaurav/cement-composite-strength-prediction) 
        - 📌 Tech Stack: Python (Pandas, NumPy, Seaborn, Matplotlib), Scikit-Learn, ANN (TensorFlow), Streamlit
        - Developed a predictive model to estimate concrete compressive strength, optimizing material composition for enhanced structural performance.
        - Engineered key features (Water-Cement Ratio, Strength-Age Ratio) and utilized core mix components (Cement, Fly Ash, Slag, Water, Superplasticizer, Age) to improve accuracy.
        - Applied Artificial Neural Networks (ANNs) and Random Forest, achieving a Test R² Score of 0.962.
        - Optimized hyperparameters using Keras Tuner enhancing model generalization.

        """)

# --- Certifications Tab ---
with tabs[2]:
    st.header("📜 Certifications")

    certifications = [

        {
            "title": "Master in data science, Data Analytics with Artificial Intelligence ",
            "issuer": "IT Vedant",
            "thumb": "https://storage.googleapis.com/personal-portfolio-data/images/IT_Vedant_course.jpg",
            "link": "https://itv-uploads.s3.ap-south-1.amazonaws.com/certificates/cce_certificate16866_.jpg"
        },

        {
            "title": "Data Analysis with Python",
            "issuer": "IBM",
            "thumb": "https://storage.googleapis.com/personal-portfolio-data/images/IBM_Data_Analytics.jpg",
            "link": "https://coursera.org/verify/your-cert-id"
        },
        {
            "title": "British Airways Job Simulation",
            "issuer": "Forage",
            "thumb": "https://storage.googleapis.com/personal-portfolio-data/images/British_Airways.jpg",
            "link": "https://www.theforage.com/certificate-link"
        },
        {
            "title": "Data Science 360",
            "issuer": "FutureSkills Prime",
            "thumb": "https://storage.googleapis.com/personal-portfolio-data/images/Data_Science_360.jpg",
            "link": "https://futureskillsprime.in/verify/certificate"
        }
        ]

    cols = st.columns(3)

    for i, cert in enumerate(certifications):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="border:1px solid #444; border-radius:10px; padding:10px; margin-bottom:20px; text-align:center;">
                    <a href="{cert['link']}" target="_blank">
                        <img src="{cert['thumb']}" style="width:100%; height:auto; border-radius:6px;" />
                        <p style="margin-top:10px; font-weight:bold;">{cert['title']}</p>
                        <p style="margin-top:-10px; font-size:13px; color:gray;">{cert['issuer']}</p>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )


# --- Achievements Tab ---
with tabs[3]:
    st.header("🏆 Achievements")
    st.markdown("""
    - **📄 Research Paper Publication**: "A Framework to Make Voting System Transparent Using Blockchain Technology"
    - Journal: International Journal for Research in Engineering Application & Management (IJREAM)
    - ISSN: 2454-9150 | Vol. 10, Issue 01, April 2024
    - DOI: 10.35291/2454-9150.2024.0261 | Paper ID: IJREAMV10SSJ2411
    - [Read Paper](https://ijream.org/papers/IJREAMV10SSJ2411.pdf)
    ---
    - **National Service Scheme (NSS) | Volunteer (2 Years)**
        - Led community development initiatives and participated in leadership training programs.
        - Organized and executed social awareness campaigns at the college and local level.
    - **Association of Computer Engineering Students (ACES) | Head of Technical Committees**
        - Managed technical operations for departmental and college-level events.
        - Led a team in organizing workshops, hackathons, and coding competitions.


    """)
