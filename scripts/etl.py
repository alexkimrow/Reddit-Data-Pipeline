from googleapiclient.discovery import build
import csv
import os
import pandas as pd

# Initialize the YouTube API client
api_key = "AIzaSyApUza12jSo55p41Go8zOa2x9wWiAhs5y0"
video_id = "q8q3OFFfY6c"  # Example video ID
youtube = build("youtube", "v3", developerKey=api_key)


def get_video_comments(video_id, max_results=100):
    """Extract comments from the specified YouTube video."""
    comments = []
    results = (
        youtube.commentThreads()
        .list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText",
        )
        .execute()
    )

    while results:
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            authorDisplayName = item["snippet"]["topLevelComment"]["snippet"][
                "authorDisplayName"
            ]
            publishedAt = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
            likeCount = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            authorChannelId = (
                item["snippet"]["topLevelComment"]["snippet"]
                .get("authorChannelId", {})
                .get("value", "N/A")
            )
            commentId = item["snippet"]["topLevelComment"]["id"]

            comments.append(
                {
                    "comment": comment,
                    "authorDisplayName": authorDisplayName,
                    "publishedAt": publishedAt,
                    "likeCount": likeCount,
                    "authorChannelId": authorChannelId,
                    "commentId": commentId,
                }
            )

        # Check if there are more pages
        if "nextPageToken" in results:
            page_token = results["nextPageToken"]
            results = (
                youtube.commentThreads()
                .list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=max_results,
                    pageToken=page_token,
                    textFormat="plainText",
                )
                .execute()
            )
        else:
            break

    return comments


def load_data(comments, filename="data/youtube_comments.csv"):
    """Load the comments data into a CSV file under the 'data' directory."""
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df = pd.DataFrame(comments)
    df.to_csv("data/raw_comments.csv", index=False)


def main():
    """The main ETL process."""
    comments = get_video_comments(video_id)
    load_data(comments)
    print("ETL process completed successfully.")


if __name__ == "__main__":
    main()
