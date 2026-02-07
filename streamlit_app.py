import streamlit as st

st.set_page_config(page_title="For You ❤️", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    }
    .container {
        background: white;
        padding: 40px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        max-width: 520px;
        margin: auto;
        margin-top: 20vh;
    }
    .title {
        color: #ff4d6d;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        margin-bottom: 20px;
    }
    .poem {
        margin-top: 20px;
        font-size: 18px;
        line-height: 1.6;
        color: #333;
        background: #fff0f5;
        padding: 20px;
        border-radius: 12px;
    }
    </style>

    <div class="container">
        <div class="title">Heyyy Love You ❤️</div>
        <p class="subtitle">Wishing you a very Happy Propose Day 💍</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Button section
# Button section
if st.button("Hey I have something for you click below 💌"):
    st.markdown(
        """
        <div class="poem">
            <p>
                In every smile I find my home,<br>
                In your voice my heart finds calm,<br>
                You are my today and every tomorrow,<br>
                My little peace in all the chaos.
            </p>
            <p><b>Hey my little small world, love you ❤️</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )
