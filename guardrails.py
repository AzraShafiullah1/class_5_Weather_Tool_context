from pydantic import BaseModel



from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    input_guardrail,
)

from my_config import config


class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)

@input_guardrail
async def math_guardrail( 
     context: RunContextWrapper, agent: Agent, input: str 
) -> GuardrailFunctionOutput:
    print(f"guardrail is running with {input}")
    return GuardrailFunctionOutput(
    output_info="",
    tripwire_triggered=False,
    )
  

agent = Agent(  
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
)

result = Runner.run_sync(agent, "Hello, can you help me solve for x: 2x + 3 = 11?",run_config=config)

print("result>>>",result.final_output)