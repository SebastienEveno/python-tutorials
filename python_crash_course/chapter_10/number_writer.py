import json

if __name__ == "__main__":
    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f:
        json.dump(numbers, f)
    
    with open(filename) as f:
        numbers = json.load()
    print(numbers)