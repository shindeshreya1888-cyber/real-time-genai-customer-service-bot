
import streamlit as st

from src.multimodal_rag import ask_multimodal_rag
from src.conversation_memory import ConversationMemory
from src.rag import ask_rag
from src.scheduler import start_scheduler
from src.medical_rag import ask_medical
from src.research_assistant import search_research_papers
from src.paper_summarizer import summarize_paper


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NovaAssist - AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# START KNOWLEDGE-BASE SCHEDULER
# ============================================================

try:
    start_scheduler()
except Exception as error:
    print(f"Scheduler could not start: {error}")


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        margin-top: 15px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .card {
        background-color: #111827;
        border: 1px solid #263244;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 600;
    }

    .card-text {
        color: #9ca3af;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_memory" not in st.session_state:
    st.session_state.conversation_memory = ConversationMemory()

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

if "assistant_mode" not in st.session_state:
    st.session_state.assistant_mode = "Customer Support"


# ============================================================
# SIDEBAR AND ASSISTANT SELECTION
# ============================================================

with st.sidebar:
    st.title("🤖 NovaAssist")
    st.caption("Your Multi-Mode AI Assistant")

    st.success("Application Ready")
    st.divider()

    selected_mode = st.selectbox(
        "Choose an Assistant",
        [
            "Customer Support",
            "Medical Q&A",
            "Research Assistant"
        ],
        index=[
            "Customer Support",
            "Medical Q&A",
            "Research Assistant"
        ].index(st.session_state.assistant_mode)
    )

    # Clear old chat when the user changes assistants.
    if selected_mode != st.session_state.assistant_mode:
        st.session_state.assistant_mode = selected_mode
        st.session_state.messages = []
        st.session_state.conversation_memory.clear()
        st.session_state.pending_question = None

    st.divider()

    if selected_mode == "Customer Support":
        st.subheader("📚 Knowledge Base")
        st.write("• Customer service information")
        st.write("• Shipping updates")
        st.write("• Refund and return policies")
        st.write("• Order and payment information")

        st.divider()
        st.subheader("⚙️ Technologies")
        st.write("• Python")
        st.write("• Gemini")
        st.write("• LangChain and RAG")
        st.write("• ChromaDB")
        st.write("• APScheduler")
        st.write("• Streamlit")

    elif selected_mode == "Medical Q&A":
        st.subheader("🩺 Medical Knowledge")
        st.write("• MedQuAD question-answer dataset")
        st.write("• Medical information retrieval")
        st.write("• Disease detection")
        st.write("• Symptom detection")
        st.write("• Treatment-term detection")

        st.caption(
            "For educational information only. "
            "This assistant does not diagnose medical conditions."
        )

    else:
        st.subheader("📄 Research Knowledge")
        st.write("• arXiv research-paper search")
        st.write("• Paper abstracts and authors")
        st.write("• Extractive summaries")
        st.write("• Links to original papers")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.conversation_memory.clear()
        st.session_state.pending_question = None
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 NovaAssist</div>',
    unsafe_allow_html=True
)

if selected_mode == "Customer Support":
    subtitle = (
        "AI-powered customer support using "
        "Retrieval-Augmented Generation (RAG)"
    )
elif selected_mode == "Medical Q&A":
    subtitle = (
        "Retrieve educational medical information "
        "from the MedQuAD dataset"
    )
else:
    subtitle = (
        "Discover research papers and explore "
        "their abstracts and summaries"
    )

st.markdown(
    f'<div class="subtitle">{subtitle}</div>',
    unsafe_allow_html=True
)


# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3 = st.columns(3)

if selected_mode == "Customer Support":
    features = [
        (
            "🧠 RAG-Powered",
            "Retrieves relevant knowledge before generating answers."
        ),
        (
            "📚 Dynamic Knowledge",
            "Supports updating the customer-service knowledge base."
        ),
        (
            "🖼️ Image Support",
            "Allows users to submit an image with a question."
        )
    ]

elif selected_mode == "Medical Q&A":
    features = [
        (
            "🩺 Medical Retrieval",
            "Finds related questions and answers in MedQuAD."
        ),
        (
            "🔍 Entity Detection",
            "Identifies supported disease, symptom and treatment terms."
        ),
        (
            "📖 Educational Information",
            "Displays retrieved information with a medical disclaimer."
        )
    ]

else:
    features = [
        (
            "🔎 Paper Search",
            "Searches arXiv for relevant research papers."
        ),
        (
            "📝 Abstract Summaries",
            "Creates a short extractive summary of each abstract."
        ),
        (
            "🔗 Paper Links",
            "Provides links to the original research papers."
        )
    ]

