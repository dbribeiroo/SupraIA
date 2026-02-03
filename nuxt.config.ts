export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',

  future: {
    compatibilityVersion: 4,
  },

  modules: ['@nuxtjs/tailwindcss'],

  devtools: { enabled: true },

  runtimeConfig: {
  
    openaiKey: '', 
  }
})