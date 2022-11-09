import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import serial.tools.list_ports
import serial


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title('MPA 2023')

        ##Velocidades de conexão
        # Esses valores numca podem ser alterados
        self.velocidades = ("300", "600", "1200", "2400", "4800", "9600", "19200", "1200", "38400", "115200")

        ##Paryti
        # Valores de do bit de paridade
        self.parity = ("Nenhuma", "Par", "Impar")

        ##Stop bits
        # Valores dos bits de parada
        self.Stop_bit = ("1", "2")

        # Estado do botão de envio
        self.estado = ""

        # Buffer de recebimento de arquivo .HEX
        self.buffer = ""

        # Variável de opção
        self.variavel_opcao = tk.StringVar(self)

        # Instanciando uma janela
        self.criando_janela()

    def criando_janela(self):

        ##posicionamento
        paddings = {'padx': 5, 'pady': 5}

        # Texto menu de seleção portas COM
        combobox_label = ttk.Label(self, text="COM:")
        combobox_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        ##Menu de seleção portas COM
        # Caixa de seleção
        self.combobox_COM = ttk.Combobox(self, values=self.porta_serial(), state="readonly")
        self.combobox_COM.grid(column=0, row=1, sticky=tk.W, **paddings)

        # Texto seleção de velocidade de concção
        label = ttk.Label(self, text="Valocidade:")
        label.grid(column=2, row=0, sticky=tk.W, **paddings)

        # Menu de seleção de velocidade conexão
        self.combobox_VEL = ttk.Combobox(self, values=self.velocidades)
        self.combobox_VEL.grid(column=2, row=1, sticky=tk.W, **paddings)

        # Texto seleção de bit de paridade
        label = ttk.Label(self, text="Parity:")
        label.grid(column=3, row=0, sticky=tk.W, **paddings)

        # Menu bit de paridade
        self.combobox_PARIDADE = ttk.Combobox(self, values=self.parity)
        self.combobox_PARIDADE.grid(column=3, row=1, sticky=tk.W, **paddings)

        # Texto seleção de bit de parada
        label = ttk.Label(self, text="Stop bit:")
        label.grid(column=4, row=0, sticky=tk.W, **paddings)

        # Menu bit de parada
        self.combobox_PARADA = ttk.Combobox(self, values=self.Stop_bit)
        self.combobox_PARADA.grid(column=4, row=1, sticky=tk.W, **paddings)

        # Botão conectar
        BTN_conectar = ttk.Button(self, text='Conectar', command=self.conectar)
        BTN_conectar.grid(column=0, row=2, sticky=tk.W, **paddings)

        # Botão Desconectar
        BTN_desconectar = ttk.Button(self, text='Desonectar', command=self.desconectar)
        BTN_desconectar.grid(column=0, row=3, sticky=tk.W, **paddings)

        # Botão Ligar
        BTN_ligar = ttk.Button(self, text='Ligar', command=self.ligar)
        BTN_ligar.grid(column=2, row=2, sticky=tk.W, **paddings)

        # Botão Desligar
        BTN_Deligar = ttk.Button(self, text='Delisgar', command=self.desligar)
        BTN_Deligar.grid(column=3, row=2, sticky=tk.W, **paddings)

        # Botão lêr arquivos
        BTN_Carregar = ttk.Button(self, text='Ler arquivo', command=self.carrega_arquivo)
        BTN_Carregar.grid(column=4, row=2, sticky=tk.W, **paddings)

        # Botão enviar
        BTN_Enviar = ttk.Button(self, text='Enviar', command=self.enviar)
        BTN_Enviar.grid(column=5, row=2, sticky=tk.W, **paddings)

        # Texto Laybel Path arquivo .HEX
        Text_Laybel_Path = ttk.Label(self, text='Path')
        Text_Laybel_Path.grid(column=6, row=0, sticky=tk.W, **paddings)

        # Laybel Path arquivo .HEX
        self.Laybel_Path = tk.Entry(self, width=50)
        self.Laybel_Path.grid(column=6, row=1, sticky=tk.W, **paddings)

        # Caixa de texto Arquivo .HEX
        self.CAIXA_Texto = tk.Text(self,width=90,height=10)
        self.CAIXA_Texto.grid(column = 6,row = 3, sticky=tk.W,**paddings)


    def porta_serial(self):

        self.a = serial.tools.list_ports.comports()
        return self.a

    def obter_COM(self):

        COM = self.combobox_COM.get()
        # print(COM[0:4])
        return COM[0:4]

    def obter_VEL(self):

        VEL = self.combobox_VEL.get()
        # print(VEL)
        return VEL

    def conectar(self):

        self.velocidade = self.obter_VEL()
        self.porta = self.obter_COM()
        while True:  # Loop para a conexão com o Arduino
            try:  # Tenta se conectar, se conseguir, o loop se encerra
                # self.conexao =serial.Serial('COM10', self.velocidade)
                self.conexao = serial.Serial(self.porta, self.velocidade)
                print(self.conexao)  # Mostra o buffer de conexão
                break
            except:
                pass

    def desconectar(self):

        self.status = self.conexao.close()
        print(self.status)  # Mostra o buffer de conexão

    def ligar(self):

        ligar = self.conexao.write('L'.encode())
        print(ligar)  # //Mostra a informação de que foi enviada ao micro
        self.conexao.flush()

    def desligar(self):

        desligar = self.conexao.write('D'.encode())
        print(desligar)  # //Mostra a informação de que foi enviada ao micro
        self.conexao.flush()

    def carrega_arquivo(self):

        self.Laybel_Path.delete("0", "end")
        self.Path_arquivo = filedialog.askopenfilename()
        self.Laybel_Path.insert(0, self.Path_arquivo)
        self.processar()

    def processar(self):

        with open(self.Path_arquivo,"r") as arquivo:
            self.buffer = arquivo.read()





    def enviar(self):

        self.CAIXA_Texto.insert(1.0 ,self.buffer)
        #print(self.buffer)




if __name__ == "__main__":
    app = Application()
    app.mainloop()
