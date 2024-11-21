import customtkinter as ctk
import os
from tkinter import filedialog
import datetime
from gtts import gTTS
from PIL import Image

ctk.set_appearance_mode('system')


# BUSCANDO DATA E HORA ATUAL PARA USAR NO NOME DO AQUIVO DE AUDIO
data_atual = datetime.datetime.today().strftime("%H-%M-%S__%d-%m-%y") 
# PASTA DE DESTINO
caminho = 'C:/Users/Ludmilla/Desktop/MATERIAL/auto-prints/audios/'
# IMPORTANDO IMAGENS
img_btn = ctk.CTkImage(light_image=Image.open("E:/ARQUIVOS/Programas - EXE/Programação/CodigosFinalizados/MNP-Códigos/icone de som_light.png"), dark_image=Image.open("E:/ARQUIVOS/Programas - EXE/Programação/CodigosFinalizados/MNP-Códigos/icone de som_dark.png"), size=(20, 20))

#######################################################################
# CÓDIGO PARA ALTERAÇÕES SIMPLES EM TEXTOS
def primeira_letra():
    area_texto2.delete("1.0", ctk.END)
    texto = area_texto1.get("1.0", "end-1c")
    conteudo = texto.capitalize()
    area_texto2.insert("1.0", conteudo)
    janela.after(5000, limpar_a1)

def tudo_maiuscula():
    area_texto2.delete("1.0", ctk.END)
    texto = area_texto1.get("1.0", "end-1c")
    conteudo = texto.upper()
    area_texto2.insert("1.0", conteudo)
    janela.after(5000, limpar_a1)

def tudo_minuscula():
    area_texto2.delete("1.0", ctk.END)
    texto = area_texto1.get("1.0", "end-1c")
    conteudo = texto.lower()
    area_texto2.insert("1.0", conteudo)
    janela.after(5000, limpar_a1)

def toda_primeira_letra():
    area_texto2.delete("1.0", ctk.END)
    texto = area_texto1.get("1.0", "end-1c")
    conteudo = texto.title()
    area_texto2.insert("1.0", conteudo)
    janela.after(5000, limpar_a1)


#######################################################################
# SELECIONANDO ARQUIVO TXT DO PC PARA TRANSFORMAR EM AUDIO
def selecionar_arquivo():
    arquivo_texto = filedialog.askopenfilename(title="Selecione um arquivo",
                    filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")))
    if area_texto1:
        with open (arquivo_texto, "r", encoding="utf-8") as arquivo:
             conteudo = arquivo.read()
             area_texto1.delete("1.0", ctk.END)
             area_texto1.insert("1.0", conteudo)

#######################################################################
# TRANSFORMANDO TEXTO EM AUDIO
def pegar_informacoes():
    texto = area_texto1.get("1.0", "end-1c")
    lingua = "pt"
    tts = gTTS(texto, lang=lingua)
    tts.save(f'{caminho}gerador-{data_atual}.mp3') # COMANDO PARA SALVAR
    limpar_a1()
    txt_respota()

#######################################################################
# LIMPANDO A AREA DE TEXTO 1
def limpar_a1():
    area_texto1.delete("1.0", ctk.END)

#######################################################################
# LIMPANDO A JANELA TODA
def btn_limpar():
    area_texto1.delete("1.0", ctk.END)
    area_texto2.delete("1.0", ctk.END)
        
#######################################################################
# EXIBINDO TEXTO COMO RESPOSTA
def txt_respota():
    txt_audio_resposta.configure(text="Áudio criado com sucesso!!!")
    texto_resposta.configure(text='Abrir Pasta do Audio')
    janela.after(3000, limpar_tr)    

def limpar_tr():
    txt_audio_resposta.configure(text="")
    texto_resposta.configure(text="")
    
#######################################################################
# CONSTRUÇÃO DA JANELA
janela = ctk.CTk()
janela.title('Editor de Textos')
#janela.geometry('600x510')
janela.resizable(width=False, height=False)

# TEXTO - TITULO DENTRO DA JANELA
label_da_janela = ctk.CTkLabel(janela, text='___________MANIPULADOR DE TEXTOS_____________', 
                font=('Impact', 25)).grid(row=0, column=0, columnspan=5, pady=2, padx=5)
#######################################################################
#TEXTOS DA JANELA
caixa = ctk.CTkLabel(janela, text='Digite seu texto',
         text_color='Black', font=('Verdana', 15, 'bold')).grid(row=1, column=0, pady=0, padx=0)

caixa2 = ctk.CTkLabel(janela, text='Transcrição',
         text_color='Black', font=('Verdana', 15, 'bold')).grid(row=3, column=0, sticky="w", pady=0, padx=10)
 

# AREA PARA COLHER O TEXTO
area_texto1 = ctk.CTkTextbox(janela, text_color='White', fg_color='Black', height=150, width=550)
area_texto1.grid(row=2, column=0, columnspan=5, pady=5, padx=5)

area_texto2 = ctk.CTkTextbox(janela, text_color='White', fg_color='Black', height=150, width=550)
area_texto2.grid(row=4, column=0, columnspan=5, pady=5, padx=5)

# BOTOES DE COMANDO
botao_0 = ctk.CTkButton(janela, text='Selecionar Arquivo', command=selecionar_arquivo).grid(row=1, column=4, padx=0, pady=2)

botao_1 = ctk.CTkButton(janela, text='TEXTO', command=tudo_maiuscula).grid(row=7, column=0, padx=2, pady=5)
botao_2 = ctk.CTkButton(janela, text='Texto', command=primeira_letra).grid(row=7, column=1, padx=2, pady=5)
botao_3 = ctk.CTkButton(janela, text='Texto >> Audio', command=pegar_informacoes, image=img_btn).grid(row=6, column=0, columnspan=5, padx=2, pady=2)
botao_4 = ctk.CTkButton(janela, text='texto', command=tudo_minuscula).grid(row=7, column=3, padx=2, pady=5)
botao_5 = ctk.CTkButton(janela, text='Tex To', command=toda_primeira_letra).grid(row=7, column=4, padx=2, pady=5)

botao_limpar = ctk.CTkButton(janela, text='Limpar', font=('Arial', 15), fg_color='Green', width=30, command=btn_limpar).grid(row=6, column=4, sticky="e", padx=2, pady=0)

# # AREA PARA RESPOSTA DO PROGAMA
txt_audio_resposta =  ctk.CTkLabel(janela, text=f" ", text_color='Blue')
txt_audio_resposta.grid(row=3, column=0, columnspan=5, padx=2, pady=2)
texto_resposta =  ctk.CTkLabel(janela, text=f" ", text_color="blue", cursor="hand2")
texto_resposta.grid(row=8,  column=0, columnspan=5, padx=0, pady=2)
texto_resposta.bind("<Button-1>", lambda e: txt_respota(os.startfile(caminho)))

janela.mainloop()
