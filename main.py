from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
    you are making conversations with programmers so make it straight to the point
    
    Questions: {questions}
    Context: {context}


"""

model = OllamaLLM(model='gemma:2b')
prompt_template = ChatPromptTemplate.from_template(template=template)
chain = prompt_template | model


def run():
    print("Type Exit to exit: ")
    context = ''
    user_in = ''
    while user_in.lower() != 'exit':
        user_in = input("you: ")
        out = chain.invoke({"questions": user_in, "context": context})
        print(out)
        context += "user: {user_in}, AI: {out}" 
    return "Conversation done"


run()