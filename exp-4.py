from copy import deepcopy

InitialState=['B','C','D','A']
GoalState=['A','B','C','D']
ResidialStack=[[],[],[],['B','C','D','A']]
new=[['A'], ['D'], ['C'], ['B']]
def solve(Stack):
    while True:
        cost=calculate_cost(Stack)
        print(Stack,cost)
        Stack=generate_solutions(Stack,cost)
        if GoalState in Stack:
            print(Stack,calculate_cost(Stack))
            print("Goal Found")
            break


def generate_solutions(ResidialStack,f):
    bestneighbor = ResidialStack
    # print("Neighbors:")
    for i in ResidialStack:
        if(len(i)==0):
            continue
        ele=i[-1]
        for j in range (len(ResidialStack)):
            if ResidialStack[j]==i:
                continue
            else:
                ResidialStack[j].append(ele)
                i.remove(ele)
                # print(ResidialStack,calculate_cost(ResidialStack))
                if calculate_cost(ResidialStack)>f:
                    bestneighbor=deepcopy(ResidialStack)
                    f=calculate_cost(ResidialStack)
                    # print("selected:",bestneighbor)
                ResidialStack[j].remove(ele)
                i.append(ele)

    return bestneighbor
        
    
def calculate_cost(stacks):
    cost=0
    for stack in stacks:
        for i in range(len(stack)):
            if stack[i]!=GoalState[i]:
                cost-=i
            else:
                cost+=i
    return cost

solve(ResidialStack)
# sol=generate_solutions(new,0)
