def cipher(msg):
    return "".join([chr(219 - ord(i)) if i.islower() else i for i in msg])
msg = "Hello, world!"
code = cipher(msg)
print("暗号化: " + code)
print("復号: " + cipher(code))