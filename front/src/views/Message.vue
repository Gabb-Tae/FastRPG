<template>
  <div class="message-container">
      {{ msg }}
  </div>
</template>

<script>
export default {
    name: "Message",
    props: {
        msg: String
    }
}
</script>

<style>
.message-container {
    color: #85007a;
    background-color: #fbccff ;
    border: 2px solid #ffbbfd;
    border-radius: 5px;
    padding: 10px;
    max-width: 400px;
    margin: 30px auto;
}

</style>