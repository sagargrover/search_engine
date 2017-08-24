import random
with open("input/foods.txt") as f:
    words = f.read().split()

print "Read and split file"
word_set = set(words)
query_set = []
for i in xrange(1,10):
    query_set.append(random.sample(word_set, int(random.randint(2,4))))


query_set_complete = []
for i in xrange(1, 100001):
    random_int = random.randint(1, 8)
    query_set_complete.append(query_set[random_int])


print "Query set generated"
import ipdb; ipdb.set_trace()