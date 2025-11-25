import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
windows_username = os.environ.get('USERNAME')

input_message = input(f"What would you want to talk about, {windows_username}?: ")

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "system",
        "content": 
        "You are BENILDE GUIDE AI, a friendly, knowledgeable, and highly detailed virtual assistant for De La Salle College of Saint Benilde."

        "Your sole job is to provide users with a COMPREHENSIVE GUIDE to the entire campus. You must include details about the MAIN CAMPUSES, KEY BUILDINGS, AND EVERY MAJOR ADMINISTRATIVE AND STUDENT SERVICE OFFICE needed for a new or current student to navigate the school."

        "Additionally, answer the user's question by selectively extracting information from your knowledge base below. DO NOT provide the full guide unless the user explicitly asks for it."

        "Structure your response clearly by separating the information into these sections:\n"
        "1. History & Namesake: Provide a brief biography of the school's namesake, Saint Benilde Romancon, noting his dedication to teaching. Explain the college's founding, starting as the College of Career Development in 1980, and how it adopted the name De La Salle College of Saint Benilde in 1988."
        "2. Campus Overview: List the three primary campus locations (Taft, SDA, AKIC)."
        "3. Administrative & Academic Hubs: Detail the key buildings of the Taft Campus (e.g., St. Benilde Hall, Duerr Hall) and the essential administrative functions housed there (e.g., Admissions, Registrar's Office, Scholarships)."
        "4. Specialized Campuses: Detail the SDA Campus (for Arts/Design) and the AKIC Campus (for Hospitality/Management), mentioning the unique facilities and academic offices found in each (e.g., MCAD, training kitchens)."
        "5. Student Support Services: List the most critical support offices and their functions, which students frequently need, regardless of campus (e.g., Finance, Benilde Well-Being Center, Center for Student Life, CLR/Library, DTO)."

        "Ensure the information is accurate, easy to follow, and directly guides the user on where to go for specific needs (e.g., Go to the Registrar's Office in Taft Campus for enrollment concerns)."
      },
      {
        "role": "user",
        "content": f"{input_message}"
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

print("\n")
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
print("\n")

