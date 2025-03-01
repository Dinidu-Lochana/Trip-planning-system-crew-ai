from crewai import Task
from tools import serper_tool
from agents import destination_recommender, budget_planner, itinerary_generator
from textwrap import dedent

def create_tasks(user_inputs):
    """Generate task descriptions dynamically using user inputs"""
    origin = user_inputs["origin"]
    budget = user_inputs["budget"]
    interests = user_inputs["interests"]
    trip_days = user_inputs["trip_days"]

    # Destination Recommender Task
    destination_recommender_task = Task(
        description=dedent(f"""
            Analyze and recommend the best travel destinations based on
            user preferences such as budget, preferred climate, travel
            type (adventure, luxury, backpacking), and accessibility.

            This task involves evaluating multiple destinations, considering
            factors like seasonal weather, visa requirements, local attractions,
            and average travel costs.

            Your final answer must be a detailed report on the top recommended
            destinations, including a summary of their main attractions,
            estimated costs, and the best time to visit.

            Budget Range: {budget}
            Interests: {', '.join(interests)}
        """),
        agent=destination_recommender,
        tools=[serper_tool],
        expected_output="Detailed report on the best destinations including key attractions, estimated travel costs, and best travel seasons."
    )

    # Budget Planner Task
    budget_planner_task = Task(
        description=dedent(f"""
            Generate a detailed budget breakdown for the selected destination, 
            ensuring that all major expenses are covered and optimized within 
            the user's spending limit.

            This budget should account for:
            - Flight costs (round-trip from {origin})
            - Accommodation options (hotels, Airbnb, hostels)
            - Daily meal expenses based on preferred dining style
            - Activities and sightseeing costs
            - Local transportation (public transport, taxis, rentals)
            - Additional expenses (insurance, shopping, emergency funds)

            The budget must be realistic, considering seasonal price fluctuations 
            and exchange rates. Optimize the spending plan while ensuring a 
            high-quality travel experience.

            Your final answer MUST include a clear and structured cost breakdown 
            per category, along with recommendations for saving money without 
            compromising the experience.

            Budget Limit: {budget}
            Trip Duration: {trip_days} days
        """),
        agent=budget_planner,
        tools=[serper_tool],
        expected_output="A structured breakdown of estimated expenses across key travel categories, with recommendations for cost optimization."
    )

    # Itinerary Generator Task
    itinerary_generator_task = Task(
        description=dedent(f"""
            Expand this guide into a full {trip_days}-day travel itinerary 
            with detailed per-day plans, including weather forecasts, places 
            to eat, packing suggestions, and a budget breakdown.

            You MUST suggest actual places to visit, actual hotels to stay in, 
            and actual restaurants to go to, ensuring each recommendation is 
            relevant to the traveler’s interests.

            This itinerary should cover all aspects of the trip, from arrival 
            to departure, integrating destination insights with practical 
            travel logistics.

            Your final answer MUST be a complete expanded travel plan, 
            formatted as markdown, encompassing a daily schedule, anticipated 
            weather conditions, recommended clothing and items to pack, and a 
            detailed budget, ensuring THE BEST TRIP EVER.

            Be specific and justify each recommendation – explain why you chose 
            each place, what makes them special, and how they contribute to 
            an unforgettable experience!

            Trip Duration: {trip_days} days
            Traveling from: {origin}
            Traveler Interests: {', '.join(interests)}
        """),
        agent=itinerary_generator,
        tools=[serper_tool],
        expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown."
    )

    return [destination_recommender_task, budget_planner_task, itinerary_generator_task]
