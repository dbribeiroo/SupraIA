<template>
  <div class="container mx-auto max-w-4xl px-4 py-8 flex flex-col h-screen">
      <!-- Header -->
      <header class="flex items-center justify-center gap-4 mb-6">
        <img src="/logosupra.png" alt="Supra AI" class="h-12" />
        <h1 class="text-3xl font-bold text-white">Supra AI</h1>
      </header>

      <!-- Chat Messages -->
      <div class="flex-1 overflow-y-auto bg-slate-800/50 rounded-2xl p-4 mb-4 backdrop-blur-sm">
        <div v-if="messages.length === 0" class="flex flex-col items-center justify-center h-full text-slate-400">
          <img src="/bonecosupra.png" alt="Supra" class="w-32 h-32 mb-4 opacity-50" />
          <p class="text-lg">Como posso ajudar?</p>
        </div>

        <div v-else class="space-y-4">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            :class="[
              'flex',
              msg.role === 'user' ? 'justify-end' : 'justify-start'
            ]"
          >
            <div
              :class="[
                'max-w-[80%] px-4 py-3 rounded-2xl',
                msg.role === 'user'
                  ? 'bg-purple-600 text-white rounded-br-sm'
                  : 'bg-slate-700 text-slate-100 rounded-bl-sm'
              ]"
            >
              <p class="whitespace-pre-wrap">{{ msg.content }}</p>
            </div>
          </div>

          <div v-if="isLoading" class="flex justify-start">
            <div class="bg-slate-700 text-slate-100 px-4 py-3 rounded-2xl rounded-bl-sm">
              <div class="flex gap-1">
                <span class="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
                <span class="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
                <span class="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="bg-slate-800/50 rounded-2xl p-4 backdrop-blur-sm">
        <form @submit.prevent="sendMessage" class="flex gap-3">
          <input
            v-model="currentInput"
            type="text"
            placeholder="Digite sua mensagem..."
            class="flex-1 bg-slate-700 text-white placeholder-slate-400 px-4 py-3 rounded-xl border border-slate-600 focus:border-purple-500 focus:outline-none transition-colors"
            :disabled="isLoading"
          />
          <button
            type="submit"
            :disabled="isLoading || !currentInput.trim()"
            class="bg-purple-600 hover:bg-purple-700 disabled:bg-slate-600 disabled:cursor-not-allowed text-white px-6 py-3 rounded-xl font-medium transition-colors"
          >
            Enviar
          </button>
        </form>
      </div>
  </div>
</template>

<script setup lang="ts">
import { useSupraIA } from '../composables/useSupraIA';

const { messages, currentInput, isLoading, sendMessage } = useSupraIA();
</script>
