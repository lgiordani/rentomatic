import datetime
import json
import uuid

import pytest

from rentomatic.serializers import storageroom_serializer as srs
from rentomatic.domain.storageroom import StorageRoom


def test_serialize_domain_storageroom():
    code = uuid.uuid4()

    room = StorageRoom(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293
    )

    expected_json = """
        {{
            "code": "{}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """.format(code)

    json_storageroom = json.dumps(room, cls=srs.StorageRoomEncoder)

    assert json.loads(json_storageroom) == json.loads(expected_json)


def test_serialize_domain_storageruum_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.StorageRoomEncoder)
