import chainlit as cl

from agency import WorkoutPlanningAgent

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