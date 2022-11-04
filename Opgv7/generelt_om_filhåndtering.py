def write_to_file(data):
    f=open("my_file.txt","w")
    f.write(data)
    f.close()

def read_from_file(file):
    f=open("my_file.txt","r")
    innhold=f.read()
    print(innhold)
    
def main():
    answer=""
    while answer!="done":
        answer = input("Do you want to read or write")
        if answer =="write":
            inp=input("what do you want to write")
            write_to_file(inp)
        elif answer == "read":
            read_from_file("my_file.txt")
        elif answer =="done":
            return
main()