<template>
  <div class="register-page">
    <q-card class="register-card">
      <q-card-section>
        <div class="text-h5 text-center text-weight-bold">FleetFlow Register</div>

        <div class="text-caption text-center q-mt-sm">Create Your Account</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="form.name" label="Full Name" outlined class="q-mb-md" />

        <q-input v-model="form.email" label="Email" outlined class="q-mb-md" />

        <q-input
          v-model="form.password"
          label="Password"
          type="password"
          outlined
          class="q-mb-md"
        />

        <q-select v-model="form.role" :options="roles" label="Role" outlined />
      </q-card-section>

      <q-card-actions align="center">
        <q-btn label="Register" color="primary" class="full-width" @click="register" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

import axios from 'axios'

const roles = ['admin', 'manager', 'driver']

const form = reactive({
  name: '',

  email: '',

  password: '',

  role: 'manager',
})

const register = async () => {
  try {
    const response = await axios.post(
      '/api/auth/register',

      form,
    )

    console.log(response.data)
  } catch (error) {
    console.log(error)
  }
}
</script>

<style scoped>
.register-page {
  height: 100vh;

  display: flex;

  justify-content: center;

  align-items: center;

  background: #f4f7fe;
}

.register-card {
  width: 450px;

  padding: 20px;

  border-radius: 12px;
}
</style>
