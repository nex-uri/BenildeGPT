# BenildeGPT
<b>Overiew:</b> <br>The new AI-Powered customer support system is a chatbot powered by Groq that answers user inquiries exclusively regarding the school curriculum and its details, academic concerns and school processes. The main target audience is the students of De La Salle College of Saint Benilde, particularly those who are geographically distant or who do not have their own time to go to the facilities. This is because many students, even now, still frequently question staff and faculty members regarding their concerns in the school system.</br>

<b>Objectives:</b>
<br>1. To develop an AI tool where students can get answers from their inquiries exclusively regarding the school curriculum and its details, academic concerns and school processes.
<br>2. To integrate the Groq API into the system in order for the chatbot to process student questions accurately and efficiently.
<br>3. To implement all essential system features such as user input handling, API communication and response generation to ensure smooth operation.
<br>4. To create a modern, user-friendly chat interface utilizing Tkinter that allows users to converse with the AI interface.

<b>Scope:</b>
<br>1. The program accepts the user's input.
<br>2. The output shows in the prompt when the user message is sent to the Groq API.
<br>3. The program uses Python, Integrated API, and many libraries/frameworks.

<b>Limitations:</b>
<br>1. The program does not accept the user's input if there are any unnecessary topics.
<br>2. There is no login or authentication system implemented.
<br>3. The program requires an active internet connection to retrieve API data.
<br>4. Due to budget limitations, the program lacks an implemented database and therefore does not save user messages.</br>

<b>Programming Tools</b>
<br>1. Programming Language: Python 3.x
<br>2. IDE: Visual Studio 2022
<br>3. Environment: GitHub, Windows Terminal / Git Bash
<br>4. Libraries / Frameworks: Tkinter, Groq, PIL (ImageTk & Image), Update, OS</br>

<b>Libraries / Frameworks Used</b>
<br>1. Tkinter — for graphical user interface
<br>2. Groq — for AI / LLM integration
<br>3. PIL (Pillow) — for image processing which they are: ImageTk and Image
<br>4. Update — for updating components 
<br>5. OS — for system-level functions</br>

<b>How the User interacts with the Program:</b>
<br>1. The user will open the program
<br>2. A window will show where the user can type out their questions.
<br>3. The user then types any inquiries that they have about anything to do with Benilde (e.g., rules, programs, requirements, e-jeep schedule, etc.)</br>

<b>Chat Generation Logic:</b>
<br>1. The question from the user is sent to Groq AI by the program via the internet.
<br>2. Based on its training and our instructions, the AI reads the query and starts thinking of the best answer.
<br>3. Little by little (also known as streaming) the AI returns with the answer, just like ChatGPT they are typing slowly.
<br>4. The program finds the best answer suited for the inquiry that was given and displays it in the chat window.</br>

<b>GUI Interface Flow:</b>
<br>1. At the bottom of the window is the chatbox where the user will type their inquiries.
<br>2. When an inquiry is sent, the AI’s answer will display above the chatbox or above the user’s inquiry.
<br>3. The chat will continue on as the users’ keeps on sending their inquiries.</br>

<b>Error Handling:</b>
<br>1. If a user doesn’t type anything but still clicks send or enter, the program will ignore the user’s input.
<br>2. The AI stops responding whenever there is a network issue or the API key is invalid. The error will show in the console rather than the chat interface.</br>

# Key Features:
<b>1. AI Chatbot Guide for Benilde Campus:</b> Utilization of the Groq API called openai/gpt-oss-20b whose purpose is to become an AI who guides users about Benilde. It is also a virtual assistant where all its knowledge is specifically designed around De La Salle College of Saint Benilde.</br>
<br><b>2. Specialized Knowledge Base:</b>  The AI’s sole job is only for topics regarding De Lasalle College of Saint Benilde since it is pre-programed to have specific details around the college’s history (St. Benilde Romancon), campus locations (Taft, SDA, AKIC), academic hubs, specialized campuses, and student support services.</br>
<br><b>3. Curriculum & Accreditation Awareness:</b> Has the means to provide accurate and precise information about the length of a trimester towards the undergraduate and graduate programs, SPaCE (Professional Education) Offerings and accreditation status while also including respective accreditation bodies (PAASCU, CHED and AUN-QA).</br>
<br><b>4. Interactive Tkinter GUI:</b> Features a custom Graphical User Interface built with Tkinter, including a dark-themed window (#202024 background), custom application icons, and a scrollable text area for chat history.</br>
<br><b>5. Real-Time Streaming Responses:</b> Using the streaming option (stream=True) of the application, the AI generates responses to user messages in small chunks as they are received creating more natural sound effects for the user while typing.</br>
<br><b>6. Natural Language Formatting:</b> The AI has to follow a very strict set of rules that it cannot format long markdown tables but rather it must provide the information in sentence format using clear natural language bullet points when displaying information on the GUI.</br>
<br><b>7. User Experience (UX) Elements:</b> In order to enhance the user experience, a placeholder will be shown where the user will enter their message ("Enter your message here”). A ‘Send’ button will be present in addition to clear visual separation of different User and AI fonts (User - Bold; AI - Green Bold). In addition to a ‘Send’ button, it also allows users to use the enter key as a way of sending the user message to the Groq API.</br>





