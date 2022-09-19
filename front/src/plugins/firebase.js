import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';


const firebaseConfig = {
    apiKey: "AIzaSyAndddyQYMOeyNhPggGYQyiU1G6p7uSsMY",
    authDomain: "gabb-todo-list-vue.firebaseapp.com",
    projectId: "gabb-todo-list-vue",
    storageBucket: "gabb-todo-list-vue.appspot.com",
    messagingSenderId: "14606819995",
    appId: "1:14606819995:web:db30539211d4cc164adc3e"
  };

firebase.initializeApp(firebaseConfig)

const db = firebase.firestore()
const auth = firebase.auth()


const profileCollection = db.collection('profile')
const taskCollection = db.collection('task')
const fichaCollection = db.collection('ficha')

export {
      db,auth,profileCollection,taskCollection,fichaCollection
  }
