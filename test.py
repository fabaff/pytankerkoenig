import pytankerkoenig
import os

print(pytankerkoenig.getStationData(os.environ['api_key'],'5bd71e9d-7001-4908-a29d-36c28d6eb615'))

print(pytankerkoenig.getNearbyStations(os.environ['api_key'],50.75,7.25,3,'all','dist'))

print(pytankerkoenig.getPriceList(os.environ['api_key'],['5bd71e9d-7001-4908-a29d-36c28d6eb615','005056ba-7cb6-1ed2-bceb-92a737c6ad35']))
