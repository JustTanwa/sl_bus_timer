#!/usr/bin/env python3
import requests
import json
import dotenv
import os
# Load environment variables from .env file
dotenv.load_dotenv()

def fetch_bus_times(site_id):
    """
    Fetches bus departure times for a given site ID using the Trafiklab SL Transport API.

    Args:
        site_id (int): The unique identification number for the stop/site.

    Returns:
        dict: A dictionary containing the API response, or None if an error occurs.
    """
    base_url = "https://transport.integration.sl.se/v1/sites"
    endpoint = f"{base_url}/{site_id}/departures"

    try:
        response = requests.get(endpoint)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def summarize_departures(data, site_id='N/A'):
    """
    Summarizes the departure information from the API response.

    Args:
        data (dict): The JSON response from the API.
    """
    if data and "departures" in data:
        print(f"--- Departures for Site ID: {site_id} ---")
        if not data["departures"]:
            print("No departures found for this site at the moment.")
            return

        for departure in data["departures"]:
            direction = departure.get("direction", "N/A")
            destination = departure.get("destination", "N/A")
            scheduled_time = departure.get("scheduled", "N/A")
            expected_time = departure.get("expected", "N/A")
            display_time = departure.get("display", "N/A")
            transport_mode = departure.get("transport", {}).get("name", "N/A")
            line_number = departure.get("journey", {}).get("line", "N/A")

            print(f"  Transport: {transport_mode} {line_number}")
            print(f"  Direction: {direction} (Destination: {destination})")
            print(f"  Scheduled: {scheduled_time}")
            print(f"  Expected: {expected_time}")
            print(f"  Display Time: {display_time}")
            print("-" * 30)
    else:
        print("No departure data available or invalid response format.")

def main():
    departures_data = fetch_bus_times(os.getenv('SITE_ID')) 

    if departures_data:
        summarize_departures(departures_data)
    else:
        print("Failed to retrieve departure data.")

if __name__ == "__main__":
    main()