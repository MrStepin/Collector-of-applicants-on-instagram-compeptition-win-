Finder_of_winners_in_instagram_competition
=====================
Description how to work this script:  
This script is collect applicants on instagram competition winner.  
Script provide you users, which:  liked post, followed page, added comment with name of any friend.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```pip install -r requirements.txt```

How to use this script:  
* Create file with name ```.env``` which contain you instagram login and password like this ```login=123``` ```password=111```
* Add name page with competition to``` bot.get_user_followers("beautybar.rus") ```   
in ``` def followers(exist_and_likers_user_list):   
    for existing_user_id in exist_and_likers_user_list:
        followers_user_list = bot.get_user_followers("beautybar.rus")	
        if followers_user_list[0] != existing_user_id[0]:
            exist_and_likers_user_list.remove(existing_user_id)
    return exist_and_likers_user_list ```
* Execute in CMD this script with URL as arguments
For example:  
```Finder_of_winners_in_instagram_competition.py "https://www.instagram.com/p/BtON034lPhu/"```

Script will works several minutes(it depends from qty of comments)
Result: 
``` ```
