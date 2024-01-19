from langchain.prompts import PromptTemplate
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType, create_react_agent, AgentExecutor


from tools.tools import get_profile_url


def lookup(name: str) -> str:
    """
    Lookup for LinkedIn profile URL given a person's full name.
    :param name: The full name of the person.
    :return: The LinkedIn profile URL.
    """

    llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")

    template = '''Answer the following questions as best you can. You have access to the following tools:

            {tools}

            Use the following format:

            Question: the input question you must answer
            Thought: you should always think about what to do
            Action: the action to take, should be one of [{tool_names}]
            Action Input: the input to the action
            Observation: the result of the action
            ... (this Thought/Action/Action Input/Observation can repeat N times)
            Thought: I now know the final answer
            Final Answer: the final answer to the original input question

            Begin!

            Question: Given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page. Your answer should only contain a URL.
            Thought:{agent_scratchpad}'''

    prompt = PromptTemplate.from_template(template)

    tools = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful when you need to get the linkedin url of a person",
        )
    ]

    agent = create_react_agent(
        llm,
        tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True)


    response = agent_executor.invoke({'name_of_person': name})

    return response['output'].strip()
