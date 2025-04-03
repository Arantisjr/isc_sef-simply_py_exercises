status_code = 404

def check_code(status_code):
    match status_code:
        case 200:
            return "OK: The request was successful."
        case 301:
            return "Moved Permanently: The resource has been permanently moved."
        case 404:
            return "Not Found: The requested resource was not found."
        case 500:
            return "Internal Server Error: The server encountered an error."
        case _:
            return f"Unknown status code: {status_code}"
        


print(check_code(status_code))



# if status_code == 200:
#     print("OK: The request was successful.")
# elif status_code == 301:
#     print("Moved Permanently: The resource has been permanently moved.")
# elif status_code == 404:
#     print("Not Found: The requested resource was not found.")
# elif status_code == 500:
#     print("Internal Server Error: The server encountered an error.")
# else:
#     print(f"Unknown status code: {status_code}")