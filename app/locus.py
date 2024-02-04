from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def courses(self):
    #     self.client.get("/courses/BTC-USD")
    #
    # @task
    # def courses(self):
    #     self.client.get("/courses/BTC-RUB")

    @task
    def courses(self):
        self.client.get("/test")
