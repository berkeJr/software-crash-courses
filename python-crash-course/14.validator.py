# Example of a custom module to be imported


# Here we imported regular expression core module. 
import re


# Here we created a function named validate_email(email)
def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email)) # We use match function here. 
# returns true or false 