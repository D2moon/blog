<template>
  <div class="layout">
    <!-- ✅ 统一的导航栏 -->
    <nav class="navbar">
      <router-link to="/" class="nav-link">主页</router-link>
      <router-link to="/about" class="nav-link">关于我</router-link>
      <router-link to="/contact" class="nav-link">联系我们</router-link>
    </nav>

    <!-- ✅ 主要内容区域 -->
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<style>
/* ✅ 移除导航栏黑框 */
.navbar {
  display: flex;
  justify-content: flex-start; /* 左对齐 */
  padding: 10px 20px;
  background-color: transparent;
  border-bottom: none;
}

/* ✅ 导航链接样式 */
.nav-link {
  text-decoration: none;
  color: blue; /* 默认蓝色 */
  font-size: 18px;
  font-weight: bold;
  margin: 0 15px;
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
  margin: 20px auto; /* 居中 */
  padding: 20px;
  text-align: left; /* 文本左对齐 */
}
</style>
