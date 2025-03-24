<script setup lang="ts">
import Layout from "./components/Layout.vue"
</script>

<template>
  <Layout>
    <div id="app">
      <router-view></router-view> <!-- 这里用于显示当前路由匹配的组件 -->
    </div>
  </Layout>
</template>

<style>
/* 你可以在这里设置全局样式 */
</style>
