<template>

  <div class="container">
    
    <h2 id="titulo">{{titulo}}</h2>
    <br>
    <div class="grid-container">

    <div class="grid-child">
      
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D4" @click="D4" id="dado" class="white--text">Rolar D4</v-btn>
      <br> <br>
      <v-img src="../assets/dices/d4-icon.png" width="100"
      style="cursor: pointer;" data-type="20"
      @click="D4"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ quatro }}</p> 
      </span>
  </div>
  <div class="grid-child">
       
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D6" @click="D6" id="dado" class="white--text">Rolar D6</v-btn>
      <br> <br>
      <v-img src="../assets/dices/d6-icon.png" width="100"
      style="cursor: pointer;" data-type="20"
      @click="D6"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ seis }}</p> 
      </span>
  </div>
  <div class="grid-child">
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D8" @click="D8" id="dado" class="white--text">Rolar D8</v-btn>
      <br> <br>
      <v-img src="../assets/dices/d8-icon.png" width="100"
      style="cursor: pointer;" data-type="20"
      @click="D8"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ oito }}</p> 
      </span>
  </div>
  <div class="grid-child">
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D10" @click="D10" id="dado" class="white--text">Rolar D10</v-btn>
      <br><br>
      <v-img src="../assets/dices/d10-icon.png" width="100"
      style="cursor: pointer;" data-type="10"
      @click="D10"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ dez }}</p> 
      </span>
  </div>
  <div class="grid-child">
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D12" @click="D12" id="dado" class="white--text">Rolar D12</v-btn>
      <br> <br>
      <v-img src="../assets/dices/d12-icon.png" width="100"
      style="cursor: pointer;" data-type="12"
      @click="D12"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ doze }}</p> 
      </span>
  </div>
  <div class="grid-child" >
      <span class="input-group-btn">
      <v-btn color=#8b0292 @keyup.enter="D20" @click="D20" id="dado" class="white--text">Rolar D20</v-btn>
      <br><br>
      <v-img id="d20" src="../assets/dices/d20-icon.png" 
      width="100"
      style="cursor: pointer;" data-type="20"
      @click="D20"></v-img>
      <br>
      <p style="font-size: 18px; font-style: italic;">Resultado: {{ vinte }}</p> 
      </span>
  </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'dados',
  data() {
    return {
      titulo: "Rolar de Dados Online",
      quatro: '',
      seis: '',
      oito:'',
      dez:'',
      doze:'',
      vinte:'',
      
    };
  },
  methods: {
    D4() {
      this.quatro = Math.floor(Math.random()*4+1);
    },
    D6() {
      this.seis = Math.floor(Math.random()*6+1);
    },
    D8() {
      this.oito = Math.floor(Math.random()*8+1);
    },
    D10() {
      this.dez = Math.floor(Math.random()*10+1);
    },
    D12() {
      this.doze = Math.floor(Math.random()*12+1);
    },
    D20() {
      this.vinte = Math.floor(Math.random()*20+1);
    },
  },
};
</script>

<style>
  .grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-gap: 20px;
}
#dado{
    margin: 0 auto;
}
 #titulo {
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }

</style>