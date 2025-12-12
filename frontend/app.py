import streamlit as st
import requests

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="AI Model Router",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Dark Theme and Styling
# This injects HTML/CSS to override default Streamlit styles
st.markdown("""
    <style>
    /* Main Background - Dark Gradient */
    .stApp {
        background: linear-gradient(to bottom right, #0e1117, #161b22);
        color: #e6e6e6;
    }

    /* Input Field Styling */
    .stTextInput > div > div > input {
        background-color: #21262d;
        color: #ffffff;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 15px;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2ea043;
        box-shadow: 0 4px 12px rgba(35, 134, 54, 0.4);
    }

    /* Result Card Styling */
    .result-card {
        background-color: #21262d;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Header Styling */
    h1 {
        text-align: center;
        background: -webkit-linear-gradient(45deg, #61dafb, #d67bf5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 800;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. The UI Layout
# Using columns to center and constrain width for a cleaner look
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Header
    st.markdown("<h1>AI Model Router</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e; margin-bottom: 30px;'>Intelligent routing for your toughest questions.</p>", unsafe_allow_html=True)

    # Input Section
    question = st.text_input("Ask a question", placeholder="Type your query here...", label_visibility="collapsed")
    
    st.write("") # Spacer

    # Button and Logic
    if st.button("Ask AI"):
        if question:
            # Adding a spinner for better UX while waiting for the request
            with st.spinner("Processing request..."):
                try:
                    # --- CORE CODE STARTS ---
                    r = requests.post("http://localhost:8000/ask?question=" + question)
                    answer = r.json()["answer"]
                    # --- CORE CODE ENDS ---
                    
                    # Display Result in a nice card
                    st.markdown(f"""
                        <div class="result-card">
                            <h3 style="color: #58a6ff; margin-top: 0;">Response:</h3>
                            <p style="font-size: 1.1em; line-height: 1.6;">{answer}</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                except Exception as e:
                    st.error(f"Error connecting to server: {e}")
        else:
            st.warning("Please enter a question first.")