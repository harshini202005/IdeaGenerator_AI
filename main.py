import streamlit as st
import generator

st.set_page_config(page_title="AI Generator Hub", page_icon="🚀", layout="wide")


st.markdown(
    "<h1 style='text-align:center; color:grey;'>🚀 AI Generator Hub</h1>",
    unsafe_allow_html=True
)

st.markdown("### Create Ideas Instantly with AI")


st.sidebar.header("⚙️ Settings")

mode = st.sidebar.selectbox(
    "Choose Mode",
    ("Startup", "Story", "Game", "Product")
)

domain = st.sidebar.selectbox(
    "Select Domain",
    ("Technology", "Healthcare", "Finance", "Education", "Entertainment")
)

theme = st.sidebar.selectbox(
    "Select Theme",
    ("Futuristic", "Luxury", "Minimal", "Creative", "Eco-friendly")
)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("✨ Generate Idea"):
    with st.spinner("Generating magic... ✨"):
        result = generator.generate_output(mode, domain, theme)

    st.session_state.history.append(result)

    
    st.markdown("## 🎯 Result")

    for item in result:
        st.markdown(
    f"""
    <div style='
        background:#eef4ff;
        color:#1a237e;
        padding:15px;
        border-radius:12px;
        margin:10px 0;
        font-size:16px;
        border:1px solid #d6e4ff;
    '>
        {item}
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown("## 🕘 History")
for h in st.session_state.history[-5:]:
    st.sidebar.write("•", h[0])