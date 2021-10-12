import tweepy
import wget

# Authentication requirements
auth = tweepy.OAuthHandler("//", "//")
auth.set_access_token("//", "//")

api = tweepy.API(auth)

# Get the username of the account we want to use

username_input = input("""Please enter the username of the user you wish to see (case-sensitive): """)

# Find the user on twitter and obtain the associated id

selected_user = api.get_user(username_input)
selected_user_id = selected_user.id_str

# Setup to explore the selected user

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
            favorite_response = input("Would you like to favorite this tweet (Y/n)? ").lower()

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

# Download the media into a specified folder/path

path_for_download = "path/for/download"
for download in download_files:
    wget.download(download, out=path_for_download)

print("Finished.")


