from rentomatic.shared import use_case as uc
from rentomatic.shared import response_object as res


class StorageRoomListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_storageroom = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_storageroom)
