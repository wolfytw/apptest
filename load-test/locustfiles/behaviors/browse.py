from locust import HttpUser, task, between

class BrowseUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def browse(self):
        self.client.get("/")  # Simulate browsing the homepage
        self.client.get("/about")  # Simulate browsing the about page
        self.client.get("/contact")  # Simulate browsing the contact page
        # Add more pages as needed to simulate user browsing behavior