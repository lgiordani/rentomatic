from unittest import mock

from rentomatic.shared import request_object as req, response_object as res
from rentomatic.shared import use_case as uc


def test_use_case_cannot_process_valid_requests():
    valid_request_object = mock.MagicMock()
    valid_request_object.__bool__.return_value = True

    use_case = uc.UseCase()
    response = use_case.execute(valid_request_object)

    assert not response
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.message == \
        'NotImplementedError: process_request() not implemented by UseCase class'


def test_use_case_can_process_invalid_requests_and_returns_response_failure():
    invalid_request_object = req.InvalidRequestObject()
    invalid_request_object.add_error('someparam', 'somemessage')

    use_case = uc.UseCase()
    response = use_case.execute(invalid_request_object)

    assert not response
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == 'someparam: somemessage'


def test_use_case_can_manage_generic_exception_from_process_request():
    use_case = uc.UseCase()

    class TestException(Exception):
        pass

    use_case.process_request = mock.Mock()
    use_case.process_request.side_effect = TestException('somemessage')
    response = use_case.execute(mock.Mock)

    assert not response
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.message == 'TestException: somemessage'
