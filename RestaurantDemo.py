import requests
import json

def main():
    # Take city name as input
    city = input("Enter the city name -")

    # Setting the SerpAPI key(hardcoded)
    api_key = "2f2ba5aafd7eb22ba05952634f4f945a47af76e4bb31a1350c9097c9a0425bb5"

    # Define parameters required for the Google search
    params = {
        "engine": "google_local",
        "q": f"top restaurants in {city}",
        "api_key": api_key
    }

    # Send the GET request to SerpAPI
    response = requests.get("https://serpapi.com/search", params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error fetching the data ")
        return

    data = response.json()

    # Extract restaurant list
    restaurants = data.get("local_results", [])

    # If no results found stops the execution
    if not restaurants:
        print(f"No restaurant results found for '{city}'. Please try a different city.")
        return

   # Sort restaurants by rating and then by number of reviews
    def sort_key(item):
        return item.get("rating"), item.get("reviews")


  # Apply custom sort, highest rated restaurants first
    sorted_restaurants = sorted(restaurants, key=sort_key, reverse=True)

    # Prepare the result dictionary
    results = {}
    for restaurant in sorted_restaurants[:10]:
        name = restaurant.get("title")
        rating = restaurant.get("rating")
        reviews = restaurant.get("reviews")
        address = restaurant.get("address")

        if name:  # Only include if restaurant has a name
            results[name] = {
                "rating": rating,
                "reviews": reviews,
                "address": address
            }

    # Save the results to a JSON file
    with open("restaurants.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Top 10 restaurants saved to restaurants.json")

# Call the main function
main()
