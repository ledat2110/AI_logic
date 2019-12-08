class IOHandler:
    def read_file(self, path):
        # Safe open file
        with open(path) as f:
            lines = [line for line in f]

        return lines

    def parser(self, path):
        lines = self.read_file(path)
        # Split up 
        alpha = lines[0].strip()
        knowledge_base = [x.strip() for x in lines[2:]]

        return alpha, knowledge_base

    def __init__(self, path):
        """
            path: where is contain input file
            alpha: str
            statemnt: list of str
        """
        self.alpha, self.knowledge_base = self.parser(path)
    
    def write_file(self, path, flag, result_statements):
      with open(path,'w') as outfile:
        for line in result_statements:
          outfile.write(str(len(line)))
          outfile.write('\n')
          for statement in line:
            outfile.write(statement.to_string())
            outfile.write('\n')
        
        outfile.write(str(flag))
