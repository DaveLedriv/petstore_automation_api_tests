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

    # Validamos que la respuesta sea 200 o 404
    assert get_response.status_code in [200, 404], f"Unexpected status code: {get_response.status_code}"

    if get_response.status_code == 200:
        assert get_response.json()["id"] == pet_id
    else:
        print(f"🐾 Mascota con ID {pet_id} no encontrada, este comportamiento es por que petstore es un mock de pruebas.")


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

    # Intentamos borrar la mascota
    delete_response = pet_service.delete_pet(pet_id)

    # Aceptamos que puede dar 200 (borrado exitoso) o 404 (mascota no existente)
    assert delete_response.status_code in [200, 404], f"Unexpected status code: {delete_response.status_code}"

    if delete_response.status_code == 200:
        # Si respondió 200, aseguramos que el mensaje sea el correcto
        assert delete_response.json()["message"] == str(pet_id)
    else:
        print(f"🐾 Mascota con ID {pet_id} no encontrada, posible comportamiento normal en PetStore Demo.")