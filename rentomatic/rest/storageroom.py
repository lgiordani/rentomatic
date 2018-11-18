import json
from flask import Blueprint, request, Response

from rentomatic.use_cases import request_objects as req
from rentomatic.shared import response_object as res
from rentomatic.repository import memrepo as mr
from rentomatic.use_cases import storageroom_use_cases as uc
from rentomatic.serializers import storageroom_serializer as ser

blueprint = Blueprint('storageroom', __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

storageroom1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': -0.09998975,
    'latitude': 51.75436293,
}

storageroom2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': 0.18228006,
    'latitude': 51.74640997,
}

storageroom3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}


@blueprint.route('/storagerooms', methods=['GET'])
def storageroom():
    qrystr_params = {
        'filters': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_object = req.StorageRoomListRequestObject.from_dict(qrystr_params)

    repo = mr.MemRepo([storageroom1, storageroom2, storageroom3])
    use_case = uc.StorageRoomListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.StorageRoomEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
