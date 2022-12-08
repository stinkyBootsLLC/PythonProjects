"""
    File Name: day05.py
    Created Date: 12/06/2022
    Author: Eduardo Estrada
    Purpose:  
        --- Day 5: Supply Stacks ---
        https://adventofcode.com/2022/day/5
        --- Part One ---
        One crate at a time  
        --- Part Two ---
        If more than one crate then MOVE all crates at a time keeping the same order
        else one crate at a time
"""

# returns a dictionary of lists of stacks with crates
def get_organized_stacks(stacks, crates):
    key = 0
    for x in reversed (crates):
        for y in x[1::4]:
            stacks[str(key)].append(y)
            key += 1
        key = 0
    return stacks

# returns an dictionary of empty lists
def get_stacks(amount):
    dict = {}
    for i in range(int(amount)):
        dict[str(i)] = []
    return dict

# returns stacks without any blank spaces
def get_clean_stacks(organized_stacks, number_of_stacks):
    
    new_stack = get_stacks(number_of_stacks)
    
    for key in organized_stacks: 
        l = [values for values in organized_stacks[key] if values.strip()]
        for v in l:
            new_stack[str(key)].append(v)
      
    return new_stack

# returns the rearranged stacks
def get_rearrange_crates(cleaned_stacks, instructions, all_crates=None):

    for x in instructions:
        steps = x.split(' ')
        amount, source, destination = map(int, [steps[1], steps[3], steps[5]])
        # we start at 0
        source -= 1
        destination -= 1

        if all_crates is not None:
            if amount > 1:
                cleaned_stacks[str(destination)].extend(cleaned_stacks[str(source)][-amount:])
                cleaned_stacks[str(source)] = cleaned_stacks[str(source)][:-amount]
            else:
                for index in range(amount):
                    crate = cleaned_stacks[str(source)].pop()
                    cleaned_stacks[str(destination)].append(crate) 
        else:
            for index in range(amount):
                crate = cleaned_stacks[str(source)].pop()
                cleaned_stacks[str(destination)].append(crate)

    return cleaned_stacks

# returns a string
def get_answer(stacks):
    answer = ""
    for key, crates in stacks.items():
        top_crate = crates.pop()
        answer += top_crate
    return answer

with open('input.txt', 'r', encoding="utf-8") as f:

    lines = f.readlines()
    instructions = [] 
    crates = [] 
    crates2 =[]
    number_of_stacks = 0

    # seperate the input file
    for line in lines:
        if len(line.strip()) > 0:
            x = line.strip()
            if x[0] == "1":
                # line with number of stacks needed
                stacks = x.replace(" ", "")
                number_of_stacks = stacks[-1]
            elif x[0] == "m":
                # start of the move to and from instructions 
                instructions.append(x)
            else:
                crates.append(line)
                crates2.append(line)

    # get the required number of stacks
    empty_stacks = get_stacks(number_of_stacks)
    empty_stacks2 = get_stacks(number_of_stacks)
    # organize the stacks and crates
    organized_stacks = get_organized_stacks(empty_stacks, crates)
    organized_stacks2 = get_organized_stacks(empty_stacks2, crates2)
    # remove blanks
    cleaned_stacks = get_clean_stacks(organized_stacks, number_of_stacks) 
    cleaned_stacks2 = get_clean_stacks(organized_stacks2, number_of_stacks)
    # perform instructions
    rearranged_stacks = get_rearrange_crates(cleaned_stacks, instructions)
    rearranged_stacks2 = get_rearrange_crates(cleaned_stacks2, instructions, "yes")
    #  get the answers
    answer1 = get_answer(rearranged_stacks)
    answer2 = get_answer(rearranged_stacks2)
    print(answer1)
    print(answer2)



         
    