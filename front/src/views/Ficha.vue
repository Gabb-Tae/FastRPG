<template>
  <div>
    <div>
      <Message :msg="msg" v-show="msg" />
      <form id="fichaform">
        <h3>Criação Rápida de Ficha</h3>
        <div class="input-container-nome" id="gerador_nomes">
        <input type="text" id="nome" name="nome" v-model="nome" placeholder="Nome do Personagem">
        <v-icon class="btn" slot="append" @click="gerar()">mdi-dice-multiple</v-icon>
        </div>
        <div class="input-container">
          <label id="classe" for="classe">Classe: </label>
          <select name="classe" id="classe" v-model="classe">
              <option value="">Selecione sua Classe</option>
              <option v-for="classe in classes" 
              :key="classe.id" :value="classe">{{ classe.title }}
              </option>
          </select>
        </div>
        <div class="input-container">
          <label id="raca" for="raca">Raça: </label>
          <select name="raca" id="raca" v-model="raca">
              <option value="">Selecione sua Raça</option>
              <option v-for="raca in racas" 
              :key="raca.id" :value="raca">{{ raca.title }}
              </option>
          </select>
        </div>
        <div class="input-container">
          <label id="nivel" for="nivel">Nivel: </label>
          <select name="nivel" id="nivel" v-model="nivel">
              <option value="">Selecione seu Nivel</option>
              <option v-for="nivel in niveis" 
              :key="nivel.id" :value="nivel">{{ nivel.title }}
              </option>
          </select>
        </div>
        <div class="input-container">
          <v-btn id="enviar" class="submit-btn" @click="adicionar">Criar minha Ficha</v-btn>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Message from './Message.vue';
import gerarnome from '@/utils/gerarnome.js'
import gerarsobrenome from '@/utils/gerarsobrenome.js'
import * as fb from "@/plugins/firebase"
import { niveis, classes, racas } from '@/assets/db/db'
export default {
  name: "fichaform",
  data(){

    return {
      classes: null,
      racas: null,
      niveis: null,
      nome: '',
      classe: null,
      raca: null,
      nivel:  null,
      msg: null,
      uid: '',
      ficha: [],
    }
  },
  methods: {
    getFichas(){
      this.classes = classes;
      this.racas = racas;
      this.niveis = niveis;
    }, 
    async adicionar() {
      await fb.fichaCollection.add({
        nome: this.nome,
        dataGravacao: new Date().toISOString().slice(0, 10),
        owner: this.uid,
        classe: this.classe.title,
        raca: this.raca.title,
        nivel: this.nivel.title,
        forca: this.classe.Força + this.raca.Força,
        destreza: this.classe.Destreza + this.raca.Destreza,
        constituicao: this.classe.Constituição + this.raca.Constituição,
        inteligencia: this.classe.Inteligencia + this.raca.Inteligencia,
        vidamax: this.classe.vida * this.nivel.vida,
        sabedoria: this.classe.Sabedoria + this.raca.Sabedoria,
        carisma: this.classe.Carisma + this.raca.Carisma,
        tamanho: this.raca.tamanho,
        deslocamento: this.raca.Deslocamento,
        idioma: this.raca.idioma,
        caracteristicas: this.raca.Caracteristicas,
        habilidade: this.classe.habilidade,
        descricao: this.classe.descricao,
        
      });
      this.msg = `Ficha de ${this.nome} Criada com Sucesso, Confira o Arquivo`;

      setTimeout(() => this.msg = "", 3000);
      this.nome = "";
      this.classe = "";
      this.raca = "";
      this.nivel = "";
    },
    gerar(){
      this.nome = gerarnome()+gerarsobrenome()
    },

  },
  mounted(){
    this.getFichas(),
    this.uid = fb.auth.currentUser.uid;
  },
  components: {
    Message
  }
}
</script>

<style scoped>
 #fichaform{
   max-width: 400px;
   margin: 0 auto;
 }

 .input-container{
   display: flex;
   flex-direction: column;
 }
 .input-container-nome {
  display: flex;
  flex-direction: row;
  width: 600px;
  margin-bottom: 15px;
  padding: 5px 10px;
  border-left: 4px solid #8b0292;

}
  #classe,#raca,#nivel {
   margin-bottom: 15px;
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }

 .label {
   font-weight: bold;
   margin-bottom: 15px;
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }

 .input,select {
   padding: 5px 10px;
   width: 300px;
 }

#enviar{
   background-color: #a23ea7;
   color: #222;
   font-weight: bold;
   border: 2px solid #222;
   padding: 10px;
   font-size: 16px;
   margin: 0 auto;
   cursor: pointer;
   transition: .5s;
 }

#enviar:hover{
   background-color: transparent;
   color: #222;
 }
</style>