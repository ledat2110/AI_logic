from statement import Statement

def change_state_statement(statement):
  temp_statement = Statement(statement= statement)

  for k, v in temp_statement.literal_dict.items():
    temp_statement.literal_dict[k] = - v

  return temp_statement

class PLResolution:
  def add_negative_alpha(self, alpha, statements):
    statements.append(change_state_statement(alpha))
    return alpha, statements

  def init_resolution(self, statements, result_statements):
    new_statement = []

    for i in range(len(statements)-1):
      for j in range(i+1,len(statements)):
        temp_value = statements[i].resolution(statements[j].literal_dict)

        if temp_value is not None:
            temp_statement = Statement(literal_dict = temp_value)

            if temp_statement not in statements: # You can optimize 
              new_statement.append(temp_statement)
    
    result_statements.append(new_statement)

    return statements, result_statements


  def resolution(self, alpha, statements):
    result_statements = []
    flag = False

    # Step 0: add negative alpha 
    alpha, statements = self.add_negative_alpha(alpha, statements)
    # Step 1: create new statement
    statements, result_statements = self.init_resolution(statements, result_statements)
    # Step 2:
    while len(result_statements[-1]) != 0:
      new_statement = []

      for i in range(1):
        for statement in statements:
          for another_statement in result_statements[-1]:
            temp_value = statement.resolution(another_statement.literal_dict)

            if temp_value is not None:
              temp_statement = Statement(literal_dict= temp_value)
              if temp_statement not in statements: # You can optimize 
                new_statement.append(temp_statement)

                if len(temp_statement.literal_dict) == 0: 
                  statements += result_statements[-1]
                  result_statements.append(new_statement)
                  flag = True
                  return flag, result_statements
            
      statements += result_statements[-1]
      result_statements.append(new_statement)

    return flag, result_statements

  def __init__(self, alpha, statements): 
    self.flag, self.result_statements = self.resolution(alpha, statements)