<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-lg">Analytics</div>

    <q-card class="q-mb-md">
      <q-card-section>
        <div class="text-h6">Revenue</div>

        <div class="text-h4">OMR {{ revenue }}</div>
      </q-card-section>
    </q-card>

    <q-card>
      <q-card-section>
        <div class="text-h6 q-mb-md">Top Products</div>

        <q-list>
          <q-item v-for="item in topProducts" :key="item.product_id">
            <q-item-section>
              {{ item.product_name }}
            </q-item-section>

            <q-item-section side>
              {{ item.quantity_sold }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const revenue = ref(0)

const topProducts = ref([])

const loadAnalytics = async () => {
  const revenueResponse = await axios.get('/api/analytics/revenue')

  revenue.value = revenueResponse.data.total_revenue

  const productResponse = await axios.get('/api/analytics/top-products')

  topProducts.value = productResponse.data.data
}

onMounted(() => {
  loadAnalytics()
})
</script>
