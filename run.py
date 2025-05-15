import numpy as np
import matplotlib.pyplot as plt


def avaliar_funcao(funcao, x):
    return eval(funcao)


def atualizar_annotacao(event):
    if event.inaxes:  
        x_mouse = event.xdata  
        y_mouse = avaliar_funcao(funcao, x_mouse)  
        annotacao.xy = (x_mouse, y_mouse) 
        annotacao.set_text(f"X = {x_mouse:.2f}, Y = {y_mouse:.2f}") 
        annotacao.set_visible(True)  
    else:
        annotacao.set_visible(False)  
    plt.draw()  


funcao = input("Digite a função exponencial (use 'x' como variável, por exemplo, '0.01 * 2**x'): ")


x_valor = float(input("Digite o valor de X para calcular Y: "))

# Calcular Y
y_valor = avaliar_funcao(funcao, x_valor)
print(f"Para X = {x_valor}, Y = {y_valor:.10f}")


x = np.arange(0, x_valor + 1, 1)  


y = [avaliar_funcao(funcao, xi) for xi in x]


plt.ticklabel_format(style='plain', axis='y')


fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label=f'Y = {funcao}')

plt.title('Gráfico da Função Exponencial')
plt.xlabel('Valor de X')
plt.ylabel('Valor de Y')
plt.grid(True)
plt.legend()


annotacao = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"))
annotacao.set_visible(False)  

fig.canvas.mpl_connect("motion_notify_event", atualizar_annotacao)

plt.show()