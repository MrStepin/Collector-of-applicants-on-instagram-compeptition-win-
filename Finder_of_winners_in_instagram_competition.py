import os, instabot
from instabot import Bot 
from dotenv import load_dotenv
import re
import argparse
import sys

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    return parser

def get_comments(all_comments):
    comments = []
    correct_comment = re.findall(r"@([a-zA-Z0-9]{1,15})", str(comment_text["text"]))
    for comment_text in all_comments:
        if correct_comment !=[]:
            comments.append(correct_comment)
    return comments

def is_user_exist(user_id):
    return user_id == None

def get_likers_users(existing_users):
    for existing_user_id in existing_users:
        try:
            userid_applicant, userid_friend = existing_user_id
        except ValueError:
            pass 
        likers_user = bot.get_media_likers(userid_applicant)	
        if likers_user != userid_applicant:
            try:
                existing_users.remove(existing_user_id)
            except IndexError: 
                pass      
    return existing_users 

def get_followers(exist_and_likers_user):   
    for existing_user_id in exist_and_likers_user:
        followers_user = bot.get_user_followers("beautybar.rus")	
        if followers_user[0] != existing_user_id[0]:
            exist_and_likers_user.remove(existing_user_id)
    return exist_and_likers_user        

if __name__ == '__main__': 

    load_dotenv()
    login = os.getenv("login")
    password = os.getenv("password")	
    bot = Bot()
    bot.login(username = login, password = password)

    entered_links = createparser()
    cmd_argument = entered_links.parse_args()

    post_id = bot.get_media_id_from_link(cmd_argument.url)
    all_comments = bot.get_media_comments_all(post_id)

    comments = get_comments(all_comments)

    for user_name in comments:
        try:
            applicant_user_name, friend_user_name = user_name
        except ValueError:
            pass    
        user_id = bot.get_user_id_from_username(applicant_user_name)
        existing_users = []
        if is_user_exist(user_id):
            try:	
                friend_user_id = bot.get_user_id_from_username(friend_user_name)
            except IndexError: 
                pass   	
            if is_user_exist(friend_user_id):
                username_and_id = (user_id, applicant_user_name)
                try: 		
                    existing_users.append(username_and_id)
                except IndexError: 
                    pass  

    exist_and_likers_user = get_likers_users(existing_users)
    foll_exist_likes_user = get_followers(exist_and_likers_user)

    for number, name_of_user in enumerate(foll_exist_likes_user, 1):
        final_list = set(name_of_user)	
        print("{0}. {1}".format(number, final_list))
