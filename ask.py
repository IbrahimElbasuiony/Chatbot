from create_vector_query_engine import create_vector_tool
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from Agent_prompt import before_chat_prompt
from llama_index.core import PromptTemplate

load_dotenv()


def print_long_text(text, words_per_line=20):
    words = text.split()
    for i in range(0, len(words), words_per_line):
        print(' '.join(words[i:i + words_per_line]))


""" THIS IS THE MAIN FUNCTION WILL TAKE USER INPUT AND RETURN THE RESPONSE """


def ask():
    react_system_prompt = PromptTemplate(before_chat_prompt)

    query_engine = create_vector_tool()
    # now using your API key
    agent = ReActAgent.from_tools(llm=OpenAI("gpt-4o", temperature=0),
                                  tools=[query_engine],
                                  verbose=False,
                                  )
    agent.update_prompts({"agent_worker:system_prompt": react_system_prompt})

    return agent


while True:
    agent = ask()
    user_input = input("=>")

    response = agent.chat(user_input)

    print_long_text(response.response)
