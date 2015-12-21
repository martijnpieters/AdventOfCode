import md5

key = "bgvyzdsv"
i = 0
while True:
    h = md5.new(key + str(i)).hexdigest()
    if h.startswith("00000"):
        print(i)
        exit()
    i += 1