def get_input(f, lines_per_case, transforms):
    numCases = int(f.readline())
    
    case_inputs = []

    for case in range(numCases):
        case_input = []

        for i in range(lines_per_case):
            case_input.append(transforms[i](f.readline().strip()))

        case_inputs.append(case_input)

    return (numCases, case_inputs)

def get_output_string(case, ans):
    return 'Case #' + str(case) + ': ' + str(ans) + '\n'

def print_output(fw, numCases, case_inputs, get_ans):
    for case in range(1, numCases + 1):
        fw.write(get_output_string(case, get_ans(case_inputs[case-1])))

def process(fname, num_lines, transforms, get_ans):
"""Process the input to calculate and write out the correct output

fname --  The name of the input file
num_lines -- The number of lines PER case
transforms -- The transforms to apply to each line of a case
get_ans -- The method that takes a case as an input and returns the output for the case
"""
   
    with open(fname) as fr, open(fname + '.out', 'w') as fw:
        numCases, case_inputs = get_input(fr, num_lines, transforms)
        print_output(fw, numCases, case_inputs, get_ans)
