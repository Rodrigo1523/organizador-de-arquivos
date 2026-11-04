from pathlib import Path
import shutil

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi"],
}


def descobrir_categoria(extensao):
    """Recebe uma extensão (ex: '.png') e devolve o nome da categoria."""
    for categoria, extensoes in CATEGORIAS.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"


def organizar(pasta):
    """Move cada arquivo da pasta para uma subpasta da sua categoria."""
    pasta = Path(pasta)

    if not pasta.is_dir():
        print("Pasta não encontrada. Verifique o caminho.")
        return

    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            categoria = descobrir_categoria(arquivo.suffix)
            destino = pasta / categoria
            destino.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino / arquivo.name))
            print(f"Movido: {arquivo.name} -> {categoria}/")

    print("Organização concluída!")


if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta: ")
    organizar(caminho)