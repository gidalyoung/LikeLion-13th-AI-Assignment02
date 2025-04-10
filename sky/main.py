import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일의 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키와 시스템 메시지 불러오기
API_KEY = os.environ["API_KEY"]
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

# Together API의 기본 URL과 사용할 모델 설정
BASE_URL = "https://api.together.xyz"
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"  # 사용할 LLaMA3.1 모델

# OpenAI 클라이언트 초기화 (Together API 사용을 위한 설정)
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 시스템 메시지를 포함한 대화 메시지 초기화
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE}
]

print("챗봇을 시작합니다! (종료하려면 'exit' 입력)")

# 챗봇 루프 시작
while True:
    user_input = input("You: ")  # 사용자 입력 받기

    # 'exit' 또는 'quit' 입력 시 챗봇 종료
    if user_input.lower() in ["exit", "quit"]:
        print("챗봇을 종료합니다.")
        break

    # 사용자 입력을 메시지 목록에 추가
    messages.append({"role": "user", "content": user_input})

    # 모델에게 메시지를 보내고 응답 받기
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.4  # 창의성(무작위성) 조절: 낮을수록 덜 창의적
    )

    # 응답에서 챗봇의 메시지 추출
    chatbot_reply = response.choices[0].message.content

    # 챗봇 응답 출력
    print("Chatbot:", chatbot_reply)

    # 챗봇의 응답도 메시지 목록에 추가 (대화 유지 목적)
    messages.append({"role": "assistant", "content": chatbot_reply})

# --- 아이디어 작성 ---
# 이 챗봇을 어디에 응용할 수 있을까요?
# 예: '~에 적용해 응용 해보고 싶다'
# 1. 특정 기관 단체에 대한 정보를 입력하고 그 기관에 맞는 챗봇을 만들어 보고 싶다.
# ex: 유치원 상담쳇봇:(원비 납부 방법을 알려줘),(4/15일 하늘반 일정을 알려줘),(오늘 유치원 식단을 알려주고 알러지유발 음식을 알려줘줘)