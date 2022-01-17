class Agenda:   
   
    def Inserir(self): #Insesir contato

        nome = input("Nome: ")
        numero = input("Numero: ")
        email = input("Email: ")
        
        contatos = open('Contatos.txt', 'a')
        contatos.write("{}-{}-{}\n".format(nome, numero, email))
        contatos.close()    

        print("\nContato adicionado com sucesso!")                 
    #---------------------------------------------------------------------

    def Remover(self): #Remover contato 
        busc = (input("\n\nDigite parte ou o numero de celular completo do contato que vai ser removido: "))          
        print("\n\n")

        aux2 = 0
        contatos = open('Contatos.txt', 'r') #buscando contato
        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(busc)   
 
            if aux != -1:
                print(linha)                 #Mostrando contato que será removido, ou não
                aux2 = 1  
            
        if aux2 != 0:
            escolha = int (input("Deseja remover o contato acima?\n1 - Sim\n2 - Não\n\nInsira sua escolha:  "))
            
            if escolha == 1:
                contatos = open('Contatos.txt', 'r')
                x1 = []
                x2 = []

                for linha in contatos:
                    x1.append(linha) 
                
                for linha in range (0, len(x1)):
                    if busc not in x1[linha]:
                        x2.append(x1[linha])

                contatos.close()
                contatos = open('Contatos.txt', 'w')

                for i in range (0, len(x2)):                    
                    contatos.write(x2[i]) 

                print("\nContato Excluído!\n")
                contatos.close()            
        else:
            print("\nContato não consta na agenda.\n")
    #---------------------------------------------------------------------

    def Buscar(self): #Buscar contato
        busc = input("\n\nDigite o nome, numero ou email do contato: ")
        print("\n\n")

        contatos = open('Contatos.txt', 'r')
        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(busc)

            if aux != -1:
                print(linha)

        contatos.close()
    #---------------------------------------------------------------------

    def Editar(self): #Editando contatos
        busc = (input("\n\nDigite Email ou numero de celular do contato que vai ser editado, seja completo ou partes: "))          
        print("\n\n")

        aux2 = 0
        contatos = open('Contatos.txt', 'r') #buscando contato
        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(busc)   
 
            if aux != -1:
                print(linha)                 #Mostrando contato que será editado, ou não
                aux2 = 1  
            
        if aux2 != 0:
            escolha = int (input("O que deseja editar no contato acima?\n1 - Nome\n2 - Telefone\n3 - Email\n4 - Todo o contato\n\nInsira sua escolha:  "))
            
            
            contatos = open('Contatos.txt', 'r')
            x1 = []
            x2 = []

            for linha in contatos:
                x1.append(linha) 
                
            for linha in range (0, len(x1)):
                if busc in x1[linha]:
                    pos = x1.index(x1[linha])
                    aux3 = x1[pos]                                                

            contatos.close()

            #----------------------

            if escolha == 1:        #Editando apenas nome
                novo = input("\nInsira o nome que substituirá o atual:  ")
                               
                #Encontrando nome atual/antigo
                aux4 = aux3.find("-")
                aux3 = aux3[aux4:]                
                aux3 = (novo+aux3)                
                print("aux3 --->",aux3)
                contatos = open('Contatos.txt', 'w')
                for i in range (0, len(x1)):
                    if busc not in x1[i]:
                        contatos.write(x1[i])
                    
                    else:
                        contatos.write(aux3)   
                print("Contato editado com sucesso!")  

            #----------------------

            elif escolha == 2:        #Editando apenas numero
                novo = input("\nInsira o numero que substituirá o atual:  ")                     
                #Encontrando numero atual/antigo
                aux4 = aux3.find("-") 
                aux5 = aux3.rfind("-")             
                
                nomex = aux3[:aux4] + "-"
                emailx = aux3[aux5:]
                aux3 = (nomex + novo + emailx)                              

                contatos = open('Contatos.txt', 'w')
                for i in range (0, len(x1)):
                    if busc not in x1[i]:
                        contatos.write(x1[i])
                    
                    else:
                        contatos.write(aux3)   
                print("Contato editado com sucesso!") 

            #----------------------

            elif escolha == 3:        #Editando apenas email
                novo = input("\nInsira o email que substituirá o atual:  ")                     
                #Encontrando email atual/antigo                
                aux4 = aux3.rfind("-")    
                aux3 = aux3[:aux4] + "-"               
                aux3 = (aux3+novo)              

                contatos = open('Contatos.txt', 'w')
                for i in range (0, len(x1)):
                    if busc not in x1[i]:
                        contatos.write(x1[i])
                    
                    else:
                        contatos.write(aux3+"\n")   
                print("Contato editado com sucesso!")

            #----------------------

            elif escolha == 4:        #Editando contato inteiro                        
                nome = input("\n\nNome: ")
                numero = input("Numero: ")
                email = input("Email: ")    

                aux3 = (nome+"-"+numero+"-"+email)  
                print("aux3 ----->",aux3)     

                contatos = open('Contatos.txt', 'w')
                for i in range (0, len(x1)):
                    if busc not in x1[i]:
                        contatos.write(x1[i])
                    
                    else:
                        contatos.write(aux3+"\n")   
                print("Contato editado com sucesso!")

            else:
                print("\nOpção inválida! Tente novamente com uma opção disponível.")      

    #---------------------------------------------------------------------

class Menu: #Criando menu para poder usar como loop
    def Iniciar_menu(self):             
        print("""\n\n             
            ---MENU AGENDA---  
              [1] Inserir   
              [2] Remover   
              [3] Buscar    
              [4] Editar    
              [5] Finalizar 
            \n""")     
    
menu = Menu() #setando
escolhaX = 0 

while escolhaX != 5: #Se manter dentro do menu, até finalizar nas opções
    try:
        if escolhaX == 0: #Só para aparecer o primeiro menu. Está aqui para ficar dentro do "Try"
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))
            
        elif escolhaX <1 or escolhaX>4 :
            input("\nNumero invalido!\nDigite qualquer tecla para voltar ao menu.")
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))    
                
        elif escolhaX == 1:
            contatos = Agenda()
            contatos.Inserir()
                
            input("\n\nAperte qualquer tecla para voltar ao menu.")
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))

        elif escolhaX == 2:
            contatos = Agenda()
            contatos.Remover()

            input("\n\nAperte qualquer tecla para voltar ao menu.")
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))

        elif escolhaX == 3:
            contatos = Agenda()
            contatos.Buscar()

            input("\n\nAperte qualquer tecla para voltar ao menu.")
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))

        elif escolhaX == 4:
            contatos = Agenda()
            contatos.Editar()

            input("\n\nAperte qualquer tecla para voltar ao menu.")
            menu.Iniciar_menu()
            escolhaX = int(input("Digite sua escolha com um numero correspondente acima: "))
                

    except ValueError:
        print("\n\nDigite apenas números!")
        input("Aperte qualquer tecla para voltar ao menu.")

print("\n\n\n\nAgenda finalizada com sucesso, até breve! =)")