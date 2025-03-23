<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const posts = ref([]);

onMounted(async () => {
  const res = await axios.get('http://127.0.0.1:5000/api/posts');
  posts.value = res.data;
});
</script>

<template>
  <div>
    <h1>博客文章</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <router-link :to="'/post/' + post.id">
          <h2>{{ post.title }}</h2>
        </router-link>
      </li>
    </ul>
  </div>
</template>
