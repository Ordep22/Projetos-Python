from tkinter import *
from typing import List, Any
import serial.tools.list_ports
import serial
from tkinter import ttk, messagebox
from tkinter import filedialog
import CRC16_MODBUS
from time import sleep

import MONTA_PROTOCOLO

root = Tk()


class Application:
    # --------------------------------------------------------------------------------------------------------------#
    ###                                     Variáveis de inicialização                                           ###
    # --------------------------------------------------------------------------------------------------------------#

    ##Velocidades de conexão
    # Esses valores numca podem ser alterados
    velocidades = ("300", "600", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200")

    ##Paryti
    # Valores de do bit de paridade
    parity = ("Nenhuma", "Par", "Impar")

    ##Stop bits
    # Valores dos bits de parada
    Stop_bit = ("1", "2")

    data_bytes = (serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS)

    time_out = 0

    def __init__(self):
        self.file = None
        self.tamanho = None
        self.protocolo = None
        self.buffer_hex = []
        self.Path_arquivo = None
        self.combobox_PARADA = None
        self.BTN_conectar = None
        self.combobox_PARIDADE = None
        self.combobox_DBITS = None
        self.conexao = None
        self.stopbits = None
        self.databits = None
        self.porta = ""
        self.velocidade = None
        self.BTN_recarregar = None
        self.icon = None
        self.combobox_VEL = None
        self.combobox_COM = None
        self.frame = None
        self.root = root
        self.tela()
        self.quadro()
        self.funcionalidades()
        root.mainloop()

    def tela(self):
        self.root.title("Bootloader Módulo de Potência Ande 2023")
        self.root.geometry("700x600+350+150")
        self.root.resizable(False, False)

    def quadro(self):
        self.frame = Frame(self.root, bd=4, bg="#FFFFFF")
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)

    def funcionalidades(self):

        ##Menu de seleção portas COM
        # Texto menu de seleção portas COM
        combobox_label = Label(self.frame, text="COM:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
        combobox_label.place(relx=0.00, rely=0.03, relwidth=0.1, relheight=0.09)
        # Caixa de seleção
        self.combobox_COM = ttk.Combobox(self.frame, values=self.porta_serial(), state="readonly")
        self.combobox_COM.place(relx=0.0, rely=0.23, relwidth=0.15, relheight=0.2)

        # Menu de seleção de velocidade conexão
        # Texto seleção de velocidade de concção
        label = Label(self.frame, text="Valocidade:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
        label.place(relx=0.16, rely=0.03, relwidth=0.1, relheight=0.09)
        # Caixa de seleção
        self.combobox_VEL = ttk.Combobox(self.frame, state="readonly", values=Application.velocidades)
        self.combobox_VEL.place(relx=0.16, rely=0.23, relwidth=0.15, relheight=0.2)

        ##Data bits
        # Texto seleção data bits
        self.label = Label(self.frame, text="Data bits:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
        self.label.place(relx=0.32, rely=0.03, relwidth=0.1, relheight=0.09)
        # Menu data bits
        self.combobox_DBITS = ttk.Combobox(self.frame, state="readonly", values=Application.data_bytes)
        self.combobox_DBITS.place(relx=0.32, rely=0.23, relwidth=0.15, relheight=0.2)

        ##Menu de seleção de bit de paridade
        # Texto seleção de bit de paridade
        self.label = Label(self.frame, text="Parity:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
        self.label.place(relx=0.48, rely=0.03, relwidth=0.1, relheight=0.16)
        # Menu bit de paridade
        self.combobox_PARIDADE = ttk.Combobox(self.frame, state="readonly", values=Application.parity)
        self.combobox_PARIDADE.place(relx=0.48, rely=0.23, relwidth=0.15, relheight=0.2)

        ##Stop Bits
        # Texto seleção de bit de parada
        self.label = Label(self.frame, text="Stop bit:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
        self.label.place(relx=0.64, rely=0.03, relwidth=0.1, relheight=0.16)
        # Menu bit de parada
        self.combobox_PARADA = ttk.Combobox(self.frame, state="readonly", values=Application.Stop_bit)
        self.combobox_PARADA.place(relx=0.64, rely=0.23, relwidth=0.15, relheight=0.2)

        # Botão conectar
        self.BTN_conectar_status = "Conectar"
        self.BTN_conectar = Button(self.frame, text="Conectar", font=("Arial", 10), command=self.conectar)
        self.BTN_conectar.place(relx=0.80, rely=0.23, relwidth=0.15, relheight=0.2)

        # Botão recarregar
        self.icon = PhotoImage(file=r"RB.png")
        self.BTN_recarregar = Button(self.frame, image=self.icon, command=self.atuallizar)
        self.BTN_recarregar.place(relx=0.96, rely=0.23, relwidth=0.04, relheight=0.2)

        # Botão lêr arquivos
        BTN_Carregar = Button(self.frame, text='Ler arquivo', font=("Arial", 10), command=self.carrega_arquivo)
        BTN_Carregar.place(relx=0.48, rely=0.55, relwidth=0.15, relheight=0.2)

        # Botão enviar
        BTN_Enviar = Button(self.frame, text='Enviar', font=("Arial", 10), command=self.enviar)
        BTN_Enviar.place(relx=0.64, rely=0.55, relwidth=0.15, relheight=0.2)

        # Laybel Path arquivo .HEX
        self.Laybel_Path = Entry(self.frame, width=50, bg="#FFFFFF")
        self.Laybel_Path.place(relx=0.0, rely=0.55, relwidth=0.47, relheight=0.2)

        # Caixa de texto Arquivo .HEX
        self.CAIXA_Texto = Text(self.root, width=90, height=10, bg="#FFFFFF")
        self.CAIXA_Texto.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.70)

    ###Talvez fosse interessante jogar para outro arquivo
    def porta_serial(self):

        self.a = serial.tools.list_ports.comports()
        return self.a

    def obter_COM(self):
        # Conecta com portas seriais até COM99
        porta = self.combobox_COM.get()
        #
        # COM = porta[0:7].rstrip(" -")
        #
        # return COM

        COM = porta.strip(" ")

        # print(COM[0:6])

        return COM[0:4]

    def obter_VEL(self):

        VEL = self.combobox_VEL.get()
        # print(VEL)
        return VEL

    def obter_DBITS(self):

        DBits = self.combobox_DBITS.get()
        return DBits

    def obter_PARITY(self):

        PARITY = self.combobox_PARIDADE.get()
        return PARITY

    def obter_STOPBIT(self):

        STOPBIT = self.combobox_PARADA.get()
        return STOPBIT

    def conectar(self):

        self.velocidade = self.obter_VEL()
        self.porta = self.obter_COM()
        self.databits = self.obter_DBITS()
        self.parity = self.obter_PARITY()
        self.stopbits = self.obter_STOPBIT()

        while True:  # Loop para a conexão serial
            try:  # Tenta se conectar, se conseguir, o loop se encerra

                if self.BTN_conectar['text'] == "Conectar":
                    #
                    # self.conexao = serial.Serial(self.porta, self.velocidade)
                    self.conexao = serial.Serial('COM12', self.velocidade)

                    if self.conexao.is_open == TRUE:
                        self.BTN_conectar['text'] = "Desconectar"
                    break

                if self.BTN_conectar['text'] == "Desconectar" and self.conexao.is_open == TRUE:
                    self.BTN_conectar['text'] = "Conectar"
                    self.conexao.close()
                    break

            except:

                messagebox.showerror("Erro", "Erro de conexão")
                break

    '''
    def ligar(self):

        ligar = self.conexao.write('L'.encode())
        print(ligar)  # Mostra a informação de que foi enviada ao micro
        self.conexao.flush()

    def desligar(self):

        desligar = self.conexao.write('D'.encode())
        print(desligar)  # Mostra a informação de que foi enviada ao micro
        self.conexao.flush()    
    '''

    def carrega_arquivo(self):
        # Carregar o arquivo para o buffer
        self.Laybel_Path.delete("0", "end")
        self.CAIXA_Texto.delete(1.0, "end")
        self.Path_arquivo = filedialog.askopenfilename()
        self.Laybel_Path.insert(0, self.Path_arquivo)
        self.processar()

    def processar(self):
        # Passa o arquivo para uma string buffer

        index = 0
        j = 0
        self.protocolo = []
        self.cabecalho = 'LUPA'
        self.comando = '0'
        self.tamanho = ''

        crc16 = CRC16_MODBUS.crc16()
        protocolo = MONTA_PROTOCOLO.monta_protocolo()

        self.buffer_crc = []
        try:
            self.buffer = []
            if self.Path_arquivo != "":
                self.file = open(self.Path_arquivo, 'r')

                for i in self.file:
                    self.buffer.append(i.strip())
                    # print(self.buffer[index])

                    # Monta o protocolo com as informações drecebidas do buffer
                    item_e_protocolo = protocolo.Protocolo(self.buffer[index])

                    # Recebe uma lista com o elemento em hexadecimal e seu respsctivo CRC
                    item_e_CRC = crc16.Converte_ASCII_HEX(item_e_protocolo)

                    index += 1

            self.file.flush()


        except:

            pass

    def enviar(self):

        # Sempre que entrar neste evento a caixa de texto será limpa
        self.CAIXA_Texto.delete(1.0, "end")
        try:
            for i in range(0, len(self.protocolo), 1):
                self.conexao.write(self.protocolo[i].encode())
                self.CAIXA_Texto.insert(END, self.protocolo[i])
                self.CAIXA_Texto.insert(END, '\n\n')
                print(self.protocolo[i])
                # if i % maxBytesEnvio == 0:
                #     self.conexao.flush()

            self.conexao.flush()

        except:

            messagebox.showwarning("Alerta", "Por favor conecte ao dispositivo!")
            pass

    def atuallizar(self):

        # Atualiza todos os boxes de seleção
        self.combobox_COM.set('')
        self.combobox_VEL.set('')
        self.combobox_PARIDADE.set('')
        self.combobox_DBITS.set('')
        self.combobox_PARADA.set('')
        self.Laybel_Path.delete("0", "end")
        self.CAIXA_Texto.delete(1.0, "end")

        try:

            if self.conexao.is_open == TRUE:
                self.BTN_conectar['text'] = "Conectar"
                self.conexao.close()
        except:
            pass

        self.combobox_COM["values"] = self.porta_serial()


Application()
