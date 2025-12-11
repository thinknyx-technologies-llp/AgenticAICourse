from smolagents import CodeAgent, InferenceClientModel, WebSearchTool

model = InferenceClientModel()
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

result = agent.run("What's the temprature in Paris today?")
print(result)