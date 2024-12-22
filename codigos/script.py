
# bibliotecas
import os
import dotenv
import openai
import json

# leitura dos dados de credenciais
diretorio_projeto = dotenv.find_dotenv(f"{os.path.abspath(os.curdir)}/.env")
dotenv.load_dotenv(diretorio_projeto)

chave_autenticacao_api = os.environ.get("OPENAI-API-KEY")

# leitura dos dados de parametros
with open(f"{os.path.abspath(os.curdir)}/parametros.json", "r", encoding='utf-8') as arquivo:
    parametros = json.load(arquivo)

# interacao com o modelo conversacional
agente = openai.OpenAI(api_key=chave_autenticacao_api)
conversa = agente.chat.completions.create(
    model=parametros['modelo'],
    store=True,
    messages=[
        {
            "role": "developer",
            "content": parametros['prompts']['desenvolvedor']
        },
        {
            "role": "system",
            "content": parametros['prompts']['sistema']
        },
        {
            "role": "user",
            "content": parametros['prompts']['usuario']
        }
    ]
)

print(conversa.choices[0].message)
