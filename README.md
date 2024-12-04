# manipulador_txt
 Script para manipular textos e/ou palavas.

 O script necessita de duas pastas para seu funcionamento.
 1 - Pasta com as imagens utilizadas nos icones dos botões.
 2 - Pasta para o armazenamentos dos arquivos de audios criados.

manipulador_txt/
│
├── manipulador_txt.py  # Código principal
├── Manipulador_TXT/
│   ├── audios  # Destino dos áudios criados
│   ├──icones  # Pasta com as imagens
│       ├── cadeado.ico
│       ├── cheve.ico
│       ├── icone de som.png
│       ├── manipulador_txt_icone.ico
├── README.md  

 IMPORTANTE:
 Ao executar o script, dará um ERRO inicial necessário, 
 o programa criará as pastas necessárias. Certifique-se 
 que as imagens disponibilizadas estão dentro da pasta "icones".

 Então a segunda vez que você executar, ele rodará sem problemas.

 O código tem as seguintes funcionalidades:
 "Multifuncional" e "Número" - Enumerar - Multiplicar
 "Digite seu código" - Demais funções
 "Transcrição" - Resultados dos comandos
 "Formatar" - Muda a formatação de exibição dos resultados.

 Selecionar arquivos - Utilizar textos de arquivos no formato .txt 
                       do computador do usuário.
 Botões Verde e Vermelho - Encriptação de textos na Cifra de César (Base 3).
                          (
                            É possivel alteração da Base no código fonte do projeto. 
                          Basta o conhecimento de como funciona a Cifra de César. 
                          Então faça o deslocamento do alfabéto na variável: 
                          "cifra = str.maketrans", nas funções 'Encriptar' e 'Decriptar'. 
                          Obs: Você precisa modificar corretamente os 4 alfabetos.
                          )
Dica: 
    A Cifra de César é uma Encriptação de nivél baixo. Para aumentar a segurança, 
    estude a cifra e utilize Bases diferentes para letras maiúsculas e minúsculas.

Bom Uso! 