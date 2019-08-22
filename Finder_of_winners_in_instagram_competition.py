import os, instabot
from instabot import Bot 
from dotenv import load_dotenv
import re
import argparse
import sys

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    return parser

def get_comments_list(all_comments):
    comments_list = []
    for comment_text in all_comments:
        if re.findall(r"@([a-zA-Z0-9]{1,15})", str(comment_text["text"])) !=[]:
            comments_list.append(re.findall(r"@([a-zA-Z0-9]{1,15})", str(comment_text["text"])))
    return comments_list

def is_user_exist(user_id):
    if user_id == None:
        return False
    else: 
        return True

def likers_users(existing_users_list):
    for existing_user_id in existing_users_list:
        likers_user_list = bot.get_media_likers(existing_user_id[0])	
        if likers_user_list[0] != existing_user_id[0]:
            existing_users_list.remove(existing_user_id)
    return existing_users_list  

def followers(exist_and_likers_user_list):   
    for existing_user_id in exist_and_likers_user_list:
        followers_user_list = bot.get_user_followers("beautybar.rus")	
        if followers_user_list[0] != existing_user_id[0]:
            exist_and_likers_user_list.remove(existing_user_id)
    return exist_and_likers_user_list        

if __name__ == '__main__': 

    load_dotenv()
    login = os.getenv("login")
    password = os.getenv("password")	
    bot = Bot()
    bot.login(username = login, password = password)

    entered_links = createParser()
    competition_link = entered_links.parse_args()

    post_id = bot.get_media_id_from_link(competition_link.url)
    all_comments = bot.get_media_comments_all(post_id)

    comments_list = get_comments_list(all_comments)

    for user_name in comments_list:
        user_id = bot.get_user_id_from_username(user_name[0])
        existing_users_list = []
        if is_user_exist(user_id) == True:
            try:	
                friend_user_id = bot.get_user_id_from_username(user_name[1])
            except IndexError: 
                pass   	
            if is_user_exist(friend_user_id) == True:
                username_and_id = (user_id, user_name[0])		
                existing_users_list.append(username_and_id)

    exist_and_likers_user_list = likers_users(existing_users_list)
    foll_exist_likes_userlist = followers(exist_and_likers_user_list)

    for name_of_user in foll_exist_likes_userlist:
        final_list = set(name_of_user[1])	
    print(final_list)
