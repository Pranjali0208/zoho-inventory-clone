<template>
  <q-page class="q-pa-md">
    <div class="text-h4 text-weight-bold q-mb-lg">Dashboard</div>

    <div class="row q-col-gutter-md">
      <div class="col-12 col-md-3">
        <q-card>
          <q-card-section>
            <div class="text-grey">Products</div>

            <div class="text-h4">
              {{ dashboard.total_products }}
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-12 col-md-3">
        <q-card>
          <q-card-section>
            <div class="text-grey">Customers</div>

            <div class="text-h4">
              {{ dashboard.total_customers }}
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-12 col-md-3">
        <q-card>
          <q-card-section>
            <div class="text-grey">Invoices</div>

            <div class="text-h4">
              {{ dashboard.total_invoices }}
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-12 col-md-3">
        <q-card>
          <q-card-section>
            <div class="text-grey">Revenue</div>

            <div class="text-h4">OMR {{ dashboard.total_revenue }}</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const dashboard = ref({})

const loadDashboard = async () => {
  const response = await axios.get('/api/dashboard/summary', {
    withCredentials: true,
  })

  dashboard.value = response.data
}

onMounted(() => {
  loadDashboard()
})
</script>
