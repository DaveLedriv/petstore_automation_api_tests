import pytest
from services.pet_service import PetService
from utils.data_builder import generate_pet_data

@pytest.fixture
def pet_service():
    return PetService()

@pytest.fixture
def new_pet_data():
    return generate_pet_data()

def test_create_pet(pet_service, new_pet_data):
    response = pet_service.create_pet(new_pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == new_pet_data["name"]
    assert response.json()["status"] == "available"

def test_get_pet(pet_service, new_pet_data):
    # Primero creamos una nueva mascota
    create_response = pet_service.create_pet(new_pet_data)
    pet_id = create_response.json()["id"]

    # Luego consultamos la mascota
    get_response = pet_service.get_pet(pet_id)
    assert get_response.status_code == 200
    assert get_response.json()["id"] == pet_id

def test_update_pet(pet_service, new_pet_data):
    # Creamos mascota
    create_response = pet_service.create_pet(new_pet_data)
    pet_id = create_response.json()["id"]

    # Actualizamos su nombre
    updated_data = new_pet_data.copy()
    updated_data["name"] = updated_data["name"] + "_Updated"

    update_response = pet_service.update_pet(updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"].endswith("_Updated")

def test_delete_pet(pet_service, new_pet_data):
    # Creamos mascota
    create_response = pet_service.create_pet(new_pet_data)
    pet_id = create_response.json()["id"]

    # Borramos mascota
    delete_response = pet_service.delete_pet(pet_id)
    assert delete_response.status_code == 200

    # Intentamos obtener la mascota (debe fallar)
    get_response = pet_service.get_pet(pet_id)
    assert get_response.status_code == 404
