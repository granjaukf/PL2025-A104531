import re

def markdownCabecalho(markdown):
    markdown = re.sub(r'^(#{1,3})\s*(.*)$',
                      lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>",
                      markdown, flags=re.MULTILINE)
    return markdown

def markdownBold(markdown):
    markdown = re.sub(r'\*\*(?P<bold>.*?)\*\*',r'<b>\g<bold></b>',markdown)
    
    return markdown

def markdownItalic(markdown):
    markdown = re.sub(r'\*(?P<italic>.*?)\*',r'<i>\g<italic></i>',markdown)
    
    return markdown

def markdownLink(markdown):
    markdown = re.sub(r'\[(?P<texto>.*?)\]\((?P<link>.*?)\)',r'<a href="\g<link>">\g<texto></a>',markdown)
    
    return markdown

def markdownImagem(markdown):
    markdown = re.sub(r'!\[(?P<texto>.*?)\]\((?P<link>.*?)\)',r'<img src="\g<link>" alt="\g<texto>"/>',markdown)
    
    return markdown
    
def markdownListaNumerada(markdown):
    def list_replacer(match):
        items = match.group('items').strip().split("\n")
        items_html = "\n".join(f"<li>{item[3:]}</li>" for item in items)
        return f"<ol>\n{items_html}\n</ol>"

    markdown = re.sub(r'(?P<items>(?:^\d+\..*\n?)+)', list_replacer, markdown, flags=re.MULTILINE)
    
    return markdown


def main():
    
    file = open("resultados.txt",'w')
    
    cabecalho = "# Exemplo"
    markdown1 = markdownCabecalho(cabecalho)
        
    bold = "Este é um **exemplo**"
    markdown2 = markdownBold(bold)
        
    italic = "Este é um *exemplo*"
    markdown3 = markdownItalic(italic)
        
    imagem = "Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)"
    markdown4 = markdownImagem(imagem)
    
    link = "Como pode ser consultado em [página da UC](http://www.uc.pt)"   
    markdown5 = markdownLink(link)
    
    listaNumerada = """1. Primeiro item
2. Segundo item
3. Terceiro item"""
    markdown6 = markdownListaNumerada(listaNumerada)
    
    print("Conversão do cabeçalho:", markdown1, file=file)
    print("-------------------------------------",file=file)
    print("Conversão bold:", markdown2,file=file)
    print("-------------------------------------",file=file)
    print("Conversão italic:", markdown3,file=file)
    print("-------------------------------------",file=file)
    print("Conversão imagem:", markdown4,file=file)
    print("-------------------------------------",file=file)
    print("Conversão link:", markdown5,file=file)
    print("-------------------------------------",file=file)
    print("Conversão da lista numerada:\n", markdown6,file=file)
    
    
if __name__ == "__main__":
    main()
        
        