import uuid
from rentomatic.domain.storageroom import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    storageroom = StorageRoom(code, size=200, price=10,
                         longitude='-0.09998975',
                         latitude='51.75436293')
    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 10
    assert storageroom.longitude == -0.09998975
    assert storageroom.latitude == 51.75436293


def test_storageroom_model_from_dict():
    code = uuid.uuid4()
    storageroom = StorageRoom.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': '-0.09998975',
            'latitude': '51.75436293'
        }
    )
    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 10
    assert storageroom.longitude == -0.09998975
    assert storageroom.latitude == 51.75436293
