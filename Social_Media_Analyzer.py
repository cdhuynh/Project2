import tweepy
import wget
import pytest
import os

# Authentication requirements
auth = tweepy.OAuthHandler("...", "...")
auth.set_access_token("...",
                      "...")

api = tweepy.API(auth)

# Get the username of the account we want to use

username_input = input("""Please enter the username of the user you wish to see (case-sensitive): """)

# Find the user on twitter and obtain the associated id
#

if not username_input.isalnum():
    print("Not a valid input. Ending program.")
    quit()
else:
    selected_user = api.get_user(username_input)
    selected_user_id = selected_user.id_str

# Setup to explore the selected user timeline.

selected_user_timeline = tweepy.Cursor(api.user_timeline, tweet_mode="extended", id=selected_user_id).items(20)

download_files = set()

# For the tweets in the selected user timeline, we scan to see if their is media.

for tweet in selected_user_timeline:
    if 'media' in tweet.entities:

        # Obtain the tweet id for use in creating a favorite if desired
        tweet_with_media_id = tweet.id

        for media in tweet.entities['media']:

            # Print the media url to determine whether or not to save the tweet
            print(media['media_url'])
            download_files.add(media['media_url'])

            # Determine whether or not to create a favorite
            favorite_response = input("""Would you like to favorite this tweet (Y/n/skip)?: """).lower()

            if favorite_response == "yes" or favorite_response == "y":
                tweet_status = api.get_status(tweet_with_media_id)
                is_tweet_favorite = tweet_status.favorited
                if is_tweet_favorite:
                    print("Tweet already in favorites. Moving on...")
                    print("\n")
                elif not is_tweet_favorite:
                    print("Adding to favorites...")
                    api.create_favorite(tweet_with_media_id)
                    print("\n")
            elif favorite_response == "no" or favorite_response == "n":
                print("Tweet will not be added to favorites...")
                print("\n")
            elif favorite_response == "s" or favorite_response == "skip":
                print("Skipping...")

# Download the media into a specified folder/path

path_for_download = "path/for/download"
for download in download_files:
    wget.download(download, out=path_for_download)

print("Finished.")


def test_username_search():
    # check if the username is valid with alpha/numeric characters and no whitespaces.
    assert username_input.isalnum()


def test_selected_user_credentials():
    # if there is no valid username:
    # make sure that credentials are not obtained and these vars do not have any value.
    if not username_input.isalnum():
        assert selected_user is None
        assert selected_user_id is None


def test_favorite_response():
    # Check that the favorite response is valid characters and no numbers
    # Check for either yes, no, and that corresponding favorite creation responds accordingly.
    assert favorite_response.isalpha()

    if favorite_response == "yes" or "y":
        assert api.create_favorite(tweet_with_media_id)
    elif favorite_response == "no" or "n":
        assert api.create_favorite(tweet_with_media_id) is None
    elif favorite_response == "s" or "skip":
        assert print("Skipping...")
    else:
        assert False


def test_file_path():
    # Check for a valid path for download.
    assert os.path.exists(path_for_download)