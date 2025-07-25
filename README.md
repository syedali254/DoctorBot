==========================
DOCTORBOT PROJECT DOCUMENTATION
==========================

Project Overview:
-----------------
DoctorBot is a Django-based chatbot application that uses LangChain with Google Generative AI (Gemini) and FAISS for conversational question answering. The chatbot interacts with a knowledge base stored in text files, allowing users to ask questions and receive intelligent responses.

The project includes:
- Django backend for serving chatbot API requests.
- LangChain Conversational Retrieval Chain for contextual responses.
- FAISS vector store for efficient document search.
- Memory support to maintain chat history.
- A simple frontend (index.html) for user interaction.

---------------------------------------------------

Features:
---------
1. Chatbot powered by Google Generative AI (Gemini).
2. Context-aware responses using ConversationalRetrievalChain.
3. Vector-based search with FAISS.
4. Web interface built with Django templates.
5. Configurable knowledge base from text files.
6. Supports environment variables for API key management.

---------------------------------------------------

Project Structure:
------------------
DoctorBot/
│
├── chatbot/
│   ├── data/
│   │   └── file1.txt         (Knowledge base)
│   ├── views.py              (Main chatbot logic)
│   ├── templates/
│   │   └── index.html        (Frontend UI)
│
├── manage.py                 (Django entry point)
├── requirements.txt          (Dependencies)

---------------------------------------------------

Setup Instructions:
-------------------
1. Clone the repository:
   git clone https://github.com/syedali254/DoctorBot.git
   cd DoctorBot

2. Create and activate a virtual environment:
   python -m venv venv
   On Windows: venv\Scripts\activate
   On Linux/Mac: source venv/bin/activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Set your Google API Key:
   Create a .env file in the root directory with the following line:
   GOOGLE_API_KEY=your_api_key_here

   OR set it as a system environment variable:
   export GOOGLE_API_KEY=your_api_key_here

5. Run database migrations:
   python manage.py migrate

6. Start the Django development server:
   python manage.py runserver

7. Open your browser and navigate to:
   http://127.0.0.1:8000

---------------------------------------------------

How the Backend Works:
----------------------
- The knowledge base file (chatbot/data/file1.txt) is loaded and converted into embeddings using Google Generative AI Embeddings.
- FAISS is used to store and retrieve the relevant documents.
- LangChain’s ConversationalRetrievalChain combines the LLM (Gemini model) with the retriever and a memory buffer.
- When a user sends a message via POST request to `/chat`, the chatbot:
    a. Processes the question.
    b. Searches for relevant data in FAISS.
    c. Returns the AI-generated response as JSON.

---------------------------------------------------

API Endpoint:
-------------
1. POST /chat
   Request: message=<your_question>
   Response: {"response": "<answer_from_bot>"}

Example:
--------
Request:
  {"message": "What is the content of file1?"}

Response:
  {"response": "The file contains ... "}

---------------------------------------------------

Frontend (index.html):
----------------------
- index.html contains a basic UI for interacting with the chatbot.
- User messages are sent to the backend `/chat` endpoint using AJAX or fetch API.
- The chatbot's response is displayed on the page dynamically.

---------------------------------------------------

Dependencies:
-------------
The main dependencies are:
- Django
- LangChain
- FAISS
- Google Generative AI SDK
- Python-dotenv (for environment variables)

All dependencies are listed in `requirements.txt`.

---------------------------------------------------

Future Enhancements:
--------------------
- Add voice-based chat support.
- Allow dynamic updates to the knowledge base.
- Improve UI/UX with a modern chatbot interface.
- Deploy the app on cloud platforms like AWS or Vercel.

---------------------------------------------------

License:
--------
This project is licensed under the MIT License.

---------------------------------------------------
