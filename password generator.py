import  random
import string
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*()_+{}[]|\:;'?/><"
all_chars = lower + upper + numbers + symbol
length = 16
password = ''.join(random.sample(all_chars,length))
print("Generated Password: ",password)