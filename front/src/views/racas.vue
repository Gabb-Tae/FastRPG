<template>
    <v-container class="pa-8" fluid>
    <h1 class="h1">Raças</h1>
        <v-list>
          <v-list-item v-for="raca of racas" v-bind:key="raca.id"> 
            <v-list-item-content><h3 id="raca-title">{{raca.title}}
              </h3>Força: {{raca.Força}}, Destreza: {{raca.Destreza}}, 
               Constituição: {{raca.Constituição}}, Inteligencia; {{raca.Inteligencia}}, 
               Sabedoria: {{raca.Sabedoria}}, Carisma: {{raca.Carisma}} <br>
            Tamanho: {{raca.tamanho}} <br>
            Deslocamento: {{raca.Deslocamento}} <br>
            Idioma: {{raca.idioma}} <br>
            Caracteristicas: {{raca.Caracteristicas}} 
            <br>
            </v-list-item-content> <br>
          </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
import { racas } from '@/assets/db/db'
export default {
  data(){
    return {
      racas: null, 
      } 
  },
  methods: {
    async getFichas(){
      this.racas = racas;}
},
  mounted(){
    this.getFichas()
  }
}
</script>

<style scoped>
 #raca-title {
   font-weight: bold;
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }
.h1{
  padding: 5px 10px;
  border-left:4px solid #8b0292;
}

</style>