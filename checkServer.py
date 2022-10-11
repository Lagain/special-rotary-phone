import socket

def is_running(site):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        site = input('Website to check: ')
        if is_running(f'{site}.com'):
            print(f"{site}.com")
        else:
            print(f'Issue connecting to {site}.com')
        if input("Would you like to check another website? (y/n) ") in {'n', 'N'}:
            break