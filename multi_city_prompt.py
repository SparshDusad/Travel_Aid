def build_multi_city_prompt(cities, days, interests, budget, pace, style):
    per_city_days = days // len(cities)
    return f"""
    Plan a {days}-day multi-city itinerary for: {', '.join(cities)}.
    - Days per city: ~{per_city_days}
    - Interests: {interests}
    - Budget: {budget}
    - Pace: {pace}
    - Style: {style}
    """
