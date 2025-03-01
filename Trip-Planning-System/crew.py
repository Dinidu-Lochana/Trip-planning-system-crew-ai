from crewai import Crew, Process
from agents import destination_recommender, budget_planner, itinerary_generator
from tasks import create_tasks

# User input
origin = input("Enter your departure city: ")
budget = float(input("Enter your total budget (in USD): "))
interests = input("Enter your travel interests (comma-separated): ").split(',')
trip_days = int(input("Enter the duration of your trip (in days): "))


user_inputs = {
    'origin': origin,
    'budget': budget,
    'interests': interests,
    'trip_days': trip_days
}


tasks = create_tasks(user_inputs)

# Crew User inputs
crew = Crew(
    agents=[destination_recommender, budget_planner, itinerary_generator],
    tasks=tasks,
    process=Process.sequential,  
)

# Trip planning process
result = crew.kickoff(inputs=user_inputs)

# Output
print("\n✨ Your Trip Plan ✨\n")
print(result)