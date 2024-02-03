from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)

    # @task
    # def courses(self):
    #     self.client.get("/courses/BTCRUB")
    #
    # @task
    # def courses(self):
    #     self.client.get("/courses/BTCUSDT")

    @task
    def courses(self):
        self.client.get("/test")