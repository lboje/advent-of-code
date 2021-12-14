"""
Reads from an input.txt file. 



"""
import os


def main():
    decreasing = 0
    increasing = 0

    filePath = os.path.join(os.path.dirname(__file__), "input.txt")

    #Note: I'm pretending that incorrect input files don't exist for advent of code
    with open(filePath, "r") as file:
        line = file.readline()
        precedent = int(line.strip())
        line = file.readline()

        while line:
            line = int(line.strip())
            if line > precedent:
                increasing = increasing + 1
            else:
                decreasing = decreasing + 1
            precedent = line
            line = file.readline()
    print(increasing)


if __name__ == "__main__":
    main()