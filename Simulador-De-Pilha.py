class Pilha:
    def __init__(self, max_size):
        self.item = []
        self.max_size = max_size
    
    def push(self, item):
        if len(self.item) >= self.max_size:
            print("Erro, Limite maximo atingido")
        else:
            self.item.append(item)
            print("Item adicionado!")
    
    def pop(self):
        print("Pop")
        return self.item.pop()
    
    def peek(self):
        print(self.item)
        return self.item[-1] if self.item else None

    def is_empty(self):
        return len(self.item) == 0

def menu():
    max_size = int(input("Digite o tamanho maximo da pilha: "))
    pilha = Pilha(max_size)
    while True:
        print("----<Simulador de Pilha>-----")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        op = input("Digite a opção que deseja:")

        if op == '1':
            item = input("Digite o nome do item: ")
            pilha.push(item)

        if op == '2':
            pilha.pop()
    
        if op == '3':
            pilha.peek()

        if op == '4':
            pilha.is_empty()
menu()