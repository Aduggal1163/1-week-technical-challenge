import requests
import streamlit as st
#IMPORTANT In LangServe, /invoke endpoint
#  is used to execute the LLM or chain and get the response.
#  The base route only defines the chain, but /invoke actually runs it and returns the output.
st.set_page_config(page_title="Gemini AI Generator", layout="centered")
st.title("GEMINI AI GENERATOR")
option=st.radio("Choose what you want: ",["✍️ Essay writing","🎶 Poem writing"])

if option == "✍️ Essay writing":
    topic = st.text_input("Enter essay topic")

    if st.button("Generate Essay"):
        if topic.strip() == "":
            st.warning("Please enter a topic")
        else:
            with st.spinner("Generating essay..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/essay/invoke",
                        json={"input": {"topic": topic}}
                    )
                    result = response.json()['output']['content']
                    st.success("Essay generated successfully")
                    st.write(result)

                except Exception as e:
                    st.error("⚠️ FastAPI server not running or API error")


elif option == "🎶 Poem writing":
    topic = st.text_input("Enter poem topic")

    if st.button("Generate Poem"):
        if topic.strip() == "":
            st.warning("Please enter a topic")
        else:
            with st.spinner("Generating poem..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/poem/invoke",
                        json={"input": {"topic": topic}}
                    )
                    result = response.json()['output']['content']
                    st.success("Poem generated successfully")
                    st.write(result)

                except Exception as e:
                    st.error("⚠️ FastAPI server not running or API error")