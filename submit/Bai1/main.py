from pl_resolution import PLResolution
from statement import Statement
from utils import IOHandler
import re

class App:
    def read_file(self, path):
        self.ioHandler = IOHandler(path)
        statements = [Statement(statement=x) for x in self.ioHandler.knowledge_base]
        self.alpha = self.ioHandler.alpha
        self.statements = statements

    def resolution(self):
      plResolution = PLResolution(self.alpha, self.statements)
      self.flag = plResolution.flag
      self.result_statements = plResolution.result_statements 
    
    def write_file(self, path):
      self.ioHandler.write_file(path, self.flag, self.result_statements)

    def __init__(self, infile, outfile):
        self.read_file(infile)
        self.resolution()
        self.write_file(outfile)
        
if __name__ == '__main__':
    file_name = str(input('your input file name: '))
    index = re.findall(r'\d',file_name)
    file_out = 'result.txt'
    if len(index) == 1:
      file_out = 'result{}.txt'.format(int(index[0]))
    app = App(file_name,file_out)
