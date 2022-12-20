import binascii
from tkinter import *
import serial.tools.list_ports
import serial
from tkinter import ttk, messagebox
from tkinter import filedialog
import CRC16_MODBUS
import SERIAL
import MONTA_PROTOCOLO
import MONTA_PACOTE
import DECODIFICA_SERIAL
from time import sleep
import time

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
    parity = (serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE)

    ##Stop bits
    # Valores dos bits de parada
    Stop_bit = (serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO)

    data_bytes = (serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS)

    time_out = 0

    def __init__(self):
        self.string_protocolo = None
        self.buffer_crc = None
        self.infoCaixatexto = None
        self.info = None
        self.buffer = None
        self.buffer_pacote = None
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
        self.root.iconphoto(False, PhotoImage(
            file=r"Lupa.png"))
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
        label = Label(self.frame, text="Velocidade:", font=("Arial", 10), anchor=W, bg="#FFFFFF")
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

        # Botão Limpara caixa de texto
        BTN_Enviar = Button(self.frame, text='Lipar', font=("Arial", 10), command=self.limpar)
        BTN_Enviar.place(relx=0.80, rely=0.55, relwidth=0.15, relheight=0.2)

        # Laybel Path arquivo .HEX
        self.Laybel_Path = Entry(self.frame, width=50, bg="#FFFFFF")
        self.Laybel_Path.place(relx=0.0, rely=0.55, relwidth=0.47, relheight=0.2)

        # Caixa de texto Arquivo .HEX
        self.CAIXA_Texto = Text(self.root, width=90, height=10, bg="#FFFFFF")
        self.CAIXA_Texto.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.70)
        self.CAIXA_Texto.configure(state="disable")

    ###Talvez fosse interessante jogar para outro arquivo
    def porta_serial(self):

        self.a = serial.tools.list_ports.comports()
        return self.a

    def obter_COM(self):
        # Conecta com portas seriais até COM99
        porta = self.combobox_COM.get()

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

                if self.BTN_conectar['text'] == "Conectar" and self.conexao != "" and self.velocidade != "":

                    # self.conexao = serial.Serial(self.porta, self.velocidade)
                    # self.conexao = serial.Serial(self.porta, self.velocidade,self.databits,self.parity,self.stopbits)
                    self.conexao = serial.Serial("COM4", 115200)

                    if self.conexao.is_open == TRUE:
                        self.BTN_conectar['text'] = "Desconectar"
                        break

                elif self.BTN_conectar['text'] == "Desconectar" and self.conexao.is_open == TRUE:
                    self.BTN_conectar['text'] = "Conectar"
                    self.conexao.close()
                    break

                else:
                    break

            except:

                messagebox.showerror("Atenção", "Não foi possível conectar")
                break

    def carrega_arquivo(self):

        # Função responsável por carregar o arquivo

        ##Carregar o arquivo para o buffer

        # Limpa a caixa de texto de enderoço do arquivo
        self.Laybel_Path.delete("0", "end")

        # Limpas as informações contidas na caixa de texto
        self.CAIXA_Texto.delete(1.0, "end")

        # Obtem o endereço(path) do arqiovo
        self.Path_arquivo = filedialog.askopenfilename()

        # Insere o enderço do arquivo na caixa de endereço do arquivo
        self.Laybel_Path.insert(0, self.Path_arquivo)

        # Se o endereço do arquivo não for fazio irá verificar qual o formato do arquivo
        if self.Path_arquivo != "":

            if '.txt' in self.Path_arquivo:
                self.processar()

            elif '.TXT' in self.Path_arquivo:
                self.processar()

            elif '.hex' in self.Path_arquivo:
                self.processar()

            elif '.HEX' in self.Path_arquivo:
                self.processar()

            else:
                messagebox.showerror("Erro", "Arquivo incompativel!")
                self.Laybel_Path.delete("0", "end")

        else:
            messagebox.showwarning("Alerta", "Nenhum arquivo selecionado")

    def processar(self):

        # Função responsável por processar os dados carregados

        index = 0

        # Importanto os bibliotecas desenvolvidas
        crc16 = CRC16_MODBUS.crc16()
        protocolo = MONTA_PROTOCOLO.monta_protocolo()
        pacote = MONTA_PACOTE.monta_pacote()

        self.buffer_crc = []
        self.buffer_pacote = []
        self.string_protocolo = []

        try:
            self.buffer = []

            # Se o endereço do arquivo (path) for diferente de vazio o arquivo será aberto
            if self.Path_arquivo != "":
                self.file = open(self.Path_arquivo, 'r')

                for i in self.file:
                    self.buffer.append(i.strip())
                    # print(self.buffer[index])

                    # Monta o protocolo com as informações recebidas do buffer
                    string_protocolo, array_protocolo = protocolo.Protocolo(self.buffer[index])

                    # Calcula o CRC16_ModBus da sttring_protocolo('LUPA+TAMANHO+COMANDO+DADOS')
                    selcitem_e_CRC = crc16.crc16(array_protocolo, 0, len(array_protocolo))

                    self.string_protocolo.append(string_protocolo)

                    # Monta o cacote completo de dados array_protocolo + CRC
                    pacoteMontado = pacote.dados(array_protocolo, selcitem_e_CRC)

                    # Adciona a um buffer cada linha do pacote
                    self.buffer_pacote.append(pacoteMontado)

                    index += 1

            self.file.close()



        except:

            pass

    def enviar(self):

        # Está enviando mesmo sem estra conectado - ajustar

        decoficaPacote = DECODIFICA_SERIAL.decodifica_serial()

        # Sempre que entrar neste evento a caixa de texto será limpa
        self.CAIXA_Texto.delete(1.0, "end")

        # Vetor para comparação dos dados enviado e recebidos
        try:

            for i in range(0, len(self.buffer_pacote), 1):

                stringDadoenviado = ""

                for y in range(0, len(self.buffer_pacote[i]), 1):

                    elemento_buffer_pacote = self.buffer_pacote[i][y]

                    if y < (len(self.buffer_pacote[i]) - 3):
                        self.escreveTextarea(self.string_protocolo[i][y])

                    self.conexao.write(elemento_buffer_pacote)

                try:
                    # Lendo o que esta sendo enviado do STM32
                    dadoLido = self.conexao.read()

                    # Esse print não é necessario
                    print(dadoLido)

                    # Processando o que foi recebido



                except:

                    print('Nada chegou!')
                    pass

                self.escreveTextarea("\n")

        except:
            messagebox.showwarning("Alerta", "Nenhum dado a ser enviado!")
            pass

    def atuallizar(self):

        # Atualiza todos os boxes de seleção
        self.combobox_COM.set('')
        self.combobox_VEL.set('')
        self.combobox_PARIDADE.set('')
        self.combobox_DBITS.set('')
        self.combobox_PARADA.set('')
        self.Laybel_Path.delete("0", "end")
        self.CAIXA_Texto.configure(state="normal")
        self.CAIXA_Texto.delete(1.0, "end")
        self.CAIXA_Texto.configure(state="disable")

        try:

            if self.conexao.is_open == TRUE:
                self.BTN_conectar['text'] = "Conectar"
                self.conexao.close()
        except:
            pass

        self.combobox_COM["values"] = self.porta_serial()

    def limpar(self):

        self.buffer_pacote = ""
        self.CAIXA_Texto.configure(state="normal")
        self.CAIXA_Texto.delete(1.0, "end")
        self.CAIXA_Texto.configure(state="disabled")

    def escreveTextarea(self, info):

        info = str(info).strip("''b")

        self.infoCaixatexto = info

        self.CAIXA_Texto.configure(state="normal")

        for i in range(0, len(self.infoCaixatexto), 1):
            # print(info[i])

            self.CAIXA_Texto.insert(END, f'{self.infoCaixatexto[i]}', )

            self.CAIXA_Texto.update()

            # sleep(0.000005)

        # self.CAIXA_Texto.insert(END, f'\n\n')

        self.CAIXA_Texto.configure(state="disabled")


Application()
