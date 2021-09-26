README

This program contains simple code segments that were used to explore the functions of the Twitter API. The tweepy library was imported in Python, and was used to access the Twitter API. I focused on functions that I may want to utilize within the next phase of the project 2. In addition, tweepy documentation https://docs.tweepy.org/en/v4.0.0/api.html
and stackoverflow were used to generate and gain reference for these tests, specifically for syntax correction and reference. 


The first example was to retrieve the usernames of tweets that appeared in the authenticated user's home_timeline. The results were as expected, displaying the usernames of the displayed tweets on the timeline. This was based on Tweepy documentation with slight modification. 


The second test was to obtain information regarding a specific Twitter user. In this case, the NASA account was used for this test. I wanted to explore the api.user_timeline and user api functionality.
To do this, the username was specified and retrieved, followed by the id of the Twitter user. The test was designed to retrieve the 5 most recent tweets from NASA using the api.user_timeline.
Following this, a simple iteration was performed to obtain the id number, text, and location of the tweet. The authenticated user could then favorite a tweet given the id information provided from the iteration. 
One thing to note about the results, however, is that if a tweet has already been favorited, the program will produce an error and specify that the tweet has already been favorited. In this case,
the stream listener used after this code would not run.  

The third test was to explore the authenticated user and the api functions associated with them. In this case, I explored updating the profile description using the provided api.update_profile. 
I also tried updating the profile with certain conditions; in this test, I updated the profile description of my test account should the number of followers on NASA's account should change, and display that number in the profile description.
The output was expected as the profile description did update and provided the current follower count of NASA's Twitter account; however, the page must be refreshed for changes to appear. 
If the username is not spelled correctly, an error would occur (code 50) that states the user could not be found. 


The fourth test was designed to test a stream listener. In this case, tweets were to be printed in real-time from a specified user. To do this, the stream was filtered and was set to stream only tweets from the NASA account by supplying the specified id. 
The stream listener can also filter by tweets with certain phrases which was tested and successfully output the expected results. 
