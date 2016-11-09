import pytest

from rentomatic.shared.domain_model import DomainModel

from rentomatic.repository import memrepo


storageroom1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': '-0.09998975',
    'latitude': '51.75436293',
}

storageroom2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': '0.18228006',
    'latitude': '51.74640997',
}

storageroom3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': '0.27891577',
    'latitude': '51.45994069',
}

storageroom4 = {
    'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
    'size': 93,
    'price': 48,
    'longitude': '0.33894476',
    'latitude': '51.39916678',
}


@pytest.fixture
def storagerooms():
    return [storageroom1, storageroom2, storageroom3, storageroom4]


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.code for dm in domain_models_list]) == set([d['code'] for d in data_list])


def test_repository_list_without_parameters(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    assert repo.list() == storagerooms


def test_repository_list_with_filters_unknown_key(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    with pytest.raises(KeyError):
        repo.list(filters={'name': 'aname'})


def test_repository_list_with_filters_unknown_operator(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    with pytest.raises(ValueError):
        repo.list(filters={'price__in': [20, 30]})


def test_repository_list_with_filters_price(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    _check_results(repo.list(filters={'price': 60}), [storageroom3])
    _check_results(repo.list(filters={'price__eq': 60}), [storageroom3])
    _check_results(repo.list(filters={'price__lt': 60}), [storageroom1, storageroom4])
    _check_results(repo.list(filters={'price__gt': 60}), [storageroom2])


def test_repository_list_with_filters_size(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    _check_results(repo.list(filters={'size': 93}), [storageroom4])
    _check_results(repo.list(filters={'size__eq': 93}), [storageroom4])
    _check_results(repo.list(filters={'size__lt': 60}), [storageroom3])
    _check_results(repo.list(filters={'size__gt': 400}), [storageroom2])


def test_repository_list_with_filters_code(storagerooms):
    repo = memrepo.MemRepo(storagerooms)

    _check_results(
        repo.list(filters={'code': '913694c6-435a-4366-ba0d-da5334a611b2'}), [storageroom3])
