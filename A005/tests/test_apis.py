import datetime
from mercado_bitcoin.apis import DaySummaryAPI, TradesAPI, MercadoBitcoinAPI
import pytest
from unittest.mock import patch
import requests

class TestDaySummaryAPI:
    @pytest.mark.parametrize(
        'coin, date, expected',
        [
            ('BTC', datetime.date(2022, 1, 1), 'https://www.mercadobitcoin.net/api/BTC/day-summary/2022/1/1'),
            ('ETH', datetime.date(2021, 12, 31), 'https://www.mercadobitcoin.net/api/ETH/day-summary/2021/12/31')
        ]
    )
    def test_get_endpoint(self, coin, date, expected):
        actual = DaySummaryAPI(coin=coin)._get_endpoint(date=date)
        assert actual == expected

class TestTradesAPI:
    @pytest.mark.parametrize(
        'date, expected',
        [
            (datetime.datetime(2019,1,1), 1546311600),
            (datetime.datetime(2021,1,1), 1609470000),
            (datetime.datetime(2022,3,1), 1646103600),
            (datetime.datetime(2022,3,1,0,0,5), 1646103605)
        ]
    )
    def test_get_unix_epoch(self, date, expected):
        actual = TradesAPI(coin='TEST')._get_unix_epoch(date)
        assert actual == expected

    @pytest.mark.parametrize(
    'coin, date_from, date_to, expected',
    [
        ('TEST', datetime.datetime(2019,1,1), datetime.datetime(2021,1,1), 'https://www.mercadobitcoin.net/api/TEST/trades/1546311600/1609470000'),
        ('TEST', datetime.datetime(2022,3,1), datetime.datetime(2022,3,1,0,0,5), 'https://www.mercadobitcoin.net/api/TEST/trades/1646103600/1646103605'),
        ('BTC', datetime.datetime(2022,3,1), None, 'https://www.mercadobitcoin.net/api/BTC/trades/1646103600'),
        ('BTC', None, datetime.datetime(2022,3,1), 'https://www.mercadobitcoin.net/api/BTC/trades'),
        ('ETH', None, None, 'https://www.mercadobitcoin.net/api/ETH/trades')
    ]
    )
    def test_get_endpoint(self, coin, date_from, date_to, expected):
        actual = TradesAPI(coin=coin)._get_endpoint(date_from=date_from, date_to=date_to)
        assert actual == expected

    def test_get_endpoint_date_from_greater_than_date_to(self):
        with pytest.raises(RuntimeError):
            TradesAPI(coin='TEST')._get_endpoint(date_from=datetime.datetime(2021,1,1), date_to=datetime.datetime(2019,1,1))



@pytest.fixture
@patch('mercado_bitcoin.apis.MercadoBitcoinAPI.__abstractmethods__', set())
def fixture_mercado_bitcoin_api():
    return MercadoBitcoinAPI(coin='TEST')

def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.json_data = json_data
            self.status_code = status_code
        
        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.status_code != 200:
                raise Exception
    
    if args[0] == 'valid_endpoint':
        return MockResponse(json_data={'mock_key': 'mock_value'}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)

#@patch('apis.MercadoBitcoinAPI.__abstractmethods__', set()) # Não precisa essa linha porque já está ali em cima do fixture.
class TestMercadoBitcoinAPI:
    @patch('requests.get')
    @patch('mercado_bitcoin.apis.MercadoBitcoinAPI._get_endpoint', return_value='valid_endpoint')
    def test_get_data_requests_is_called(self, mock_get_endpoint, mock_requests, fixture_mercado_bitcoin_api):
        fixture_mercado_bitcoin_api.get_data()
        mock_requests.assert_called_once_with('valid_endpoint')

    @patch('requests.get', side_effect=mocked_requests_get)
    @patch('mercado_bitcoin.apis.MercadoBitcoinAPI._get_endpoint', return_value='valid_endpoint')
    def test_get_data_with_valid_endpoint(self, mock_get_endpoint, mock_requests, fixture_mercado_bitcoin_api):
        actual = fixture_mercado_bitcoin_api.get_data()
        expected = {'mock_key': 'mock_value'}
        assert actual == expected

    @patch('requests.get', side_effect=mocked_requests_get)
    @patch('mercado_bitcoin.apis.MercadoBitcoinAPI._get_endpoint', return_value='invalid_endpoint')
    def test_get_data_status(self, mock_get_endpoint, mock_requests, fixture_mercado_bitcoin_api):
        with pytest.raises(Exception):
            fixture_mercado_bitcoin_api.get_data()