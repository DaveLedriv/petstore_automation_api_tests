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
