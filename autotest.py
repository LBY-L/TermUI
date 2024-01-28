import os
def Files():
    file = open('README.md', 'a')
    for i in os.listdir("Tests"):
        with open('Tests/' + i, 'r') as Test:
            file.write("\n**/Tests/" + i +"**\n```python\n" + Test.read() + "```\n")
    file.close()

def Run():
    try:
        os.system("pip3 install .")
    except:
        os.system("pip3 install --break-system-packages .")
    
    try:
        os.remove("TermUI.egg-info")
        os.remove("build")
    except:
        pass

    for i in os.listdir("Tests"):
        os.system("python3 Tests/" + i)
    print("\nTest Compleated!")
    
if __name__ == "__main__":
    Green = "\x1b[32m"
    Yellow = "\x1b[33m"
    Red = "\x1b[91m"
    Magenta = "\x1b[35m"
    Reset = "\x1b[0m"
    
    Question = input(f"{Green}Do you want to write Tests/ files to README.md? ({Yellow}y{Reset}/{Red}n{Reset}/{Magenta}c{Reset}{Green}){Reset} ")
    Question = Question.lower()
    if Question == "y" or Question == "yes":
        Run()
        Files()
    elif Question == "n" or Question == "no":
        Run()
    elif Question == "c" or Question == "cancel":
        pass

