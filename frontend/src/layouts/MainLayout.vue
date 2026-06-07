<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" @click="drawer = !drawer" />

        <q-toolbar-title> FleetFlow ERP </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" show-if-above bordered>
      <q-list>
        <q-item clickable to="/dashboard">
          <q-item-section avatar>
            <q-icon name="dashboard" />
          </q-item-section>

          <q-item-section> Dashboard </q-item-section>
        </q-item>

        <q-item clickable to="/products">
          <q-item-section avatar>
            <q-icon name="inventory_2" />
          </q-item-section>

          <q-item-section> Products </q-item-section>
        </q-item>

        <q-item clickable to="/customers">
          <q-item-section avatar>
            <q-icon name="groups" />
          </q-item-section>

          <q-item-section> Customers </q-item-section>
        </q-item>

        <q-item clickable to="/suppliers">
          <q-item-section avatar>
            <q-icon name="local_shipping" />
          </q-item-section>

          <q-item-section> Suppliers </q-item-section>
        </q-item>

        <q-item clickable to="/invoices">
          <q-item-section avatar>
            <q-icon name="receipt_long" />
          </q-item-section>

          <q-item-section> Invoices </q-item-section>
        </q-item>

        <q-item clickable to="/analytics">
          <q-item-section avatar>
            <q-icon name="analytics" />
          </q-item-section>

          <q-item-section> Analytics </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

const drawer = ref(true)
</script>
