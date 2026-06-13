def get_http_error(error_code):
    result = ''
    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad request"
        case 404:
            result = "Not found"
        case _:
            result = "Uknown error"
    return result
 
def main():
    print(get_http_error(400))
 
if __name__ == "__main__":
    main()