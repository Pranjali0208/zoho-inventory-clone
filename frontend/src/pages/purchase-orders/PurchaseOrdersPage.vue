<template>
  <q-page class="q-pa-md">
    <div class="row items-center justify-between q-mb-md">
      <div class="text-h4">Purchase Orders</div>

      <q-btn color="primary" label="Create PO" />
    </div>

    <q-table :rows="purchaseOrders" :columns="columns" row-key="id" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const purchaseOrders = ref([])

const columns = [
  {
    name: 'po_number',
    label: 'PO Number',
    field: 'po_number',
  },

  {
    name: 'supplier',
    label: 'Supplier',
    field: 'supplier',
  },

  {
    name: 'order_date',
    label: 'Order Date',
    field: 'order_date',
  },

  {
    name: 'status',
    label: 'Status',
    field: 'status',
  },
]

const loadPurchaseOrders = async () => {
  const response = await axios.get('/api/purchase-orders', {
    withCredentials: true,
  })

  purchaseOrders.value = response.data.data
}

onMounted(() => {
  loadPurchaseOrders()
})
</script>
