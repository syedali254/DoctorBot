from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os

# Set your API key (for local testing, use .env or environment variable)
api_key = os.getenv("GOOGLE_API_KEY")  # Ensure this is set in your system or .env

# Load and embed the knowledge base
loader = TextLoader("chatbot/data/file1.txt")  # ✅ Put file here
docs = loader.load()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# Memory for conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Set up the Conversational Retrieval Chain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
)

# Index Page
def index(request):
    return render(request, 'index.html')

# Chat View

from django.http import JsonResponse

def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        if user_input:
            result = qa_chain.invoke({"question": user_input})
            print(result['answer'])
            response = result.get("answer") or "Sorry, I couldn't understand that."
            return JsonResponse({"response": response})
    return JsonResponse({"response": "Invalid request"})
