import time

from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/user-count")

    @task
    def create_account(self):
        self.client.post("/create-account", json={"username":fake.email(), "password": fake.password()})

    @task
    def add_job(self):
        self.client.post("/add-job", json={"job_title": fake.job()})

    @task(5)
    def view_job(self):
        self.client.get(f"/job?title={fake.job()}", name="/job")
        time.sleep(1)