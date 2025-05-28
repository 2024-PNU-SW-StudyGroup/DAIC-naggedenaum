# -------------------------------------------------------------
# Doc Scheduler – Streamlit 앱 (single‑file)
# -------------------------------------------------------------
# 주요 기능
# 1) 문서/이미지 업로드 → Upstage Document Parse API 로 원문 추출
# 2) 일정·마감일 키워드 파싱 → Task 리스트 생성
# 3) 3 종 Worksheet 템플릿(타임라인·리스트·칸반) 중 하나 선택해 시각화
# 4) 결과 CSV / Markdown 다운로드 & 재사용 가능
# -------------------------------------------------------------
# 요구 라이브러리 (가상환경에서 설치 권장)
#   pip install streamlit requests python-dotenv pandas plotly python-dateutil
# -------------------------------------------------------------

import os
import re
import uuid
from datetime import datetime, timedelta
from typing import List, Dict

import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from dateutil import parser as dtparse
from dotenv import load_dotenv

# ─────────────────────────────── 환경 변수 로드
load_dotenv()
UPSTAGE_API_KEY = os.getenv("UPSTAGE_API_KEY", "")
if not UPSTAGE_API_KEY:
    st.error("환경 변수 UPSTAGE_API_KEY 가 설정되지 않았습니다. .env 파일을 확인하세요.")
    st.stop()

UPSTAGE_PARSE_URL = "https://api.upstage.ai/v1/document-ai/document-parse"
HEADERS = {"Authorization": f"Bearer {UPSTAGE_API_KEY}"}

# ─────────────────────────────── UI 설정
st.set_page_config(page_title="Doc Scheduler", layout="wide")
st.title("📄 Doc Scheduler – 문서 기반 일정 워크시트")
st.markdown("업로드한 PDF/HWP/PPTX/이미지에서 **일정·마감일**을 추출해 원하는 형식의 워크시트를 바로 만듭니다.")

# 사이드바 – 업로드 & 옵션
with st.sidebar:
    st.header("1️⃣ 문서 업로드")
    files = st.file_uploader(
        "PDF · HWP · DOCX · PPTX · 이미지(JPG/PNG) 다중 선택 지원",
        accept_multiple_files=True,
    )

    st.header("2️⃣ 파싱 & 워크시트 옵션")
    output_fmt = st.selectbox("Upstage 출력 형식", ["text", "markdown", "html"])
    split_unit = st.selectbox("Split 단위", ["none", "page", "element"])

    st.divider()
    ws_template = st.radio(
        "✏️ 워크시트 템플릿", ["Timeline (Gantt)", "Checklist", "Kanban"],
        help="SOLAR AI 선호도는 미지원 – 기본 3 종 템플릿 제공"
    )

    run_button = st.button("🚀 파싱 실행", disabled=not files)

# ─────────────────────────────── 헬퍼 함수

def call_upstage(file_name: str, file_bytes: bytes) -> str:
    """Upstage Document Parse API 호출 → 원문 텍스트 반환"""
    resp = requests.post(
        UPSTAGE_PARSE_URL,
        headers=HEADERS,
        timeout=120,
        files={"document": (file_name, file_bytes)},
        data={
            "output_format": output_fmt,
            "split": split_unit,
            "ocr": "auto",
        },
    )
    resp.raise_for_status()
    # content 구조: {"content": {"text"|"html"|"markdown": "..."}}
    return resp.json()["content"][output_fmt]


def extract_tasks(text: str) -> List[Dict]:
    """텍스트에서 (날짜·시간) 패턴을 찾아 Task 리스트로 단순 추출.
    규칙 (heuristic)
      • YYYY-MM-DD, YYYY/MM/DD, MM/DD, MM-DD, DD일 등 날짜 패턴
      • 같은 줄/앞뒤 30자 이내 문장을 제목으로 간주
    """
    # ① 날짜 정규식 패턴 모음
    date_patterns = [
        r"\d{4}[./-]\d{1,2}[./-]\d{1,2}",     # 2025-05-28 / 2025.05.28 / 2025/05/28
        r"\d{1,2}[./-]\d{1,2}",               # 05-28 / 05/28 / 5.28
        r"\d{1,2}일",                          # 28일
    ]
    regex = re.compile("|".join(date_patterns))

    tasks = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = regex.search(line)
        if not m:
            continue
        date_str = m.group()
        try:
            # dateutil parse – 년도 생략 시 올해로 가정
            dt = dtparse.parse(date_str, default=datetime.today())
            title = line.replace(date_str, "").strip(" -:·.\u2022") or "무제"
            tasks.append({
                "Task": title,
                "Start": dt.date(),
                "Finish": (dt + timedelta(hours=1)).date(),  # Finish = Start (+1 day 시 표시용)
                "Deadline": dt.date(),
            })
        except (ValueError, OverflowError):
            continue
    return tasks


def render_timeline(df: pd.DataFrame):
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
    fig.update_yaxes(autorange="reversed")  # earliest at top
    st.plotly_chart(fig, use_container_width=True)


def render_checklist(df: pd.DataFrame):
    st.markdown("### ✔️ Checklist")
    for i, row in df.iterrows():
        st.checkbox(f"{row['Deadline']} – {row['Task']}", key=f"chk_{i}")


def render_kanban(df: pd.DataFrame):
    st.markdown("### 🗂️ Kanban (Board 단순 구현)")
    cols = st.columns(3)
    for idx, (_, row) in enumerate(df.iterrows()):
        with cols[idx % 3]:
            st.info(f"**{row['Task']}**\n\n📅 {row['Deadline']}")


def worksheet_view(df: pd.DataFrame):
    if ws_template == "Timeline (Gantt)":
        render_timeline(df)
    elif ws_template == "Checklist":
        render_checklist(df)
    else:
        render_kanban(df)

    st.download_button(
        "📥 CSV 다운로드",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"worksheet_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
    )
    st.download_button(
        "📥 Markdown 다운로드",
        data=df.to_markdown(index=False).encode(),
        file_name="worksheet.md",
        mime="text/markdown",
    )

# ─────────────────────────────── 실행 로직
if run_button and files:
    all_tasks: List[Dict] = []

    for f in files:
        with st.spinner(f"Upstage 파싱 중…  ({f.name})"):
            try:
                parsed_text = call_upstage(f.name, f.getvalue())
            except Exception as e:
                st.error(f"{f.name}: API 호출 실패 – {e}")
                continue

        # 추출
        tasks = extract_tasks(parsed_text)
        if not tasks:
            st.warning(f"❔ {f.name} 에서 일정 패턴을 찾지 못했습니다.")
            continue
        st.success(f"✅ {f.name} → {len(tasks)} 건 추출")
        all_tasks.extend(tasks)

    if all_tasks:
        st.divider()
        st.header("3️⃣ 워크시트 결과")
        df_tasks = pd.DataFrame(all_tasks)
        worksheet_view(df_tasks)
    else:
        st.error("추출된 일정 데이터가 없습니다. 패턴(날짜·시간) 포함 여부를 확인하세요.")

# ─────────────────────────────── 푸터
with st.expander("ℹ️ 앱 정보 / 향후 로드맵"):
    st.markdown(
        "* SOLAR AI 선호 템플릿 추천, Notion/Google Calendar 연동, Diff‑Privacy 강화 등은 로드맵에 포함되어 있습니다."\
    )
