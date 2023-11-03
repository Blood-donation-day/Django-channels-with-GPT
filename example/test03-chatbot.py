# test03-chatbot.py

import os
import openai

from dotenv import load_dotenv # python-dotenv 라이브러리 활용
load_dotenv()

# Tip: OPENAI_API_KEY 환경변수 로딩 후에, openai 라이브러리를 임포트하면
# 자동으로 api_key 적용이 됩니다.

openai.api_key = os.getenv("OPENAI_API_KEY")

# API KEY 설정에 오류가 있는 지 확인하기 위함
print("api_key :", repr(openai.api_key))

# 챗봇 응답 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"},
    ],
)

print(response["choices"][0]["message"]["content"])

print(response["usage"]["completion_tokens"])