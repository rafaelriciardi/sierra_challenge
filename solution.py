import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Sierra Studio // AI Engineering Interview
# 1. What problems do you see with this code?
#   - The temperature is set to a high value, which can make the model less deterministic and predictable.
#   - There is a lack of test cases. We only have one test for the True class and none for the False one.
#   - The prompt is not wrong, but it could be improved to enhance accuracy and the expected outputs.
#   - The code is not fail safe. It will break if anything goes wrong, such as API unavailability or bad responses from the model.
#   - Thinking as system integration, the return of the model as string forces a transformation every time its values need to be accessed
# 2. What ideas do you have to make it better?
#   - [Done] Adjust the temperature to a lower value, making the model more deterministic and predictable, which is very important for this task.
#   - [Done] Change the functions return to a json object to be used in the next steps of the system.
#   - [Done]Create unit tests, with real examples, containing spams and not spams content.
#   - [Done] Restructure the prompt with clearer and more strict instructions, making it less prone to hallucination.
#   - [Done] Add the few-shot technique to the prompt, providing a few examples and their expected outputs.
#   - Add a fallback option to another LLM service, enhancing the availability of the solution itself.
#   - Use a retry mechanism to ensure the output is as expected.
#   - Implement exception handling to act when the input is not as expected and when other kinds of errors hit the application, preventing it from breaking.
# 
# Don't use AI to answer this question :)

def check_spam(email: str) -> str | None:
    prompt = f"""\
        You are part of a system and your task is to determine if a given email is spam or not.
        Your output should be a valid JSON object according to the format bellow. As a part of a system, your answer should be restricted only to the json, nothing more.

        Return a valid JSON object with the format:
        {{
            is_spam: boolean flag of the classification, true for spam and False for not spam // bool
            reason: report in the field how you think step by step and why you classified it as a spam or not. // str
        }}

        As a classifier, take in consideration the following definitions:
        - Spam: A Spam message is any unwanted message sent in bulk to people who never asked for it, typically with the goal of selling something, promoting a scam, or spreading malicious links.
        - Not Spam: A Not Spam message is simply any email you actually want to receive. It's the legitimate communication you expect, like updates from colleagues, shipping notifications, or newsletters you've subscribed to.
        
        Examples of Spam e-mails:
        1 - PESQUISA MARCA XAROPE\nEste é um questionário de pesquisa e sua participação é importante. Responda abaixo. Agradecemos sua participação!\n\nVocê já comprou ou pensa em comprar um xarope para tosse ou produto similar?\nMarque apenas uma opção abaixo:\ Já comprei recentemente  Já comprei, mas faz tempo Nunca comprei, mas penso em comprar Nunca comprei e não pretendo comprar
        2 - Dear Marcos Rauthman, \n\n We’re thrilled to announce the launch of a new course: Retrieval Augmented Generation (RAG), taught by AI engineer and educator Zain Hasan.\n\n This hands-on course shows you how to build production-ready RAG systems, connecting language models to external data sources to improve accuracy, reduce hallucinations, and support real-world use cases.\n\n What you’ll learn in the Retrieval Augmented Generation (RAG) Course: \n\n You'll move beyond prototype-level LLM apps to build full RAG pipelines that are scalable, adaptable, and grounded in real context. In detail, you’ll:\n\n Combine retrievers and LLMs using tools like Weaviate, Together.AI, and Phoenix\nEvaluate system performance, balance cost-speed-quality tradeoffs, and prep your pipeline for deployment\nApply effective retrieval such as keyword search, semantic search, and metadata filtering, and know when to use each\n\n You’ll work with real-world datasets from domains like healthcare, media, and e-commerce, gaining a practical foundation and engineering judgment you can apply in production settings.\n\n RAG is now at the core of many production-grade AI systems:\n\n According to a Grand View Research report, industry analysts project that companies will spend over $11 billion by 2030 on infrastructure and tools to support RAG workloads, up from an estimated $1.2 billion in 2024. Meanwhile, a K2View survey found that 86% of companies using generative AI now rely on retrieval-based techniques to improve accuracy and customization.\n\n It’s already powering production systems across internal search, customer support, knowledge assistants, and more.\n\n This course is designed for software engineers, ML practitioners, and technical professionals building with LLMs. If your applications require accuracy, traceability, and relevance, this course will show you how to get there with RAG.\n\n Enroll Now!\n\n  Keep learning, \n The DeepLearning.AI Team
        
        Examples of Not Spam e-mails:
        1 - Hi Mary,\n\nCorrect, there was a mistake. I will send you a new email with a form, so you can fill that one out. Please ignore the previous one.\nLet me know if you have any questions.\n\nBest,\nValentina
        2 - Este é um lembrete do assunto desta solicitação:\n\nOlá, Junior.\n\n \n\nPoxa, sentimos muito por essa experiência com a nossa plataforma 🙁\n\n \n\nAnalisamos a sua solicitação e o processo de cancelamento do seu pedido já foi iniciado, tá bom?\n\n \n\nO cancelamento do pedido será realizado assim que o produto retornar ao nosso centro de distribuição e passar por uma análise.\n\n \n\nNúmero da Coleta: 237757876\n\n \n\nO compromisso para a primeira tentativa de coleta é até dia 19/01/2024\n\n \n\nO fluxo de coleta ou envio do produto é muito simples, são 2 etapas:\n\n \n\nEtapa 1\n\n \n\n1) Coloque todos os acessórios e manuais recebidos (fones de ouvido, cartão de memória, etc.) na embalagem;\n2) Embale o produto na embalagem original. Mas se não tiver, pode utilizar outra caixa desde que seja devidamente lacrada;\n3) Lacre a caixa. O produto só poderá ser postado nessas condições;\n4) Apresente o código de postagem ao atendente (informado acima);\n5) Apresente a nota fiscal ao atendente dos Correios\n6) Não esqueça de guardar o seu comprovante de postagem.\n\n \n\nApós recebimento do produto a autorização do estorno acontecerá da seguinte forma:\n\n \n\n◾Pagamento em cartão de crédito: em até 5 dias úteis, ou no próximo ciclo da fatura, caso ela esteja fechada.\n\n \n\n◾Pagamento em pontos: em até 2 dias úteis.\n\n \n\n◾Pagamento em pix: em até 4 dias úteis.\n\n \n\nAinda tem dúvidas? Responda esse e-mail que continuaremos com a nossa conversa.\n\n \n\nConte com a gente.\nItaú Shop\n\n \n\n \n\n\n\nItaú Shop


        Email to classify: {email}"""

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}], 
        temperature=0.2, 
        max_tokens=100,
    )

    response = json.loads(completion.choices[0].message.content)
    return response


# Moved the tests from here to a unit test scheme at tests/tests.py

# email = "hi how r u bro i have million dollar deal just sign here"
# res = check_spam (email)
# if res:
#     print(json.dumps(res,indent=2))
    