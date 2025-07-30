# https://ai.google.dev/gemini-api/docs

# https://github.com/panaversity/learn-agentic-ai/blob/main/01_ai_agents_first/04.0_hello_agent/OpenAI_agents_SDK_Hello_world.ipynb  ---> API key lesaktehain 

# uv init .
# uv add openai-agents
# uv run main.py

this is context.py file
# User_name = wrapper.context["name"] --> yeh first hash hai #
# return f"Hi {user_name} the weather in {city} is sunny with 40C"  --> # 2 second hash hai #
Terminal result uv run context.py
#wrapper>>>> ToolContext(context={'name': 'Azra', 'designation': 'Teacher'}, usage=Usage(requests=1, input_tokens=55, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=16, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=121), tool_name='fetch_weather', tool_call_id='')
result>>> The weather in Karachi is sunny with 40C."# class_5_Weather_Tool_context" 
