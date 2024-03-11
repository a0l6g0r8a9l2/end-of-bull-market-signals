import time
import schedule
from app.database import Base, engine, SessionLocal
from services.yt_channels import get_views_and_subscribers
from app.schemas import Channel

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)


# Dependency for database connection
def get_db():
    """
    Yields a database session object for use within a context manager.
    Closes the session automatically after use.

    Returns:
        SessionLocal: A database session object.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def store_views_and_subscribers():
    """
    Retrieves YouTube channel data using the `get_views_and_subscribers` function,
    creates Channel objects, and stores them in the database.

    Raises:
        Exception: If an error occurs during data retrieval or database operations.
    """
    try:
        data = get_views_and_subscribers()
        session = next(get_db())

        channel_objects = []
        for item in data:
            channel_objects.append(
                Channel(
                    channel_id=item["id"],
                    channel_title=item["title"],
                    view_count=item["viewCount"],
                    subscriber_count=item["subscriberCount"],
                    created_at=item["date"],
                )
            )

        session.add_all(channel_objects)
        session.commit()

        print("Views and subscribers YT data stored successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Schedules the `store_views_and_subscribers` function to run daily at 00:05.
    Starts the scheduling loop to continuously check for jobs.
    """

    schedule.every().day.at("00:05").do(store_views_and_subscribers)

    while True:
        schedule.run_pending()
        time.sleep(5)  # Adjust sleep time as needed (e.g., 60 seconds)


if __name__ == "__main__":
    main()
