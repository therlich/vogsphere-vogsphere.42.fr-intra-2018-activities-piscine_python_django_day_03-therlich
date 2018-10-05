from path import Path

def execute():
    Path.mkdir('./my_dir')
    Path('./my_dir/my_file.txt').touch()
    my_file=open('./my_dir/my_file.txt','r+')
    my_file.write("Hello world!")
    my_file.seek(0)
    print(my_file.read())


if __name__=="__main__":
    execute()
