n= input('How many times')
min=None
max=None
for i in range(n):
    broj=input('Brojevi:\n\n')
    if min is None:
        min=broj;
        max=broj;
    elif broj < min:
        min=broj
    elif broj > max:
        max = broj
print ("max je ", max)
print ("min je ", min)
