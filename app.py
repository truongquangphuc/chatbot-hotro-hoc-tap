import streamlit as st
from main import get_query

st.set_page_config(
    page_title="Hỗ trợ học tập Chuyên đề năm 2024",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("Hỗ trợ học tập chuyên đề năm 2024")

if "messages" not in st.session_state.keys():
    # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Hãy đặt các câu hỏi về Chuyên đề năm 2024!"}
    ]


if prompt := st.chat_input(
    "Đặt câu hỏi"
):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:  # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Đang trả lời..."):
            if prompt is not None:
                # response = gemini_pro.complete(prompt)
                response = get_query(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response.response_gen:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
                message = {"role": "assistant", "content": full_response}
                st.session_state.messages.append(message)
