from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.environ.get("GOOGLE_API_KEY")  # must be set in Streamlit Secrets
)
def generate_itinerary(destination, days, interests, budget, pace, style, weather_note=""):
    prompt = f"""
    Plan a {days}-day itinerary for {destination}.
    - Interests: {interests}
    - Budget: {budget}
    - Pace: {pace}
    - Style: {style}
    {f"- Weather notes: {weather_note}" if weather_note else ""}
    
    For each day, split into Morning, Afternoon, Evening.
    Include local food, hidden gems, activities, cultural tips.
    """
    return model.invoke([HumanMessage(content=prompt)]).content
