import random



def generate_pet_data():
    pet_id = random.randint(1000, 9999)
    return {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": f"Pet_{pet_id}",
        "photoUrls": [
            "https://example.com/photo.png"
        ],
        "tags": [
            {
                "id": 1,
                "name": "tag1"
            }
        ],
        "status": "available"
    }


def generate_order_data():
    order_id = random.randint(1000, 1999)
    pet_id = random.randint(1000, 9999)
    return {
        "id": 98,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2025-04-28T19:18:19.677Z",
        "status": "placed",
        "complete": True
    }