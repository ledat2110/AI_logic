from solver import *

def read_file(file_name):
    try:
        with open(file_name) as fn:
            text = fn.read()
        fn.close()

        text = text.split('%questions\n')

        rules_text = text[0]
        query_text = text[1]
        
        query_text = query_text.split('\n')
        
        return rules_text, query_text
    except:
        print("File does not exist")

def write_file(file_name, text):
    try:
        with open(file_name,'w') as fn:
            for line in text:
                fn.write(line + '\n')
        fn.close()
    except:
        print("File does not exist")

def main():
    file_name = str(input('your KB file name: '))

    rules_text, query_text = read_file(file_name)

    solver = Solver(rules_text)

    solutions = []
        
    for query in query_text:
        solution = solver.find_solutions(query)
        if isinstance(solution, bool):
            solutions.append('True.' if solution else 'False.')

        elif isinstance(solution, dict):
            solutions.append("\n".join("{} = {}".format(variable, value[0] if len(value) == 1 else value) for variable, value in solution.items()))
                                                        
        else:
            solutions.append("No solutions found.")

    write_file('solutions.txt',solutions)


if __name__ == "__main__":
    main()

