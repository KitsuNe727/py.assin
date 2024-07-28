def operations():
    x = set(['addition', 'subtraction', 'multiplication', 'division', 'modulus'])

    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))

    add_result = n + m
    sub_result = n - m
    mul_result = n * m
    div_result = n / m
    mod_result = n % m

    results_set = {
        ('addition', add_result),
        ('subbtraction', sub_result),
        ('multiplication', mul_result),
        ('division', div_result),
        ('modulus', mod_result)
    }


    for assign, y in results_set:
        print(f"The {assign} of {n} and {m} is: {y}")

operations()
