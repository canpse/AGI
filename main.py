while True:
    # read the contents of ai_memory into the z list
    with open("ai_memory", "r") as file:
        z = file.readline().strip().split()
        print(z[-100:])

    # initialize the f vector to be the same as the z vector
    f = z.copy()

    # initialize the product vector to an empty list
    product = []


    # iterate through the corresponding elements of the two input vectors and concatenate them into a new string
    for z_i, f_i in zip(z, f):
        product.append(z_i + f_i)
        

    resposta = input("Reposta esperada: ").split()
    product.extend(resposta)

    # prompt the user to enter new elements and add them to the product vector
    new_elements = input("Enter new elements separated by spaces: ").split()
    product.extend(new_elements)

    # print the product vector


    # append the product vector to the end of the file "memory.txt"
    with open("ai_memory", "w") as file:
        file.writelines(" ".join(product))
