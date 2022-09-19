<template>
  <v-container class="pa-8" fluid>
<div>
  <div id="cabecalho">
  FastRPG
  </div>
  <div>
    <section>
      <div id="Fastrpg">
        O que é o RPG e como o FastRPG é útil?
      </div>
      <v-img src="../assets/images/art-rpg.jpg"></v-img>
      <br>
      <div id="RPG">
        RPG
      </div>
      <div id="texto_int">
RPG é a sigla em inglês para role-playing game, um gênero de jogo onde os jogadores assumem o papel de personagens imaginários, em um mundo fictício.
Onde você pode ser oque quiser como um elfo, anão, mago, guerreiro. Claro existem algumas regras dentro de cada sistema afinal não é no início de jogo que simplesmente você pode sair voando, atirando raio “laser” pelos olhos, etc.
O sistema é onde se diz as regras e onde se acham os livros, o mais jogado mundialmente é o D&D (Dungeons and Dragons) uma simulação de mundo medieval de fantasia, com dragões monstros tudo que você possa imaginar.
      </div> <br>
      <div id="texto_rpg">
O RPG é um jogo de mesa bem estruturado e cooperativo (normalmente não há vencedores), em que, cada jogador controla, tipicamente, um único personagem. Durante o curso do jogo, cada jogador dirige as ações de seu personagem e suas interações com outros personagens. Uma partida geralmente dura varias sessões, chamadas de aventuras. Um conjunto de aventuras relacionadas entre si, é chamada campanha.

Os resultados das escolhas do grupo e a história básica do jogo é determinada pelo lider, também chamado mestre do jogo, ou ainda como narrador, conforme as regras e com a interpretação do lider sobre essas regras. O lider escolhe e descreve os vários Personagens não jogadores (NPCs), que os personagens encontram, o cenário em que essas relações ocorrem, e os resultados desses encontros baseados nas escolhas e ações dos jogadores. As extensas regras do jogo, que cobrem áreas diversas como interações sociais, uso de magia, combate e o efeito do ambiente nos personagens, ajudam o mestre em suas decisões.
</div> <br>
      <div id="fast-title">
        FastRPG
      </div>
      <div id="text-fast">
Nosso site busca trazer maior facilidade para construção de personagem e auxílio em outras funções, como rolagem de dados e conversores de moedas
 <br>
        Dentre nossas funções estão:
<br>
- Duas listas, contendo todas as Raças ( <v-icon>mdi-gnome</v-icon> ) e Classes ( <v-icon>mdi-anvil</v-icon>) que o livro oficial de Dungeons and Dragons tem disponivel.
<br>
- Rolador de Dados (<v-icon>mdi-dice-multiple</v-icon>): Existem uma variedade imensa de dados, temos os principais e mais importantes, sendo eles de 4,6,8,10,12 e 20 lados. Podendo ser rodados ao clicar no botão "Rolar"
<br>
- Conversor de Moedas ( <v-icon>mdi-bitcoin</v-icon> ): Colocando o valor em peças de ouro podendo converter para Prata, Cobre e Platina
<br>
- Gerador Simplificado de personagem( <v-icon>mdi-dice-d20</v-icon> ): Podendo excolher sua Raça, Classe, Niível, e Nome (Podendo tambem o aleatorizar), e apos a criação, sua ficha estará disponivel no Arquivo de Fichas ( <v-icon>mdi-bookshelf</v-icon> )
<br>
</div>
    </section>
    <br>
    <div id="breve">
      Em Breve:
    </div>
    <div>
      - Visualização de Ficha (Durante a Criação)
      <br>
      - Gerador de Nomes Individual
      <br>
      - Ficha Mais Completa
      <br>
      - Delete e Curtir de Forma Funcional
      <br>
      - E Muito Mais!
    </div>
  </div>
</div>
  </v-container>
</template>

<script>
import * as fb from "@/plugins/firebase"
export default {
  data(){
    return {
      uid: '',
      novaTarefa: '',
      tarefas: [],
    };
  },
  mounted() {
    this.uid = fb.auth.currentUser.uid;
  },
  methods: {
    async buscarTarefasDoServidor() {
      this.tarefas = [];
      const logTasks = await fb.taskCollection.where("owner", "==", this.uid).get();
      for (const doc of logTasks.docs){
        this.tarefas.push({
          id: doc.id,
          titulo: doc.data().titulo
        });
      }
    },
    async adicionar() {
      await fb.taskCollection.add({
        titulo: this.novaTarefa,
        dataGravacao: new Date().toISOString().slice(0, 10),
        owner: this.uid,
      });
      this.novaTarefa = "";
      this.buscarTarefasDoServidor();
    },
  },
}
</script>

<style scoped>
 #cabecalho{
   margin: 0 auto;
   font-weight: bold;
   font-size: 50px;
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
}
 #Fastrpg {
  max-width: 400px;
  margin-left: auto;
  margin-right: auto; 
  font-style: italic;
 }
 #RPG,#fast-title,#breve{
    max-width: 400px;
    border-left: 4px solid #8b0292;
    font-weight: bold;
 }

</style>