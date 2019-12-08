from collections import OrderedDict


class Statement:
    def is_positive_literal(self, literal):
        return (literal[0] != '-')

    def literal_tokenizer(self, statement):
        temp_list = statement.split()
        temp_list = temp_list[::2]

        return { (x if self.is_positive_literal(x) else x[1:]): (1 if self.is_positive_literal(x) else -1)  for x in temp_list}

    def __init__(self, statement = None, literal_dict = None):

        """
            statement: str
            literal_dict: dictionary of literals 

            testing 1:
            statement = Statement('-A OR B')
            statement.literal_dict
            statement_2 = Statement('A')
            statement_2.literal_dict
            print(statement_2.resolution(statement.literal_dict))
            "{'B': 1}"


            statement = Statement('A OR B')
            statement.literal_dict
            statement_2 = Statement('A')
            statement_2.literal_dict
            print(statement_2.resolution(statement.literal_dict))
            None


            statement = Statement('-A')
            statement.literal_dict
            statement_2 = Statement('A')
            statement_2.literal_dict
            print(statement_2.resolution(statement.literal_dict))
            {}
        """
        self.literal_dict = {}

        if statement is not None:
            self.literal_dict = self.literal_tokenizer(statement)
            
        if literal_dict is not None:
            self.literal_dict = literal_dict

    def __eq__(self, other):
      if not isinstance(other, Statement):
        # don't attempt to compare against unrelated types
        return NotImplemented

      return self.literal_dict == other.literal_dict


    def __repr__(self):
      return str(self.literal_dict)

    def resolution(self, another_statement_dict):
        # Suppose we can't 
        key_list = []

        # Find inner key
        for key, value in self.literal_dict.items():
            temp_value = another_statement_dict.get(key, None)
            if temp_value is not None:
                if value != temp_value:
                    key_list.append(key)
        
        if len(key_list) == 1:
            result = OrderedDict()
            for key, value in self.literal_dict.items():
                if key != key_list[0]:
                    result[key] = value
            
            for key, value in another_statement_dict.items():
                if key != key_list[0]:
                    result[key] = value
            
            return {k:v for k,v in result.items() }
        else:
            return None

    def to_string(self):
      if len(self.literal_dict.items()) != 0:
        result = [ k if v > 0 else '-' + k for k, v in self.literal_dict.items()]
        result = ' OR '.join(result)
      else:
        result = "{}"
        
      return result
      