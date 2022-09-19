<template>
  <form id="Conversor">
    <h1>Conversor de Moedas</h1>
    <div>
      <h3 id="po_pc">  Converter Ouro para Cobre </h3>
      <input type="number" name="po_pc" id="po_pc" v-model.number="po_pc_resultado" placeholder="Digite um Número" v-on:tab="gerar_po_pc">
      <v-icon class="btn" slot="append" @click="gerar_po_pc">mdi-dice-d12-outline</v-icon>
      <br>
      <h4>  Resultado: {{po_pc_resultado*100}} </h4>
      <br>
      <br>
      <h3 id="po_pp">  Converter Ouro para Prata </h3>
      <input type="number" name="po_pp" id="po_pp" v-model.number="po_pp_resultado" placeholder="Digite um Número" v-on:tab="gerar_po_pp">
      <v-icon class="btn" slot="append" @click="gerar_po_pp">mdi-dice-d12-outline</v-icon>
      <br>
      <h4> Resultado: {{po_pp_resultado*10}} </h4>
      <br>
      <br>
      <h3 id="po_platina">  Converter Ouro para Platina </h3>
      <input type="number" name="po_platina" id="po_platina" v-model.number="po_platina_resultado" placeholder="Digite um Número" v-on:tab="gerar_po_platina">
      <v-icon class="btn" slot="append" @click="gerar_po_platina">mdi-dice-d12-outline</v-icon>
      <br>
      <h4> Resultado: {{po_platina_resultado*0.1}} </h4>
    </div>
  </form>
</template>

<script>
export default {
  data (){
    return{
      po_pc_resultado: {},
      po_pp_resultado: {},
      po_platina_resultado: {},
          }
  },
     methods:{
    gerar_po_pc() {
      this.po_pc_resultado = {}
    },
    gerar_po_pp() {
      this.po_pp_resultado = {}
    },
    gerar_po_platina() {
      this.po_platina_resultado = {}
    },
  }

}
</script>

<style>
 #po_platina,#po_pc,#po_pp {
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }
</style>