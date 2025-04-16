dic = {"Asha" : "1234", "Abhi":"8727"}

def log_in(name,password):
    if name in dic:
        if dic[name] == password:
            return "Login successfull"
        else:
            return "Login unsuccessfull"
    else:
        return "User doesn't exist"
    
print(log_in("Asha","12"))
print(log_in("Asha","1234"))
print(log_in("A","12"))