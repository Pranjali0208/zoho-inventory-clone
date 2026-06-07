<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-md">Customers</div>

    <q-table :rows="customers" :columns="columns" row-key="id" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const customers = ref([])

const columns = [
  {
    name: 'name',
    label: 'Name',
    field: 'name',
  },

  {
    name: 'email',
    label: 'Email',
    field: 'email',
  },

  {
    name: 'phone',
    label: 'Phone',
    field: 'phone',
  },
]

const loadCustomers = async () => {
  const response = await axios.get('/api/customers', {
    withCredentials: true,
  })

  customers.value = response.data.data
}

onMounted(() => {
  loadCustomers()
})
</script>
