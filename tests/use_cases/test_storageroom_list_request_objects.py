from rentomatic.use_cases import request_objects as ro


def test_build_storageroom_list_request_object_without_parameters():
    req = ro.StorageRoomListRequestObject()

    assert bool(req) is True


def test_build_file_list_request_object_from_empty_dict():
    req = ro.StorageRoomListRequestObject.from_dict({})

    assert bool(req) is True
