import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.utilities import DuckDuckGoSearchAPIWrapper

# 1. Load environment variables from .env
load_dotenv()

# 2. Get your API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# 3. Initialize the LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",  # Change to gpt-4 if available
    openai_api_key=openai_api_key
)

# 4. Add a simple search tool
search = DuckDuckGoSearchAPIWrapper()
tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Search the web for current information"
    )
]

# 5. Create the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 6. Run the agent
if __name__ == "__main__":
    query = "What's the latest news about AI agents?"
    print(f"🤖 Asking agent: {query}")
    response = agent.run(query)
    print("\nAgent Response:\n", response)