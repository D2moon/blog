<template>
    <div class="markdown-content" v-html="htmlContent"></div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { marked } from "marked";
  
  const htmlContent = ref(""); // 存储转换后的 HTML
  
  const loadMarkdown = async () => {
    try {
      // 假设 Markdown 文件存放在 public/posts/example.md
      const response = await fetch("/posts/example.md");
      const markdownText = await response.text();
      htmlContent.value = marked(markdownText); // 转换 Markdown 为 HTML
    } catch (error) {
      console.error("加载 Markdown 失败:", error);
    }
  };
  
  onMounted(loadMarkdown);
  </script>
  
  <style>
  /* ✅ 样式优化 */
  .markdown-content {
    max-width: 50vw;
    margin: auto;
    padding: 20px;
    line-height: 1.8;
  }
  
  .markdown-content h1 {
    font-size: 2rem;
    border-bottom: 2px solid #ddd;
    padding-bottom: 5px;
  }
  
  .markdown-content p {
    margin-bottom: 15px;
  }
  
  .markdown-content a {
    color: #007bff;
    text-decoration: none;
  }
  
  .markdown-content a:hover {
    text-decoration: underline;
  }
  </style>
  