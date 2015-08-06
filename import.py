import unicodedata
from py2neo import Graph, Node, Relationship

g = Graph()
g.delete_all()

starts = 'Stockholm', 'Edinburgh'

for start in starts:
	print "\nStarting " + start
	start_node = g.merge_one('Airport', property_key='name', property_value=start)
	for l in open(start + '.csv'):
		items = l.split(',')
		airline = unicodedata.normalize('NFKD', unicode(items[0], encoding='utf-8')).encode('ascii', 'ignore')
		print "Airline is " + airline
		for airport in items[1:]:
			airport = unicodedata.normalize('NFKD', unicode(airport, encoding='utf-8')).encode('ascii', 'ignore').strip().split('-')[0]
			print "Endpoint is " + airport
			end_node = g.merge_one("Airport", property_key='name', property_value=airport)
			g.create(Relationship(start_node, "FLIES_TO", end_node, airline=airline))
