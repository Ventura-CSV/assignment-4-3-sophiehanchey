def main():
    number = int(input('Enter your input: '))
    result = []
    
    # do the division 
    while number >= 2:
        result.append(number % 2)
        number = number // 2

    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
