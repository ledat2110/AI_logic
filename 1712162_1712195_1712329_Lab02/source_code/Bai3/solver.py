from Interpreter import *
from parser import *
from collections import defaultdict

class Solver:

    def __init__(self, rules_text):
        self.rules = Parser(rules_text).parse_rules()
        self.database = Database(self.rules)

    def find_solutions(self, query_text):

        query = Parser(query_text).parse_query()

        query_variable_map = {}
        variables_in_query = False

        for argument in query.arguments:
            if isinstance(argument, Variable):
                variables_in_query = True
                query_variable_map[argument.name] = argument

        matching_query_terms = [item for item in self.database.query(query)]

        if matching_query_terms:
            if query_variable_map:
                solutions_map = defaultdict(list)
                for matching_query_term in matching_query_terms:
                    matching_variable_bindings = query.match_variable_bindings(matching_query_term)
                    for variable_name, variable in query_variable_map.items():
                        solutions_map[variable_name].append(matching_variable_bindings.get(variable))

                return solutions_map

            else:
                return True if not variables_in_query else None
        
        else:
            return False if not variables_in_query else None