for column, feature in zip([col1, col2, col3], features):
    with column:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">{feature[0]}</div>
                <div class="card-text">{feature[1]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SAMPLE QUESTIONS
# ============================================================

st.subheader("💡 Try asking")

if selected_mode == "Customer Support":
    sample_questions = [
        "How can I track my order?",
        "What is the refund policy?",
        "How long does shipping take?"
    ]

elif selected_mode == "Medical Q&A":
    sample_questions = [
        "What are the symptoms of asthma?",
        "Who is at risk for diabetes?",
        "What is hypertension?"
    ]

else:
    sample_questions = [
        "machine learning",
        "large language models",
        "computer vision"
    ]

sample_columns = st.columns(3)

for index, question in enumerate(sample_questions):
    with sample_columns[index]:
        if st.button(question, use_container_width=True):
            st.session_state.pending_question = question
            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# IMAGE UPLOAD - CUSTOMER SUPPORT ONLY
# ============================================================

uploaded_image = None

if selected_mode == "Customer Support":
    uploaded_image = st.file_uploader(
        "📷 Upload an image (optional)",
        type=["png", "jpg", "jpeg"],
        help="Upload an image related to your customer-support question."
    )

    if uploaded_image is not None:
        st.image(
            uploaded_image,
            caption="Uploaded image",
            width=300
        )


# ============================================================
# CHAT INPUT
# ============================================================

if selected_mode == "Customer Support":
    input_placeholder = (
        "Ask about orders, shipping, refunds or returns..."
    )
elif selected_mode == "Medical Q&A":
    input_placeholder = (
        "Ask an educational medical question..."
    )
else:
    input_placeholder = (
        "Search research papers, e.g. machine learning..."
    )

typed_question = st.chat_input(input_placeholder)


# ============================================================
# DETERMINE QUESTION
# ============================================================

question_to_process = None

if typed_question:
    question_to_process = typed_question.strip()

elif st.session_state.pending_question:
    question_to_process = st.session_state.pending_question
    st.session_state.pending_question = None


# ============================================================
# PROCESS QUESTION
# ============================================================

if question_to_process:
    if not question_to_process:
        st.warning("Please enter a question.")
        st.stop()

    # Display and save the user message.
    with st.chat_message("user"):
        st.markdown(question_to_process)

    st.session_state.messages.append({
        "role": "user",
        "content": question_to_process
    })

    st.session_state.conversation_memory.add_message(
        "user",
        question_to_process
    )

    # Generate the assistant response.
    with st.chat_message("assistant"):
        try:
            # ------------------------------------------------
            # MEDICAL Q&A ASSISTANT
            # ------------------------------------------------

            if selected_mode == "Medical Q&A":
                with st.spinner(
                    "Searching the medical knowledge base..."
                ):
                    result = ask_medical(question_to_process)

                assistant_response = result.get(
                    "answer",
                    "No answer was returned."
                )

                st.markdown(assistant_response)

                entities = result.get("entities", {})

                with st.expander("View detected medical entities"):
                    st.write(
                        "**Diseases:**",
                        ", ".join(entities.get("diseases", []))
                        or "None detected"
                    )

                    st.write(
                        "**Symptoms:**",
                        ", ".join(entities.get("symptoms", []))
                        or "None detected"
                    )

                    st.write(
                        "**Treatments:**",
                        ", ".join(entities.get("treatments", []))
                        or "None detected"
                    )

            # ------------------------------------------------
            # RESEARCH ASSISTANT
            # ------------------------------------------------

            elif selected_mode == "Research Assistant":
                with st.spinner(
                    "Searching arXiv for research papers..."
                ):
                    papers = search_research_papers(
                        question_to_process,
                        max_results=5
                    )

                if not papers:
                    assistant_response = (
                        "I could not find any research papers for this "
                        "query. Please try another topic or check your "
                        "internet connection."
                    )
                    st.markdown(assistant_response)

                else:
                    assistant_response = (
                        f"I found {len(papers)} research paper(s) "
                        f"for **{question_to_process}**. "
                        "Their details are displayed below."
                    )
                    st.markdown(assistant_response)

                    for index, paper in enumerate(papers, start=1):
                        title = paper.get("title", "Untitled paper")

                        with st.expander(f"{index}. {title}"):
                            authors = paper.get("authors", [])
                            st.write(
                                "**Authors:**",
                                ", ".join(authors) if authors
                                else "Not listed"
                            )

                            st.write(
                                "**Published:**",
                                paper.get("published", "Unknown")
                            )

                            abstract = paper.get(
                                "abstract",
                                "No abstract available."
                            )
                            st.write("**Abstract:**")
                            st.write(abstract)

                            summary = summarize_paper(abstract)
                            st.write("**Short summary:**")
                            st.write(summary)

                            paper_link = paper.get("link", "")
                            if paper_link.startswith("https://") or (
                                paper_link.startswith("http://")
                            ):
                                st.markdown(
                                    f"[Read the original paper]({paper_link})"
                                )

            # ------------------------------------------------
            # CUSTOMER SUPPORT ASSISTANT
            # ------------------------------------------------

            else:
                with st.spinner(
                    "Searching the customer-support knowledge base..."
                ):
                    conversation_context = (
                        st.session_state.conversation_memory.get_context()
                    )

                    if uploaded_image is not None:
                        assistant_response = ask_multimodal_rag(
                            question=question_to_process,
                            image_bytes=uploaded_image.getvalue(),
                            mime_type=uploaded_image.type,
                            conversation_context=conversation_context
                        )
                    else:
                        assistant_response = ask_rag(
                            question_to_process,
                            conversation_context
                        )

                st.markdown(str(assistant_response))

            # ------------------------------------------------
            # SAVE ASSISTANT RESPONSE
            # ------------------------------------------------

            st.session_state.messages.append({
                "role": "assistant",
                "content": str(assistant_response)
            })

            st.session_state.conversation_memory.add_message(
                "assistant",
                str(assistant_response)
            )

        except Exception as error:
            st.error(
                "The assistant could not process your question."
            )
            st.caption(
                "Check the terminal for details, then try again."
            )
            st.exception(error)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "NovaAssist | Customer Support • Medical Q&A • Research Assistant"
)
st.caption(
    "Built with Python, Streamlit, RAG, ChromaDB, MedQuAD and arXiv."
)
