def generate_google_map_link(destination):
    return f"https://www.google.com/maps/search/?api=1&query={destination.replace(' ', '+')}"
