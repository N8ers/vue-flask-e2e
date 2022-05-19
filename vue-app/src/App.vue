<script setup>
import { ref, onMounted } from "vue";

const isLoading = ref(true);

const getPunchLine = () => {
  console.log("I will make a network request to the falsk api: '/punch-line'");
};

onMounted(() => {
  console.log("I will make a network request to the flask api '/data'");
});
</script>

<template>
  <div>
    <h1>Vue-Flask-e2e Test!!!</h1>
    <div v-if="isLoading">Loading Data...</div>
    <hr />
    <div>
      <h3>What did the chicken say to the farmer?</h3>
      <button @click="getPunchLine">???</button>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
