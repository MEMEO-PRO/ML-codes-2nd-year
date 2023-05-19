import random 
import numpy as np


flag = False
while flag == False:
    
    binary_array = []
    decimal_array = []
    fx = []
    fx_sum = 0
    for i in range(1, 32):
        binary_string = bin(i)[2:].zfill(5)
        binary_array.append(binary_string)
    # print(binary_array)
    random_numbers = random.sample(binary_array, 4)
    # print(random_numbers)
    count = 0
    
    for binary_string in random_numbers:
        decimal_value = int(binary_string, 2)
        decimal_array.append(decimal_value)
        fx.append(decimal_value*decimal_value)
        fx_sum += decimal_value*decimal_value
        # print(f"Binary: {binary_string} -> Decimal: {decimal_value}")

    fx_avg = fx_sum/4
    expected_count = []
    for ele in fx:
        expected = ele/fx_avg
        expected_count.append(expected)

    expected_count = list(map(round,expected_count))
    # print(expected_count)

    for i in range(len(expected_count)):
        if expected_count[i] == 0:
            random_num = random.sample(binary_array,1)
            random_numbers[i] = random_num
        else:
            count = count+1

    if count == 4:
        flag = True

print("Randomly selected sample from population = ",random_numbers)  
print("Expected count = ",expected_count)


pair1_index = random.randint(1,4)
pair2_index = random.randint(1,4)

# print(pair1_index,pair2_index)
temp = 0
temp = random_numbers[0]
random_numbers[0] = random_numbers[0][:pair1_index]+random_numbers[1][pair1_index:]
random_numbers[1] = random_numbers[1][:pair1_index]+temp[pair1_index:]
temp = random_numbers[2]
random_numbers[2] = random_numbers[2][:pair2_index]+random_numbers[3][pair2_index:]
random_numbers[3] = random_numbers[3][:pair2_index]+temp[pair2_index:]

# print(random_numbers,pair1_index,pair2_index)

print("Sample after mutation: ",random_numbers)


fx = []
index = -1
high = -1
for binary_string in random_numbers:
    decimal_value = int(binary_string, 2)
    decimal_array.append(decimal_value)
    fx.append(decimal_value*decimal_value)
    # fx_sum += decimal_value*decimal_value
    # print(f"Binary: {binary_string} -> Decimal: {decimal_value}")


for i in range(len(fx)):
    # print(random_numbers[i])
    if(int(random_numbers[i],2)>high):
        high = int(random_numbers[i],2)
        index = i
        
print(f"Best Genetic combination after 1 iteration = {random_numbers[index]}")