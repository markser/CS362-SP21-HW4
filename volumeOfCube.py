# to run the program
# python3 volumeOfCube.py 
# then input side length of the cube in console

def calculateVolumeOfCube(cubeSideLength):
    # if isinstance(cubeSideLength, str):
    #     print("Please enter a integer")
    # elif cubeSideLength < 0:
    #     print("Please enter a positive integer greater than 0")
    # else:
    print("Volume of Cube: {0}".format(cubeSideLength))
    return cubeSideLength

def retrieve_input():
    try:
        cubeSideLength = float(input('Enter side length of cube: '))
        if cubeSideLength > 0:
            return 3*cubeSideLength
        else:
            print("Please enter a positive integer greater than 0")
    except ValueError:
        print("Please enter a integer ")

def main():
    cubeSideLength = retrieve_input()
    if cubeSideLength != None:
        calculateVolumeOfCube(cubeSideLength)


if __name__ == "__main__":
    main()
