import streamlit as st
from genai_travel import generate_itinerary
from weather import get_weather_summary
from email_utils import send_email_with_attachment
from storage import save_itinerary, load_itinerary
from maps import generate_google_map_link
from datetime import datetime
import os
import json

st.set_page_config(page_title="TravelGPT - AI Trip Planner", page_icon="👛", layout="wide")

st.title("TravelGPT 👛")
st.caption("Your personalized AI-powered travel concierge")

# Sidebar Input
with st.sidebar:
    st.header("🔧 Plan Settings")
    destination = st.text_input("🌍 Destination", placeholder="e.g., Italy")
    days = st.slider("🗓️ Trip Length (days)", 1, 30, 5)
    travel_style = st.selectbox("🛋️ Style", ["Solo", "Couple", "Family", "Adventure", "Luxury", "Budget"])
    interests = st.text_area("🔎 Interests", placeholder="museums, hiking, food...")
    pace = st.radio("⚡ Pace", ["Relaxed", "Moderate", "Packed"])
    budget = st.select_slider("💲 Budget", ["Low", "Medium", "High"])
    user_email = st.text_input("📧 Email (optional, for sending itinerary)")
    trip_name = st.text_input(":bookmark: Trip Name", placeholder="My Italy Trip")
    generate_btn = st.button(":airplane: Generate Itinerary")

if generate_btn:
    if not destination:
        st.error("Please enter a destination.")
    else:
        with st.spinner("Getting weather data..."):
            weather_summary = get_weather_summary(destination)

        with st.spinner("Creating AI itinerary..."):
            plan = generate_itinerary(destination, days, interests, budget, pace, travel_style, weather_summary)

        st.success("Here's your AI-powered itinerary!")

        # Show map link
        st.markdown(f"[View {destination} on Google Maps]({generate_google_map_link(destination)})")

        # Display itinerary in expandable sections
        for i, day_block in enumerate(plan.split("Day ")):
            if i == 0: continue
            parts = day_block.split("\n", 1)
            if len(parts) == 2:
                title, content = parts
                with st.expander(f"Day {title.strip()}"):
                    st.markdown(content)

        # Optional email sending
        if user_email:
            with st.spinner("Sending itinerary to email..."):
                try:
                    send_email_with_attachment(user_email, f"Your {trip_name} Itinerary", "Please find your plan attached.", None)
                    st.success("Email sent successfully!")
                except Exception as e:
                    st.error(f"Failed to send email: {str(e)}")

        # Save itinerary
        with open(os.path.join("data", f"{trip_name}.json"), "w", encoding="utf-8") as f:
            json.dump({
                "destination": destination,
                "plan": plan,
                "created_at": datetime.now().isoformat()
            }, f, indent=2)

# History Section
st.markdown("---")
st.subheader(":open_file_folder: View Saved Itineraries")
trip_to_load = st.selectbox("Select a saved trip:", options=os.listdir("data") if os.path.exists("data") else [])

if trip_to_load:
    with open(os.path.join("data", trip_to_load), "r", encoding="utf-8") as f:
        loaded = json.load(f)
    st.markdown(f"**Trip Name**: {trip_to_load}")
    st.markdown(f"**Destination**: {loaded.get('destination')}")
    st.markdown(loaded.get("plan"))