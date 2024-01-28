def Files():
    import os
    file = open('README.md', 'a')
    for i in os.listdir("Tests"):
        with open('Tests/' + i, 'r') as Test:
            file.write("\n**/Tests/" + i +"**\n```python\n" + Test.read() + "```\n")
    file.close()

def Run():
    import os
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
    Question = input("Do you want to write Tests/ files to README.md? (y/n) ")
    if Question == "y" or "yes":
        Run()
        Files()
    elif Question == "n" or "no":
        Run()

