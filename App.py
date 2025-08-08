import streamlit as st
import json
from streamlit_js_eval import streamlit_js_eval
from Service import generate

# ~~~~~~~~~~~~~~~~~~~~~~~~
# ====== Header ======
# ~~~~~~~~~~~~~~~~~~~~~~~~

# === Page New Tab ===
st.set_page_config(
    page_title="Colego - Cover Letter Generator",
    page_icon="🥑",
    layout="centered",
)

# === Title ===
st.markdown("""
<div style='text-align: center; padding-bottom: 20px;'>
    <span style='font-size: 52px; font-weight: bold; margin-right: 30px;'>🥑Colego</span><br>
    <span style='font-size: 15px; color: gray;'>
        Generate a personalized and professional cover letter quickly.
    </span>
</div>
""", unsafe_allow_html=True)

# === Token Instruction ===
st.markdown("""
<div style="border: 1px solid #f0ad4e; padding: 15px; border-radius: 10px; background-color: #fff3cd;">
  <span style="font-size: 18px;">⚠️ <strong>For a better experience</strong></span><br>
  <span style="font-size: 16px;">we recommend using your <strong>personal Hugging Face Token</strong>.<br>
  You can enter it in the <strong>Token Setting</strong> section below.</span>
</div>
""", unsafe_allow_html=True)



# ~~~~~~~~~~~~~~~~~~~~~~~~
# ====== Selection Bar ======
# ~~~~~~~~~~~~~~~~~~~~~~~~

# === Tab ===
tab1, tab2 = st.tabs(["🧩 Colego Generator", "🗝️ Token Setting"])

# ===~~~~~~===
# === Token ===
# ===~~~~~~===
with tab2:
    st.markdown("### Hugging Face Token")

    token_input = st.text_input("Paste your Hugging Face token:",
                                placeholder="e.g. hf_abc123def456...",
                                type="password")

    if st.button("Save Token"):
        if token_input.startswith("hf_"):
            st.session_state.hf_token = token_input
            st.success("✅ Token saved.")
        else:
            st.error("❌ Invalid token. A token should start with `hf_`.")

    with st.expander("How to get your token"):
        st.markdown("""
        1. Go to [huggingface.co](https://huggingface.co)
        2. Navigate to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
        3. Click **"New token"**, set permissions to **Read**, and copy the token
        4. Paste it into the box above
        """)

# ===~~~~~~===
# === Form ===
# ===~~~~~~===
with tab1:
# === Instruction ===
    st.markdown("""
    <div style="
        background-color: #f0f8ff;
        padding: 15px 25px;
        border-left: 6px solid #4a90e2;
        font-size: 18px;
        font-weight: 500;
        border-radius: 8px;
        color: #333;
        margin-top: 25px;
        margin-bottom: 25px;
    ">
        ✨ <strong>Fill in the forms below to generate your personalized cover letter.</strong>
    </div>
    """, unsafe_allow_html=True)

# === Section 1: Personal Info ===
    page_data = {
        "applicant_name": "",
        "applicant_email": "",
        "applicant_phone": "",
        "user_skills": "",
        "user_background": ""
    }

    local_data = streamlit_js_eval(js_expressions="localStorage.getItem('user_info')", key="get_user_info")

    if local_data and isinstance(local_data, str):
        restored = json.loads(local_data)
        page_data.update(restored)
        st.info("✅ Loaded saved information from local")

    st.markdown("### Personal Information")

    # == Info ==
    with st.form(key='info_form'):
        applicant_name = st.text_input("Full Name", value=page_data.get("applicant_name", ""),placeholder="e.g. Colego")

        applicant_email = st.text_input("Email Address", value=page_data.get("applicant_email", ""),
                                        placeholder="e.g. email@example.com")

        applicant_phone = st.text_input("Phone Number", value=page_data.get("applicant_phone", ""),
                                        placeholder="e.g. 123-456-7890")

        user_skills = st.text_area("Technical & Soft Skills", value=page_data.get("user_skills", ""),
                                   placeholder="Please list your skills here.",
                                   height=150)

        user_background = st.text_area("Personal Background", value=page_data.get("user_background", ""),
                                       placeholder="Describe your academic background, experiences, career interests, etc...",
                                       height=500)

        st.markdown("<div style='font-size: 13px; color: gray; margin-top: -10px;'>"
                    "**This information helps generate a tailored cover letter."
                    "</div>", unsafe_allow_html=True)

        save_button = st.form_submit_button("Save Personal Info", help='Save your personal information to your local')

    # == Save ==
        if save_button:
            data = {
                "applicant_name": applicant_name,
                "applicant_email": applicant_email,
                "applicant_phone": applicant_phone,
                "user_skills": user_skills,
                "user_background": user_background
            }
            js_code = f"localStorage.setItem('user_info', JSON.stringify({json.dumps(data)}))"
            streamlit_js_eval(js_expressions=js_code, key="save_user_info")
            st.success("✅ Information saved successfully!")

    # st.markdown("</div>", unsafe_allow_html=True)

    # == Delete ==
    if local_data:
        if st.button("🗑️ Delete Saved Info"):
            streamlit_js_eval(js_expressions="localStorage.removeItem('user_info')", key="clear_user_info")
            st.success("🧹 Cleared saved data. Please refresh.")

# === Section 2: Generator ===
    st.markdown("### Generator")

    with st.form(key='Generator'):

        # == Job Details ==
        st.markdown("<h4 style='color:#1f4e79;'>🏷️ Job Details</h4>", unsafe_allow_html=True)

        job_title = st.text_input("Position Title", placeholder="e.g. Software Engineer Intern")

        company_name = st.text_input("Company Name", placeholder="e.g. OpenAI")

        job_description = st.text_area(
            "Job Description",
            placeholder=(
                "Paste the full job description here.\n\n"
                "Include:\n"
                "- Required qualifications\n"
                "- Daily responsibilities\n"
                "- Technologies used\n"
                "- Desired soft skills"
            ),
            height=300
        )

        # == Focus Point ==
        st.markdown("<h4 style='margin-top: 30px; color:#1f4e79;'>🎯 Cover Letter Focus (Optional)</h4>", unsafe_allow_html=True)

        focus_points = st.text_area(
            "Key Points or Strengths to Emphasize",
            placeholder=(
                "List traits or experiences to highlight.\n\n"
                "Examples:\n"
                "- Passion for AI research\n"
                "- Experience leading student clubs\n"
                "- Collaboration & problem-solving"
            ),
            height=200
        )

        # == Generate ==
        submit_button = st.form_submit_button(label='Generate Cover Letter')



# ~~~~~~~~~~~~~~~~~~~~~~~~
# ====== Generate ======
# ~~~~~~~~~~~~~~~~~~~~~~~~
        if submit_button:
            if not job_title or not company_name or not job_description:
                st.error("❗ Please fill in all required fields (title, company, and description).")
            else:
                with st.spinner("Generating your cover letter..."):
                    #
                    with open("prompt.json", "r", encoding="utf-8") as f:
                        prompt = json.load(f)

                    messages = []

                    for i in prompt:
                        content = i["content"].format(
                            job_title=job_title,
                            company_name=company_name,
                            user_background=user_background,
                            user_skills=user_skills,
                            job_description=job_description,
                            applicant_name=applicant_name,
                            applicant_email=applicant_email,
                            applicant_phone=applicant_phone,
                            focus_points=focus_points
                        )
                        messages.append({"role": i["role"], "content": content})

                    #
                    cover_letter = generate(messages)

                    st.success("✅ Cover letter generated!")
                st.markdown("### Your Cover Letter:")
                st.write(cover_letter)

