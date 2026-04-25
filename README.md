# Correios API RAG Agent

Este é um agente inteligente (RAG - Retrieval-Augmented Generation) especializado em responder perguntas sobre a API dos Correios, extraindo informações do Manual de Integração oficial.

O projeto utiliza o framework **LangChain**, banco de dados vetorial **ChromaDB** e roda 100% localmente utilizando o **Ollama** para processamento de texto (geração e embeddings).

## Tecnologias Utilizadas

- **Python**
- **LangChain**
- **ChromaDB** (Banco de dados vetorial local)
- **Ollama**
  - **Embeddings**: `nomic-embed-text`
  - **LLM**: `llama3.2`

## Como Funciona

1. O script `create_database.py` extrai o texto de todos os arquivos PDF dentro da pasta `pdfs/`.
2. O texto é separado em pequenos fragmentos (chunks) e vetorizado utilizando o modelo local `nomic-embed-text`.
3. Os vetores são salvos localmente na pasta do ChromaDB (`db/`).
4. Ao rodar o `main.py`, a pergunta do usuário é comparada na base de dados para buscar os contextos mais relevantes, e em seguida, o modelo `llama3.2` gera a resposta.

## Pré-requisitos

Para rodar este projeto, você precisa ter:

1. Python instalado na máquina.
2. [Ollama](https://ollama.com/) instalado e rodando.
3. Fazer o download dos modelos do Ollama. Abra seu terminal e execute:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3.2
   ```

## Instalação e Uso

1. Instale as bibliotecas necessárias que estão listadas no `requirements.txt`:
   ```bash
   py -m pip install -r requirements.txt
   ```

2. Certifique-se de criar a pasta `pdfs/` na raiz do seu projeto e colocar o PDF do Manual de Integração dos Correios lá dentro.

3. **Crie a base de dados vetorial:**
   ```bash
   py create_database.py
   ```

4. **Inicie o Agente para fazer suas consultas:**
   ```bash
   py main.py
   ```

## Exemplos de Perguntas para o Agente

Aqui estão algumas sugestões do que perguntar assim que o agente iniciar:

1. *"Eu quero saber como fazer uma consulta das informações de um CEP na API dos Correios, qual a url e quais os parametros devo utilizar? Qual resposta devo esperar?"*
2. *"Quais são os pré-requisitos para utilizar a API dos correios?"*
