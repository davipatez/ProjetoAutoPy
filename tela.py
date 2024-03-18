import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('BrightColors')
        #Layout
        layout = [
            [sg.Text('Nome:', size=(5,0)), sg.Input(size=(20,0), key='nome')],

            [sg.Text('Idade:', size=(5,0), ), sg.Input(size=(20,0),key='idade')],

            [sg.Text('Sexo:', size=(5,0))],
            [sg.Checkbox('Masc', key='M'), sg.Checkbox('Fem', key='F'), sg.Checkbox('N/A', key='nenhum')],

            [sg.Text('Formação:', size=(8,0))],
            [sg.Radio('Ens. Médio','form', key='em'), sg.Radio('Ens. Superior','form', key='es')],

            [sg.Button('Enviar')],

            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        #Extrair dados da tela
        

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            masc = self.values['M']
            fem = self.values['F']
            none = self.values['nenhum']
            en_superior = self.values['es']
            en_medio = self.values['em']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'masc: {masc}')
            print(f'fem: {fem}')
            print(f'none: {none}')
            print(f'formacao: {en_superior}')
            print(f'formacao: {en_medio}')
            print('')

tela = TelaPython()
tela.Iniciar()