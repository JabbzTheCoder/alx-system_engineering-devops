#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API for a subreddit's subscriber count.
  
  Args:
      subreddit: The name of the subreddit to query (string).
  
  Returns:
      The subscriber count for the subreddit (integer) or 0 if invalid.
  """
  # Base URL for subreddit information
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  
  # Set custom User-Agent to avoid rate limit issues
  headers = {"User-Agent": "My Reddit API Script v1.0"}
  
  try:
    # Send GET request without following redirects
    response = requests.get(url, allow_redirects=False, headers=headers)
    
    # Check for successful response (200 OK)
    if response.status_code == 200:
      data = response.json()
      # Extract subscriber count from JSON data
      return data.get("data", {}).get("subscribers", 0)
    else:
      # Handle unsuccessful response (e.g., 404 Not Found)
      return 0
  except requests.exceptions.RequestException as e:
    # Handle any other exceptions during request
    print(f"Error: An error occurred: {e}")
    return 0