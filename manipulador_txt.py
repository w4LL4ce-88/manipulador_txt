import customtkinter as ctk
from tkinter import messagebox, filedialog, PhotoImage
import datetime
from gtts import gTTS
from PIL import Image
import os

# MODO DE EXIBIÇÃO
ctk.set_appearance_mode('dark')

#######################################################################
# BUSCANDO DATA E HORA ATUAL PARA USAR NO NOME DO AQUIVO DE AUDIO
data_atual = datetime.datetime.today().strftime("%H-%M-%S__%d-%m-%y") 
# PASTA DE DESTINO
caminho = os.path.join(os.path.dirname(__file__), 'Manipulador_TXT')
icones = os.path.join(os.path.dirname(__file__), caminho, 'icones/')
audios = os.path.join(os.path.dirname(__file__), caminho, 'audios/')
os.makedirs(caminho, exist_ok=True)
os.makedirs(icones, exist_ok=True)
os.makedirs(audios, exist_ok=True)

# IMPORTANDO ICONES DO PROGRAMA
img_ico = os.path.join(icones, 'manipulador_txt_icone.ico')
img_btn = ctk.CTkImage(Image.open(os.path.join(icones, 'icone de som.png')))
img_btn_e = ctk.CTkImage(Image.open(os.path.join(icones, 'cadeado.ico')))
img_btn_d = ctk.CTkImage(Image.open(os.path.join(icones, 'cheve.ico')))

#######################################################################
def multiplicar():
    palavra = caixa.get()
    numero = caixa_n.get()
    area_texto2.delete("1.0", ctk.END)
    if not palavra.strip() or not numero.strip():
        messagebox.showwarning("Aviso", "Insira uma PALAVRA e um NÚMERO")
    numero = int(numero)    
    for i in range(numero):
        i = palavra
        if opt.get():
            resultado = numero * f'{i} '
        else:
            resultado = numero * f'{i}\n'
    area_texto2.insert("1.0", resultado)
        # janela.after(3000, limpar)

#######################################################################
# FUNÇÃO ENUMERAR
def enumerar():
    palavra = caixa.get()
    palavra = palavra.title()
    vezes = caixa_n.get()
    if not caixa_n.get():
        messagebox.showwarning("Aviso", "Insira um número válido")
    vezes = int(vezes)
    area_texto2.delete("1.0", ctk.END)
    inicio = 0
    for i in range(vezes):
        inicio += 1
        if palavra.strip() and not opt.get():
            area_texto2.insert("end", f'{inicio}. {palavra} - \n')    
        if palavra.strip() and opt.get():
            area_texto2.insert("end", f'{palavra} - {inicio} - \n')      
        if opt.get() and not palavra.strip():
            area_texto2.insert("1.0", f'{inicio} - \n')                                  
        elif not palavra.split():
            area_texto2.insert("end", f'{inicio} - \n')          

#######################################################################
# FUNCÃO ENCRIPITAR
def encriptar():
    msg = area_texto1.get("1.0", "end-1c")
    cifra = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "defghijklmnopqrstuvxwyzabcDEFGHIJKLMNOPQRSTUVXWYZABC") # <- Alteração da Base
    msg_ecrp = msg.translate(cifra)
    area_texto2.delete("1.0", ctk.END)
    area_texto2.insert("1.0", f'((Encript))\n\n{msg_ecrp}')
    limpar_a1()

