import { createRequire } from 'node:module';
import path from 'node:path';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// semi-ui 的 exports 字段不暴露 dist/css，从入口反推包根目录，
// 这样依赖装在上级目录共享时仍然解析得到
const require = createRequire(import.meta.url);
const semiRoot = path.resolve(path.dirname(require.resolve('@douyinfe/semi-ui')), '../..');
const semiCss = path.join(semiRoot, 'dist/css/semi.min.css');

export default defineConfig({
  plugins: [react()],
  resolve: { alias: { '@semi-css': semiCss } },
  server: {
    host: '127.0.0.1',
    port: 5174,
    // 部分环境收不到 fs 事件，轮询兜底保证热更新
    watch: { usePolling: true, interval: 300 },
  },
});
