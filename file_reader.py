from document import Document


class FileReader():
    def __init__(self, file_name):
        self.documents = []
        self.read_file(file_name)

    def read_file(self, file_name):
        lines = []
        with open(file_name, "r") as f:
            for line in f:
                lines.append(line)

        # index = 6
        # while index < len(lines)-1:
        #     summary = lines[index].strip()[15:].strip()
        #     text = lines[index+1].strip()[12:].strip()
        #     doc = Document(summary, text, index/9)
        #     if 'ry: Um, why so much $$ when the product     ' in text:
        #         print index
        #         print text
        #         import ipdb; ipdb.set_trace()
        #     self.documents.append(doc)
        #     index += 9

        index = 0
        for line in lines:
            if 'review/summary:' in line:
                summary = lines[index].strip()[15:].strip()
                text = lines[index+1].strip()[12:].strip()
                user_id = lines[index-5][19:].strip()
                product_id = lines[index-6][18:].strip()
                time = lines[index-1][12:].strip()
                score = lines[index-2][13:].strip()
                doc = Document(summary, text, index/9, user_id, product_id, time, score)
                self.documents.append(doc)
            index +=1

        print "Read file"