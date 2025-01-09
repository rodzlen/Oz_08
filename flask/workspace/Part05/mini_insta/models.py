users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]
def get_users_list():
    return users

def add_user(username):
    if username:
        users.append({"username":username,"posts":[]})
        return {"username":username}
    else:
        return None
def get_post(username):
    for i in users:
        if i['username'] == username:
            return i['posts']
        
    return None

def add_post(username, title):
    for user in users:
        if user['username'] == username:
            if 'posts' not in user:
                user['posts']=[]
            user['posts'].append({'title':title,"likes":0})
            return title
    return None

def press_like(username,title):
    for user in users:
        if user['username'] == username:
            for post in user['posts']:
                if post['title'] == title:
                    post['likes']+=1
                    return post
            
    return None
def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return {"msg":"Successfully user information deleted"}
    return{"msg":"not exist user"}
    