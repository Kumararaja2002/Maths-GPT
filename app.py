import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq

# load .env
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY') 
groq_api_key = os.getenv('GROQ_API_KEY') 

# llm
llm = ChatGroq(model='Gemma2-9b-It', groq_api_key=groq_api_key)

# Initalize the MATH tool
# Wikipedia Tool
wiki_api_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wiki_api_wrapper.run,
    description="A tool for searching the internet to find the various informations on the topics mentioned"
)

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name = "Calculator",
    func= math_chain.run,
    description= "A tool for answering Math related questions"
)

# prompt
prompt = """
You are agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""
# prompt template
prompt_template = PromptTemplate(input_variables=['question'],template=prompt)

# Combine all the tools into Chain
chain = LLMChain(llm=llm,prompt = prompt_template)

reasoning_tool = Tool(
    name = "Reasoning Tool",
    func= chain.run,
    description="A tool for answering logic-based and reasoning questions"
    )

# Initalize the agents

assistant_agent = initialize_agent(
    tools = [wikipedia_tool, calculator, reasoning_tool],
    llm= llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_errors =True
)

# Streamlit App
st.set_page_config(page_title="Text To MAth Problem Solver And Data Serach Assistant",page_icon="🧮")
st.title("Text To Math Problem Solver")

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant','content':'Hi, I am a Math chatbot who can answer all your maths questions'}
    ]
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

question=st.text_area("Enter your question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("Find my answer"):
    if question:
        with st.spinner("Generating the response..."):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)

            st_callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_callback])

            st.session_state.messages.append({'role':'assistant','content':response})
            st.write("#### Response:")
            st.success(response)

    else:
        st.warning("Please enter the question.")