import numpy as np

class jogador:
    def __init__(self,numero,posicao,nome,forca):
        self.numero = numero
        self.posicao = posicao
        self.nome = nome
        self.forca = forca

    def __str__(self):
        return f"numero {self.numero}, posicao {self.posicao},nome {self.nome}, forca {self.forca}"

list=[]; list5=[]; list4=[];list3=[];list2=[];list1=[]

def adicionar_jogadores():
    list.append(jogador(7,"gandula","reto",99))
    list.append(jogador(7,"gandula","reto",4))
    list.append(jogador(7,"gandula","reto",98))
    list.append(jogador(7,"gandula","reto",4))
    list.append(jogador(7,"gandula","reto",96))
    list.append(jogador(7,"gandula","reto",95))
    list.append(jogador(7,"gandula","reto",9))
    list.append(jogador(7,"gandula","reto",93))
    list.append(jogador(7,"gandula","reto",92))
    list.append(jogador(7,"gandula","reto",91))
    list.append(jogador(7,"gandula","reto",6))
    list.append(jogador(7,"gandula","reto",89))
    list.append(jogador(7,"gandula","reto",88))
    list.append(jogador(7,"gandula","reto",25))
    list.append(jogador(7,"gandula","reto",86))
    list.append(jogador(7,"gandula","reto",85))
    list.append(jogador(7,"gandula","reto",70))
    list.append(jogador(7,"gandula","reto",83))
    list.append(jogador(7,"gandula","reto",82))
    list.append(jogador(7,"gandula","reto",20))
    return list

list = adicionar_jogadores()
tentativas = 1
while(True):
    list.sort(key=lambda a: a.forca,reverse=True)

    # for jogador in list:
    #     print(jogador)

    list1.extend(list[0: 4])
    np.random.shuffle(list1)
    list2.extend(list[4: 8])
    np.random.shuffle(list2)
    list3.extend(list[8: 12])
    np.random.shuffle(list3)
    list4.extend(list[12: 16])
    np.random.shuffle(list4)
    list5.extend(list[16: 20])
    np.random.shuffle(list5)

    # print("TIER 1")
    # for jogador in list1:
    #     print(jogador)
    # print("_____________________")
    # print("TIER 2")
    # for jogador in list2:
    #     print(jogador)
    # print("_____________________")
    # print("TIER 3")
    # for jogador in list3:
    #     print(jogador)
    # print("_____________________")
    # print("TIER 4")
    # for jogador in list4:
    #     print(jogador)
    # print("_____________________")
    # print("TIER 5")
    # for jogador in list5:
    #     print(jogador)
    # print("_____________________")


    time_a = [list1[0],list2[0],list3[0],list4[0],list5[0]]
    soma_a = 0
    for jogador in time_a:
        soma_a += jogador.forca
    media_time_a = soma_a/5

    time_b =[list1[1],list2[1],list3[1],list4[1],list5[1]]
    soma_b = 0
    for jogador in time_b:
        soma_b += jogador.forca
    media_time_b = soma_b/5

    time_c =[list1[2],list2[2],list3[2],list4[2],list5[2]]
    soma_c = 0
    for jogador in time_c:
        soma_c += jogador.forca
    media_time_c = soma_c/5

    time_d =[list1[3],list2[3],list3[3],list4[3],list5[3]]
    soma_d = 0
    for jogador in time_d:
        soma_d += jogador.forca
    media_time_d = soma_d/5



    media_geral = (soma_a + soma_b + soma_c + soma_d) / 20

    if((media_geral + 5 < media_time_a or media_geral - 5 > media_time_a) or 
    (media_geral + 5 < media_time_b or media_geral - 5 > media_time_b) or 
    (media_geral + 5 < media_time_c or media_geral - 5 > media_time_c) or 
    (media_geral + 5 < media_time_d or media_geral - 5 > media_time_d)):
        tentativas += 1
    else:
        print("ok")
        break
print(f"levaram-se {tentativas} tentativas")

print("TIME 2")
for jogador in time_a:
    print(jogador)
print("______________")
print("TIME 2")
for jogador in time_b:
    print(jogador)
print("______________")
print("TIME 3")
for jogador in time_c:
    print(jogador)
print("______________")
print("TIME 4")
for jogador in time_d:
    print(jogador)

