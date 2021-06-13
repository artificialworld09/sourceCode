data={
    'hi':'Hello sir, how are you?',
    'how are you?':'I am fine sir',
    'who are you?':"I'm a Python program, my name is Alexa",
    'hello':'Hello sir, how are you?',
    'what is your name':'My name is Alexa',
    'how old are you':"I'm 12 years old",
}
while True:
    d=input('Ask you question: ').lower()

    for i in data:
        q=i
        a=data[i]

        if d in q:
            print('\t',a)
    if d=='goodbye':
        print('\tShuting down, Thank you sir...')
        break