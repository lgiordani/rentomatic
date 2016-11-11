import json
from flask import Blueprint, Response

from rentomatic.use_cases import request_objects as req
from rentomatic.repository import memrepo as mr
from rentomatic.use_cases import storageroom_use_cases as uc
from rentomatic.serializers import storageroom_serializer as ser

blueprint = Blueprint('storageroom', __name__)


@blueprint.route('/storagerooms', methods=['GET'])
def storageroom():
    request_object = req.StorageRoomListRequestObject.from_dict({})

    repo = mr.MemRepo()
    use_case = uc.StorageRoomListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.StorageRoomEncoder),
                    mimetype='application/json',
                    status=200)