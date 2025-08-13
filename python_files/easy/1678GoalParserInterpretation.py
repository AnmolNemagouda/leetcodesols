class Solution:
    def interpret(self, command: str) -> str:
        nl=""
        for i in range(0,len(command)):
            if command[i] == "G":
                nl+="G"
            elif command[i]=="(" and command[i+1]==")":
                nl+="o"
            elif command[i]=="(" and command[i+1]=="a":
                nl+="al"
        
        return nl