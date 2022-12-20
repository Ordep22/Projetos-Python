import MPA23FILE





class trafegoDados:

    def __init__(self):

        self.conexao = None

    def escrevendo(self,pacote):

        self.pacote = pacote

        try:
            if self.conexao.is_oppen():
                self.conexao.write(self.pacote)

        except:
            return 0


    def lendo(self):

        try:

            if self.conexao.is_oppen():
                self.conexao.read(self.conexao.inWaiting())

        except:
            return 0
