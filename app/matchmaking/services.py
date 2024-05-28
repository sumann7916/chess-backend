#Create list of users currently searchinf for a match, with their config, use redis to store the list
#Create a function to add a user to the list

import redis


def add_user_to_searching_list(user):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.rpush('searching_users', user)
    