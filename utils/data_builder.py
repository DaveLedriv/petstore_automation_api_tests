import random

def generate_pet_data():
    pet_id = random.randint(1000, 9999)
    return {
        "id": pet_id,
        "name": f"Pet_{pet_id}",
        "status": "available"
    }
