# Author: Lucas Gabriel

import sys

# try-except para evitar erros de importacao dos modulos
try:
    import Tkinter as tk

except ImportError:
    import tkinter as tk

try:
    import tkinter.ttk as ttk

except ImportError:
    sys.exit('Erro: Erro ao importar o modulo "tkinter", verifique o mesmo e tente novamente.')

try:
    from generate_new_RSA_keys import generate_new_keys

except ImportError:
    sys.exit('Erro: Erro ao importar o arquivo "gerar_novas_chaves.py", verifique o arquivo e tente novamente.')
          
try:
    import criptography_RSA

except ImportError:
    sys.exit('Erro: Erro ao importar o arquivo "criptografia.py", verifique o arquivo e tente novamente.')

# arquivos de chave padrao
chavePublicaArquivo = 'chave_publica.pem'
chavePrivadaArquivo = 'chave_privada.pem'

# arquivos de criptografia padao
textoCriptografadoArquivo = 'texto_criptografado.encrypt'
textoDescriptografadoArquivo = 'texto_descriptografado.txt'

def vp_start_gui():
    # funcao para iniciar o codigo
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()
    

w = None
def create_Toplevel1(root, *args, **kwargs):
    # funcao para quando o modulo é importado
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        # Esta classe configura e preenche a toplevel window. top é a janela que contém toplevel.
        _bgcolor = '#d9d9d9'  # 'gray85'
        _fgcolor = '#000000'  # 'black'
        _compcolor = '#d9d9d9'  # 'gray85'
        _ana1color = '#d9d9d9'  # 'gray85'
        _ana2color = '#ececec'  # 'gray92'
        font9 = '-family {Segoe UI} -size 9 -weight bold -slant roman ' \
                '-underline 0 -overstrike 0'
        self.style = ttk.Style()

        if sys.platform == 'win32':
            self.style.theme_use('winnative')

        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font='TkDefaultFont')
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        # configuracoes da janela
        top.geometry('720x443+279+123')
        top.title('APS - Criptografia em RSA')
        top.configure(background='#444444')
        top.configure(highlightbackground='#d9d9d9')
        top.configure(highlightcolor='black')

        # configuracoes da jenala notebook (Criptografar / Chaves)
        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
        [('selected', _compcolor), ('active', _ana2color)])
        self.TNotebook = ttk.Notebook(top)
        self.TNotebook.place(relx=0.0, rely=0.0, relheight=1.007, relwidth=1.006)

        self.TNotebook.configure(takefocus='')
        self.TNotebook_t0 = tk.Frame(self.TNotebook)
        self.TNotebook.add(self.TNotebook_t0, padding=3)
        self.TNotebook.tab(0, text='Criptografia', compound='left', underline='-1',)
        self.TNotebook_t0.configure(background='#d9d9d9')
        self.TNotebook_t0.configure(highlightbackground='#d8d8d8')
        self.TNotebook_t0.configure(highlightcolor='black')
        self.TNotebook_t1 = tk.Frame(self.TNotebook)
        self.TNotebook.add(self.TNotebook_t1, padding=3)
        self.TNotebook.tab(1, text='Chaves', compound='left', underline='-1', )
        self.TNotebook_t1.configure(background='#d9d9d9')
        self.TNotebook_t1.configure(highlightbackground='#d9d9d9')
        self.TNotebook_t1.configure(highlightcolor='black')

        self.TFrameCriptografar = ttk.Frame(self.TNotebook_t0)
        self.TFrameCriptografar.place(relx=0.014, rely=0.036, relheight=0.419
                                      , relwidth=0.94)
        self.TFrameCriptografar.configure(relief='groove')
        self.TFrameCriptografar.configure(borderwidth='2')
        self.TFrameCriptografar.configure(relief='groove')

        def btcriptografia_click():  # funcao para criptografar o texto

            # pega a mensagem da entrada de texto da criptografia
            mensagem = str(self.ScrolledentryCriptografia.get())

            # pega o nome do arquivo onde sera salvo o texto criptografado
            textoCriptografadoArquivo = str(self.EntryNomeArquivoCriptografia.get())

            # limpa o campo de resultado
            self.TextResultado.delete('1.0', tk.END)

            # envia a mensagem para a funcao de criptografar, retorna a mensagem criptografada
            criptografado = criptography_RSA.encrypt_text(mensagem, chavePublicaArquivo, textoCriptografadoArquivo)

            # verifica se deu erro durante o processo de criptografia e retorna o erro se tiver, se nao retorna a mensagem padrao de confirmacao da criptografia
            if 'Erro:' in criptografado:
                saida = criptografado
            
            else:
                saida = f'Texto criptografado com sucesso. Salvo no arquivo "{textoCriptografadoArquivo}".\nTexto criptografado = {str(criptografado)}'

            # abilita a entrada de resultados, imprime o valor de saida e desabilita a caixa de resultado
            self.TextResultado.configure(state='normal')
            self.TextResultado.delete('1.0', tk.END)
            self.TextResultado.insert('1.0', saida)
            self.TextResultado.configure(state='disabled')

        def btdecriptografia_click():  # funcao para descriptografar o texto

            # limpa a saida da descriptografia
            self.ScrolledtextDescriptografia.delete('1.0', tk.END)

            # pega o nome do arquivo criptografado
            arquivo = str(self.EntryNomeArquivoCriptografia.get())

            # pega o nome do arquivo onde sera salvo o texto descriptografado
            textoDescriptografadoArquivo = str(self.EntryNomeArquivoDescriptografia.get())

            # envia o nome do arquivo para a funcao de descriptografar, retorna a mensagem descriptografada
            descriptografado = criptography_RSA.decrypt_text(arquivo, chavePrivadaArquivo, textoDescriptografadoArquivo)

            # verifica se deu erro durante o processo de descriptografia e retorna o erro se tiver, se nao retorna a mensagem padrao de confirmacao da descriptografia
            if 'Erro:' in descriptografado:
                saida = descriptografado
            
            else:
                saida = f'Texto descriptografado apartir do arquivo "{arquivo}"\nTexto descriptografado salvo no arquivo "{textoDescriptografadoArquivo}".\nTexto descriptografado = {descriptografado}'            

            # imprime o texto descriptografado
            self.ScrolledtextDescriptografia.insert('1.0', saida)

        # configuracoes do botao de criptografar
        self.ButtonCriptografar = tk.Button(self.TFrameCriptografar)
        self.ButtonCriptografar.place(relx=0.015, rely=0.057, height=44, width=137)
        self.ButtonCriptografar.configure(activebackground='#ececec')
        self.ButtonCriptografar.configure(activeforeground='#000000')
        self.ButtonCriptografar.configure(background='#00b783')
        self.ButtonCriptografar.configure(disabledforeground='#a3a3a3')
        self.ButtonCriptografar.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.ButtonCriptografar.configure(foreground='#000000')
        self.ButtonCriptografar.configure(highlightbackground='#d9d9d9')
        self.ButtonCriptografar.configure(highlightcolor='black')
        self.ButtonCriptografar.configure(pady='0')
        self.ButtonCriptografar.configure(text='Criptografar')
        self.ButtonCriptografar.configure(command=btcriptografia_click)

        # configuracoes da entrada de texto da criptografia
        self.ScrolledentryCriptografia = ScrolledEntry(self.TFrameCriptografar)
        self.ScrolledentryCriptografia.place(relx=0.237, rely=0.286, height=56, relwidth=0.747)
        self.ScrolledentryCriptografia.configure(background='white')
        self.ScrolledentryCriptografia.configure(disabledforeground='#a3a3a3')
        self.ScrolledentryCriptografia.configure(foreground='black')
        self.ScrolledentryCriptografia.configure(highlightbackground='#d9d9d9')
        self.ScrolledentryCriptografia.configure(highlightcolor='black')
        self.ScrolledentryCriptografia.configure(insertbackground='black')
        self.ScrolledentryCriptografia.configure(insertborderwidth='1')
        self.ScrolledentryCriptografia.configure(selectbackground='#c4c4c4')
        self.ScrolledentryCriptografia.configure(selectforeground='black')

        # configuracoes da entrada do nome do arquivo criptografado
        self.LabelNomeArquivoCriptografia = tk.Label(self.TFrameCriptografar)
        self.LabelNomeArquivoCriptografia.place(relx=0.244, rely=0.057, height=21, width=185)
        self.LabelNomeArquivoCriptografia.configure(activebackground='#f9f9f9')
        self.LabelNomeArquivoCriptografia.configure(activeforeground='black')
        self.LabelNomeArquivoCriptografia.configure(background='#d9d9d9')
        self.LabelNomeArquivoCriptografia.configure(disabledforeground='#a3a3a3')
        self.LabelNomeArquivoCriptografia.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.LabelNomeArquivoCriptografia.configure(foreground='#000000')
        self.LabelNomeArquivoCriptografia.configure(highlightbackground='#d9d9d9')
        self.LabelNomeArquivoCriptografia.configure(highlightcolor='black')
        self.LabelNomeArquivoCriptografia.configure(text='Nome do arquivo criptografado:')

        self.EntryNomeArquivoCriptografia = tk.Entry(self.TFrameCriptografar)
        self.EntryNomeArquivoCriptografia.place(relx=0.525, rely=0.057, height=20, relwidth=0.457)
        self.EntryNomeArquivoCriptografia.configure(background='white')
        self.EntryNomeArquivoCriptografia.configure(disabledforeground='#a3a3a3')
        self.EntryNomeArquivoCriptografia.configure(font='TkFixedFont')
        self.EntryNomeArquivoCriptografia.configure(foreground='#000000')
        self.EntryNomeArquivoCriptografia.configure(highlightbackground='#d9d9d9')
        self.EntryNomeArquivoCriptografia.configure(highlightcolor='black')
        self.EntryNomeArquivoCriptografia.configure(insertbackground='black')
        self.EntryNomeArquivoCriptografia.configure(selectbackground='#c4c4c4')
        self.EntryNomeArquivoCriptografia.configure(selectforeground='black')
        self.EntryNomeArquivoCriptografia.insert(tk.INSERT, textoCriptografadoArquivo)

        # configuracoes da texto de resultado
        self.LabelResultado = tk.Label(self.TFrameCriptografar)
        self.LabelResultado.place(relx=0.0, rely=0.629, height=61, width=134)
        self.LabelResultado.configure(background='#d9d9d9')
        self.LabelResultado.configure(disabledforeground='#a3a3a3')
        self.LabelResultado.configure(font=font9)
        self.LabelResultado.configure(foreground='#000000')
        self.LabelResultado.configure(text='Resultado:')

        self.TextResultado = tk.Text(self.TFrameCriptografar)
        self.TextResultado.place(relx=0.237, rely=0.686, relheight=0.251, relwidth=0.747)
        self.TextResultado.configure(background='white')
        self.TextResultado.configure(font='TkTextFont')
        self.TextResultado.configure(foreground='black')
        self.TextResultado.configure(highlightbackground='#d9d9d9')
        self.TextResultado.configure(highlightcolor='black')
        self.TextResultado.configure(insertbackground='black')
        self.TextResultado.configure(selectbackground='#c4c4c4')
        self.TextResultado.configure(selectforeground='black')
        self.TextResultado.configure(wrap='word')
        self.TextResultado.configure(state='disabled')

        # frame de descriptografar
        self.TFrameDescriptografar = ttk.Frame(self.TNotebook_t0)
        self.TFrameDescriptografar.place(relx=0.014, rely=0.478, relheight=0.443, relwidth=0.94)
        self.TFrameDescriptografar.configure(relief='groove')
        self.TFrameDescriptografar.configure(borderwidth='2')
        self.TFrameDescriptografar.configure(relief='groove')

        # configuracoes do botao de descriptografar
        self.ButtonDescriptografar = tk.Button(self.TFrameDescriptografar)
        self.ButtonDescriptografar.place(relx=0.015, rely=0.054, height=44, width=137)
        self.ButtonDescriptografar.configure(activebackground='#ececec')
        self.ButtonDescriptografar.configure(activeforeground='#000000')
        self.ButtonDescriptografar.configure(background='#00b783')
        self.ButtonDescriptografar.configure(disabledforeground='#a3a3a3')
        self.ButtonDescriptografar.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.ButtonDescriptografar.configure(foreground='#000000')
        self.ButtonDescriptografar.configure(highlightbackground='#d9d9d9')
        self.ButtonDescriptografar.configure(highlightcolor='black')
        self.ButtonDescriptografar.configure(pady='0')
        self.ButtonDescriptografar.configure(text='Descriptografar')
        self.ButtonDescriptografar.configure(command=btdecriptografia_click)

        # configuracoes da entrada do nome do arquivo descriptografado
        self.TLabelNomeArquivoDesciptografia = ttk.Label(self.TFrameDescriptografar)
        self.TLabelNomeArquivoDesciptografia.place(relx=0.244, rely=0.027, height=29, width=176)
        self.TLabelNomeArquivoDesciptografia.configure(background='#d9d9d9')
        self.TLabelNomeArquivoDesciptografia.configure(foreground='#000000')
        self.TLabelNomeArquivoDesciptografia.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.TLabelNomeArquivoDesciptografia.configure(relief='flat')
        self.TLabelNomeArquivoDesciptografia.configure(text='Nome do arquivo normal:')

        self.EntryNomeArquivoDescriptografia = tk.Entry(self.TFrameDescriptografar)
        self.EntryNomeArquivoDescriptografia.place(relx=0.467, rely=0.054, height=20, relwidth=0.51)
        self.EntryNomeArquivoDescriptografia.configure(background='white')
        self.EntryNomeArquivoDescriptografia.configure(disabledforeground='#a3a3a3')
        self.EntryNomeArquivoDescriptografia.configure(font='TkFixedFont')
        self.EntryNomeArquivoDescriptografia.configure(foreground='#000000')
        self.EntryNomeArquivoDescriptografia.configure(highlightbackground='#d9d9d9')
        self.EntryNomeArquivoDescriptografia.configure(highlightcolor='black')
        self.EntryNomeArquivoDescriptografia.configure(insertbackground='black')
        self.EntryNomeArquivoDescriptografia.configure(selectbackground='#c4c4c4')
        self.EntryNomeArquivoDescriptografia.configure(selectforeground='black')
        self.EntryNomeArquivoDescriptografia.insert(tk.INSERT, textoDescriptografadoArquivo)

        # configuracoes da saida da descriptografia
        self.ScrolledtextDescriptografia = ScrolledText(self.TFrameDescriptografar)
        self.ScrolledtextDescriptografia.place(relx=0.237, rely=0.324, relheight=0.6, relwidth=0.742)
        self.ScrolledtextDescriptografia.configure(background='white')
        self.ScrolledtextDescriptografia.configure(font='TkTextFont')
        self.ScrolledtextDescriptografia.configure(foreground='black')
        self.ScrolledtextDescriptografia.configure(highlightbackground='#d9d9d9')
        self.ScrolledtextDescriptografia.configure(highlightcolor='black')
        self.ScrolledtextDescriptografia.configure(insertbackground='black')
        self.ScrolledtextDescriptografia.configure(insertborderwidth='3')
        self.ScrolledtextDescriptografia.configure(selectbackground='#c4c4c4')
        self.ScrolledtextDescriptografia.configure(selectforeground='black')
        self.ScrolledtextDescriptografia.configure(wrap='none')

        # frame informativo das chaves
        self.FrameChaves = tk.Frame(self.TNotebook_t1)
        self.FrameChaves.place(relx=0.014, rely=0.024, relheight=0.801, relwidth=0.968)
        self.FrameChaves.configure(relief='groove')
        self.FrameChaves.configure(borderwidth='2')
        self.FrameChaves.configure(relief='groove')
        self.FrameChaves.configure(background='#d9d9d9')
        self.FrameChaves.configure(highlightbackground='#d9d9d9')
        self.FrameChaves.configure(highlightcolor='black')

        # tenta ler o arquivo da chave publica, se nao achar cria um arquivo com uma nova chave publica
        try:
            with open(chavePublicaArquivo, 'rb') as arquivo:
                chavePublica = arquivo.read().split()

            # formata o texto de saida da chave publica para melhor visualizacao
            chavePublica = f'Chave E = {int(chavePublica[0])}\n\nChave N = {int(chavePublica[1])}'
        
        except IOError:
            chavePublica = 'Arquivo contendo as chaves publicas não encontrado.'
            
        # configuracoes da saida da chave publica
        self.ScrolledtextChavePublica = ScrolledText(self.FrameChaves)
        self.ScrolledtextChavePublica.place(relx=0.022, rely=0.119, relheight=0.839, relwidth=0.447)
        self.ScrolledtextChavePublica.configure(background='white')
        self.ScrolledtextChavePublica.configure(font='TkTextFont')
        self.ScrolledtextChavePublica.configure(foreground='black')
        self.ScrolledtextChavePublica.configure(highlightbackground='#d9d9d9')
        self.ScrolledtextChavePublica.configure(highlightcolor='black')
        self.ScrolledtextChavePublica.configure(insertbackground='black')
        self.ScrolledtextChavePublica.configure(insertborderwidth='3')
        self.ScrolledtextChavePublica.configure(selectbackground='#c4c4c4')
        self.ScrolledtextChavePublica.configure(selectforeground='black')
        self.ScrolledtextChavePublica.configure(wrap='none')
        self.ScrolledtextChavePublica.insert(tk.INSERT, chavePublica)
        self.ScrolledtextChavePublica.configure(state='disabled')

        self.TLabelChavePublica = ttk.Label(self.FrameChaves)
        self.TLabelChavePublica.place(relx=0.022, rely=0.03, height=19, width=306)
        self.TLabelChavePublica.configure(background='#d9d9d9')
        self.TLabelChavePublica.configure(foreground='#000000')
        self.TLabelChavePublica.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.TLabelChavePublica.configure(relief='flat')
        self.TLabelChavePublica.configure(text='Chaves Publicas:')

        # tenta ler o arquivo da chave privada, se nao achar cria um arquivo com uma nova chave privada
        try:
            with open(chavePrivadaArquivo, 'rb') as arquivo:
                chavePrivada = arquivo.read().split()

            # formata o texto de saida da chave privada para melhor visualizacao
            chavePrivada = f'Chave D = {int(chavePrivada[0])}\n\nChave N = {int(chavePrivada[1])}'

        except IOError:
            chavePrivada = 'Arquivo contendo as chaves privadas não encontrado.'

        # configuracoes da saida da chave privada
        self.ScrolledtextChavePrivada = ScrolledText(self.FrameChaves)
        self.ScrolledtextChavePrivada.place(relx=0.496, rely=0.119, relheight=0.839, relwidth=0.476)
        self.ScrolledtextChavePrivada.configure(background='white')
        self.ScrolledtextChavePrivada.configure(font='TkTextFont')
        self.ScrolledtextChavePrivada.configure(foreground='black')
        self.ScrolledtextChavePrivada.configure(highlightbackground='#d9d9d9')
        self.ScrolledtextChavePrivada.configure(highlightcolor='black')
        self.ScrolledtextChavePrivada.configure(insertbackground='black')
        self.ScrolledtextChavePrivada.configure(insertborderwidth='3')
        self.ScrolledtextChavePrivada.configure(selectbackground='#c4c4c4')
        self.ScrolledtextChavePrivada.configure(selectforeground='black')
        self.ScrolledtextChavePrivada.configure(wrap='none')
        self.ScrolledtextChavePrivada.insert(tk.INSERT, chavePrivada)
        self.ScrolledtextChavePrivada.configure(state='disabled')

        self.TLabelChavePrivada = ttk.Label(self.FrameChaves)
        self.TLabelChavePrivada.place(relx=0.49511, rely=0.03, height=19, width=316)
        self.TLabelChavePrivada.configure(background='#d9d9d9')
        self.TLabelChavePrivada.configure(foreground='#000000')
        self.TLabelChavePrivada.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.TLabelChavePrivada.configure(relief='flat')
        self.TLabelChavePrivada.configure(text='Chaves Privadas:')

        def btgerar_novas_chaves_click():  # funcao para gerar novas chaves aleatorias

            generate_new_keys()  # chava a funcao que gera novos arquivos contendo as chaves

            # le o arquivo da chave publica
            with open(chavePublicaArquivo, 'rb') as chavepba:
                chavePublica = chavepba.read().split()

            # formata o texto de saida da chave publica para melhor visualizacao
            chavePublica = f'Chave E = {int(chavePublica[0])}\n\nChave N = {int(chavePublica[1])}'

            # abilita a entrada de dados da chave publica, imprime o valor da chave e desabilita a entrada de dados
            self.ScrolledtextChavePublica.configure(state='normal')
            self.ScrolledtextChavePublica.delete('1.0', tk.END)
            self.ScrolledtextChavePublica.insert(tk.INSERT, chavePublica)
            self.ScrolledtextChavePublica.configure(state='disabled')

            # le o arquivo da chave privada
            with open(chavePrivadaArquivo, 'rb') as chavepva:
                chavePrivada = chavepva.read().split()

            # formata o texto de saida da chave privada para melhor visualizacao
            chavePrivada = f'Chave D = {int(chavePrivada[0])}\n\nChave N = {int(chavePrivada[1])}'

            # abilita a entrada de dados da chave privada, imprime o valor da chave e desabilita a entrada de dados
            self.ScrolledtextChavePrivada.configure(state='normal')
            self.ScrolledtextChavePrivada.delete('1.0', tk.END)
            self.ScrolledtextChavePrivada.insert(tk.INSERT, chavePrivada)
            self.ScrolledtextChavePrivada.configure(state='disabled')

        # configuracoes do botao de geracao de novas chaves
        self.ButtonGerarNovasChaves = tk.Button(self.TNotebook_t1)
        self.ButtonGerarNovasChaves.place(relx=0.014, rely=0.861, height=34, width=127)
        self.ButtonGerarNovasChaves.configure(activebackground='#ececec')
        self.ButtonGerarNovasChaves.configure(activeforeground='#000000')
        self.ButtonGerarNovasChaves.configure(background='#DB4A39')  ##d9d9d9
        self.ButtonGerarNovasChaves.configure(disabledforeground='#a3a3a3')
        self.ButtonGerarNovasChaves.configure(font='-family {Segoe UI} -size 9 -weight bold')
        self.ButtonGerarNovasChaves.configure(foreground='#000000')
        self.ButtonGerarNovasChaves.configure(highlightbackground='#d9d9d9')
        self.ButtonGerarNovasChaves.configure(highlightcolor='black')
        self.ButtonGerarNovasChaves.configure(pady='0')
        self.ButtonGerarNovasChaves.configure(text='Gerar Novas Chaves')
        self.ButtonGerarNovasChaves.configure(command=btgerar_novas_chaves_click)


