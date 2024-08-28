class Pilha:
    def __init__(self, max_size):
        self.item = []
        self.max_size = max_size
    
    def push(self, item):
        if len(self.item) >= self.max_size:
            print("Limite máximo atingido")
        else:
            self.item.append(item)
            print("Item adicionado!")
    
    def pop(self):
        if self.is_empty():
            print("a pilha está vazia!")
        else:
            print("Último item removido")
            return self.item.pop()
    
    def peek(self):
        if self.is_empty():
            print("pilha está vazia!")
            return None
        else:
            print("Topo da pilha:", self.item[-1])
            return self.item[-1]
    
    def is_empty(self):
        return len(self.item) == 0

def menu():
    max_size = int(input("Digite o tamanho máximo da pilha: "))
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

        elif op == '2':
            pilha.pop()

        elif op == '3':
            pilha.peek()

        else:
            print("Opção inválida")

menu()
