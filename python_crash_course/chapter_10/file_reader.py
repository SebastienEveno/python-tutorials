if __name__ == "__main__":
    # file_name = 'pi_digits.txt'
    # with open(file_name) as file_object:
    #     lines = file_object.readlines()
    
    # pi_string = ''
    # for line in lines:
    #     pi_string += line.strip()

    # print(pi_string)
    # print(len(pi_string))

    file_name = 'pi_million_digits.txt'
    with open(file_name) as file_object:
        lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    
    print(f"{pi_string[:52]}...")
    print(len(pi_string))

    if '042993' in pi_string:
        print("Your birthday appears in the first million digits of pi!")