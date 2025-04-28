import pytest
from services.order_service import OrderService
from utils.data_builder import generate_order_data

@pytest.fixture
def order_service():
    return OrderService()

@pytest.fixture
def new_order_data():
    return generate_order_data()

def test_create_and_get_order(order_service, new_order_data):
    # Crear una orden
    create_response = order_service.create_order(new_order_data)
    assert create_response.status_code == 200

    order_id = create_response.json()["id"]

    # Obtener la orden creada
    get_response = order_service.get_order_by_id(order_id)
    assert get_response.status_code == 200
    assert get_response.json()["id"] == order_id
