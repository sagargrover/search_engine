import json

class Document():
    def __init__(self, summary, text, doc_no, user_id, product_id, time, score):
        self.summary = summary
        self.text = text
        self.user_id = user_id
        self.product_id = product_id
        self.time = time
        self.doc_no = doc_no
        self.score = score

    def __repr__(self):
        return json.dumps(self.as_dict, indent=4, separators=(',', ': '), default=str)

    @property
    def as_dict(self):
        return {
            'Summary': self.summary,
            'Text': self.text,
            'Doc no': self.doc_no,
            'Product id': self.product_id,
            'time': self.time,
            'User id': self.user_id,
            'Score': self.score

        }

    @property
    def entire_text(self):
        return self.summary + " " + self.text

    @property
    def token_set(self):
        tokens = self.entire_text.replace(".", " ").split(" ")
        tokens = [x.lower() for x in tokens]
        return set(tokens)

