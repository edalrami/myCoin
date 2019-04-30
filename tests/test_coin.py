# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:34:26 2019

@author: edalr
"""
import pytest

import coin as mycoin


TEST_DATA = [("Bitcoin", "BTC") , ("Ethereum", "ETH"), ("EdwinCoin", "EDC"), ("EthereumClassic", "ETC")]
TEST_IDS = ["Ok coin", "Good Coin", "Best Coin", "Bad Coin"]

MARKET_DATA = [(4000, 17, 68000) , 
              (140, 105, 14700), 
              (1, 3, 3)]

MARKET_IDS = ["TEST1", "TEST2", "TEST3"]

@pytest.mark.parametrize('coin_name, coin_sym', TEST_DATA, ids= TEST_IDS)
def test_coin_object_basic_initialization(coin_name, coin_sym):
    coin_obj = mycoin.Coin(coin_name, coin_sym)
    assert isinstance(coin_obj, mycoin.Coin)
    assert coin_obj.circulating == 0
    assert coin_obj.price == 0
    assert coin_obj.mineable == False
    assert coin_obj.fixed_supply == False
    assert coin_obj.mineable == False
    

def test_edwin_coin_initialization():
    coin_obj = mycoin.edwin_coin()
    assert coin_obj.name == "EdwinCoin"
    assert coin_obj.symbol == "EDC"

@pytest.mark.parametrize('coin_price, circulating_supply, result', MARKET_DATA, ids= MARKET_IDS)    
def test_coin_object_market_cap(coin_price, circulating_supply, result):
    coin_obj = mycoin.edwin_coin()
    coin_obj.inputCoinData(coin_price, circulating_supply)
    coin_obj.getMarketCap()
    assert coin_obj.mc == result
    
    
def test_edwin_coin_mineable():
    coin_obj = mycoin.edwin_coin()
    coin_obj.setMineable()
    assert coin_obj.mineable == True
    
def test_edwin_coin_fixed_supply():
    coin_obj = mycoin.edwin_coin()
    coin_obj.setFixedSupply()
    assert coin_obj.fixed_supply == True
    
    
def test_coin_object_market_cap_error():
    coin_obj = mycoin.edwin_coin()
    coin_obj.inputCoinData('Test', '4')
    with pytest.raises(TypeError):
        coin_obj.getMarketCap()
    
    

    