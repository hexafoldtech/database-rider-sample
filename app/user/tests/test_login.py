from typing import List



from fastapi.testclient import TestClient
from dbrider.decorator import dataset

@dataset(dataset_paths=["datasets/login_data.yml"])
def test_login(client: TestClient, header: dict, payload: List[dict]) -> None:
    assert True
