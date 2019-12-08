from functools import reduce

class Term:

    def __init__(self,functor,arguments = []):
        self.functor = functor
        self.arguments = arguments
    
    def match_variable_bindings(self,other_term):

        if isinstance(other_term, Variable):
            return other_term.match_variable_bindings(self)

        if isinstance(other_term,Term):
            if self.functor != other_term.functor or len(self.arguments) != len(other_term.arguments):
                return None
            
            zipped_argument_list = list(zip(self.arguments,other_term.arguments))

            matched_argument_var_bindings = [arguments[0].match_variable_bindings(arguments[1]) for arguments in zipped_argument_list]

            return reduce(Database.merge_bindings,[{}] + matched_argument_var_bindings)

    def substitute_variable_bindings(self,variable_bindings):
        return Term(self.functor,[argument.substitute_variable_bindings(variable_bindings) for argument in self.arguments])

    def query(self,database):
        yield from database.query(self)

    def __str__(self):
        return str(self.functor) if len(self.arguments) == 0 else str(self.functor) + " ( " + ", ".join(str(argument) for argument in self.arguments) + " ) "

    def __repr__(self):
        return str(self)


class Right ( Term ):

    def __init__(self, functor = 'TRUE', arguments = []):
        super().__init__(functor, arguments = arguments)

    def substitute_variable_bindings(self, variable_bindings):
        return self
    
    def query(self, database):
        yield self

class Variable:

    def __init__ (self,name):
        self.name = name
    
    def match_variable_bindings(self, other_term):
        bindings = {}

        if self != other_term:
            bindings[self] = other_term
            
        return bindings

    def substitute_variable_bindings(self,variable_bindings):
        bound_variable_value = variable_bindings.get(self)

        if bound_variable_value:
            return bound_variable_value.substitute_variable_bindings(variable_bindings)
        
        return self

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)

class Rule:

    def __init__(self,head,tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        return str(self.head) + ' :- ' + str(self.tail)

    def __repr__(self):
        return str(self)

class Conjunction(Term):

    def __init__(self, arguments):
        self.functor = ''
        self.arguments = arguments

    def query(self, database):
        
        def find_solutions(self, database, argument_index, variable_bindings):

            if argument_index >= len(self.arguments):
                yield self.substitute_variable_bindings(variable_bindings)
            else:
                current_term = self.arguments[argument_index]

                for item in database.query(current_term.substitute_variable_bindings(variable_bindings)):
                    combined_variable_bindings = Database.merge_bindings(current_term.match_variable_bindings(item),variable_bindings)

                    if combined_variable_bindings is not None:
                        yield from find_solutions(self, database, argument_index + 1, combined_variable_bindings)

        yield from find_solutions(self,database,0,{})

    def substitute_variable_bindings(self, variable_bindings):
        return Conjunction([argument.substitute_variable_bindings(variable_bindings) for argument in self.arguments])
    
    def __str__(self):
        return ", ".join(str(argument) for argument in self.arguments)

    def __repr__(self):
        return str(self)

class Database:

    def __init__(self,rules):
        self.rules = rules

    def query(self,goal):

        for index, rule in enumerate(self.rules):
            matching_head_var_bindings = rule.head.match_variable_bindings(goal)

            if matching_head_var_bindings is not None:
                
                matched_head_item = rule.head.substitute_variable_bindings(matching_head_var_bindings)
                matched_tail_item = rule.tail.substitute_variable_bindings(matching_head_var_bindings)

                for matching_item in matched_tail_item.query(self):

                    matching_tail_var_bindings = matched_tail_item.match_variable_bindings(matching_item)
                    yield matched_head_item.substitute_variable_bindings(matching_tail_var_bindings)

    @staticmethod

    def merge_bindings(first_bindings_map, second_bindings_map):

        if first_bindings_map is None or second_bindings_map is None:
            return None

        merged_bindings = {}

        for variable, value  in first_bindings_map.items():
            merged_bindings[variable] = value
        
        for variable, value in second_bindings_map.items():

            if variable in merged_bindings:

                existing_variable_binding = merged_bindings[variable]
                shared_bindings = existing_variable_binding.match_variable_bindings(value)

                if shared_bindings is not None:
                    for variable, value in shared_bindings.items():
                        merged_bindings[variable] = value
                else:
                    return None
            else:
                merged_bindings[variable] = value

        return merged_bindings

    def __str__(self):
        return ".\n".join(str(rule) for rule in self.rules)

    def __repr__(self):
        return str(self)

