from login import log_in

def test_cases():
    assert((log_in("Asha","12"))) == "Login unsuccessfull"
    assert((log_in("Asha","1234"))) == "Login successfull"
    assert((log_in("A","12"))) == "User doesn't exist"

