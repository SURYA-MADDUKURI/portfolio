import streamlit as st

# Set page config for a modern dark theme
st.set_page_config(page_title="Surya Maddukuri - AI/ML Portfolio", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for dark theme and styling
st.markdown("""
<style>
    .stApp { background-color: #1A1A1A; color: #E6E6E6; }
    .hero-banner { background: linear-gradient(90deg, #1E90FF, #4682B4); padding: 40px; text-align: center; border-radius: 15px; }
    .hero-title { font-size: 52px; color: #FFFFFF; margin-bottom: 10px; }
    .hero-subtitle { font-size: 20px; color: #E6E6E6; }
    .section-header { font-size: 32px; color: #1E90FF; margin-top: 30px; margin-bottom: 15px; }
    .content-text { font-size: 18px; color: #B0B0B0; }
    .skill-chip { background-color: #4682B4; color: #FFFFFF; padding: 8px 15px; border-radius: 20px; margin: 5px; display: inline-block; }
    .exp-box { background-color: #2A2A2A; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #1E90FF; }
    .project-box { background-color: #2A2A2A; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #4682B4; }
    .progress-bar { background-color: #333; border-radius: 5px; }
    .progress-fill { background-color: #1E90FF; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown('<div class="hero-banner"><div class="hero-title">Surya Maddukuri</div><div class="hero-subtitle">AI/ML Specialist ', unsafe_allow_html=True)

# About Me Section with Image
st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="content-text">I am a Computer Science and Engineering graduate with a deep passion for AI and machine learning. My expertise lies in developing and optimizing AI models, with a focus on data processing, NLP, and visualization. I have hands-on experience in Python, deep learning, and collaborative workflows, making me a strong fit for roles that require innovation and technical precision. I aim to contribute to impactful AI projects by leveraging my skills to solve real-world challenges.</p>', unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1600585154343-5b9c54f2d2b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60", caption="Working on AI Solutions", use_container_width=True)

# Skills Section with Progress Bars
st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
skills = {
    "Python": 90,
    "Machine Learning": 85,
    "Deep Learning": 80,
    "Pandas": 85,
    "NumPy": 85,
    "Visualization": 75,
    "NLP": 70
}
col1, col2 = st.columns([2, 1])
with col1:
    for skill, proficiency in skills.items():
        st.markdown(f'<span class="skill-chip">{skill}</span>', unsafe_allow_html=True)
        st.progress(proficiency)
with col2:
    st.image("https://images.unsplash.com/photo-1516321318423-7d6a9183b4d9?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60", use_container_width=True)

# Work Experience Section
st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
st.markdown('<div class="exp-box"><b>AI/ML Intern</b><br>Lyros Technologies, Hyderabad | January 2025 - Ju 2023<br>Collaborated with a team to develop and optimize machine learning models for predictive analytics using Python, Pandas, and NumPy. Implemented NLP techniques to analyze customer feedback data, improving sentiment analysis accuracy by 15%. Created visualizations using Matplotlib and Seaborn to present insights to stakeholders.</div>', unsafe_allow_html=True)

# Projects Section with Visual
st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="project-box"><b>Bloom Filter (2021 - 2022)</b><br>Developed a Bloom filter over encrypted cloud data for multi-keyword search, enabling efficient and scalable data retrieval systems.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-box"><b>Sentiment Analysis with NLP (2023)</b><br>Built a deep learning model using Python and TensorFlow to classify sentiments in social media data. Utilized Pandas and NumPy for data preprocessing and achieved 85% accuracy through hyperparameter tuning and model optimization.</div>', unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1551288049-b5f3a44fbaba?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60", caption="AI Model Development", use_container_width=True)

# Certificates Section
st.markdown('<div class="section-header">Certificates</div>', unsafe_allow_html=True)
st.markdown('<p class="content-text"><b>Machine Learning & Deep Learning Workshop</b><br>Pivotalsoft, PRIST Deemed to be University</p>', unsafe_allow_html=True)
st.markdown('<p class="content-text"><b>Software Development Workshop</b><br>Certification for a three-day workshop on Software Development</p>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
st.markdown('<p class="content-text">📍 Rajahmundry, India<br>📧 suryamaddukuri4380@gmail.com<br>📞 +91 8332967735</p>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="content-text" style="text-align: center; margin-top: 30px;">Built with ❤️ using Streamlit | Surya Maddukuri © 2025</p>', unsafe_allow_html=True)