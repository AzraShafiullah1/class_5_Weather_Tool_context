from agents import Agent, Runner, function_tool
from my_config import config
from typing_extensions import TypedDict
from typing_extensions import TypedDict


class MyDataType(TypedDict):
    num : int
    num2 : int
    sum: int

@function_tool
async def fetch_weather(city: str) -> str:
    """
    Fetch weather according to the given city

    Args:
        city: city for weather
    """
    return f"the weather in {city} is sunny with 40C"

simple_agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    #tools=[fetch_weather],
    output_type=MyDataType
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input="what is 2 plus 5",
    run_config=config
)

print("Result>>>>", result.final_output)
print("Result Type>>>", type(result.final_output))
