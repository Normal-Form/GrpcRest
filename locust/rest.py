from locust import HttpUser, task


class StudentRestTest(HttpUser):
    @task
    def studentdata(self):
        self.client.get("/students")
