def count(hours):
    minutes = hours * 3 
    result = 2 ** minutes
    return result

bacteria = int(input('\nEnter initial count of bacteria: '))
hours = int(input('Enter the number of hours: '))
print('\nThe number of bacteria per hour will be:')

result = 0
for i in range (1, bacteria + 1):
    result += count(hours)
    print(f"Hour {i} = {result}")
print()