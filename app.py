# Load the libraries
import streamlit as st
from utils import summerize_text

# Set the page configuration
st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set the title 
st.title("Text :blue[Summarizations]")

# Set the session state
if "output" not in st.session_state:
    st.session_state['output'] = False

st.write("")
with st.container():
    user_input = st.text_area("Enter Your Article or Text:\n", height=200)

    if user_input is not None :
        data = {
            "inputs": user_input,
            # "parameters": {
            #     "max_length": 500, 
            #     "min_length": 5,  
            #     "do_sample": False
            # }
        }

        result = summerize_text(payload=data)
        st.session_state['output'] = result

if st.button("Summarize Text"):
    st.header("Result:")
    with st.container(border=True):
        if st.session_state['output']:
            st.write(st.session_state['output'][0]['summary_text'])
