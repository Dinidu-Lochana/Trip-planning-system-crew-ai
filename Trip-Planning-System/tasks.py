from crewai import Task
from tools import serper_tool
from agents import destination_recommender,budget_planner,itinerary_generator


# Destination Recommender Task
destination_recommender_task = Task(
    description=(
        "Analyze user preferences to suggest the best travel destinations."
        "Consider factors such as budget, travel type (adventure, luxury, backpacking),"
        "weather preferences, and accessibility."
        "Provide a ranked list of recommended destinations with brief explanations."
    ),
    expected_output="A list of 3-5 recommended travel destinations with reasons for selection.",
    tools=[serper_tool], 
    agent=destination_recommender,
)

# Budget Planner Task
budget_planner_task = Task(
    description=(
        "Create a detailed budget breakdown for the selected destination."
        "Calculate costs for flights, accommodation, meals, activities, and transportation."
        "Ensure the budget is optimized based on the user's total spending limit."
    ),
    expected_output="A structured breakdown of estimated expenses across key travel categories.",
    tools=[serper_tool],  
    agent=budget_planner,
)

# Itinerary Generator Task
itinerary_generator_task = Task(
    description=(
        "Generate a day-by-day itinerary for the selected travel destination."
        "Include suggested activities, sightseeing spots, dining options, and local experiences."
        "Ensure the itinerary aligns with the user's interests and trip duration."
    ),
    expected_output="A well-structured itinerary with daily activity recommendations.",
    tools=[serper_tool],  
    agent=itinerary_generator,
)


