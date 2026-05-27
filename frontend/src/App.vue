<template>
  <div v-if="authStore.loading" class="loading-container">
    <q-spinner color="primary" size="50px" />
  </div>

  <router-view v-else />
</template>

<script setup>
import { onMounted } from 'vue'

import { useAuthStore } from 'src/stores/auth-store'

const authStore = useAuthStore()

onMounted(async () => {
  await authStore.getAuthenticatedUser()
})
</script>

<style scoped>
.loading-container {
  height: 100vh;

  display: flex;

  justify-content: center;

  align-items: center;
}
</style>
