This Python script fetches the top 10 restaurants for a given city using the SerpAPI Google Local API. It extracts restaurant details like name, rating, reviews, and address, then saves the results into a json file.

Approach

1.User Input: The script prompts the user to enter a city name.

2.SerpAPI Request: It sends a GET request to SerpAPI using the Google Local engine, querying for "top restaurants in <city>".

3.Data Extraction: The response is parsed, and restaurant data is extracted from the local_results field.

4.Sorting Logic: Results are sorted by:

-Rating (highest first)

-Number of reviews (as a secondary sort key)

5.JSON Output: The top 10 restaurants are saved to restaurants.json 

Challenges Faced

1.Finding a reliable data source:
Initial attempts to scrape data from sites like Yelp failed because it got stuck in a captcha loop while logging in

2.Choosing SerpAPI:

After exploring alternatives, SerpAPI was chosen because it provided structured results through a proper REST API.

3.Understanding API Parameters & Output:

Time was spent reviewing SerpAPI documentation to understand:

-Required parameters (engine, q, api_key)

-What fields the API returns (local_results, title, rating, reviews, address)

