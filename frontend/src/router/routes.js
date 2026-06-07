import { useAuthStore } from 'src/stores/auth-store'

const authGuard = async () => {

  const authStore = useAuthStore()

  if (!authStore.user) {

    await authStore.getAuthenticatedUser()
  }

  if (!authStore.isAuthenticated) {

    return '/login'
  }
}

const routes = [

  {
    path: '/login',
    component: () => import('pages/auth/LoginPage.vue')
  },

  {
    path: '/register',
    component: () => import('pages/auth/RegisterPage.vue')
  },

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),

    beforeEnter: authGuard,

    children: [

      {
        path: 'dashboard',
        component: () =>
          import('pages/dashboard/DashboardPage.vue')
      },

      {
        path: 'products',
        component: () =>
          import('pages/products/ProductsPage.vue')
      },

      {
        path: 'customers',
        component: () =>
          import('pages/customers/CustomersPage.vue')
      },

      {
        path: 'suppliers',
        component: () =>
          import('pages/suppliers/SuppliersPage.vue')
      },

      {
        path: 'invoices',
        component: () =>
          import('pages/invoices/InvoicesPage.vue')
      },

      {
        path: 'analytics',
        component: () =>
          import('pages/analytics/AnalyticsPage.vue')
      },
      {
  path: 'purchase-orders',
  component: () =>
    import(
      'pages/purchase-orders/PurchaseOrdersPage.vue'
    )
},{
  path: 'inventory',
  component: () =>
    import(
      'pages/inventory/InventoryPage.vue'
    )
},
{
  path: 'purchase-orders/:id',
  component: () =>
    import(
      'pages/purchase-orders/PurchaseOrderDetailsPage.vue'
    )
},
{
  path: 'invoice-summary/:id',
  component: () =>
    import(
      'pages/invoices/InvoiceSummaryPage.vue'
    )
},

    ]
  },

  {
    path: '/:catchAll(.*)*',
    component: () =>
      import('pages/ErrorNotFound.vue')
  }

]

export default routes