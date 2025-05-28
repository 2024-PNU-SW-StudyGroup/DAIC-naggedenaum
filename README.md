# DAIC-내께더나음

<br>

```md
# [ToTime]

## 📌 개요
ToTime, 문서 기반 일정 추출 및 워크시트 자동화 플랫폼
PDF, PPT, 이미지 등의 다양한 형태의 문서를 Parsing한 후, 시간을 다루는 형태의 데이터를 추출하여 사용자가 원하는 형태의 워크시트를 생성, 그룹 단위의 프로젝트나 협업을 돕는 서비스입니다.

## 🎯 문제 정의 및 기대 효과
문제 - 대학생들의 팀 단위의 활동부터 대학병원에서의 회진 일정, 단체에서의 프로젝트 진행상황까지 우리는 일정이 포함된 다양한 문서들을 주고 받으며, 업무를 진행하게 됩니다.
이때, 일정을 정확히 파악하지 못해 차질이 생기게 되는 문제는 우리를 항상 따라다니고, 일정 누락이나 업무 중복 등의 문제는 협업을 진행할 때에 감수해야만 하는 사항이 되어있습니다.
또한, 매일 쏟아지는 업무와 문서들 속에서 정확히 일정을 파악하고, 업무환경을 조성하는 것은 그것 자체로 피곤하고 지루한 업무가 되어버립니다.

저희는, 이러한 비효율성과 불편을 인지하였고, "충분히 해결할 수 있지 않을까? " 라는 결론에 도달하게 되었습니다!
문서의 일정과 내용을 Document Parse를 이용해 정리하고, 내용을 기반으로 사용자에게 Worksheet를 제공하는 ToTime 서비스를 통해, 사용자는 자신의 업무에 온전히 집중할 수 있게 됩니다!

저희의 서비스는 특정 사용자나, 단체에 국한되어 있지 않습니다.
사회 전반의 보펀적 사용자에게 "일정 정리"라는 업무의 한 단계를 대신 부담하여 주며, 실무 상황에서 발생하는 갈등을 편리하게 해결 해 줄 수 있습니다.
이를 통해 사용자에게는 편의를, 단체에게는 갈등 해소라는 가치를 제공한다고 설명드릴 수 있습니다.
 

## ✅ Upstage API 활용
Upstage Document Parse: 년도, 날짜, 시간 등의 시간 데이터를 포함하는 문서를 파싱하는 데에 이용됨. 높은 정확도로 문서 내의 데이터를 가져오고, 이를 기반으로 worksheet를 제공함.

Solar Embedding: Upstage Document Parse API를 이용해 얻은 문서의 내용을 SOLAR Embedding API를 이용해 임베딩 한 후, 문서 내용 전반의 중요도를 수치화하는 AI 모델을 제작.
이를 기반으로 완성된 WorkSheet를 중요도에 따라 정렬하는 기능, 중요도를 보여주는 기능을 사용자에게 제공함.


## 🚀 주요 기능
| 주요 기능                  | 설명                                                                 |
|---------------------------|----------------------------------------------------------------------|
| 문서 파싱                 | PDF, PPT, 이미지 문서에서 일정/시간/마감일 정보 자동 추출                     |
| 타임라인 생성              | 자동으로 추출된 일정 정보를 시각화 (클릭 시 상세 링크 포함)                          |
| 워크시트 생성              | 사용자가 제공한 일정 정보, 문서 내용을 기반으로 업무 리스트, 체크리스트, 일정표 등 자동 구성      |
| 중요도/우선순위 정렬        | Solar embedding api 기반 중요도 분석을 통해 업무 중요도/우선순위에 따른 자동 정렬        |
| 외부 연동                  | 완성된 WorkSheet를 Notion, Google Calendar와 연동하여 실무에 직접 활용 가능                             |
| 개인정보 보호 기능 (계획)    | Differential Privacy 적용, 조직별 인트라넷 기반 서비스 제공 예정                     |

## 🖼️ 데모
> 스크린샷이나 데모 영상(GIF 또는 구글 드라이브 링크 등)을 포함해주세요.
- 예시:  
  ![데모 스크린샷](./assets/demo.png)

## 웹 시나리오
| 단계 | 내용                                  |
| -- | ----------------------------------- |
| 1  | 사용자가 문서를 업로드 (PDF, PPT, 이미지 등 포함)   |
| 2  | Upstage 문서 파싱 API로 일정, 시간, 마감일 등 추출 |
| 3  | LLM 및 embedding을 통해 중요도, 우선순위 분석    |
| 4  | 사용자가 선택한 템플릿에 맞춰 워크시트 자동 생성         |
| 5  | 워크시트에는 타임라인, 업무 요약, 체크리스트 포함        |
| 6  | 선택적으로 Notion, Google Calendar 등과 연동 |
| 7  | 결과는 실제 실무자가 바로 업무에 적용 가능한 형태로 출력    |

## 🔬 기술 구현 요약
AI 모델: 임베딩 이용
문서 내의 요소들을 API를 이용해 임베딩 한 후, 중요도를 퍼센테이지로 측정하는 모델 적용

## 🧰 기술 스택 및 시스템 아키텍처
> 사용한 언어 및 프레임워크를 작성하고 시스템 아키텍처 이미지를 첨부해주세요.

## 🔧 설치 및 사용 방법
> 리포지토리 클론 이후 application을 실행할 수 있는 명령어를 작성해주세요.
> 실행할 수 있는 환경이 제한되어 있는 경우, 이곳에 배포 환경을 알려주세요.
> 실제로 배포하고 있다면, 배포 중인 사이트를 알려주셔도 됩니다.
> 아래는 예시입니다.

\```bash
git clone https://github.com/your-username/project-name.git
cd project-name
pip install -r requirements.txt
\```

## 📁 프로젝트 구조
> 프로젝트 루트 디렉토리에서 주요 파일 및 폴더의 역할 및 목적을 작성해주세요.
> 필요없다고 생각되는 부분은 생략하셔도 됩니다.
> 아래는 예시입니다.

\```bash
project-name/
├── README.md               # 프로젝트 설명서
├── app.py                  # 애플리케이션 메인 파일
├── src/                    # 핵심 로직, 파이프라인, 유틸리티 등
│   ├── model.py
│   └── utils.py
├── models/                 # 모델 체크포인트 및 학습된 가중치
├── assets/                 # 이미지, 동영상, 샘플 출력 등
├── data/                   # 샘플 입력/출력 데이터
└── tests/                  # 테스트 코드
\```

## 🧑‍🤝‍🧑 팀원 소개

| 이름  | 역할          | GitHub                                       |
| --- | ----------- | -------------------------------------------- |
| 최지훈 | 팀장 / 모델 개발 | (https://github.com/zihoonman)     |
| 이현우 | 웹 개발 | (https://github.com/carsleeper)     |
| 이서준 | 웹 개발 | (https://github.com/Leeseojun035) |

## 💡 참고 자료 및 아이디어 출처 (Optional)

* [Upstage Document Parse](https://www.upstage.ai/products/document-parse)
* [Upstage Building end-to-end RAG system using Solar LLM and MongoDB Atlas](https://www.upstage.ai/blog/en/building-rag-system-using-solar-llm-and-mongodb-atlas)
* [Upstage Building end-to-end RAG system using Solar LLM and MongoDB Atlas](https://www.upstage.ai/blog/en/building-rag-system-using-solar-llm-and-mongodb-atlas)

```

 

