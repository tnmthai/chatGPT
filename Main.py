import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

#     api_key = st.sidebar.text_input("APIkey", type="password")
    api_key =st.secrets["key"]
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("ChatGPT for non-account")

        # st.write("---")

        s_example = "Hello, how are you today?"
        input = st.text_area(
            "Use the example below or input your own text in English",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
