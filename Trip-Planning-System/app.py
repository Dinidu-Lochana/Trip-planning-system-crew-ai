import streamlit as st
from crewai import Crew, Process
from agents import destination_recommender, budget_planner, itinerary_generator
from tasks import create_tasks
import asyncio
import nest_asyncio

# Nest_asyncio for fix asyncio event loop issues
nest_asyncio.apply()

def main():
    st.title("🌍 AI-Powered Trip Planner")
    st.markdown("Plan your next trip with AI-powered recommendations. Let's make your travel dreams come true!")

    with st.form("trip_form"):
        st.subheader("✈️ Trip Details")
        # Inputs
        origin = st.text_input("Enter your departure city:", placeholder="e.g., New York")
        budget = st.number_input("Enter your total budget (in USD):", min_value=100, step=50, value=1000)
        interests = st.text_input("Enter your travel interests (comma-separated):", placeholder="e.g., beaches, hiking, museums" )
        trip_days = st.number_input("Enter the duration of your trip (in days):", min_value=1, step=1, value=7)
        submit_button = st.form_submit_button("Plan My Trip")

    if submit_button:
        with st.spinner("✨ Generating your trip plan... Please Wait..."):
            user_inputs = {
                "origin": origin,
                "budget": budget,
                "interests": [i.strip() for i in interests.split(",")],
                "trip_days": trip_days
            }

            tasks = create_tasks(user_inputs)

            # Crew User inputs
            crew = Crew(
                agents=[destination_recommender, budget_planner, itinerary_generator],
                tasks=tasks,
                process=Process.sequential,
                verbose=True
            )

            result = crew.kickoff()

        st.success("✅ Your AI-powered trip plan is ready!")
        st.markdown("---")
        st.subheader("📝 Your Trip Plan")
        st.markdown(result )

if __name__ == "__main__":
    main()
