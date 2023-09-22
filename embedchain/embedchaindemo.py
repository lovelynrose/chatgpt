# pip install embedchain

import os

os.environ["OPENAI_API_KEY"] = your_key

from embedchain import App

chat_bot = App()

chat_bot.add("data/functional doc.docx")
chat_bot.add('pdf_file', "data/sadhana paper.pdf")

chat_bot.add_local("qna_pair",("What is embedchain","framework to easily create LLM powered bots over any dataset"))

result = chat_bot.chat("""
what are the user roles
""")
print(result)

result = chat_bot.query("""
what is the dataset used for research 
""")
print(result)

result = chat_bot.query("""
is embedchain a framework
""")
print(result)
