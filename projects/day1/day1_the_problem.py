from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv(override=True)

llm = ChatAnthropic(model="claude-sonnet-4-5")
question = "What were the top 3 headlines on Hacker News yesterday?"
response = llm.invoke(question)

print(f"QUESTION: {question}\n")
print(f"CLAUDE'S ANSWER:\n{response.content}")
