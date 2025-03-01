from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import serper_tool

load_dotenv()

# Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True, # Getting all details
                             termperature=0.5, # Randomness
                             google_api_key=os.getenv(GOOGLE_API_KEY))

# Destination Recommender Agent
destination_recommender = Agent(
    role="Destination Recommender",
    goal='Suggest the best travel destinations based on user preferences like budget, travel type, and climate.',
    verbose=True,  # Give more info
    memory=True,
    backstory=(
        "With an in-depth understanding of various travel destinations and user preferences, "
        "your mission is to help users discover the best places for their next adventure."
    ),
    tools=[serper_tool],
    llm=llm,
    allow_delegation=True, # Communication with other agents
)

# Budget Planner Agent
budget_planner = Agent(
    role="Budget Planner",
    goal='Break down the total travel budget into categories like flights, accommodation, activities, and meals.',
    verbose=True,  # Give more info
    memory=True,
    backstory=(
        "You are skilled in organizing finances, with a keen eye for balancing the travel budget, "
        "ensuring every aspect of the trip is affordable while maintaining the quality of the experience."
    ),
    tools=[serper_tool],
    llm=llm,
    allow_delegation=True, # Communication with other agents
)

# Itinerary Generator Agent
itinerary_generator = Agent(
    role="Itinerary Generator",
    goal='Create a day-by-day travel itinerary based on the destination and user preferences for activities.',
    verbose=True,  # Give more info
    memory=True,
    backstory=(
        "Your expertise lies in crafting detailed itineraries, ensuring every day of the trip is packed with memorable experiences "
        "that align with the user’s interests, whether it’s sightseeing, adventure, or relaxation."
    ),
    tools=[serper_tool],
    llm=llm,
    allow_delegation=True, # Communication with other agents
)

