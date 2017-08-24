from file_reader import FileReader

class Indexer():
    def __init__(self):
        self.documents = []
        self.index = {}
        self.parse_documents()
        self.build_index()

    def parse_documents(self):
        f = FileReader("input/foods.txt")
        self.documents = f.documents

    def build_index(self):

        for doc in self.documents:
            if doc.doc_no % 10000 == 0:
                print "Doc no: " + str(doc.doc_no)
            for token in doc.token_set:
                self.index[token] = []

        for doc in self.documents:
            if doc.doc_no % 10000 == 0:
                print "Doc no: " + str(doc.doc_no)
            for token in doc.token_set:
                self.index[token].append(doc.doc_no)

        for key, value in self.index.iteritems():
            self.index[key] = list(set(self.index[key]))

        print "Built index"