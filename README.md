tool_for_instagram_competition
=====================
 
This script collects applicants on winner of instagram competition.  
Applicants should: like post; follow page; add comment with name of any friend;  

Python3 should be installed.  
Use pip to install dependencies:  
```pip install -r requirements.txt```

How to use this script:  
* Create file  ```.env``` with you instagram login and password, like this: ```LOGIN=123``` ```PASSWORD=111```
* Execute this script in CMD with URL of competition and name of page as arguments.
For example:  
```python tool_for_instagram_competition.py "https://www.instagram.com/p/BtON034lPhu/" "beautybar.rus"```

Script will work for several minutes (it depends from qty of comments)
Result: 
```
1. koshkaanka
2. coolsonic2014
3. iorlaa
4. lybava19
5. oksanapogonina
6. aleksa22koss 
```
