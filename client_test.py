import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'] , quote['top_bid']['price'],quote['top_ask']['price'] , (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'] , quote['top_bid']['price'],quote['top_ask']['price'] , (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 118.13, 'size': 145}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.24, 'size': 2}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 110.79, 'size': 52}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 115.14, 'size': 12}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'] , quote['top_bid']['price'],quote['top_ask']['price'] , (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 110.5, 'size': 35}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 116.63, 'size': 183}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 113.65, 'size': 40}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.51, 'size': 84}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'] , quote['top_bid']['price'],quote['top_ask']['price'] , (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  



if __name__ == '__main__':
    unittest.main()
