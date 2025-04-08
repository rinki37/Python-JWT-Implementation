from passlib.hash import pbkdf2_sha256

# To store users in memory
users = {}
next_id = 1

class UserStore:
    @staticmethod
    def create_user(username, password):
        global next_id
        if username in users:
            return None

        users[username] = {
            "id" : next_id,
            "username" : username,
            "password_hash" : pbkdf2_sha256.hash(password),
        }

        next_id += 1

        return users[username]

    @staticmethod
    def get_user(username):
        return users.get(username)

    @staticmethod
    def get_user_by_id(user_id):
        for user in users.value():
            if user['id'] == user_id:
                return user
            return None


    @staticmethod
    def verify_user(username, password):
        user = users.get(username)
        if not user:
            return False
        return pbkdf2_sha256.verify(password, user['password_hash'])

