import streamlit as st
from PIL import Image
from streamlit_extras.mention import mention
from streamlit_extras.colored_header import colored_header

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Surya Maddukuri | AI/ML Portfolio",
                   page_icon="🤖",
                   layout="wide")

# ---- HEADER ----
st.markdown("""
<style>
.center { text-align: center; }
.highlight { font-size:1.1rem; color: #555; }
.card {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 12px;
    box-shadow: 2px 2px 15px rgba(0,0,0,.1);
    margin-bottom: 20px;
}
.section-header {
    font-size:1.3rem;
    font-weight: bold;
    color: #007BFF;
}
</style>
""", unsafe_allow_html=True)

# ---- INTRO ----
col1, col2 = st.columns([1,3])

with col1:
    try:
        profile_image = Image.open("surya.png")  # Add your image
        st.image(profile_image, use_container_width="auto")
    except FileNotFoundError:
        st.markdown("👤 *Add `surya.png` for a personal photo.*")

with col2:
    st.markdown("""
    <h1 class="center">👋 Maddukuri Surya Teja</h1>
    <h3 class="center">AI/ML & NLP Specialist | Model Optimization | MLOps</h3>
    <p class="center highlight">
    Results-driven AI/ML professional with experience in NLP pipelines, fine-tuning Transformer-based LLMs, and deploying solutions across AWS. Skilled in deep learning, statistical modeling, and workflow automation using MLOps best practices.
    </p>
    """, unsafe_allow_html=True)

# ---- LINKS ----
st.markdown("<div class='center'>", unsafe_allow_html=True)
mention("LinkedIn", "https://www.linkedin.com/in/surya-maddukuri/", icon="linkedin")
mention("GitHub", "https://github.com/surya-maddukuri", icon="github")
st.markdown("</div>", unsafe_allow_html=True)

# ---- TECHNICAL EXPERTISE ----
st.markdown("<div class='card'>", unsafe_allow_html=True)
colored_header("⚡ Technical Expertise", "#2196F3")
cols = st.columns(3)

with cols[0]:
    st.markdown("""
    - 🐍 **Python, Pandas, NumPy**
    - ⚡ **Stat Models:** Regression, Random Forest, XGBoost
    - 🕹️ **Deep Learning:** CNN, RNN, Transformers
    """)
with cols[1]:
    st.markdown("""
    - 💡 **NLP Techniques:** Tokenization, NER, LLM fine-tuning
    - 🛠️ **Frameworks:** TensorFlow, PyTorch, Keras
    - 📊 **Visualization:** Matplotlib, Seaborn
    """)
with cols[2]:
    st.markdown("""
    - ☁️ **MLOps & Cloud:** AWS, Azure, GCP
    - 🚢 **Deployment:** Docker, Kubernetes, Streamlit
    - 🔥 **Workflow Optimization:** MLflow, Apache Airflow
    """)
st.markdown("</div>", unsafe_allow_html=True)

# ---- EDUCATION ----
st.markdown("<div class='card'>", unsafe_allow_html=True)
colored_header("🎓 Education", "#9C27B0")
st.markdown("""
- **B.Tech in Computer Science Engineering (2017–2022)** — PRIST University, Chennai  
- **Certification:** Machine Learning & Deep Learning Workshop conducted by Pivotal Soft
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---- PROFESSIONAL EXPERIENCE ----
st.markdown("<div class='card'>", unsafe_allow_html=True)
colored_header("👔 Professional Experience", "#FF5722")
st.markdown("""
**Software Engineer — Lyros Technologies (Feb 2025–Present):**  
- Created an interactive tax calculator using Streamlit for state and federal calculations.  
- Developed clean, user-friendly interfaces and implemented complex bracket tax logic.  
- Created end‑to‑end NLP pipelines for text classification, sentiment detection, and named entity recognition using Hugging Face Transformers.  
- Fine‑tuned and optimized BERT and GPT‑style Transformer models for classification and summarization.  
- Created end‑to‑end ML pipelines for deployment using Kubernetes, MLflow, and Apache Airflow.

**Python Developer (Self‑Driven Projects) (2022–2025):**  
- Created automated data-processing pipelines and ML pipelines for NLP and predictive analytics.  
- Developed interactive dashboards and AI applications using Streamlit and Hugging Face.  
- Created REST APIs for seamless model access and deployment across platforms.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---- PROJECTS ----
st.markdown("<div class='card'>", unsafe_allow_html=True)
colored_header("💻 Projects & Case Studies", "#607D8B")
st.markdown("""
**Tax Calculator using Streamlit**  
- Created an interactive app for state and federal tax calculations.  
- Developed a clean and user-friendly interface.  
- Ensured precision and reliability across income scenarios.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---- CERTIFICATIONS ----
st.markdown("<div class='card'>", unsafe_allow_html=True)
colored_header("🏆 Certifications & Achievements", "#3F51B5")
st.markdown("""
- Participation in **Machine Learning & Deep Learning Workshop** conducted by Pivotal Soft.  
- Skilled in end‑to‑end AI pipelines, NLP prompt engineering, and model deployment.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---- DOWNLOAD RESUME ----
st.markdown("---")
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.markdown("### 📄 Download My Resume")
try:
    with open("surya_resume44.pdf", "rb") as file:
        st.download_button(
            label="⬇️ Download Surya Maddukuri Resume (PDF)",
            data=file.read(),
            file_name="Surya_Maddukuri_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.warning("📁 'surya_resume44.pdf' not found. Please add it to the app directory.")
st.markdown("</div>", unsafe_allow_html=True)
