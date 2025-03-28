import streamlit as st
import random

# Expanded dataset with Indian & global destinations
destinations_data = {
    "Indore": {
        "places": ["Rajwada Palace", "Sarafa Bazaar", "Patalpani Waterfall", "Lal Bagh Palace", "Chhappan Dukan"],
        "food": ["Poha & Jalebi", "Bhutte ka Kees", "Dal Bafla", "Khopra Patties", "Sabudana Khichdi"],
        "activities": ["Street food tour", "Temple visit", "Photography", "Shopping", "Nature walk"],
    },
    "Mumbai": {
        "places": ["Gateway of India", "Marine Drive", "Juhu Beach", "Siddhivinayak Temple", "Colaba Causeway"],
        "food": ["Vada Pav", "Pav Bhaji", "Misal Pav", "Bhel Puri", "Bombay Sandwich"],
        "activities": ["Beach walk", "Shopping", "Bollywood tour", "Street food crawl", "Ferry ride"],
    },
    "Jaipur": {
        "places": ["Hawa Mahal", "Amber Fort", "City Palace", "Jantar Mantar", "Nahargarh Fort"],
        "food": ["Dal Baati Churma", "Pyaaz Kachori", "Ghewar", "Laal Maas", "Ker Sangri"],
        "activities": ["Fort exploration", "Cultural shows", "Shopping", "Hot air balloon ride", "Elephant safari"],
    },
    "Varanasi": {
        "places": ["Kashi Vishwanath Temple", "Dashashwamedh Ghat", "Sarnath", "Manikarnika Ghat", "Ramnagar Fort"],
        "food": ["Banarasi Paan", "Malaiyyo", "Kachori Sabzi", "Chaat", "Thandai"],
        "activities": ["Ganga Aarti", "Boat ride", "Temple visits", "Silk shopping", "Photography"],
    },
    "Kerala": {
        "places": ["Munnar", "Alleppey Backwaters", "Kovalam Beach", "Wayanad", "Thekkady"],
        "food": ["Appam & Stew", "Puttu & Kadala", "Karimeen Pollichathu", "Sadya", "Banana Chips"],
        "activities": ["Houseboat stay", "Beach relaxation", "Tea plantation visit", "Ayurvedic spa", "Wildlife safari"],
    },
    "Delhi": {
        "places": ["Red Fort", "Qutub Minar", "India Gate", "Lotus Temple", "Humayun’s Tomb"],
        "food": ["Chole Bhature", "Parathas", "Butter Chicken", "Dahi Bhalla", "Gol Gappa"],
        "activities": ["Historical sightseeing", "Street food tour", "Shopping", "Museum visits", "Heritage walks"],
    },
    "Goa": {
        "places": ["Baga Beach", "Dudhsagar Falls", "Fort Aguada", "Basilica of Bom Jesus", "Anjuna Market"],
        "food": ["Goan Fish Curry", "Pork Vindaloo", "Bebinca", "Sorpotel", "Prawn Balchão"],
        "activities": ["Beach hopping", "Water sports", "Nightlife", "Casino cruise", "Portuguese heritage walk"],
    },
}

def generate_itinerary(destination, duration, budget, preferences, accommodation, mobility):
    itinerary = []
    places = destinations_data.get(destination, {}).get("places", ["Famous Landmark", "City Park"])
    foods = destinations_data.get(destination, {}).get("food", ["Popular Dish 1", "Popular Dish 2"])
    activities = destinations_data.get(destination, {}).get("activities", ["Sightseeing", "Food tasting"])

    random.shuffle(places)
    random.shuffle(foods)
    random.shuffle(activities)

    for day in range(duration):
        place = places[day % len(places)]
        food = foods[day % len(foods)]
        activity = activities[day % len(activities)]

        day_plan = f"""
        *Day {day + 1}:*  
        - *Morning:* Visit {place} 🏛  
        - *Afternoon:* Try {food} 🍽  
        - *Evening:* {activity} or relax at your {accommodation} 🏨  
        - *Budget Level:* {budget} 💰  
        - *Mobility Considerations:* {mobility} 🚶‍♂
        """
        itinerary.append(day_plan)
    
    return "\n".join(itinerary)

st.title("✈ Personalized Travel Itinerary Generator")
destination = st.text_input("🌍 Destination", placeholder="Enter a city (e.g., Mumbai, Jaipur, Kerala, Tokyo)")
duration = st.number_input("📅 Duration (Days)", min_value=1, max_value=14, value=3)
budget = st.selectbox("💰 Budget", ["Low", "Moderate", "High"])
preferences = st.text_input("🏞 Interests", placeholder="E.g., adventure, history, food")
accommodation = st.selectbox("🏨 Stay", ["Luxury", "Budget", "Cozy Homestay"])
mobility = st.text_input("🚶‍♂ Mobility Concerns", placeholder="E.g., walking tolerance, wheelchair access")

if st.button("Generate Itinerary"):
    if not destination:
        st.error("Please enter a destination.")
    elif destination not in destinations_data:
        st.error("City not found! Try Mumbai, Jaipur, Varanasi, Kerala, etc.")
    else:
        with st.spinner("Building your perfect travel plan..."):
            itinerary = generate_itinerary(destination, duration, budget, preferences, accommodation, mobility)
        st.subheader("🗺 Your Personalized Itinerary:")
        st.write(itinerary)