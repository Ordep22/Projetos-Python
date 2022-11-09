from tkinter import *
import serial.tools.list_ports
import serial
from tkinter import ttk
from tkinter import filedialog
from time import sleep

root = Tk()


class Application:
    # --------------------------------------------------------------------------------------------------------------#
    ###                                     Variáveis de inicialização                                           ###
    # --------------------------------------------------------------------------------------------------------------#

    ##Velocidades de conexão
    # Esses valores numca podem ser alterados
    velocidades = ("300", "600", "1200", "2400", "4800", "9600", "19200", "1200", "38400", "115200")

    ##Paryti
    # Valores de do bit de paridade
    parity = ("Nenhuma", "Par", "Impar")

    ##Stop bits
    # Valores dos bits de parada
    Stop_bit = ("1", "2")

    # Estado do botão de envio
    estado = ""

    # Buffer de recebimento de arquivo .HEX
    buffer = []

    # Pacote de processamento
    pacote = []

    data_bytes = (serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS)

    time_out = 0

    def __init__(self):
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
        self.icon =PhotoImage(file=r"RB.png")
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

        porta = self.combobox_COM.get()

        COM = porta.strip(" ")

        # print(COM)

        return COM[0:5]
        ##Se pegar uma com 12 vai dar erro

    def obter_VEL(self):

        VEL = self.combobox_VEL.get()
        #print(VEL)
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

        while True:  #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                #self.conexao =serial.Serial('COM10', self.velocidade)
                print(self.BTN_conectar['text'])

                if self.BTN_conectar['text'] == "Conectar":
                    self.conexao = serial.Serial(self.porta, self.velocidade)
                    self.BTN_conectar['text'] = "Desconectar"
                    print(self.conexao)  #Mostra o buffer de conexão

                else:

                    self.status = self.conexao.close()
                    self.BTN_conectar['text'] = "Conectar"
                    print(self.status)  #Mostra o buffer de conexão

                break
            except:
                pass

    def ligar(self):

        ligar = self.conexao.write('L'.encode())
        print(ligar)  # Mostra a informação de que foi enviada ao micro
        self.conexao.flush()

    def desligar(self):

        desligar = self.conexao.write('D'.encode())
        print(desligar)  # Mostra a informação de que foi enviada ao micro
        self.conexao.flush()

    def carrega_arquivo(self):

        self.Laybel_Path.delete("0", "end")
        self.Path_arquivo = filedialog.askopenfilename()
        self.Laybel_Path.insert(0, self.Path_arquivo)
        self.processar()

    def processar(self):
        indice = 0
        try:
            if self.Path_arquivo != "":
                file = open(self.Path_arquivo)
                for i in file:
                    self.buffer.append(i)

                self.enviar()

        except:
            pass

    def enviar(self):

        for i in self.buffer:
            serial.Serial.write(i)
            sleep(1)

    def atuallizar(self):

        print("Entrou")
        self.combobox_COM.delete("0", "end")
        self.combobox_COM["values"] = ""
        self.combobox_COM["values"] = self.porta_serial()


Application()
