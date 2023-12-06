import streamlit as st
import openai

#챗 지피티에게 글 요약을 요청하는 함수
def askGPT(prompt,apiKey): 
    client = openai.OpenAI(api_key=apiKey)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

## main 함수
def main():
    st.set_page_config(page_title="요약 프로그램") #페이지 제목

    #session_state 초기화
    if "OPENAI_API" not in st.session_state: #not in 의미는 22라인의 st.session가 21라인의 st.session 딕셔너리에 없는가?를 의미 없으면 True, 있으면 False
        st.session_state["OPENAI_API"] = "" #없으면 true이므로 fucntion 값을 진행. 한번 실행되면 저장됨

    with st.sidebar:
        open_apikey = st.text_input(label='OPEN API 키', placeholder='Enter your api key')

        if open_apikey: #키가 존재하면
            st.session_state["OPENAI_API"] = open_apikey #저장함
        st.markdown('---')

    st.header(":scroll:요약 프로그램:scroll:") #제목 글자 넣음
    st.markdown('---')

    text = st.text_area("요약 할 글을 입력하세요") #여러줄의 글을 넣을 때, text_area 사용
    if st.button("요약"): #버튼이 클릭이 되면 아래 프롬프트 실행 (구글,파파고 번역 검색하면 양식이 나옴)
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''    
        st.info(askGPT(prompt,st.session_state["OPENAI_API"]))

if __name__ == "__main__": #__name__는 특수변수임. 여기서 처음 실행한 01_su~는 __main__으로 가진다. 진입함수로 호출시키기 위해 만듦.
    main()