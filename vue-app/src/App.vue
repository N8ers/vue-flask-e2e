<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const isLoading = ref(true);
const helloMessage = ref("");
const dataResponse = ref([]);
const baseUrl = "http://127.0.0.1:5000";

const getData = async () => {
  const response = await axios({
    method: "GET",
    url: "/data",
    baseURL: baseUrl,
    mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.statusText !== "OK") {
    console.log("ERROR ", response);
  } else {
    dataResponse.value = response.data.data;
  }
};

onMounted(async () => {
  isLoading.value = true;
  const response = await axios({
    method: "GET",
    url: "/hello",
    baseURL: baseUrl,
    mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.statusText !== "OK") {
    console.log("ERROR ", response);
  } else {
    helloMessage.value = response.data;
  }
  isLoading.value = false;
});
</script>

<template>
  <div>
    <h1>Vue-Flask-e2e Test!!!</h1>
    <div data-cy="data">
      <div v-if="isLoading">Loading Data...</div>
      <div v-else>Data: {{ helloMessage }}</div>
    </div>
    <hr />
    <div>
      <button @click="getData">???</button>
      <div v-if="dataResponse.length">
        <ul v-for="data in dataResponse" :key="data.name">
          <li>{{ data.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style>
@import "@/assets/base.css";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  font-weight: normal;
}
</style>
