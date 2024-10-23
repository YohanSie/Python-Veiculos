class Veiculo():
    def __init__(self, marca, modelo, ano, valor, tipo):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._valor = float(valor)
        self._tipo = tipo

    def calcular_ipva(self):
        pass

class Carro(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.04

class Moto(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.02

class Caminhao(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.01

class Automotores():
    def __init__(self):
        self.veiculos = []

    def cadastrar(self):
        tipo = input("\nTipo do veículo (carro/moto/caminhão): ").lower().strip()
        marca = input("Marca do veículo: ")
        modelo = input("Modelo do veículo: ")
        ano = int(input("Ano do veículo: "))
        valor = float(input("Valor do veículo: "))
    
        if tipo == "carro":
            veiculo = Carro(marca, modelo, ano, valor, tipo)
        elif tipo == "moto":
            veiculo = Moto(marca, modelo, ano, valor, tipo)
        elif tipo == "caminhão":
            veiculo = Caminhao(marca, modelo, ano, valor, tipo)
        else: 
            print("Tipo inválido") 
            return

        self.veiculos.append(veiculo)
        print("O veículo foi cadastrado!\n")

    def consultar(self): 
        if not self.veiculos:
            print("Nenhum veículo cadastrado!")
        for i, veiculo in enumerate(self.veiculos, start=1):
            print(f"\n{i}. {veiculo._marca} {veiculo._modelo}\n   Ano: {veiculo._ano}\n   Valor: R${veiculo._valor:.2f}")
        
    def calcular_ipva(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
            return
        print("\nIPVA dos veículos")
        for i, veiculo in enumerate(self.veiculos, start=1):
            ipva = veiculo.calcular_ipva()
            print(f"{i} - {veiculo._marca} {veiculo._modelo}: R${ipva:.2f}\n")

    def menu(self):
        while True:
            print("\n1. Cadastrar veículo") 
            print("2. Consultar veículo")
            print("3. Calcular IPVA")
            print("4. Sair")
            op = int(input("Digite a opção: "))

            match op:
                case 1:
                    self.cadastrar()
                case 2:
                    self.consultar()
                case 3:
                    self.calcular_ipva()
                case 4:
                    print("Código encerrado!")
                    break
                case _:
                    print("Digite uma opção válida!")

sistema = Automotores()
sistema.menu()
