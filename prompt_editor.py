import json

messages = [
    {
        "role": "system",
        "content": "You are an expert cover letter writer. Your task is to write high-quality, tailored cover letters for job applicants, following the Canadian business letter format. Each cover letter must consist of exactly four clear and logical paragraphs. Each cover letter should be one and a half page long, using Times New Roman, size 12, and left-aligned formatting. Your writing should be professional, persuasive, and focused on aligning the applicant’s most relevant strengths with the job description. Use clear paragraphs, proper salutation and closing, and focus on matching the applicant’s skills with the job."
    },
    {
        "role": "user",
        "content": """I am applying for the position of {job_title} at {company_name}.

            Please write a exactly four clear and logical paragraph, one and a half page, logically flowing, and formatted cover letter that:

            - Begins with 'Dear Hiring Manager,' or a more specific salutation if possible.
            - Exactly four paragraphs: Maintains a clear, professional tone and logical structure.
            - Paragraph 1: Includes a wow statement, motivation for applying, value I can bring, and links my goals to the company's mission
            - Paragraph 2: Mentions my academic background, current courses or projects, and highlight technical skills relevant to the job
            - Paragraph 3: Describes my past experiences (internships, clubs, personal projects, volunteering), and soft skills
            - Paragraph 4: Reiterates my interest, mentions contact info, thanks the reader, and ends with 'Sincerely,' followed by my name

            Here is my personal background:

            {user_background}
            
            Here are focus points to emphasize in the cover letter:

            {focus_points}
            
            Here is my skills:
            
            {user_skills}

            Here is the job description:

            {job_description}

            My name (for the signature line): {applicant_name}

            My email: {applicant_email}

            My phone number: {applicant_phone}
            
            Please analyze my background and select only the most relevant skills, experiences, and projects that best match the job description. Ignore unrelated information. Focus on what would make me a competitive candidate.

            Here is a sample structure to reference (do not copy exactly, just follow the logic):

            ---
            Dear [Hiring Manager’s Name],

            I am writing to express my interest in the [Job Position] position at [Company Name]. As a Computer Science Co-op student at McMaster University (expected graduation: May 2027), I am eager to apply my technical skills and problem-solving abilities to your team.

            [Academic background and skills]

            [Past work/project experiences and soft skills]

            I am particularly drawn to [Company Name] because of its [value or technology]. My experience in Java, Python, and database systems would allow me to contribute effectively to your team. I have attached my resume for your review. Please feel free to reach out to me at sample@example.com or 123-456-7890 at your convenience.

            Sincerely,
            
            Sample Name
            
            sample@example.com
            
            123-456-7890
            ---

            Please output only the final cover letter text, no explanations, no formatting syntax like markdown or HTML."""
    }
]

with open("prompt.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, indent=2, ensure_ascii=False)