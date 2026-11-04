from pathlib import Path

pasta = Path("teste")
pasta.mkdir(exist_ok=True)

nomes = [
    "foto1.jpg", "foto2.png", "curriculo.pdf", "notas.txt",
    "planilha.xlsx", "video.mp4", "musica.mp3", "backup.zip",
    "instalador.exe", "arquivo_estranho.xyz",
]

for nome in nomes:
    (pasta / nome).touch()

print("Pasta 'teste' criada com", len(nomes), "arquivos.")
