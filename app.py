import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openai

openai.organization = "org-ZZktHVKSCpm93CmQw4hujuc1"
openai.api_key = "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"
st.markdown("# Main page")
st.sidebar.markdown(" :)( ")

st.title("The AIML Tutor")



txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You:{}\n".format(txt),
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

st.write(response["choices"])

