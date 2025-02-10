def adder(text):
    sum = 0
    adderOn = True 
    number = "" 

    i = 0
    while i < len(text):
        c = text[i]  

        if c.isdigit():
            number += c
        else:
            if number:  
                if adderOn: 
                    sum += int(number) 
                number = "" 

            if c.lower() == 'o':
                if i + 2 < len(text) and text[i:i+3].lower() == "off":
                    adderOn = False 
                    i += 2 
                elif i + 2 < len(text) and text[i:i+2].lower() == "on":
                    adderOn = True
                    i += 1  
            if c == '=':
                print(sum)

        i += 1 

    if number and adderOn:
        sum += int(number)

    return sum  

test_strings = [
    "123on456off789=on12",
    "567Off32On123Off456On78",
    "On123=Off456On789",
    "On12345O==ff67890On1112",
    "dwadwab=567awsOff1dwaknd32=On2323easy12"
]

for text in test_strings:
    result = adder(text)
    print(f"String: {text}")
    print(f"Resultado: {result}\n")
