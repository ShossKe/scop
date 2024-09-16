

import sys
file = open(sys.argv[1],"w+")
desf = {"key":[],"data":[]}
data = {"key":[],"data":[]}
def keyset(*kw):
    reload()
    data.update(key=list(kw))
def add(*kw):

    kw = list(kw)
    data["data"].append(kw)
def show():

    print(data)    
def delete(*,dat):

    
    for i in data["data"]:
        for k in range(len(i)): 
                for v in range(len(i[k])):
                    if data["key"][v] == zip(dat)[k]: 
                        if data["data"][i][v]:
                            x = data["data"][i]   
    data["data"].remove(x)
def reload():
    global file
    file.close()
    open(sys.argv[1],"w").close()
    file = open(sys.argv[1],"w+")

def parse():
    global f,n
    


def parse():    
    PROMPT = ">>> "
    while True:
        f = input(PROMPT)
        n = f
        if n == "exit;":
            file.close()
            sys.exit(0)
        else:    

            n = n.replace("{","(")
            n = n.replace("}",")")
            n = n.replace(";","")   
            exec(n)
        
            file.write(repr(data))

if __name__ == "__main__":

    print(
        "Scop 2024.1.0"
    )
    parse()






