export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',

  future: {
    compatibilityVersion: 4,
  },

  modules: ['@nuxt/ui'],

  css: ['~/assets/css/main.css'],

  devtools: { enabled: true },

  runtimeConfig: {
    openaiKey: '',
  },

  vite: {
    server: {
      watch: {
        usePolling: true,
      },
      hmr: {
        port: 3000,
        clientPort: 3001,
      },
    },
  },
})