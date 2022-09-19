<template>
<div class="class main-container">
  <h1>Arquivos das Fichas:</h1>
  <div id="salvos-title"> Essas são as fichas salvas: </div>
  <Dashboard />
  </div>
</template>

<script>
import Dashboard from './Dashboard.vue'
export default {
  name: "Arquivos",
  components: {
    Dashboard
  }
}
</script>

<style scoped>
#salvos-title {
   color:#222;
   padding: 5px 10px;
   border-left: 4px solid #8b0292;
 }

</style>