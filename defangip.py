def defangip(address):
    new_address = ""
    split_address = address.split(".")
    print(split_address)
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address

print(defangip("1.1.2.3"))