# O código a seguir é para facilitar os widgets com barra de rolagem 
class AutoScroll(object):
    # Configura as barras de rolagem para os widgets.

    def __init__(self, master):

        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass

        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass

        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')

        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass

        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # copiar os metodos da geometria do master (pega de ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        # ocultar e mostrar a barra de rolagem conforme necessário

        def wrapped(first, last):
            first, last = float(first), float(last)
            
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            
            else:
                sbar.grid()
            
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    # Cria um frame ttk com um determinado master e usa esse novo frame para
    # colocar as barras de rolagem e o widget

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    # Um 'standard Tkinter Textwidget padrão' com barras de rolagem que
    # mostrar/ocultar automaticamente conforme necessário

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledEntry(AutoScroll, tk.Entry):
    # Um 'standard Tkinter Textwidget padrão' com barras de rolagem horizontal que
    # mostrar/ocultar automaticamente conforme necessário

    @_create_container
    def __init__(self, master, **kw):
        tk.Entry.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    try:
        if platform.system() == 'Windows':
            widget.yview_scroll(-1 * int(event.delta / 120), 'units')
       
        elif platform.system() == 'Darwin':
            widget.yview_scroll(-1 * int(event.delta), 'units')
       
        else:
            if event.num == 4:
                widget.yview_scroll(-1, 'units')
       
            elif event.num == 5:
                widget.yview_scroll(1, 'units')
    
    except AttributeError:
        pass


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
    
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
