from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

DB_DIRECTORY = "db"

prompt_template = """
    Você é um assistente de IA especializado em buscar documentação de APIs e sanar as dúvidas dos desenvolvedores.
    Não utilize informações que não estejam no contexto a seguir para responder à pergunta do usuário.
    Se não souber a resposta, diga que não sabe ou que não encontrou a informação no contexto.

    Contexto:
    {context}

    Pergunta: {question}
    Resposta:
"""

question = input("Digite sua pergunta: ")

embedding_function = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory=DB_DIRECTORY,
    embedding_function=embedding_function
)

results = db.similarity_search_with_relevance_scores(question, k=6)

if len(results) == 0:
    print("Não foi possível encontrar uma resposta para a pergunta.")
    exit()

results_text = []

for result in results:
    text = result[0].page_content
    results_text.append(text)

context = "\n\n".join(results_text)

prompt = ChatPromptTemplate.from_template(prompt_template)

prompt = prompt.invoke({
    "context": context,
    "question": question
})

model = OllamaLLM(model="llama3.2")
response = model.invoke(prompt)

print(response)