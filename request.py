import urllib.request

url = "https://www.google.com" # URL da página que você deseja acessar
response = urllib.request.urlopen(url) # abre a página web
webContent = response.read() # lê o conteúdo da página web
textFile = open("pagina.txt", "wb") # abre um arquivo de texto para escrever o conteúdo
textFile.write(webContent) # escreve o conteúdo da página web no arquivo de texto
textFile.close() # fecha o arquivo de texto
