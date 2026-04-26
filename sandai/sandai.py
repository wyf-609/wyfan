import streamlit as st

st.set_page_config(
    page_title="三代人格同频测试",
    page_icon="🎤",
    layout="centered"
)

# =========================
# 页面美化 CSS
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5f8 0%, #f7f1ff 48%, #eef7ff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 2.25rem;
        font-weight: 800;
        color: #ff5f9e;
        margin-bottom: 0.2rem;
    }

    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #6d6278;
        margin-bottom: 1rem;
    }

    .notice {
        text-align: center;
        font-size: 0.84rem;
        color: #7f7f7f;
        background: rgba(255,255,255,0.75);
        padding: 10px 16px;
        border-radius: 999px;
        margin-bottom: 18px;
    }

    .question-card {
        background: rgba(255,255,255,0.9);
        padding: 22px 22px 18px 22px;
        border-radius: 24px;
        box-shadow: 0 12px 28px rgba(255, 95, 158, 0.12);
        border: 1px solid rgba(255,255,255,0.85);
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .question-number {
        color: #ff5f9e;
        font-size: 0.92rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .question-text {
        font-size: 1.2rem;
        font-weight: 800;
        color: #36323a;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    .result-card {
        background: white;
        padding: 32px 24px;
        border-radius: 28px;
        text-align: center;
        box-shadow: 0 14px 34px rgba(255, 95, 158, 0.18);
        border: 2px solid #ffd3e5;
        margin-top: 20px;
    }

    .result-small {
        color: #949494;
        font-size: 0.94rem;
        margin-bottom: 8px;
    }

    .result-name {
        color: #ff4e98;
        font-size: 2rem;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .result-type {
        color: #5f4d68;
        font-size: 1.2rem;
        font-weight: 700;
    }

    div.stButton > button {
        border-radius: 999px;
        border: none;
        background: linear-gradient(90deg, #ff74b1, #b889ff);
        color: white;
        font-weight: 800;
        padding: 0.72rem 1.2rem;
        box-shadow: 0 8px 20px rgba(255, 116, 177, 0.25);
    }

    div.stButton > button:hover {
        border: none;
        color: white;
        transform: translateY(-1px);
    }

    [data-testid="stRadio"] label {
        background: rgba(255,255,255,0.78);
        padding: 9px 12px;
        border-radius: 14px;
        margin-bottom: 8px;
        border: 1px solid rgba(255, 195, 222, 0.6);
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
# 成员结果池
# =========================
members = {
    "朱志鑫": {"tag": "苏新皓老公"},
    "张泽禹": {"tag": "大芒果"},
    "张极": {"tag": "铲棍的宠物猪"},
    "左航": {"tag": "邓佳鑫老公"},
    "苏新皓": {"tag": "22x老婆"},
    "童禹坤": {"tag": "精神小伙型"},
    "邓佳鑫": {"tag": "左航老公"},
    "穆祉丞": {"tag": "王橹杰老公"},
    "张子墨": {"tag": "如听仙乐耳暂明"},
    "黄朔": {"tag": "抽象型"},
    "张峻豪": {"tag": "异性恋型"},
    "余宇涵": {"tag": "出道半天即退团型"},
}

# =========================
# 题库（根据公开舞台气质做的娱乐向匹配）
# =========================
questions = [
    {
        "q": "如果突然要你在众人面前展示自己，你会？",
        "options": {
            "先稳住场面，尽量让自己表现得可靠一点": {"朱志鑫": 2, "苏新皓": 1},
            "有点紧张，但会用真诚和温柔打动别人": {"张泽禹": 2, "邓佳鑫": 1},
            "不一定按套路来，但会想办法做出个人特色": {"左航": 2, "张极": 1},
            "越到这种时候越想证明自己": {"张峻豪": 2, "余宇涵": 1},
        }
    },
    {
        "q": "朋友最常评价你的点是？",
        "options": {
            "稳，有主心骨": {"朱志鑫": 2, "苏新皓": 1},
            "好相处，很有感染力": {"张泽禹": 2, "童禹坤": 1},
            "有自己的想法，很明特别": {"左航": 2, "张子墨": 1},
            "少年感强，状态很鲜活": {"穆祉丞": 2, "黄朔": 1},
        }
    },
    {
        "q": "如果你在团队里，你更像哪种角色？",
        "options": {
            "默默扛住压力、关键时刻稳住局面的人": {"朱志鑫": 2, "余宇涵": 1},
            "把气氛带活、让大家放松的人": {"童禹坤": 2, "穆祉丞": 1},
            "对细节要求高、执行力很强的人": {"苏新皓": 2, "张峻豪": 1},
            "负责提供灵感和新鲜想法的人": {"左航": 2, "张子墨": 1},
        }
    },
    {
        "q": "你更想被别人夸哪一点？",
        "options": {
            "你很有舞台气场": {"朱志鑫": 2, "童禹坤": 1},
            "你很温柔，也很有表达力": {"张泽禹": 2, "邓佳鑫": 1},
            "你很有风格，很抓人": {"张极": 2, "左航": 1},
            "你很努力，而且在不断变强": {"苏新皓": 2, "余宇涵": 1},
        }
    },
    {
        "q": "如果要做一个个人作品，你会更偏向？",
        "options": {
            "完成度高、标准在线、尽量不出错": {"苏新皓": 2, "朱志鑫": 1},
            "带情绪、有故事感、可以打动人": {"邓佳鑫": 2, "张泽禹": 1},
            "最好有自己的风格和创意": {"左航": 2, "张子墨": 1},
            "想让别人一下子记住我": {"张极": 2, "张峻豪": 1},
        }
    },
    {
        "q": "面对压力时，你更像？",
        "options": {
            "先扛着，再慢慢处理": {"朱志鑫": 2, "余宇涵": 1},
            "会自己消化情绪，但希望作品能表达出来": {"邓佳鑫": 2, "张子墨": 1},
            "压力越大，越会逼自己练得更好": {"苏新皓": 2, "张峻豪": 1},
            "会想办法调整气氛，让自己重新恢复状态": {"童禹坤": 2, "穆祉丞": 1},
        }
    },
    {
        "q": "哪种舞台氛围最吸引你？",
        "options": {
            "全场压住、气场很强的那种": {"朱志鑫": 2, "苏新皓": 1},
            "温柔但很有情绪层次的那种": {"张泽禹": 2, "邓佳鑫": 1},
            "特别、有辨识度、有个人色彩的那种": {"张极": 2, "左航": 1},
            "热烈、鲜活、有冲劲的那种": {"童禹坤": 2, "黄朔": 1},
        }
    },
    {
        "q": "如果别人第一次见你，最可能留下什么印象？",
        "options": {
            "看起来挺稳、挺有分寸": {"朱志鑫": 2, "苏新皓": 1},
            "看起来很舒服，很容易让人有好感": {"张泽禹": 2, "张极": 1},
            "有点特别，不是很普通的那种感觉": {"左航": 2, "张子墨": 1},
            "带一点少年冲劲和成长感": {"黄朔": 2, "余宇涵": 1},
        }
    },
    {
        "q": "如果你在综艺或团体互动里，你会？",
        "options": {
            "不一定话最多，但会在关键时刻接住场面": {"朱志鑫": 2, "余宇涵": 1},
            "自然聊天、制造轻松感": {"张泽禹": 2, "童禹坤": 1},
            "偶尔来点意想不到的梗和想法": {"左航": 2, "穆祉丞": 1},
            "让大家看到我有趣又有目标的一面": {"张峻豪": 2, "张极": 1},
        }
    },
    {
        "q": "你平时做事更像哪种节奏？",
        "options": {
            "先定目标，再稳定推进": {"苏新皓": 2, "朱志鑫": 1},
            "靠感觉和灵感驱动，但想法很多": {"张子墨": 2, "左航": 1},
            "外表轻松，其实很在意最终效果": {"张极": 2, "张泽禹": 1},
            "想不断突破自己，越练越上头": {"余宇涵": 2, "张峻豪": 1},
        }
    },
    {
        "q": "你会把哪种特质视为自己的魅力？",
        "options": {
            "有担当，能给人安全感": {"朱志鑫": 2, "苏新皓": 1},
            "细腻真诚，有共情力": {"邓佳鑫": 2, "张泽禹": 1},
            "新鲜感和独特感": {"左航": 2, "张极": 1},
            "元气、灵动和少年感": {"穆祉丞": 2, "黄朔": 1},
        }
    },
    {
        "q": "如果一定要选一个成长方向，你会选？",
        "options": {
            "成为更能扛事、更有带领感的人": {"朱志鑫": 2, "余宇涵": 1},
            "成为更会表达、更能触动别人的人": {"张泽禹": 2, "邓佳鑫": 1},
            "成为更有个人作品和个人风格的人": {"张子墨": 2, "左航": 1},
            "成为更有野心、更有突破感的人": {"张峻豪": 2, "黄朔": 1},
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
# 标题
# =========================
st.markdown('<div class="main-title">🎤 三代人格同频测试</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">测测你和哪位三代成员的公开舞台气质最同频</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="notice">娱乐向测试｜基于公开舞台与作品气质做匹配，不代表真人私下真实性格或官方立场。</div>',
    unsafe_allow_html=True
)

# =========================
# 计算结果
# =========================
def calculate_result():
    scores = {name: 0 for name in members.keys()}
    for question_index, choice in st.session_state.answers.items():
        point_map = questions[question_index]["options"][choice]
        for name, score in point_map.items():
            scores[name] += score

    max_score = max(scores.values())
    top_members = [name for name, score in scores.items() if score == max_score]
    result_name = top_members[0]
    result_type = members[result_name]["tag"]
    return result_name, result_type, scores

# =========================
# 主逻辑
# =========================
total_questions = len(questions)
current_page = st.session_state.page
answered_count = len(st.session_state.answers)

progress = answered_count / total_questions
st.progress(progress, text=f"答题进度：{answered_count}/{total_questions}")

if not st.session_state.show_result:
    current_item = questions[current_page]

    st.markdown(
        f"""
        <div class="question-card">
            <div class="question-number">第 {current_page + 1} 题 / 共 {total_questions} 题</div>
            <div class="question-text">{current_item["q"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    options = list(current_item["options"].keys())
    previous_answer = st.session_state.answers.get(current_page, None)
    index = options.index(previous_answer) if previous_answer in options else 0

    choice = st.radio(
        "请选择一个最符合你的答案：",
        options,
        index=index,
        key=f"radio_{current_page}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ 上一题", disabled=current_page == 0):
            st.session_state.page -= 1
            st.rerun()

    with col2:
        if current_page < total_questions - 1:
            if st.button("下一题 ➜"):
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
            <div class="result-small">你的测试结果是</div>
            <div class="result-name">{result_name}</div>
            <div class="result-type">类型：{result_type}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

    with st.expander("查看分数明细"):
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_scores:
            st.write(f"{name}：{score} 分")

    if st.button("再测一次 🔄"):
        st.session_state.page = 0
        st.session_state.answers = {}
        st.session_state.show_result = False
        st.rerun()

st.markdown(
    '<div class="footer-text">✨ Made for fun｜三代人格同频测试</div>',
    unsafe_allow_html=True
)