from rentomatic.shared import response_object as ro


class StorageRoomListUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        storage_rooms = self.repo.list()
        return ro.ResponseSuccess(storage_rooms)
