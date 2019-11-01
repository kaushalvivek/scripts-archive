import pyperclip

while True:
    col = input('Enter Column : \n')
    array = input("Enter Values :\n")
    output = ''
    length = len(array)
    for i in range (0,length):
        if array[i] == '2':
            output = output + col+str(i+2)+','

    pyperclip.copy(str(output.rstrip(',')))
    print('Done\n')