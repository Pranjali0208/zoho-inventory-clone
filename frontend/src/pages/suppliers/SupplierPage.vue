<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-md">Suppliers</div>

    <q-table :rows="suppliers" :columns="columns" row-key="id" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const suppliers = ref([])

const columns = [
  {
    name: 'name',
    label: 'Supplier',
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

const loadSuppliers = async () => {
  const response = await axios.get('/api/suppliers', {
    withCredentials: true,
  })

  suppliers.value = response.data.data
}

onMounted(() => {
  loadSuppliers()
})
</script>
