import re
from Interpreter import *

class Parser:

    def __init__(self, input_text):

        self.token_regex = '[A-Za-z0-9_]+|:\-|[()\.,]'
        self.atom_name_regex = '^[A-Za-z0-9_]+$'
        self.variable_regex = '^[A-Z_][A-Za-z0-9_]*$'

        self.comment_regex = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|%[^\r\n]*$)"

        tokens = self.get_token_list(input_text)

        self.tokens = tokens
        self.token_iterator = iter(self.tokens)

        self.current = None
        self.finished = False
        self.scope = None

        self.parse_next()

    def remove_comments(self,input_text):

        regex = re.compile(self.comment_regex,re.MULTILINE|re.DOTALL)

        def remove_comment(match):
            if match.group(2) is not None:
                return ''
            else:
                return match.group(1)
        
        return regex.sub(remove_comment,input_text)

    def get_token_list(self, input_text):
        iterator = re.finditer(self.token_regex,self.remove_comments(input_text))
        return [token.group() for token in iterator]

    def parse_rules(self):
        rules = []
        
        while not self.finished:
            self.scope = {}
            rules.append(self.parse_rule())

        return rules

    def parse_query(self):
        self.scope = {}
        return self.parse_term()

    def parse_next(self):
        try:
            self.current = next(self.token_iterator)
            self.finished = self.token_iterator.__length_hint__() <= 0
        except StopIteration:
            self.finished = True

    def parse_atom(self):
        name = self.current

        if re.match(self.atom_name_regex,name) is None:
            raise Exception("Invalid Atom Name: " + str(name))

        self.parse_next()

        return name

    def parse_term(self):

        if self.current == '(' :

            self.parse_next()
            arguments=[]

            while self.current != ')':
                arguments.append(self.parse_term())

                if self.current not in (',',')'):
                    raise Exception('Expected , or ) in term but got ' + str(self.current))

                if self.current == ',':
                    self.parse_next()

            self.parse_next()

            return Conjunction(arguments)

        functor = self.parse_atom()

        if re.match(self.variable_regex, functor) is not None:

            if functor == '_':
                return Variable('_')

            variable = self.scope.get(functor)

            if variable is None:
                self.scope[functor] = Variable(functor)
                variable = self.scope[functor]

            return variable

        if self.current != '(':
            return Term(functor)

        self.parse_next()

        arguments = []

        while self.current != ')':
            arguments.append(self.parse_term())

            if self.current not in (',',')'):
                raise Exception('Expected , or ) in term but got ' + str(self.current))

            if self.current == ',':
                    self.parse_next()
        
        self.parse_next()

        return Term(functor,arguments)

    def parse_rule(self):
        head = self.parse_term()

        if self.current == '.':
            self.parse_next()
            return Rule(head,Right())

        if self.current != ':-':
            raise Exception('Expected :- in rule but got ' + str(self.current))

        self.parse_next()

        arguments = []

        while self.current != '.':
            arguments.append(self.parse_term())

            if self.current not in (',','.'):
                raise Exception('Expected , or . in term but got ' + str(self.current))

            if self.current == ',':
                self.parse_next()

        self.parse_next()

        tail = arguments[0] if arguments == 1 else Conjunction(arguments)
        return Rule(head,tail)