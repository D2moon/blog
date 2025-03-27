<!-- filepath: d:\Projects\blog\frontend\src\components\layout.vue -->
<template>
  <div class="layout">
    <!-- ✅ 统一的导航栏 -->
    <nav class="navbar">
      <h1 class="nav-title">Dream to Moon</h1>
      <div class="nav-container">
        <router-link to="/" class="nav-link">主页</router-link>
        <router-link to="/about" class="nav-link">关于我</router-link>
        <router-link to="/contact" class="nav-link">联系我们</router-link>
      </div>
    </nav>

    <!-- ✅ 主要内容区域 -->
    <div class="content">
      <router-view></router-view>
    </div>

    <div class="footer">
      <p>© 2025 Dream to Moon | 版权所有</p>
    </div>
  </div>
</template>

<style scoped>
.nav-title {
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 10px; /* 添加一些间距 */
  margin-top: 0; /* 确保标题没有顶部间距 */
}

/* ✅ 让 layout 始终填充整个屏幕 */
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /*🚀 确保 Layout 至少和屏幕一样高 */
}

.navbar {
  width: 100%;
  padding: 5px 20px; /* 减小顶部和底部的空白 */
  display: flex;
  flex-direction: column; /* 使标题和导航链接垂直排列 */
  align-items: flex-start; /* 确保标题和导航链接左对齐 */
}

.nav-container {
  display: flex;
  gap: 15px; /* 添加间距 */
}

/* ✅ 导航链接样式 */
.nav-link {
  text-decoration: none;
  color: rgb(67, 67, 245); /* 默认蓝色 */
  font-size: 18px;
  font-weight: bold;
  transition: color 0.3s ease-in-out;
}

/* ✅ 悬停变黑 */
.nav-link:hover {
  color: black;
}

/* ✅ 让内容区域占屏幕一半宽度 */
.content {
  width: 50vw; /* 占据屏幕的一半宽度 */
  max-width: 800px; /* 最大宽度 */
  margin: 10px auto; /* 居中 */
  padding: 20px;
  text-align: left; /* 文本左对齐 */
}
</style>