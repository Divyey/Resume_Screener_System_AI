from dotenv import load_dotenv
import openai
import streamlit as st
import os
import io
import base64
import pdf2image

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def pdf_to_image_bytes(uploaded_file):
    # Convert PDF to image (first page)
    images = pdf2image.convert_from_bytes(uploaded_file.read())
    first_page = images[0]
    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format='JPEG')
    img_bytes = img_byte_arr.getvalue()
    return img_bytes

def get_openai_vision_response(prompt, image_bytes, job_description):
    # Encode image as base64 for OpenAI API
    image_base64 = base64.b64encode(image_bytes).decode()
    image_url = f"data:image/jpeg;base64,{image_base64}"

    # Compose message for GPT-4o Vision
    messages = [
        {"role": "system", "content": "You are an expert HR analyst and recruiter."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt + "\n\nJob Description:\n" + job_description},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ]

    # Call OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4o", # "gpt-4-turbo"
        messages=messages,
        max_tokens=700,
        temperature=0.2,
    )
    return response.choices[0].message.content

# Streamlit App UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])
#uploaded_file = st.file_uploader("Upload your resume (PDF or Word)...", type=["pdf", "docx"])


if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage match")


# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume (as an image) against the job description.
# Please share your professional evaluation on whether the candidate's profile aligns with the role.
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """
input_prompt1 = """
You are an experienced Technical Human Resource Manager in the field of Data Science, Full Stack,Web Development, Big Data, Data Engineering, DEVOPS, Data Analyst, Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

# input_prompt2 = """
# You are an experienced Technical Human Resource Manager with expertise in field of Data Science, Full Stack,Web Development, Big Data, Data Engineering, DEVOPS, Data Analyst. Your role is to scrutinize the resume provided resume in light of the job description provided.
# Share your insights on the candidate's suitability for the role from an HR perspective.
# Additionally, offer advice on embracing the candidate's skills and identify areas where
# """

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack,Web Development, Big Data, Data Engineering, DEVOPS, Data Analyst and ATS functionality.
Your task is to evaluate the resume (as an image) against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        image_bytes = pdf_to_image_bytes(uploaded_file)
        # response = get_openai_vision_response(input_prompt1, pdf_content, input_text)
        response = get_openai_vision_response(input_prompt1, image_bytes, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

#submit2 = st.button("How Can I Improvise my Skills")

elif submit3:
    if uploaded_file is not None:
        image_bytes = pdf_to_image_bytes(uploaded_file)
        response = get_openai_vision_response(input_prompt3, image_bytes, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

