import Vue from 'vue'
import VueRouter from 'vue-router'
import { auth } from '../plugins/firebase'
///import { component } from 'vue/types/umd'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/Default'),
    meta: {
      // requiresAuth: true
    },
    children: [
      {
        path: '',
        name: 'Home',
        component: Home
      },
      {
        path: '/perfil',
        name: 'Perfil',
        component: () => import(/* webpackChunkName: "Perfil" */ '../views/Perfil.vue')
      },
      {
        path: '/ficha',
        name: 'Ficha',
        component: () => import(/* webpackChunkName: "Ficha" */ '../views/Ficha.vue')
      },
      {
        path: '/classes',
        name: 'Classes',
        component: () => import(/* webpackChunkName: "Classes" */ '../views/Classes.vue')
      },
      {
        path: '/racas',
        name: 'Raças',
        component: () => import(/* webpackChunkName: "racas" */ '../views/racas.vue')
      },
      {
        path: '/dados',
        name: 'Dados',
        component: () => import(/* webpackChunkName: "Dados" */ '../views/Dados.vue')
      },{
        path: '/Conversor',
        name: 'Conversor',
        component: () => import(/* webpackChunkName: "Conversor" */ '../views/Conversor.vue')
      },
      {
        path: '/lista',
        name: 'Lista',
        component: () => import(/* webpackChunkName: "lista" */ '../views/lista.vue')
      },
    ]
  },
  {
    path: '/',
    component: () => import('@/layouts/Blank'),
    children: [{
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
    }]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach(( to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth)

  if(requiresAuth && !auth.currentUser){
    next('/login')
  }else {next()}
})


export default router
