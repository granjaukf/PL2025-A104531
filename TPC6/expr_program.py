# expr_program.py
# 2025-03-17 by rmg
# ----------------------
from expr_anasin import rec_Parser
def main():
    file = open("resultados.txt", "w")
    resultado1 = rec_Parser("5 + 3 * 2")
    print(f"5 + 3 * 2 = {resultado1}",file=file)
    
    resultado2 = rec_Parser("2 * 7 - 5 * 3")
    print(f"2 * 7 - 5 * 3 = {resultado2}",file=file)  


if __name__ == "__main__":  
    main()