def decriptar():
    msg = area_texto1.get("1.0", "end-1c")
    cifra = str.maketrans("defghijklmnopqrstuvxwyzabcDEFGHIJKLMNOPQRSTUVXWYZABC", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") # <- Alteração da Base
    msg_decrp = msg.translate(cifra)
    area_texto2.delete("1.0", ctk.END)
    area_texto2.insert("1.0", f'((Decript))\n\n{msg_decrp}')
    limpar_a1()

#######################################################################
# FUNÇÃO ORDEM ALFABÉTICA
def ordem_c():
    msg = area_texto1.get("1.0", "end-1c")
    area_texto2.delete("1.0", "end-1c")
    palavras = msg.split()
    palavras.sort(reverse=True)
    for i in palavras:
        if opt.get():
            area_texto2.insert("1.0", f'{i} ')
        else:
            area_texto2.insert("1.0", f'{i}\n')

def ordem_dc():
    msg = area_texto1.get("1.0", "end-1c")
    area_texto2.delete("1.0", "end-1c")
    palavras = msg.split()
    palavras.sort(reverse=False)
    for i in palavras:
        if opt.get():
            area_texto2.insert("1.0", f'{i} ')         
        else:
            area_texto2.insert("1.0", f'{i}\n')

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
def txt_para_audio():
    texto = area_texto1.get("1.0", "end-1c")
    lingua = "pt"
    tts = gTTS(texto, lang=lingua)
    tts.save(f"{audios}gerador-{data_atual}.mp3") # COMANDO PARA SALVAR
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
    caixa.delete(0, ctk.END)
    caixa_n.delete(0, ctk.END)
        
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
janela.title('Manipulador de Textos')
janela.iconbitmap(img_ico)
#janela.geometry('600x510')
janela.resizable(width=False, height=False)

# TITULO DENTRO DA JANELA
label_da_janela = ctk.CTkLabel(janela, text='____________MANIPULADOR DE TEXTOS____________', 
                font=('Impact', 25)).grid(row=0, column=0, columnspan=5, pady=2, padx=5)

# TEXTOS DA JANELA
caixa = ctk.CTkLabel(janela, text='Digite seu texto',
         text_color='#0099cc', font=('Verdana', 15, 'bold')).grid(row=2, column=0, pady=0, padx=0)

caixa2 = ctk.CTkLabel(janela, text='Transcrição',
         text_color='#0099cc', font=('Verdana', 15, 'bold')).grid(row=4, column=0, sticky="w", pady=0, padx=10)
 

# AREA DE TEXTOS
area_texto1 = ctk.CTkTextbox(janela, text_color='White', fg_color='Black', height=150, width=550)
area_texto1.grid(row=3, column=0, columnspan=5, pady=5, padx=5)

area_texto2 = ctk.CTkTextbox(janela, text_color='White', fg_color='Black', height=150, width=550)
area_texto2.grid(row=5, column=0, columnspan=5, pady=5, padx=5)

# BOTOES DE COMANDO
botao_0 = ctk.CTkButton(janela, text='Selecione um arquivo', command=selecionar_arquivo).grid(row=2, column=4, padx=5, pady=2)

botao_1 = ctk.CTkButton(janela, text='TEXTO', command=tudo_maiuscula).grid(row=8, column=0, padx=2, pady=5)
botao_2 = ctk.CTkButton(janela, text='Texto', command=primeira_letra).grid(row=8, column=1, padx=3, pady=5)
botao_3 = ctk.CTkButton(janela, text='Texto >> Audio', command=txt_para_audio, image=img_btn).grid(row=6, column=0, columnspan=5, padx=2, pady=2)
botao_4 = ctk.CTkButton(janela, text='Tex To', command=toda_primeira_letra).grid(row=8, column=3, padx=3, pady=5)
botao_5 = ctk.CTkButton(janela, text='texto', command=tudo_minuscula).grid(row=8, column=4, padx=2, pady=5)

btn_enum = ctk.CTkButton(janela, text='Enumerar', command=enumerar).grid(row=7, column=0, padx=2, pady=5)
btn_mult = ctk.CTkButton(janela, text='Multiplicar', command=multiplicar).grid(row=7, column=4, padx=2, pady=5)

#######################################################################
# CRIANDO FRAMES E INSERINDO BOTÕES
# FRAME 1
frame = ctk.CTkFrame(master=janela, width=580, height=50, border_color='teal', border_width=1, fg_color='#999999')
frame.grid(row=1, column=0, columnspan=5, padx=1, pady=2)

text_frame = ctk.CTkLabel(frame, text=" Multifuncional ", font=('Verdana', 14, 'bold'), text_color='Black')
text_frame.pack(side='left', padx=5, pady=1)

caixa = ctk.CTkEntry(frame, placeholder_text="Texto... ", width=160, border_color='teal')
caixa.pack(side='left', padx=5, pady=5)

texto = ctk.CTkLabel(frame, text=" - ", font=('Verdana', 14, 'bold'), text_color='Black')
texto.pack(side='left', padx=5, pady=5)

caixa_n = ctk.CTkEntry(frame, placeholder_text="Números...", width=160, border_color='teal')
caixa_n.pack(side='left', padx=5, pady=5)

opt = ctk.CTkCheckBox(frame, text='Formatar  ', font=('Verdana', 13, 'bold'), text_color='Black', border_color='teal', border_width=3, hover_color='Black', onvalue=True, offvalue=False)
opt.pack(side='left', padx=5, pady=5)

#######################################################################
# FRAME 2
frame_2 = ctk.CTkFrame(master=janela, width=300, height=25, border_color='teal', border_width=1, fg_color='#999999')
frame_2.grid(row=7, column=0, columnspan=5, padx=1, pady=2)

botao_e = ctk.CTkButton(frame_2, text='', width=57, height=20, fg_color='red', hover_color='dark red', command=encriptar, image=img_btn_e)
botao_e.pack(side='left', padx=1, pady=2)
botao_az = ctk.CTkButton(frame_2, text='a-Z', width=57, height=26, text_color='Black', fg_color='white', hover_color='#0099cc', border_color='Black', border_width=2, corner_radius=1, command=ordem_c,)
botao_az.pack(side='left', padx=1, pady=2)

botao_limpar = ctk.CTkButton(frame_2, text='END', width=60, height=2, text_color='Black', fg_color='white', hover_color='#38761d', border_color='dark green', border_width=5, corner_radius=1, command=btn_limpar)
botao_limpar.pack(side='left', padx=1, pady=2) # image=img_btn_l

botao_za = ctk.CTkButton(frame_2, text='Z-a', width=57, height=26, text_color='Black', fg_color='White', hover_color='#0099cc', border_color='Black', border_width=2, corner_radius=1, command=ordem_dc)
botao_za.pack(side='left', padx=1, pady=2)
botao_d = ctk.CTkButton(frame_2, text='', width=57, height=20, fg_color='green', hover_color='dark green', command=decriptar, image=img_btn_d)
botao_d.pack(side='left', padx=1, pady=2)

#######################################################################
# AREA PARA RESPOSTA DO PROGAMA
txt_audio_resposta =  ctk.CTkLabel(janela, text=f" ", text_color='White')
txt_audio_resposta.grid(row=4, column=0, columnspan=5, padx=2, pady=2)
texto_resposta =  ctk.CTkLabel(janela, text=f" ", text_color='White', cursor="hand2")
texto_resposta.grid(row=9,  column=0, columnspan=5, padx=0, pady=2)
texto_resposta.bind("<Button-1>", lambda e: txt_respota(os.startfile(audios)))

janela.mainloop()