import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"#https://t.me/j_b_i\nimport base64\nexec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("\033[2;36m [?] اسم الملف : ")
    
    print(f"\x1b[1;92m \n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
