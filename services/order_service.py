import requests

class OrderService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def create_order(self, order_data):
        url = f"{self.BASE_URL}/store/order"
        return requests.post(url, json=order_data)

    def get_order_by_id(self, order_id):
        url = f"{self.BASE_URL}/store/order/{order_id}"
        return requests.get(url)
