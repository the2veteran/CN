from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:5000"
    @task(1)
    def send_tcp_data(self):
        data = {"node": "node1", "stats": {"established": 5, "time_wait": 2}}
        self.client.post("/collect", json=data)
