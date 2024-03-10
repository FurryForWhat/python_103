a = input('5 of 4bit binary number')
after_split = a.split(',')

print(f"{after_split[0]} in decimal is {int(after_split[0],2)}") # outputမှာ fနဲ့သုံးတာကို string literal လို့ခေါ်တယ်။
print(f"{after_split[1]} in decimal is {int(after_split[1],2)}")
print(f"{after_split[2]} in decimal is {int(after_split[2],2)}")
print(f"{after_split[3]} in decimal is {int(after_split[3],2)}")
print(f"{after_split[4]} in decimal is {int(after_split[4],2)}")