import streamlit as st

from email_generator import (
    chain,
    CONTENT_INSTRUCTIONS
)

from st_copy import copy_button


# ==========================================
# 1. Streamlit Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="centered"
)


# ==========================================
# 2. Application Title
# ==========================================

st.title("✍️ AI Content & Email Generator")

st.write(
    "Generate emails, LinkedIn posts, blogs, and "
    "product descriptions using Generative AI."
)


# ==========================================
# 3. Sidebar - Content Settings
# ==========================================

st.sidebar.header("Content Settings")

content_type = st.sidebar.selectbox(
    "Select Content Type",
    [
        "Email",
        "LinkedIn Post",
        "Blog",
        "Product Description"
    ]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Formal"
    ]
)

length = st.sidebar.selectbox(
    "Select Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)


# ==========================================
# 4. User Instruction
# ==========================================

st.subheader("Enter Your Instruction")

instruction = st.text_area(
    "What would you like to generate?",
    placeholder=(
        "Example: Write a professional email "
        "requesting two days of leave."
    ),
    height=150
)


# ==========================================
# 5. Generate Content
# ==========================================

if st.button(
    "✨ Generate Content",
    use_container_width=True
):

    # Input validation
    if not instruction.strip():

        st.warning(
            "Please enter an instruction."
        )

    elif len(instruction.strip()) < 5:

        st.warning(
            "Please provide a more detailed instruction."
        )

    else:

        try:

            # Get content-specific instructions
            content_instruction = CONTENT_INSTRUCTIONS[
                content_type
            ]

            # Prepare input for PromptTemplate
            prompt_data = {

                "content_type": content_type,

                "tone": tone,

                "length": length,

                "content_instruction":
                    content_instruction,

                "instruction":
                    instruction
            }

            # Generate content
            with st.spinner(
                "Generating content..."
            ):

                response = chain.invoke(
                    prompt_data
                )

            # Store generated content
            st.session_state[
                "generated_content"
            ] = response.content

            st.success(
                "Content generated successfully!"
            )

        except Exception as e:

            st.error(
                "Unable to generate content."
            )

            st.info(
                "Please check your API key, "
                "internet connection, or model availability."
            )

            st.caption(
                f"Error: {str(e)}"
            )


# ==========================================
# 6. Display Generated Content
# ==========================================

if "generated_content" in st.session_state:

    st.divider()

    st.subheader("Generated Content")

    # Editable generated content
    edited_content = st.text_area(
        "Edit your generated content:",
        value=st.session_state[
            "generated_content"
        ],
        height=400
    )

    # Update session state
    st.session_state[
        "generated_content"
    ] = edited_content


    # ======================================
    # 7. Copy Button
    # ======================================

    copy_button(
        edited_content
    )


    # ======================================
    # 8. Download Button
    # ======================================

    st.download_button(
        label="⬇️ Download Content",
        data=edited_content,
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
    )