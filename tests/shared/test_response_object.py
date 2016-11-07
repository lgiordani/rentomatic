from rentomatic.shared import response_object as ro


def test_response_success_is_true():
    assert bool(ro.ResponseSuccess()) is True
