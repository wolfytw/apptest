from locust import HttpUser, task, between

class SearchUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def search(self):
        search_query = "example query"
        self.client.get(f"/search?q={search_query}")