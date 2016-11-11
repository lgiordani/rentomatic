import pytest
import json
from flask import Response

from rentomatic.shared import response_object as res
from rentomatic.shared import http_response as hres


@pytest.fixture
def successful_response_object():
    return res.ResponseSuccess([])


def test_build_http_response_from_successful_response_object(successful_response_object):
    http_json_response = hres.HttpResponse(successful_response_object).json()
    expected_flask_response = Response(json.dumps(successful_response_object.value),
                                       mimetype='application/json',
                                       status=200)

    assert http_json_response.status_code == expected_flask_response.status_code
    assert http_json_response.data == expected_flask_response.data
    assert http_json_response.mimetype == expected_flask_response.mimetype


def test_build_http_response_from_resource_error_response_object():
    error_object = res.ResponseFailure.build_resource_error('')
    http_json_response = hres.HttpResponse(error_object).json()
    expected_flask_response = Response(json.dumps(error_object.value),
                                       mimetype='application/json',
                                       status=404)

    assert http_json_response.status_code == expected_flask_response.status_code
    assert http_json_response.data == expected_flask_response.data
    assert http_json_response.mimetype == expected_flask_response.mimetype


def test_build_http_response_from_parameters_error_response_object():
    error_object = res.ResponseFailure.build_parameters_error('')
    http_json_response = hres.HttpResponse(error_object).json()
    expected_flask_response = Response(json.dumps(error_object.value),
                                       mimetype='application/json',
                                       status=400)

    assert http_json_response.status_code == expected_flask_response.status_code
    assert http_json_response.data == expected_flask_response.data
    assert http_json_response.mimetype == expected_flask_response.mimetype


def test_build_http_response_from_system_error_response_object():
    error_object = res.ResponseFailure.build_system_error('')
    http_json_response = hres.HttpResponse(error_object).json()
    expected_flask_response = Response(json.dumps(error_object.value),
                                       mimetype='application/json',
                                       status=500)

    assert http_json_response.status_code == expected_flask_response.status_code
    assert http_json_response.data == expected_flask_response.data
    assert http_json_response.mimetype == expected_flask_response.mimetype
