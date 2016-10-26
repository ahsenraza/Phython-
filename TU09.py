Error=0
while True:
    mynumber=input('Please Enter A Number:')
    try:
        valid_number=int(mynumber)
        break
    except ValueError:
        Error=Error+1
        print("Seriously, don't you read the Instruction.\n asked for a number...")

print(valid_number, 'error', Error)
