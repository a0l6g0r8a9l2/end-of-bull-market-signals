from googleapiclient.discovery import build
from datetime import date
from dotenv import load_dotenv
import os

# Load API key from environment variable
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Create YouTube service object
youtube = build('youtube', 'v3', developerKey=API_KEY)


def get_channel_info(channel_id: str) -> dict:
    """
    Retrieves view and subscriber count for a given YouTube channel ID.

    Args:
        channel_id (str): The ID of the YouTube channel.

    Returns:
        dict: A dictionary containing the channel's view count and subscriber count.

    Raises:
        Exception: If an error occurs during API request execution.
    """

    try:
        channel = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()
        view_count = int(channel['items'][0]['statistics']['viewCount'])
        subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        return {"viewCount": view_count, "subscriberCount": subscriber_count}

    except Exception as e:
        print(f"Error retrieving channel info for ID {channel_id}: {e}")
        return {"viewCount": None, "subscriberCount": None}


def search_crypto_channels_yt_first_page() -> dict:
    """
    Searches YouTube for cryptocurrency channels on the first page (max 50 results).

    Returns:
        dict: A dictionary containing channel IDs as keys and channel titles as values.

    Raises:
        Exception: If an error occurs during API request execution.
    """

    try:
        search_response = youtube.search().list(
            q='crypto|bitcoin|eth|altcoins|cryptocurrency',
            part='snippet',
            type='channel',
            regionCode='US',
            maxResults=50
        ).execute()

        channels = {}
        for item in search_response['items']:
            channel_id = item['snippet']['channelId']
            title = item['snippet']['channelTitle']
            channels[channel_id] = title
        return channels

    except Exception as e:
        print(f"Error searching for crypto channels: {e}")
        return {}


def get_views_and_subscribers() -> list:
    """
    Searches for cryptocurrency channels, retrieves their view and subscriber counts,
    and returns the data in a list of dictionaries.

    Returns:
        list: A list of dictionaries, each containing channel information:
              - id (str)
              - title (str)
              - viewCount (int)
              - subscriberCount (int)
              - date (date)
    """

    channels = []
    today = date.today()

    # Get channel IDs from first page search
    channel_ids = search_crypto_channels_yt_first_page()

    for channel_id, title in channel_ids.items():
        channel_info = get_channel_info(channel_id)
        channels.append({
            "id": channel_id,
            "title": title,
            "viewCount": channel_info["viewCount"],
            "subscriberCount": channel_info["subscriberCount"],
            "date": today
        })

    return channels