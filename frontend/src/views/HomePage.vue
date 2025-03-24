<!-- filepath: d:\Projects\blog\frontend\src\views\HomePage.vue -->
<template>
  <div class="homepage">
    <!-- 顶部导航 -->
    <header>
      <nav>
        <ul>
          <li><a href="/">主页</a></li>
          <li><a href="/about">关于我</a></li>
          <li><a href="/contact">联系我们</a></li>
        </ul>
      </nav>
    </header>

    <!-- 博客介绍部分 -->
    <section class="intro">
      <h1>欢迎来到我的博客</h1>
      <p>在这里，我将分享我对编程、技术、生活的思考和探索。</p>
    </section>

    <!-- 文章列表 -->
    <section class="posts">
      <h2>最新文章</h2>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <a :href="'/post/' + post.id">{{ post.title }}</a>
          <p>{{ post.excerpt }}</p>
        </li>
      </ul>
    </section>

    <!-- 页脚 -->
    <footer>
      <p>© 2025 我的博客 | 版权所有</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 模拟从 API 获取文章数据
const posts = ref([
  { id: 1, title: '我的第一篇博客', excerpt: '这是一篇关于我如何开始写博客的文章。' },
  { id: 2, title: 'Vue 3 入门教程', excerpt: 'Vue 3 是一个非常强大的前端框架，本文将教你如何快速上手。' },
  { id: 3, title: 'Flask 后端开发', excerpt: 'Flask 是一个轻量级的 Python 框架，本文将带你走进 Flask 的世界。' },
])
</script>

<style scoped>
/* 全局样式 */
body {
  font-family: 'ZCOOL KuaiLe', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f9;
}

/* 顶部导航 */
header {
  /* 去掉背景颜色 */
  color: black; /* 将文字颜色换成黑色 */
  padding: 10px 0;
}

header nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

header nav ul li {
  margin: 0 15px;
}

header nav ul li a {
  color: black; /* 将文字颜色换成黑色 */
  text-decoration: none;
  font-weight: bold;
}

/* 博客介绍部分 */
.intro {
  text-align: center;
  padding: 50px 0;
  background-color: #e0f7fa;
}

.intro h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

.intro p {
  font-size: 18px;
}

/* 文章列表 */
.posts {
  padding: 20px;
}

.posts h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.posts ul {
  list-style: none;
  padding: 0;
}

.posts ul li {
  margin-bottom: 20px;
}

.posts ul li a {
  font-size: 22px;
  text-decoration: none;
  color: #333;
}

.posts ul li p {
  font-size: 16px;
  color: #666;
}

/* 页脚 */
footer {
  text-align: center;
  padding: 20px;
  background-color: #333;
  color: white;
}
</style>