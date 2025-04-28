import requests

class PetService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def create_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = requests.post(url, json=pet_data)
        return response

    def get_pet(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.get(url)
        return response

    def update_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = requests.put(url, json=pet_data)
        return response

    def delete_pet(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.delete(url)
        return response
