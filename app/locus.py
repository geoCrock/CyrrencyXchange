from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def btc_usd(self):
        self.client.get("/courses/BTC-USD")

    @task
    def btc_rub(self):
        self.client.get("/courses/BTC-RUB")

    @task
    def eth_usd(self):
        self.client.get("/courses/ETH-USD")

    @task
    def eth_rub(self):
        self.client.get("/courses/ETH-RUB")

    @task
    def usd_usd(self):
        self.client.get("/courses/USDT-USD")

    @task
    def usd_rub(self):
        self.client.get("/courses/USDT-RUB")
