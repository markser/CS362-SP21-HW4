# to run
# python3 averageInList.py
# then input elements in console one by one, list finishes when user inputs string

def main():
    # print("Enter integer to include in list, any non integers will exit and compute the average")
    # try block to handle the exception
    try:
        my_list = []
        
        while True:
            my_list.append(float(input()))
            
    # if the input is not-integer, just print the list
    except:
        print("This is the user input list: {0}".format(my_list))
        average = sum(my_list)/len(my_list) if len(my_list) else 0
        print("This is the average of elements in the list: {0}".format(average))


if __name__ == "__main__":
    main()
