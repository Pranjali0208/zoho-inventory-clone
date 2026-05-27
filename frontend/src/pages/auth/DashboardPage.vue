<template>
  <div class="dashboard-page">
    <q-card class="dashboard-card">
      <div class="text-h4 text-weight-bold">FleetFlow Dashboard</div>

      <div class="q-mt-md">
        Welcome,
        {{ authStore.user?.name }}
      </div>

      <div class="q-mt-sm">
        Role:
        {{ authStore.user?.role }}
      </div>

      <q-btn label="Logout" color="negative" class="q-mt-lg" @click="logout" />
    </q-card>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

import { useAuthStore } from 'src/stores/auth-store'

const router = useRouter()

const authStore = useAuthStore()

const logout = () => {
  authStore.logout()

  router.push('/login')
}
</script>

<style scoped>
.dashboard-page {
  height: 100vh;

  display: flex;

  justify-content: center;

  align-items: center;

  background: #f4f7fe;
}

.dashboard-card {
  width: 500px;

  padding: 30px;

  border-radius: 12px;
}
</style>
