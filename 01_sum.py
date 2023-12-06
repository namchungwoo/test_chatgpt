import streamlit as st
import openai

#쳇지피티에게 글요약을 요창하는 함수
def askGPT(prompt,apiKey):
    client = openai.OpenAI(api_key=apiKey)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'use':'content':prompt}

        ]
        
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

##main 함수
def main():
    st.set_page_config(page_title="요약프로그램")
    
    #session_state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state[OPENAI_API]=""

    with st.sidebar:
        open_apiKey=st.text_input(label='OPEN API키',placeholder='enter your api key')

        if open_apiKey:
            st.session_state["OPENAI_API"]
            st.markdown(____)
        
        st.header('요약프로그램')
        st.markdown('_____')

        text=st.text_area('요약할 글을 입력하세요')
        if st.button('요약'):
            prompt
            
