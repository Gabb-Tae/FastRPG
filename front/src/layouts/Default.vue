<template>
  <v-app>
    <v-app-bar app color="#8b0292" dark elevation="1">
      <v-app-bar-nav-icon @click.stop="sidebar = !sidebar"></v-app-bar-nav-icon>
      <v-img
        max-height="120"
        max-width="120"
        src="../assets/images/logo-rpg.png"
      ></v-img>
      <v-spacer></v-spacer>
          <v-icon @click="logadoOuNao">mdi-account</v-icon>
         
    </v-app-bar>
    <v-navigation-drawer app v-model="sidebar" :mini-variant.sync="mini">
      <v-list dense color="#8b0292" dark>
        <v-list-item>
          <v-list-item-action>
            <v-icon class="px=2" @click.stop="sidebar = !sidebar"
              >mdi-chevron-left</v-icon
            >
          </v-list-item-action>
          <v-list-item-title>
            <h3>FastRPG</h3>
          </v-list-item-title>
        </v-list-item>
      </v-list>
      <v-list-item @click="mini = !mini">
        <v-list-item-avatar>
          <v-icon>mdi-account</v-icon>
        </v-list-item-avatar>
        <v-list-item-content>{{nome + " " + sobrenome}}</v-list-item-content>
        <v-btn icon small><v-icon>mdi-chevron-left</v-icon></v-btn>
      </v-list-item>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-for="item of items"
          v-bind:key="item.title"
          link
          :to="item.to"
        >
          <v-list>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list>
          <v-list-item-content>{{ item.title }}</v-list-item-content>
        </v-list-item>
        <v-list-item @click="logout"><p><v-icon>mdi-exit-to-app</v-icon>Sair</p></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main><router-view> </router-view></v-main>
    <v-footer app class="py-3">
      <span class="caption"
        >FastRPG &copy;2022 <br />
        Equipe : Gabriel da Maia Leandro, Beatriz
        Cristina de Arruda, Guinnever Correa.</span
      ></v-footer
    >
  </v-app>
</template>

<script>
import * as fb from '@/plugins/firebase'
export default {
  data() {
    return {
      nome: '',
      sobrenome: '',
      uid: '',
      sidebar: true,
      mini: false,
      items: [
        { title: "Home", icon:"mdi-script-text", to:"/"},
        { title:"Ficha", icon:"mdi-dice-d20",to:"/ficha"},
        { title:"Arquivo de Fichas", icon:"mdi-bookshelf",to:"/lista"},
        { title: "Classes", icon:"mdi-anvil",to:"/classes"},
        { title: "Raças", icon:"mdi-gnome",to:"/racas"},
        { title: "Dados", icon:"mdi-dice-multiple",to:"/dados"},
        { title: "Conversor", icon:"mdi-bitcoin",to:"/Conversor"},
        { title: "Perfil", icon:"mdi-account-cog", to:"/perfil"},
        //{ title: "Sair", icon:"mdi-exit-to-app", to:"/login"}
      
      ],
    }
  },
  methods: {
    async buscarPerfilDoServidor() {
      this.uid = fb.auth.currentUser.uid;
      const lognome = await fb.profileCollection.where("uid", "==", this.uid).get();
      this.nome = "";
      this.sobrenome = "";
      for (const doc of lognome.docs){
        this.nome = doc.data().nome
        this.sobrenome = doc.data().sobrenome
      }
    },
    logadoOuNao(){
      if(this.uid){
        this.$router.push({path: "/perfil"})
      }else{
        this.$router.push({path: "/login"})
      }
    },
    async logout(){
      try{
        await fb.auth.signOut()
        this.$router.push({path:"/login"})
      }catch(error){
        console.log(error)
      }
    }
  }, 
  mounted() {
    this.uid = fb.auth.currentUser.uid;
    this.buscarPerfilDoServidor();
  }
}
</script>

<style>
</style>