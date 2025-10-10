import random
import string

pass_len = 12

charValues = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
print(charValues)

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("ur password: ", password)
      