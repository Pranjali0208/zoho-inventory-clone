<template>
  <div class="login-page">
    <q-card class="login-card">
      <q-card-section>
        <div class="text-h5 text-center text-weight-bold">FleetFlow Login</div>

        <div class="text-caption text-center q-mt-sm">Delivery Management System</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="form.email" label="Email" outlined class="q-mb-md" />

        <q-input v-model="form.password" label="Password" type="password" outlined />
      </q-card-section>

      <q-card-actions align="center">
        <q-btn label="Login" color="primary" class="full-width" @click="login" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

import { useRouter } from 'vue-router'

import { useAuthStore } from 'src/stores/auth-store'

const authStore = useAuthStore()

const router = useRouter()

const form = reactive({
  email: '',

  password: '',
})

const login = async () => {
  try {
    await authStore.login(form)

    router.push('/dashboard')
  } catch (error) {
    console.log(error)
  }
}
</script>

<style scoped>
.login-page {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f4f7fe;
}

.login-card {
  width: 400px;
  padding: 20px;
  border-radius: 12px;
}
</style>
