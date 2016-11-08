from rentomatic.shared import request_object as req


def test_invalid_request_object_is_false():
    request = req.InvalidRequestObject()

    assert bool(request) is False


def test_invalid_request_object_accepts_errors():
    request = req.InvalidRequestObject()
    request.add_error(parameter='aparam', message='wrong value')
    request.add_error(parameter='anotherparam', message='wrong type')

    assert request.has_errors() is True
    assert len(request.errors) == 2


def test_valid_request_object_is_true():
    request = req.ValidRequestObject()

    assert bool(request) is True
