#Meu modelo matemático envolve a oscilação de pessoas em um ambiente movimentado de acordo com um horário do dia.
#Ex: Em horários comerciais, a movimentação costuma ser bem maior em comparação a outros horários
#Ao longo do dia, o número de pessoas presentes em um local irá ser alterado constantemente, isso pode ser visualizado aqui
import numpy as np 
import matplotlib.pyplot as plt

#função da onda de oscilação
def oscila_pessoa(t, amp, freq, fase): #t = tempo; amp = amplitude de onda; freq = frequência de onda; fase = fase física
    return amp * np.sin(2 * np.pi * freq * t + fase) #isto constrói o formato da onda, np.sin faz o formato ondulatório

#Valores dos parâmetros
t = np.linspace(0, 23) #tempo em horas
amp = 100
freq = 1/24 #frequência por hora no dia
fase = -1.5 #Momento em que as pessoas estão mais presentes no local, período entre 9h e 18h, com pico às 12h

pessoas = oscila_pessoa(t,amp,freq,fase) #variável que chama a função


#Construindo o gráfico
plt.figure(figsize=(10,6)) #tamanho do gráfico
plt.plot(t, pessoas, color='blue')

plt.title('Alterações na quantidade de pessoas em ambientes movimentados ao longo do dia') #Título
plt.xlabel('Hora do dia (Em 24 horas)') #Nome do Eixo X
plt.ylabel('Pessoas') #Nome do Eixo Y
plt.rcParams.update({'font.size': 22})
plt.grid(True) #Apresenta linhas de grade no gráfico

plt.show() #Mostra o gráfico na tela
