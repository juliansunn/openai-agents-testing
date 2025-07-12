import logging

import chainlit as cl
from agents import Agent, Runner

logger = logging.getLogger(__name__)


class WorkoutPlanningAgent:
    """Agent using the OpenAI Agents SDK for creating comprehensive workout plans."""
    
    def __init__(self):
        self.agent = Agent(
            name="Workout Planner",
            instructions="""You are a Workout Planning Agent, an expert at creating comprehensive, personalized workout plans.

Your capabilities include:
- Creating detailed workout plans based on user preferences and goals
- Analyzing user fitness history and trends
- Designing progressive training programs
- Providing exercise recommendations with proper form guidance
- Adapting plans for different fitness levels and time constraints

When creating workout plans:
1. Gather user preferences (goals, available time, fitness level, equipment access)
2. Consider historical fitness data and trends
3. Design a progressive, sustainable program
4. Include variety to prevent plateaus and maintain motivation
5. Provide clear instructions for each exercise
6. Include rest days and recovery recommendations
7. Adapt the plan based on user feedback and progress

Key areas you can help with:
- Strength training programs
- Cardiovascular fitness plans
- Flexibility and mobility routines
- Sport-specific training
- Weight loss or muscle building programs
- Rehabilitation and injury prevention
- Home vs gym workout options

Always prioritize safety, proper form, and gradual progression. Consider the user's lifestyle, schedule, and available equipment when designing plans.""",
        )
        logger.info("Created Workout Planning Agent using OpenAI Agents SDK")
    
    async def process_message(self, user_message: str) -> str:
        """Process a user message and return the agent's response."""
        try:
            # Run the agent with the user message
            result = await Runner.run(self.agent, user_message)
            return result.final_output
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return f"I encountered an error while processing your message: {str(e)}"
    
    def reset_conversation(self) -> None:
        """Reset the conversation."""
        # The Agents SDK handles conversation state automatically
        logger.info("Reset Workout Planning Agent conversation")
    
    def get_conversation_summary(self) -> dict:
        """Get a summary of the current conversation."""
        return {
            "agent_name": "Workout Planning Agent",
            "agent_type": "OpenAI Agents SDK Agent"
        }


# Initialize the workout planning agent
workout_agent = WorkoutPlanningAgent()


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Welcome to your Personal Workout Planner! 🏋️‍♂️\n\nI'm here to help you create comprehensive, personalized workout plans based on your goals, preferences, and fitness history. I can design programs for strength training, cardio, flexibility, and more.\n\nTell me about your fitness goals, available time, current fitness level, and any equipment you have access to. I'll create a detailed plan tailored just for you!"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content.strip()
    
    # Show thinking message
    await cl.Message(content="🏋️‍♂️ Creating your personalized workout plan...").send()
    
    # Process with workout planning agent
    result = await workout_agent.process_message(user_input)
    
    # Send the response
    await cl.Message(content=result).send() 