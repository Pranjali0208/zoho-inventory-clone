<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-md">Invoices</div>

    <q-table :rows="invoices" :columns="columns" row-key="id" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const invoices = ref([])

const columns = [
  {
    name: 'invoice_number',
    label: 'Invoice',
    field: 'invoice_number',
  },

  {
    name: 'customer',
    label: 'Customer',
    field: 'customer',
  },

  {
    name: 'status',
    label: 'Status',
    field: 'status',
  },
]

const loadInvoices = async () => {
  const response = await axios.get('/api/invoices', {
    withCredentials: true,
  })

  invoices.value = response.data.data
}

onMounted(() => {
  loadInvoices()
})
</script>
