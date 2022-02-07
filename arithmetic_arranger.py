import re

def arithmetic_arranger(problems,solve=False):
    """Rewrite arithmetic problems in a vertical way.

    This function assumes that all the problems have only two arguments.

    Parameters
    ----------
    problems : list
        List containing strings with the arithmetics problems to be formated.
    solve: bool
        If True, the solution returns also the solution of the problems.
        default value : False 

    Returns
    -------
    arranged_problems : str
        String containing the problems reformated.
    """
    # Define a flag indicating of there is an error
    flag = False

    # Check if there are more than 5 problems
    if len(problems)>5:
        arranged_problems = "Error: Too many problems."
    else:
        operations = []
        operands_list = []
        operands_max_len = []
        for problem in problems:
            # Use regular expresions for finding operations and operands
            operation = re.findall(r'[+-]', problem)
            operands = re.split(r'\s[+-]\s', problem)
            # Check if the operations are '+' or '-'
            if len(operation) == 0:
                arranged_problems = "Error: Operator must be '+' or '-'."
                flag = True
                break
            else:
                operands_len = []
                for operand in operands:
                    # Check the lenght of the operands
                    if len(operand) > 4:
                        arranged_problems = "Error: Numbers cannot be more than four digits."
                        flag = True
                        break
                    else:
                        # Try to convert operands to int for checking their format
                        try:
                            int(operand) 
                        except ValueError:
                            arranged_problems = "Error: Numbers must only contain digits."
                            flag = True
                            break
                    operands_len.append(len(operand))
                # Store maximum lenght of the operans in each operation
                operands_max_len.append(max(operands_len))
                if flag == True:
                    break
            # Store operations and operands of each problem
            operations.append(operation)
            operands_list.append(operands)
        
        # Write the outcome of the function if there are no errors in the inputs
        if flag == False:
            arranged_problems = ""
            # Define number of lines depending on whether the result of the operations must be shown or not
            if solve == True:
                nlines = 4
            else:
                nlines = 3
            
            for j in range(nlines):
                for i,operands in enumerate(operands_list):
                    # Create four spaces separation between operations
                    if i > 0:
                        arranged_problems+='    '
                    # Define the lenght of each operation based on the lenght of the operands
                    if j != 1:
                        op_len = operands_max_len[i] + 2
                    else:
                        # Include the operation in the second line
                        arranged_problems +=f"{operations[i][0]:s} "
                        op_len = operands_max_len[i]
                    if j < 2:
                        arranged_problems +=f"{operands[j]:>{op_len}s}"
                    # Include a result line in the third line
                    if j == 2:
                        arranged_problems += "-"*op_len
                    # Print the result of the problems
                    if j == 3:
                        if operations[i][0] == "+":
                            result = int(operands[0]) + int(operands[1])
                        else:
                            result = int(operands[0]) - int(operands[1])
                        arranged_problems +=f"{result:>{op_len}d}"
                    if (i == len(operands_list)-1) & (j < nlines-1):
                        arranged_problems += "\n"

    return arranged_problems