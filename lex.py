def write_file():
        with open("diqka.txt", 'wt') as file:
            content = file.write("Hello World")
            print(content)
            file.close()

write_file()       

def read_file():
        with open("diqka.txt", 'rt') as file:
            content = file.readline()
            print(content)
            file.close()

read_file()