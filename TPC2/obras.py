from collections import defaultdict
import re

def parse(text):
    pattern = re.compile(r'([^;]+);\s*"{0,3}([\s\S]*?)"{0,3}\s*;(\d+);([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});(O\d+)')

    data = []
    
    for match in pattern.finditer(text): # return iterator de objetos match, o que permite acessar individualmente
        nome, desc, anoCriacao, periodo, compositor, duracao, _id = match.groups() # motivo dos grupos na expressao regular
        data.append({"nome": nome.strip(),
                    "desc": desc.strip(),
                    "anoCriacao": anoCriacao.strip(),
                    "periodo": periodo.strip(),
                    "compositor": compositor.strip(),
                    "duracao": duracao.strip(),
                    "_id": _id.strip()
                    })
    return data

def process_data(data):
    compositores = sorted(set(d["compositor"] for d in data))
    
    obras_por_periodo = defaultdict(int)
    titulos_por_periodo = defaultdict(list)
    
    for d in data:
        obras_por_periodo[d["periodo"]] += 1 
        titulos_por_periodo[d["periodo"].strip()].append(d["nome"])
    
    for key in titulos_por_periodo:
        titulos_por_periodo[key].sort()
        
    return compositores, obras_por_periodo, titulos_por_periodo

def main():
    with open("obras.csv",encoding="utf-8") as f:
        lines = f.readlines()[1:]
        text = "".join(lines)
                
    data = parse(text)
    
    compositores, obras_por_periodo, titulos_por_periodo = process_data(data)
    
    ficheiro = open('resultados.txt','w')
    
    print("Lista ordernada dos compositores:\n",file=ficheiro)
    for c in compositores:
        print(c,file=ficheiro)
    
    print("------------------------------------------",file=ficheiro)
    print("\nDistribuição das obras por período:\n",file=ficheiro)
    for periodo, count in obras_por_periodo.items():
        print(f"{periodo}: {count}",file=ficheiro)
        
    print("------------------------------------------",file=ficheiro)
    print("\nTítulo das obras por período:\n",file=ficheiro)
    for periodo, titulos in titulos_por_periodo.items():
        print(f"{periodo}: {', '.join(titulos)}",file=ficheiro)

if __name__ == "__main__":
    main()
    
    

    
            