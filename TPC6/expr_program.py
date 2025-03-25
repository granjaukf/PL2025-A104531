# expr_program.py
# 2025-03-17 by rmg
# ----------------------
from expr_anasin import rec_Parser
def main():
    file = open("resultados.txt", "w")
    resultado1 = rec_Parser("2+3")
    print(f"2+3 = {resultado1}",file=file)
    
    resultado2 = rec_Parser("67-(2+3*4)")
    print(f"67-(2+3*4) = {resultado2}",file=file)  
    
    resultado3 = rec_Parser("(9-2)*(13-4)")
    print(f"(9-2)*(13-4) = {resultado3}",file=file)  


if __name__ == "__main__":  
    main()