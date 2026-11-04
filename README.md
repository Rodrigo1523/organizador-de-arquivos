# Organizador Automático de Arquivos

Script em Python que organiza uma pasta bagunçada, separando os arquivos
em subpastas por tipo (Imagens, Documentos, Vídeos, etc.).

## Como usar

1. Clone o repositório:
```bash
   git clone https://github.com/Rodrigo1523/organizador-de-arquivos.git
   cd organizador-de-arquivos
```
2. Execute o script:
```bash
   python organizador.py
```
3. Digite o caminho da pasta que deseja organizar.

## Exemplo

Antes:
```
teste/
├── foto1.jpg
├── curriculo.pdf
└── video.mp4
```

Depois:
```
teste/
├── Imagens/foto1.jpg
├── Documentos/curriculo.pdf
└── Videos/video.mp4
```

## Tecnologias

- Python 3
- Bibliotecas padrão: `pathlib`, `shutil`

## Próximos passos

- [ ] Modo simulação (`--dry-run`)
- [ ] Receber a pasta por argumento (`argparse`)
- [ ] Tratar arquivos com nomes repetidos
- [ ] Registrar um log das ações
- [ ] Testes automatizados com `pytest`
