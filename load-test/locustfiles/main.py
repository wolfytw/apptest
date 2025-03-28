from locust import HttpUser, TaskSet, task, between

class BrowseUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def browse(self):
        self.client.get("/")

class SearchUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def search(self):
        self.client.get("/search")  # Adjust the endpoint as necessary

class UserBehavior(TaskSet):
    tasks = {BrowseUser: 2, SearchUser: 1}  # Adjust weights as necessary

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 5000