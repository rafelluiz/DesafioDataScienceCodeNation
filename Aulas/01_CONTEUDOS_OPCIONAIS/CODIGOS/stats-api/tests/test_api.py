import pytest
import requests

class TestAPI:
  @pytest.fixture
  def url(self):
    return 'http://localhost:5000/data'

  @pytest.fixture
  def data(self):
    return [1,2,3,4]

  @pytest.fixture
  def uuid(self, url, data):
    response = requests.post(url,json={"data":data})

    return response.json()['uuid']

  def test_save_data(self,uuid):
    assert uuid is not None

  def test_get_data(self,url,uuid,data):
    response = requests.get(f'{url}/{uuid}')

    assert response.ok
    assert response.json()['data'] == data

  def test_calc_mean(self,url,uuid):
    response = requests.get(f'{url}/{uuid}/mean')

    assert response.ok
    assert response.json()['result'] == pytest.approx(2.5)