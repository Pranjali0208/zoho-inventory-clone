<template>
  <q-page class="q-pa-md">
    <div class="row items-center justify-between q-mb-md">
      <div class="text-h4">Products</div>

      <q-btn color="primary" label="Add Product" />
    </div>

    <q-table title="Products" :rows="products" :columns="columns" row-key="id" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const products = ref([])

const columns = [
  {
    name: 'name',
    label: 'Product',
    field: 'name',
  },

  {
    name: 'category',
    label: 'Category',
    field: 'category',
  },

  {
    name: 'unit_price',
    label: 'Price',
    field: 'unit_price',
  },

  {
    name: 'stock_qty',
    label: 'Stock',
    field: 'stock_qty',
  },
]

const loadProducts = async () => {
  const response = await axios.get('/api/products', {
    withCredentials: true,
  })

  products.value = response.data.data
}

onMounted(() => {
  loadProducts()
})
</script>
