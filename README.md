Finder_of_winners_in_instagram_competition
=====================
Description how to work this script:  
This script is collect applicants on instagram competition winner.  
Script provide you users, which:  liked post, followed page, added comment with name of any friend.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```pip install -r requirements.txt```

How to use this script:  
* Create file with name ```.env``` which contain you instagram login and password like this ```login=123``` ```password=111```
* Execute in CMD this script with URL of competition and name of page as arguments
For example:  
```Finder_of_winners_in_instagram_competition.py "https://www.instagram.com/p/BtON034lPhu/" "beautybar.rus"```

Script will works several minutes(it depends from qty of comments)
Result: 
```
1. koshkaanka
2. coolsonic2014
3. iorlaa
4. lybava19
5. oksanapogonina
6. aleksa22koss ```
