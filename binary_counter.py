def binary_counter():
    # get user input and convert to int
    try:
        # +1 so that range iterates up to and including the requested number
        n = int(input('Enter the base 10 number to count to binary to: ')) + 1
    except ValueError:
        print('Not a valid number!')
        binary_counter()
    # iterate through the requested number
    for x in range(n):
        binary_output = ''
        # get initial quotient and remainder as tuple
        q, r = divmod(x, 2)
        # use the while loop for indefinite iteration until quotient is 0
        while q >= 0:
            # add 0 or 1 to the left of our binary number result
            # no remainder is 0, anything else is 1
            if r == 0:
                binary_output = '0' +  binary_output
            else:
                binary_output = '1' +  binary_output
            # exit the while loop if quotient is 0
            if q == 0:
                break
            # divide the number by 2, return the quotient and remainder as a tuple
            q, r = divmod(q, 2)

        print(f'{x} in binary is {binary_output}')

    return print(f'counter complete, counted to {n - 1}')

binary_counter()
