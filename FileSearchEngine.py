import os
import pickle
class search_file():

    def __init__(self):
        self.file_index = []
        self.results = []
        self.matches = 0
        self.records = 0

    def create_new_index(self, root_path):
        self.file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]
        with open('file_index.pk1', 'wb') as f:
            pickle.dump(self.file_index,f)
    def load_existing_index(self):
        try:
            with open('file_index.pk1', 'rb') as f:
                      self.file_indxe = pickle.load(f)
        except:
            self.file_index = []
    def search(self, term, search_type = 'contains'):
        self.results.clear()
        self.matches = 0
        self.records = 0
        for path, files in self.file_index:
            for file in files:
                self.records +=1
                if(search_type == 'contains' and term.lower() in file.lower() or search_type == 'startswith' and file.lower().startswith(term.lower()) or
                   search_type == 'endswith'and file.lower().endwith(term.lower())):
                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches +=1
                else:
                    continue
        with open('search_result.txt','w') as f:
            for row in self. results:
                  f.write(row + '\n')
    def test1():
        s  = search_file()
        s.create_new_index(os.getcwd()+"//C-sheet")
        s.search("")
        print(s.matches)
        print(s.results)
    
