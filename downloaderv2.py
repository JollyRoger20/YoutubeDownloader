from pytube import YouTube
from pathlib import Path


class NameGenerator:
    def __init__(self, name, badchars):
        self.name = name
        self.badchars = badchars

    def clean(self):
        for x in self.name:
            if x in self.badchars:
                if x == '$':
                    self.name = self.name.replace("$","s")
                    return self.name
                elif x in chars:
                    self.name = self.name.replace(x, ' ')
                    return self.name
            else:
                return self.name
    #def addBadCharacters(self):




print(f"#####################################\n# Python Music and video Downloader #\n#####################################\n")

while True:

    try:
        path = Path(input("Escribe el destino de la descarga: "))
        path = path.cwd().joinpath(path)
        if path.exists():
            break
        else:
            raise FileNotFoundError

    except FileNotFoundError: #investigar nombre error path inexistente
        print("Ese directorio no existe, intenta con otro")

print("Los archivos se descargarán en", path)

links = []

while True:
    url = input("Ingresa el link del video: ")
    if url:
        links.append(url)
    else:
        break

yts = []

for link in links:
    yt = YouTube(link)
    yts.append(yt)
    

chars = ['$', '.', '|',]

for yt in yts:
    name = yt.title
    ng = NameGenerator(yt.title,chars)
    name = ng.clean()
    print(f"Escoge un stream para {yt.title}:\n ")
    streams = yt.streams
    
    try:
        import prettytable
        
    except ImportError:

        for s in streams:
            print(str(streams.index(s) + 1) + "." + str(s) )
    
    while 1:

        try:
            strm = int(input("ingresa el número que prefieras: "))

            if strm > len(streams):
                raise ValueError
            else:
                yt.streams[strm - 1].download(output_path = path , filename= name)
                break

        except ValueError:
            print("[ERROR] Escoge uno de los valores de la lista")
            continue 

