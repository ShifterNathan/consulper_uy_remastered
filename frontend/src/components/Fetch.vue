<script setup>
import useFetchServices from '../services/services-api.js';
const { isLoading, error, data } = useFetchServices();
</script>

<template>
  <div>
    <h1>Our Services</h1>

    <div v-if="isLoading">Loading services...</div>

    <div v-else-if="error">
      <p>Error loading services: {{ error.message }}</p>
    </div>

    <div v-else>
      <div v-if="data && data.length" class="services-container">
        <div v-for="service in data" :key="service.slug" class="service-card">
          <img :src="service.get_image" :alt="service.service_name" class="service-image" />
          <h2>{{ service.service_name }}</h2>
          <p>{{ service.description }}</p>
          <a :href="service.get_absolute_url">Learn more</a>
        </div>
      </div>
      <div v-else>
        <p>No services available at the moment.</p>
      </div>
    </div>
  </div>
</template>


<style scoped>
.services-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.service-card {
  border: 1px solid #ddd;
  padding: 15px;
  width: 300px;
  text-align: center;
}

.service-image {
  max-width: 100%;
  height: auto;
}
</style>