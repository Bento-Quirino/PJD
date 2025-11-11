Questão 01: O que é o Unity  

a) Uma linguagem de programação para desenvolvimento de jogos 

b) Um motor de física para simulações 3D 

**c) Uma engine para desenvolvimento de jogos e experiências interativas**

d) Um software exclusivo para modelagem 3D 


Questão 02: O que faz a MainCamera, presente nas cenas do Unity  

a) Controla a iluminação principal da cena 

**b) Renderiza a cena a partir de um ponto de vista específico para o jogador**

c) Define as propriedades físicas do ambiente 

d) Gerencia os áudios principais do jogo     

 
Questão 03: Qual é a diferença entre a aba Game e a aba Scene?  

**a) Scene: edição da cena; Game: visualização do jogo em execução**

b) Scene: para modelos 3D; Game: para interfaces 2D 

c) Scene: modo de desenvolvimento; Game: modo de build 

d) Scene: edição de código; Game: edição de assets  


Questão 04: O que é o Rigidbody?  

a) Um tipo de colisor estático para cenários 

b) Um componente para animação de personagens 

**c) Um componente que adiciona física realista a um GameObject**

d) Um sistema de partículas para efeitos especiais   


Questão 05: Qual a relação entre um script e um componente?  

a) Scripts são componentes pré-definidos do Unity 

b) Componentes são scripts compilados em C++ 

**c) Scripts são tipos de componentes que adicionam comportamento personalizado**

d) São conceitos independentes sem relação direta  

 
Questão 06: O que é a aba Inspector?  

a) Local para organizar a hierarquia de objetos da cena 

**b) Mostra e permite editar as propriedades do objeto selecionado**

c) Área para visualização do jogo em tempo de execução 

d) Local para gerenciar os assets do projeto    

 
Questão 07: O que é a aba Hierarchy?  

**a) Mostra todos os GameObjects da cena atual em estrutura hierárquica**

b) Exibe a relação de herança entre scripts 

c) Organiza os arquivos do projeto por tipo 

d) Mostra o histórico de comandos executados   


Questão 08: O que é Transform e como as informações dele são armazenadas (tipo, acesso, etc..)?  

**a) Componente que armazena Position, Rotation e Scale como Vector3**

b) Script que controla transições de animação 

c) Sistema que gerencia transformações de textura 

d) Tipo de dado para cálculos matemáticos complexos 

 

Questão 09: Supondo que uma cena esteja tocando. Fazemos algumas modificações, testamos e logo em seguida paramos a cena (usando os botões de Play e Stop da interface). Qual efeito essa ação tem nas modificações? 

a) As modificações são salvas automaticamente no projeto 

**b) As modificações feitas durante o Play Mode são perdidas ao parar**

c) As modificações são aplicadas apenas aos prefabs 

d) As modificações criam uma nova versão da cena   

 

Questão 10: Escreva um trecho de código que move um objeto em velocidade constante no plano XZ
using UnityEngine;

public class MovimentoXZ : MonoBehaviour
{
    float speed = 5f;
    
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        
        Vector3 direction = new Vector3(horizontal, 0f, vertical);
        
        // Aplica o movimento
        transform.Translate(direction.normalized * speed * Time.deltaTime);
    }
}

