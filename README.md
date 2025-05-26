# DAIC-Template
> **PNU x Upstage: DOCUMENT AI CHALLENGE 리포지토리 템플릿입니다. 아래 마크다운을 프로젝트 리포지토리 형식에 맞춰서 리드미를 작성해주시면 됩니다.**

* `>`로 작성된 부분은 없애고 작성해주시면 됩니다.
* 해당 리포지토리를 fork해서 그대로 사용해주시면 됩니다. fork시 리포지토리 이름은 `DAIC-[TEAM_NAME]`으로 해주세요.
* 제출 마감일 이전까지 GitHub 리포지토리 main 브랜치에 커밋이 반영되어 있어야 유효 제출로 간주됩니다.
* README.md는 심사 기준과 연결된 내용을 의식하여 작성하는 것이 중요합니다 (예: API 활용, 문제 해결 효과 등).

<br>

```md
# [DocScheduler]

## 📌 개요
> 프로젝트에 대한 간단한 설명을 작성해주세요.
DocScheduler, 문서 기반 일정 추출 및 워크시트 자동화 플랫폼

## 🎯 문제 정의 및 기대 효과
> '어떤 문제를 해결하고자 했는가?', '해당 문제의 중요성과 필요성은 무엇인가?', '이 솔루션이 사용자 혹은 조직에 어떤 가치를 줄 수 있는가?' 등
> 해당하는 내용을 작성해주세요.

## ✅ Upstage API 활용
> 적용한 기술이나 Upstage API를 어떻게 적용했는지를 작성해주시면 됩니다.

## 🚀 주요 기능
> 프로젝트의 주요 기능을 구체적으로 설명해주세요. Application 내 구현된 부분을 이미지로 함께 첨부하셔도 좋습니다.
> 창의적인 접근 방식이나 기존 방법과의 차별점을 서술해주시면 좋습니다.
사용 시나리오 (대학 위주의 실제 활용 예시),
페이지 구성,
최대한 간결하게 구성

이미지와 최소한의 텍스트로 직관적 정보 제공

파싱 API 활용,
문서, PDF, PPT 등에서 일정, 시간, Deadline 정보 자동 추출

이미지를 포함한 문서도 처리 가능

SOLAR AI 활용 - 사용자에게 묻기,
사용자가 선호하는 Worksheet 템플릿 선택 가능

템플릿은 3개 정도로 시작해서 고도화 예정

핵심 기능: GPT IDEA,
문서의 내용을 임베딩하여 문맥을 이해하고, 우선순위 자동 판단

모델을 활용하여 중요도 기반으로 Worksheet를 구성

Worksheet 제공 페이지,
완성된 Worksheet 제공 - (카카오톡, 링크 등으로 공유 가능하도록 하기)

예시 UI: 타임라인 시각화 (클릭 시 상세 내용 링크 연결)

업무 내용 요약

시간 순서

중요도 태그 정리 등

선택사항,
Notion, Google Calendar 등과 연동 기능 제공

병원/조직 내 실무 업무에 실제 적용 용이하도록 구성

추가 개발 요소,
문서 내 민감 정보 보호를 위한 Differential Privacy 적용

회사/기관 내 인트라넷 기반 개인화된 서비스 제공 고려 
UI를 Grok(Gemini Advanced) 스타일로 구성하고자 한다면, 다음과 같은 방향을 추천합니다:

전체 화면 기반의 간결한 UI

좌측 문서 업로드 영역 / 우측 결과 실시간 반영 (WYSIWYG)

워크시트 프리뷰는 타임라인 + 리스트 뷰 전환 가능

선택형 템플릿과 자동 완성된 워크시트의 명확한 구분

- ✨ 기능 1: 핵심 기능 설명
  - 이로 인한 장점
- ✨ 기능 2: 또 다른 주요 기능 설명

## 🖼️ 데모
> 스크린샷이나 데모 영상(GIF 또는 구글 드라이브 링크 등)을 포함해주세요.
- 예시:  
  ![데모 스크린샷](./assets/demo.png)

## 🔬 기술 구현 요약
> 사용한 AI 모델이나 파이프라인, 적용 기술을 작성해주세요.

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
> 각 팀원 소개 및 역할을 작성해주세요.
> 아래는 예시이고 자유롭게 작성해주시면 됩니다.

| 이름  | 역할          | GitHub                                       |
| --- | ----------- | -------------------------------------------- |
| 개발자1 | 팀장 / 백엔드 개발 | [@developer1](https://github.com/developer1)     |
| 개발자2 | 모델 개발       | [@developer2](https://github.com/developer2)     |
| 디자인1 | 디자인    | [@designer1](https://github.com/designer1) |

## 💡 참고 자료 및 아이디어 출처 (Optional)
> 프로젝트를 개발하면서 참고했던 논문 및 기타 문헌이 있으시다면 첨부해주세요.
> 아래는 예시입니다.

* [Upstage Document Parse](https://www.upstage.ai/products/document-parse)
* [Upstage Building end-to-end RAG system using Solar LLM and MongoDB Atlas](https://www.upstage.ai/blog/en/building-rag-system-using-solar-llm-and-mongodb-atlas)

```

 

