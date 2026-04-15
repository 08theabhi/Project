import streamlit as st
from groq import Groq

st.set_page_config(page_title="StartZen Content Generator", layout="wide")

st.title("🧘 StartZenAI - Content Generator")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

product = st.text_input("Product")
audience = st.text_input("Audience")

if st.button("Generate Content"):
    if product.strip() and audience.strip():
        prompt = f"Write marketing content for {product} targeting {audience}."
        with st.spinner("Generating content..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.text = response.choices[0].message.content
    else:
        st.warning("⚠️ Please enter both Product and Audience.")

if "text" in st.session_state:
    content = st.text_area("Generated Content", st.session_state.text, height=300)
    st.download_button(
        label="⬇️ Download as TXT",
        data=content,
        file_name="marketing_copy.txt",
        mime="text/plain"
    )
else:
    st.info("👆 Enter a product and audience then click Generate Content")
