import pytest

from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679152937460&signature=P_Vl7nbJAMnd1nGU21hfbuR5T6HJHIuYbc1sB5EbLYM&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679152937460&signature=P_Vl7nbJAMnd1nGU21hfbuR5T6HJHIuYbc1sB5EbLYM&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 400"
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679152937460&signature=P_Vl7nbJAMnd1nGU21hfbuR5T6HJHIuYbc1sB5EbLYM&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"

def test_get_filtired_data(test_data, filtered_empty_from=None):
    assert len(get_filtered_data(test_data)) == 3
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) == 2

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб. \n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['03.07.2019 Перевод организации\n[СКРЫТО}  -> Счет **5560\n8221.37 USD \n']

