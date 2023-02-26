import os
import time

class file_info():
    def __init__(self):
        self.path = os.getcwd() + "//C-sheet"
    def get_all_csheet_name(self):
        dir_list = os.listdir(self.path);
        return dir_list

    def get_all_csheet_date(self):
        file_name = self.get_all_csheet_name()
        named_path = [self.path+"//"+name  for name in file_name]
        file_date = [time.ctime(os.path.getmtime(p)) for p in named_path]
        return file_date
