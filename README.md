# 🎯 **Seleção de Atividades de Programação em Python**

Explore as atividades abaixo e clique no link correspondente para visualizar a descrição completa e os detalhes.

---

## 📝 **Lista de Atividades**

### **1. [Minha Primeira Classe/Objeto](https://github.com/WallasAR/POO_in_Python_exercises/blob/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20001/Class_and_Object.py)**
> **📅 Data:** 16/02/2024  
> **📝 Descrição:**  
> - Implementação de uma classe e objeto em Python.
> - **💡 Dicas:**
>   1. A classe deve ter pelo menos um atributo mutável.
>   2. Os métodos devem manipular atributos mutáveis.

---

### **2. [Atividade: Construtores](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20002)**
> **📅 Data:** 01/03/2024  
> **📝 Descrição:**  
> - **Exercício 1:** Modele uma classe `Rádio` com estados e comportamentos, crie dois objetos e execute métodos.
> - **Exercício 2:** Melhore a classe `Bicicleta` adicionando limites para atributos e ajuste métodos para alterar estados com condições específicas.

---

### **3. [Prática: Implementação de uma CNH e Trabalhando com Datetime](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20003)**
> **📅 Data:** 15/03/2024  
> **📝 Descrição:**  
> - Implemente uma classe em Python que represente uma carteira de habilitação (CNH).
> - Identifique e manipule atributos mutáveis e imutáveis.
> - Valide e teste os métodos implementados através da criação de objetos.

---

### **4. [Atividade: Implementação da Classe `RadioFM`](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20004)**
> **📅 Data:** 22/03/2024  
> **📝 Descrição:**  
> - Implemente os métodos descritos na classe `RadioFM`:
>   1. **🔌 Método `ligar`:** Inicializa o rádio com volume mínimo e, se a antena estiver habilitada, define a frequência e estação atuais.
>   2. **🔌 Método `desligar`:** Desliga o rádio e redefine os atributos.
>   3. **🔊 Método `aumentar_volume`:** Incrementa o volume com um valor opcional, garantindo que não ultrapasse o limite máximo.
>   4. **🔉 Método `diminuir_volume`:** Decrementa o volume com um valor opcional, garantindo que não ultrapasse o limite mínimo.
>   5. **📻 Método `mudar_frequencia`:** Atualiza a frequência e estação atuais, podendo passar um valor específico ou seguir o próximo no dicionário.
> - Crie pelo menos 3 objetos e teste os métodos implementados.

---

### **5. [Atividade: Encapsulamento - Classe `Pessoa`](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20005)**
> **📅 Data:** 05/04/2024  
> **📝 Descrição:**  
> - Modele uma classe `Pessoa` utilizando conceitos como construtores, parâmetros opcionais, encapsulamento e decoradores.
> - **Atributos:** nome, idade, peso, altura, sexo, estado (vivo/morto), estado civil, cônjuge.
> - **Métodos:** envelhecer, engordar, emagrecer, crescer, casar, morrer.
> - Implementar todas as validações necessárias, e métodos que respeitem o estado atual da pessoa.

---

### **6. [Atividade Avaliativa: Consulta Médica](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20006)**
> **📅 Data:** 05/07/2024  
> **📝 Descrição:**  
> - Implemente uma classe que represente uma consulta médica com os seguintes atributos: data da consulta, data do retorno, paciente, médico, pago, cancelado.
> - **⚠️ Regras e Recomendações:**
>   1. Valor da consulta: R$ 300, sendo R$ 200 para o médico e R$ 100 para a clínica.
>   2. Utilizar construtores, encapsulamento, decoradores e atributos opcionais.
>   3. Usar a biblioteca `datetime` para manipulação de datas.
>   4. Não permitir consultas em datas menores ou iguais à data atual, nem em finais de semana.
>   5. Retorno válido por 30 dias após a consulta, e só deve ser agendado se a consulta foi paga.
> - Crie objetos e teste as regras e métodos implementados.

---

### **7. [Exercício: Associação de Classes 1:1 (Celular - Bateria)](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20007)**
> **📅 Data:** 09/08/2024  
> **📝 Descrição:**  
> - Implemente uma associação de classes entre `Celular` e `Bateria`.
> - **🔋 Classe `Bateria`:**
>   - Atributos: `código`, `capacidade`, `percentual_carga`.
>   - Métodos: `carregar`, `descarregar`.
> - **📱 Classe `Celular`:**
>   - Atributos: `Mei`, `Bateria`, `Wifi`.
>   - Métodos: `ligar_desligar`, `colocar_bateria`, `retirar_bateria`, `ligar_desligar_wifi`, `assistir_video`, `carregar`, `descarregar`.
> - Crie pelo menos 3 instâncias de cada classe e teste todos os métodos implementados.

---

### **8. [Exercício: Associação de Classes 1:N (Time - Jogador)](https://github.com/WallasAR/POO_in_Python_exercises/tree/339a40eeb2a2c6f06d9a5dc3b3a388dfb8c0bdf8/activity%20008)**
> **📅 Data:** 30/08/2024  
> **📝 Descrição:**  
> - Implemente uma associação de classes 1:N entre `Time`, `Jogador`, e `Campeonato`.
> - **⚽ Classe `Time`:**
>   - Métodos: `adicionar_jogador`, `excluir_jogador`, `transferir_jogador`, `mostrar_jogador`.
> - **🏆 Classe `Campeonato`:**
>   - Atributos: `numero_times`, `times`, `partidas`.
>   - Métodos: `mostrar_classificação`.
> - Crie objetos para representar pelo menos 4 times, adicione jogadores, realize transferências e exclua jogadores. Registre partidas no campeonato e calcule a pontuação dos times.

---
