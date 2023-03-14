class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def is_authenticated_decorator(function):
        def decor(*users):
            if users[0].is_logged_in:
                function(users[0])
        return decor

    @is_authenticated_decorator
    def create_blog_post(user):
        print(f"This is {user.name}'s new blog post")

new_user = User("ming")
new_user.is_logged_in = True
new_user.create_blog_post(new_user)