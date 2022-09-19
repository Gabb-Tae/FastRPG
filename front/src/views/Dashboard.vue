<template>
  <div id="ficha-arquivo-rows">
      <div class="ficha-arquivo-row" v-for="itens in fichas" :key="itens.id">
        <div id="ficha-title">
          Ficha de {{ itens.nome }} 
        </div>
              <div id="text">Nome: {{ itens.nome }}</div>
              <div>Raça: {{ itens.raca }}</div>
              <div>Classe: {{ itens.classe }}</div>
              <div>Nível: {{ itens.nivel }}</div>
              <div>Vida Máxima: {{itens.vidamax}}</div>
              <div>Habilidade Principal: {{itens.habilidade}}</div>
              <div>Força: {{ itens.forca }}</div>
              <div>Destreza: {{ itens.destreza }}</div>
              <div>Constituição: {{ itens.constituicao }}</div>
              <div>Inteligencia: {{ itens.inteligencia }}</div>
              <div>Sabedoria: {{ itens.sabedoria }}</div>
              <div>Carisma: {{ itens.carisma }}</div>
              <div>Tamanho: {{itens.tamanho}}</div>
              <div>Velocidade: {{itens.deslocamento}}</div>
              <div>Idioma: <p> {{itens.idioma}} </p></div>
              <div>Caracteristicas: <p> {{itens.caracteristicas}} </p></div>
              <div>Descrição: <p> {{itens.descricao}} </p> </div>
              <div>
                <button v-if="uid"><v-icon class="like-btn">mdi-thumb-up-outline</v-icon></button><br> <br>
                <button v-if="uid === itens.owner" class="delete-btn" ><v-icon>mdi-delete</v-icon></button>
              </div>
              
      </div>
  </div>
</template>

<script>
import * as fb from "@/plugins/firebase"
export default {
  name: "Dashboard",
    data() {
      return {
        uid: '',
        fichas: [],
      }
    },
  methods: {
    async buscarFichasDoServidor() {
      this.ficha = [];
      const logficha = await fb.fichaCollection.get();
      for (const doc of logficha.docs){
        this.fichas.push({
          owner: doc.data().owner,
          nome: doc.data().nome,
          classe: doc.data().classe,
          raca: doc.data().raca,
          nivel: doc.data().nivel,
          vidamax: doc.data().vidamax,
          habilidade: doc.data().habilidade,
          forca: doc.data().forca,
          destreza: doc.data().destreza,
          constituicao: doc.data().constituicao,
          inteligencia: doc.data().inteligencia,
          sabedoria: doc.data().sabedoria,
          carisma: doc.data().carisma,
          tamanho: doc.data().tamanho,
          deslocamento: doc.data().deslocamento,
          idioma: doc.data().idioma,
          caracteristicas: doc.data().caracteristicas,
          descricao: doc.data().descricao,

        });
      }
    },
    logadoOuNao(){
      if(this.uid){
        this.$router.push({path: "/perfil"})
      }else{
        this.$router.push({path: "/login"})
      }
    },

},
    mounted() {
      this.buscarFichasDoServidor();
      this.uid = fb.auth.currentUser.uid;
    }
}
</script>

<style scoped>

#ficha-title {
   font-weight: bold;
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }
#ficha-arquivo-rows,
.ficha-arquivo-row{
  display: flex;
  flex-wrap: wrap;
}

.ficha-arquivo-row div{
  width: 14%;
}

.ficha-arquivo-row{
  width: 100%;
  padding:5px 15px;
  border-bottom: 1px solid #CCC;
}

#ficha-arquivo-heading .order-id,
.ficha-arquivo-row .order-number {
  width: 10%;
}
.like-btn {
   background-color: #bf64c4;
   color: #222;
  font-weight: bold;
   border: 2px solid #8b0292;
   padding: 9.5px;
   font-size: 25px;
   margin: 0 auto;
   cursor: pointer;
   transition: .5s;
}
.like-btn:hover{
   background-color: transparent;
   color: #222;
 }

.delete-btn {
   background-color: #ca5353;
   color: #222;
   font-weight: bold;
   border: 2px solid #a00303;
   padding: 10px;
   font-size: 16px;
   margin: 0 auto;
   cursor: pointer;
   transition: .5s;
}

.delete-btn:hover{
   background-color: transparent;
   color: #222;
 }


</style>