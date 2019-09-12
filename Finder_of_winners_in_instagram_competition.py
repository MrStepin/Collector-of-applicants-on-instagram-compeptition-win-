import os, instabot
from instabot import Bot 
from dotenv import load_dotenv
import re
import argparse
import sys

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name_of_page')
    return parser

def get_comments(all_comments):
    comments = []
    for comment_text in all_comments:
        correct_comment = re.findall(r"@([a-zA-Z0-9]{1,15})", str(comment_text["text"]))
        if correct_comment !=[]:
            comments.append(correct_comment)
    return comments

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
    followers_user = bot.get_user_followers(cmd_argument.name_of_page)
    exist_and_likers_usersid = (user_id[0] for user_id in exist_and_likers_user)    
    final_list_of_usersid = (set(followers_user) & set(exist_and_likers_usersid))
    return final_list_of_usersid        

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

    existing_users = []
    for user_name in comments:
        try:
            applicant_user_name, friend_user_name = user_name
        except ValueError:
            pass    
        user_id = bot.get_user_id_from_username(applicant_user_name)
        if user_id != None:
            try:	
                friend_user_id = bot.get_user_id_from_username(friend_user_name)
            except IndexError: 
                pass   	
            if friend_user_id != None:
                username_and_id = (user_id, applicant_user_name)
                try: 		
                    existing_users.append(username_and_id)
                except IndexError: 
                    pass  

    exist_and_likers_user = get_likers_users(existing_users)
    final_list_of_usersid = get_followers(exist_and_likers_user)
    
    for number, userid in enumerate(final_list_of_usersid):
        name_of_user = bot.get_username_from_user_id(userid)	
        print("{0}. {1}".format(number, name_of_user))
