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
    list.append(jogador(7,"gandula","reto",26))
    list.append(jogador(7,"gandula","reto",50))
    list.append(jogador(7,"gandula","reto",33))
    list.append(jogador(7,"gandula","reto",55))
    list.append(jogador(7,"gandula","reto",95))
    list.append(jogador(7,"gandula","reto",21))
    list.append(jogador(7,"gandula","reto",93))
    list.append(jogador(7,"gandula","reto",92))
    list.append(jogador(7,"gandula","reto",91))
    list.append(jogador(7,"gandula","reto",42))
    list.append(jogador(7,"gandula","reto",89))
    list.append(jogador(7,"gandula","reto",45))
    list.append(jogador(7,"gandula","reto",25))
    list.append(jogador(7,"gandula","reto",86))
    list.append(jogador(7,"gandula","reto",76))
    list.append(jogador(7,"gandula","reto",70))
    list.append(jogador(7,"gandula","reto",83))
    list.append(jogador(7,"gandula","reto",82))
    list.append(jogador(7,"gandula","reto",20))
    return list

list = adicionar_jogadores()
tentativas = 1

print(len(list))

while(True):
    list.sort(key=lambda a: a.forca,reverse=True)

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

    def tirar_time(posicao_tier):
        return [list1[posicao_tier],list2[posicao_tier],list3[posicao_tier],list4[posicao_tier],list5[posicao_tier]]
    
    def tirar_media_time(time):
        soma = 0
        for jogador in time:
            soma += jogador.forca
        return soma / 5

    time_a = tirar_time(0)
    media_time_a = tirar_media_time(time_a)
    time_b = tirar_time(1)
    media_time_b = tirar_media_time(time_b)
    time_c = tirar_time(2)
    media_time_c = tirar_media_time(time_c)
    time_d = tirar_time(3)
    media_time_d = tirar_media_time(time_d)
    media_geral = (media_time_a + media_time_b + media_time_c + media_time_d) / 4

    list1.clear()
    list2.clear()
    list3.clear()
    list4.clear()

    if((media_geral + 3 < media_time_a or media_geral - 3 > media_time_a) or 
    (media_geral + 3 < media_time_b or media_geral - 3 > media_time_b) or 
    (media_geral + 3 < media_time_c or media_geral - 3 > media_time_c) or 
    (media_geral + 3 < media_time_d or media_geral - 3 > media_time_d)):
        tentativas += 1
    else:
        print("ok")
        break

print(f"levaram-se {tentativas} tentativas")

print("TIME 1")
print(media_time_a)
for jogador in time_a:
    print(jogador)
print("______________")
print("TIME 2")
print(media_time_b)
for jogador in time_b:
    print(jogador)
print("______________")
print("TIME 3")
print(media_time_c)
for jogador in time_c:
    print(jogador)
print("______________")
print("TIME 4")
print(media_time_d)
for jogador in time_d:
    print(jogador)
# a

