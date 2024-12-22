
import os
import dotenv
import openai

diretorio_projeto = dotenv.find_dotenv(f"{os.path.abspath(os.curdir)}/.env")
dotenv.load_dotenv(diretorio_projeto)

chave_autenticacao_api = os.environ.get("OPENAI-API-KEY")
agente = openai.OpenAI(api_key=chave_autenticacao_api)
