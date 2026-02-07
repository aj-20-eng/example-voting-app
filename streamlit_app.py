import streamlit as st

st.set_page_config(page_title="For You ❤️", layout="centered")

st.markdown(
    """
    <style>
    .container {
        background: white;
        padding: 40px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        max-width: 500px;
        margin: auto;
        margin-top: 20vh;
    }
    .title {
        color: #ff4d6d;
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        font-size: 20px;
    }
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    }
    </style>

    <div class="container">
        <div class="title">Heyyy Love You ❤️</div>
        <p class="subtitle">Wishing you a very Happy Propose Day 💍</p>
    </div>
    """,
    unsafe_allow_html=True
)
