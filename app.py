import streamlit as st
from groq import Groq
import base64

# MUST be first Streamlit command
st.set_page_config(page_title="StartZen", layout="wide")

# function to load image
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# change filename if needed
img = get_base64("download.jpg")

# apply background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config("StartZen Content Generator",layout="wide")
st.title("StartZenAI - Content Generator")
st.image("download.jpg")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
product = st.text_input("Product")
audience = st.text_input("Audience")
if st.button("Generate Content"):
    prompt = f"Write marketing content for {product} targeting {audience}."
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    st.session_state.text = response.choices[0].message.content
    text =response.choices[0].message.content
    st.write(text)
if "text" in st.session_state:
    content = st.text_area("Generated Content", st.session_state.text, height=300)
    st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
else:
        st.info("Generate content first")
