import streamlit as st

st.set_page_config(
    page_title="四代人格小宇宙测试",
    page_icon="✨",
    layout="centered"
)

# =========================
# 页面美化 CSS
# =========================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff1f7 0%, #f5f0ff 45%, #eef8ff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #ff5fa2;
        margin-bottom: 0.2rem;
    }

    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #6b5b75;
        margin-bottom: 1.2rem;
    }

    .notice {
        text-align: center;
        font-size: 0.82rem;
        color: #888;
        background: rgba(255, 255, 255, 0.68);
        padding: 10px 14px;
        border-radius: 999px;
        margin-bottom: 18px;
    }

    .question-card {
        background: rgba(255, 255, 255, 0.88);
        padding: 22px 22px 18px 22px;
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(255, 95, 162, 0.13);
        border: 1px solid rgba(255, 255, 255, 0.8);
        margin-top: 16px;
        margin-bottom: 18px;
    }

    .question-number {
        color: #ff5fa2;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .question-text {
        font-size: 1.25rem;
        font-weight: 800;
        color: #35303a;
        margin-bottom: 12px;
        line-height: 1.5;
    }

    .result-card {
        background: white;
        padding: 30px 20px;
        border-radius: 28px;
        text-align: center;
        box-shadow: 0 14px 38px rgba(255, 95, 162, 0.18);
        border: 2px solid #ffd2e6;
        margin-top: 24px;
    }

    .result-label {
        color: #999;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }

    .result-name {
        color: #ff4f9a;
        font-size: 2rem;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .result-type {
        color: #5d4a67;
        font-size: 1.25rem;
        font-weight: 700;
    }

    div.stButton > button {
        border-radius: 999px;
        border: none;
        background: linear-gradient(90deg, #ff6fab, #b983ff);
        color: white;
        font-weight: 800;
        padding: 0.7rem 1.2rem;
        box-shadow: 0 8px 20px rgba(255, 111, 171, 0.25);
    }

    div.stButton > button:hover {
        border: none;
        color: white;
        transform: translateY(-1px);
    }

    [data-testid="stRadio"] label {
        background: rgba(255, 255, 255, 0.72);
        padding: 9px 12px;
        border-radius: 14px;
        margin-bottom: 7px;
        border: 1px solid rgba(255, 190, 220, 0.55);
    }

    .footer-text {
        text-align: center;
        color: #999;
        font-size: 0.78rem;
        margin-top: 26px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 结果人物与类型
# =========================

members = {
    "杨博文": {"tag": "认真成长型"},
    "张桂源": {"tag": "热血冲刺型"},
    "陈奕恒": {"tag": "元气直球型"},
    "王橹杰": {"tag": "冷静观察型"},
    "左奇函": {"tag": "灵感表达型"},
    "陈浚铭": {"tag": "气氛开关型"},
    "张函瑞": {"tag": "反差甜酷型"},
    "陈思罕": {"tag": "清新潜力型"},
    "李煜东": {"tag": "安静蓄力型"},
    "杨涵博": {"tag": "松弛可爱型"},
    "官俊臣": {"tag": "稳定发光型"},
    "聂玮辰": {"tag": "潜力上升型"},
    "张奕然": {"tag": "清爽少年型"},
    "魏子宸": {"tag": "默默努力型"},
}

# =========================
# 测试题目与计分规则
# =========================

questions = [
    {
        "q": "如果突然被安排上台表演，你第一反应是？",
        "options": {
            "紧张归紧张，但马上进入状态": {"杨博文": 2, "官俊臣": 1},
            "先冷静复盘流程，不能出错": {"王橹杰": 2, "魏子宸": 1},
            "好刺激，直接冲！": {"张桂源": 2, "陈奕恒": 1},
            "先观察大家状态，再找自己的节奏": {"李煜东": 2, "陈思罕": 1},
        }
    },
    {
        "q": "在一个新集体里，你通常是？",
        "options": {
            "慢热，但熟了之后很有梗": {"张函瑞": 2, "李煜东": 1},
            "自带气氛，很快和大家玩起来": {"陈浚铭": 2, "杨涵博": 1},
            "安静但靠谱，关键时刻很稳": {"官俊臣": 2, "王橹杰": 1},
            "不一定说很多，但存在感很特别": {"左奇函": 2, "陈思罕": 1},
        }
    },
    {
        "q": "你更喜欢别人夸你什么？",
        "options": {
            "你真的很有舞台感": {"张桂源": 2, "陈奕恒": 1},
            "你很稳，很让人放心": {"官俊臣": 2, "杨博文": 1},
            "你很努力，看得出来一直在进步": {"杨博文": 2, "聂玮辰": 1},
            "你好有反差，越了解越有意思": {"张函瑞": 2, "左奇函": 1},
        }
    },
    {
        "q": "如果要拍一个短视频，你会选？",
        "options": {
            "高燃舞台混剪": {"张桂源": 2, "陈奕恒": 1},
            "搞笑日常 vlog": {"陈浚铭": 2, "杨涵博": 1},
            "治愈系慢节奏生活记录": {"张奕然": 2, "陈思罕": 1},
            "反差感变装/转场视频": {"张函瑞": 2, "左奇函": 1},
        }
    },
    {
        "q": "团队里突然冷场了，你会？",
        "options": {
            "主动抛梗，把气氛热起来": {"陈浚铭": 2, "杨涵博": 1},
            "观察一下，找合适时机接话": {"王橹杰": 2, "李煜东": 1},
            "不太抢话，但会用行动帮忙": {"官俊臣": 2, "魏子宸": 1},
            "用一个意想不到的方式破冰": {"左奇函": 2, "张函瑞": 1},
        }
    },
    {
        "q": "你做事情更像哪一种？",
        "options": {
            "目标明确，定了就认真练": {"杨博文": 2, "官俊臣": 1},
            "灵感来了就会很投入": {"左奇函": 2, "陈思罕": 1},
            "情绪到了，爆发力很强": {"张桂源": 2, "陈奕恒": 1},
            "慢慢来，但每一步都想做好": {"魏子宸": 2, "聂玮辰": 1},
        }
    },
    {
        "q": "朋友说你最大的魅力是？",
        "options": {
            "真诚感": {"陈奕恒": 2, "张奕然": 1},
            "少年感": {"张奕然": 2, "聂玮辰": 1},
            "反差感": {"张函瑞": 2, "左奇函": 1},
            "松弛感": {"杨涵博": 2, "陈浚铭": 1},
        }
    },
    {
        "q": "如果你是练习生，你最想挑战？",
        "options": {
            "唱跳舞台": {"张桂源": 2, "杨博文": 1},
            "纯 vocal 表演": {"张函瑞": 2, "陈思罕": 1},
            "搞笑综艺环节": {"陈浚铭": 2, "杨涵博": 1},
            "舞蹈/表现力舞台": {"左奇函": 2, "王橹杰": 1},
        }
    },
    {
        "q": "遇到压力时，你通常会？",
        "options": {
            "自己消化，然后继续努力": {"杨博文": 2, "魏子宸": 1},
            "找朋友聊一聊，缓一下": {"陈奕恒": 2, "杨涵博": 1},
            "用练习/忙碌转移注意力": {"张桂源": 2, "官俊臣": 1},
            "表面没事，心里疯狂复盘": {"王橹杰": 2, "李煜东": 1},
        }
    },
    {
        "q": "你的朋友圈风格更像？",
        "options": {
            "偶尔发，但每条都很有感觉": {"左奇函": 2, "张函瑞": 1},
            "日常碎片很多，很鲜活": {"陈奕恒": 2, "陈浚铭": 1},
            "认真记录成长和目标": {"杨博文": 2, "聂玮辰": 1},
            "梗图、表情包、快乐源泉": {"杨涵博": 2, "陈浚铭": 1},
        }
    },
    {
        "q": "如果要选一个练习室角色，你更像？",
        "options": {
            "默默练很多遍的细节控": {"魏子宸": 2, "杨博文": 1},
            "带大家一起嗨起来的气氛组": {"陈浚铭": 2, "陈奕恒": 1},
            "不说废话，直接指出问题的人": {"王橹杰": 2, "官俊臣": 1},
            "看起来安静，其实很有自己想法的人": {"李煜东": 2, "陈思罕": 1},
        }
    },
    {
        "q": "你最想拥有哪种出场氛围？",
        "options": {
            "一上场就很燃，像主角开大": {"张桂源": 2, "陈奕恒": 1},
            "干净清爽，越看越舒服": {"张奕然": 2, "陈思罕": 1},
            "稳稳的，不夸张但很可靠": {"官俊臣": 2, "魏子宸": 1},
            "很特别，有点神秘又有点抓人": {"左奇函": 2, "张函瑞": 1},
        }
    }
]

# =========================
# 初始化状态
# =========================

if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "show_result" not in st.session_state:
    st.session_state.show_result = False

# =========================
# 标题区
# =========================

st.markdown('<div class="main-title">✨ 四代人格小宇宙测试</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">不问你担谁，只测你和谁最同频</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="notice">粉丝自制娱乐测试｜结果仅代表气质匹配，不代表本人、公司或官方立场。</div>',
    unsafe_allow_html=True
)

# =========================
# 结果计算函数
# =========================

def calculate_result():
    scores = {name: 0 for name in members.keys()}

    for question_index, choice in st.session_state.answers.items():
        points = questions[question_index]["options"][choice]
        for name, score in points.items():
            scores[name] += score

    max_score = max(scores.values())
    top_members = [name for name, score in scores.items() if score == max_score]

    # 如果同分，取第一个
    result_name = top_members[0]
    result_type = members[result_name]["tag"]

    return result_name, result_type, scores

# =========================
# 主页面逻辑
# =========================

total_questions = len(questions)
current_page = st.session_state.page
answered_count = len(st.session_state.answers)

progress_value = answered_count / total_questions
st.progress(progress_value, text=f"答题进度：{answered_count}/{total_questions}")

if not st.session_state.show_result:
    item = questions[current_page]

    st.markdown(
        f"""
        <div class="question-card">
            <div class="question-number">第 {current_page + 1} 题 / 共 {total_questions} 题</div>
            <div class="question-text">{item["q"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    options = list(item["options"].keys())

    previous_answer = st.session_state.answers.get(current_page, None)
    index = options.index(previous_answer) if previous_answer in options else None

    choice = st.radio(
        "请选择一个最像你的答案：",
        options,
        index=index,
        key=f"radio_{current_page}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ 上一题", disabled=current_page == 0):
            st.session_state.page -= 1
            st.rerun()

    with col2:
        if current_page < total_questions - 1:
            if st.button("下一题 ➡️"):
                st.session_state.answers[current_page] = choice
                st.session_state.page += 1
                st.rerun()
        else:
            if st.button("生成我的结果 ✨"):
                st.session_state.answers[current_page] = choice

                if len(st.session_state.answers) < total_questions:
                    st.warning("还有题目没有完成哦。")
                else:
                    st.session_state.show_result = True
                    st.rerun()

else:
    result_name, result_type, scores = calculate_result()

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">你的四代人格结果是</div>
            <div class="result-name">{result_name}</div>
            <div class="result-type">类型：{result_type}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("再测一次 🔄"):
            st.session_state.page = 0
            st.session_state.answers = {}
            st.session_state.show_result = False
            st.rerun()

    with col2:
        with st.expander("查看分数明细"):
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for name, score in sorted_scores:
                st.write(f"{name}：{score} 分")

st.markdown(
    '<div class="footer-text">✨ Made for fun｜四代人格小宇宙测试</div>',
    unsafe_allow_html=True
)
