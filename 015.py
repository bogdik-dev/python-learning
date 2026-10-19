text = "я помню чудное мгновенье"
x = 0
i = 0
while i < len(text):
    if text[i] == "м":
        x += 1
    i += 1
print(x)