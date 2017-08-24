from file_reader import FileReader
f = FileReader(file_name="input/small_foods.txt")



from indexer import Indexer
i = Indexer()

from query import Query
q = Query()
a = q.execute_query(['jumbo', 'salted', 'peanuts'])
for key, values in a.iteritems():
    if values > 2:
        print key