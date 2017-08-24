from indexer import Indexer
import operator


class Query():
    def __init__(self):
        i = Indexer()
        self.index = i.index
        self.documents = i.documents

    def get_tokens_with_docs(self, q_tokens):
        token_docs = {}
        for token in q_tokens:
            if token in self.index.keys():
                token_docs[token] = self.index[token]

        return  token_docs

    def get_document_score(self, token_docs):
        docs_score = {}
        for docs in token_docs.values():
            for doc in docs:
                docs_score[doc] = 0
        for docs in token_docs.values():
            for doc in docs:
                docs_score[doc] += 1
        return docs_score

    def execute_query(self, tokens, k):
        tokens = [x.lower() for x in tokens]
        token_docs = self.get_tokens_with_docs(tokens)
        print "Got docs for tokens"
        docs_score = self.get_document_score(token_docs)
        #Documents sorted with their score
        sorted_docs_score = sorted(docs_score.items(), key=operator.itemgetter(1))
        review_tuples = sorted_docs_score[-k:]
        reviews = []
        len_tokens = len(tokens)
        for t in review_tuples:
            map_document = self.documents[t[0]].as_dict
            map_document["review_calculated_score"] = float(t[1])/float(len_tokens)
            map_document["Text"] = map_document["Text"][0:20]
            reviews.append(map_document)

        return reviews