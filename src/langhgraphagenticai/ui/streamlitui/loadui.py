import streamlit as st
import os

from src.langhgraphagenticai.ui.uiconfigfile import Config
# from ..uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="bot" + self.config.get_page_title(),layout="wide")
        st.header("bot " + self.config.get_page_title())

        with st.sidebar:
            # Get options from congig
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

        # LLM selection
        self.user_controls['selected_llm']=st.selectbox('Select LLM', llm_options)

        if self.user_controls['selected_llm']=='Groq':
            model_options=self.config.get_groq_model_options()