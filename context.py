from agents import Agent, Runner, function_tool,RunContextWrapper
from my_config import config
from typing_extensions import TypedDict
from dataclasses import dataclass


@dataclass
class UserInfo:
      name: str
      designation: str

local_context = UserInfo(name="Azra", designation="Teacher")


#class ContextType(TypedDict):    -->this is first hash # yeh oper coding ke liye # kiya hai
    # name: str                   
    # designation: str         
 

#local_context = {
 #   "name": "Azra",
 #   "designation": "Teacher"     --> ye oper ki coding ki waja se coding end hash #
#}


@function_tool
async def fetch_weather(wrapper:RunContextWrapper,city: str) -> str:
 """
    Fetch weather according to the given city

    Args:
        city: city for weather
    """
 print("wrapper>>>>",wrapper)
 # User_name = wrapper.context["name"] --> yeh first hash hai #
# return f"Hi {user_name} the weather in {city} is sunny with 40C"  --> # 2 second hash hai #
 return f"the weather in {city} is sunny with 40C"


simple_context_agent = Agent(
  name="Context Agent",
  instructions="You are a helpful assistant",
  tools=[fetch_weather]
)


result = Runner.run_sync(
  starting_agent=simple_context_agent, 
  input="What is weather in karachi?",
  context=local_context,
  run_config=config,
  
)

print("result>>>", result.final_output)