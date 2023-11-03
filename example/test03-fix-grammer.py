import os
import openai

from dotenv import load_dotenv 

# Tip: OPENAI_API_KEY 환경변수 로딩 후에, openai 라이브러리를 임포트하면
# 자동으로 api_key 적용이 됩니다.

openai.api_key = os.getenv("OPENAI_API_KEY")

# 텍스트 생성 혹은 문서 요약
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="""
Fix grammar errors:
- I is a boy
- You is a girl""".strip(),
)

print(response.choices[0].text.strip())