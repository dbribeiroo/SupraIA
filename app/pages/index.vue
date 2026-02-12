<script setup lang="ts">
const { messages, sendMessage, currentInput, isLoading, clearMessages } = useSupraIA()
const chatContainer = ref<HTMLElement | null>(null)
const showSidebar = ref(true)

watch(messages.value, async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTo({
      top: chatContainer.value.scrollHeight,
      behavior: 'smooth'
    })
  }
})

const toggleSidebar = () => {
  showSidebar.value = !showSidebar.value
}
</script>

<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900 font-sans overflow-hidden">
    
    <Transition name="slide">
      <HistoricoSidebar v-if="showSidebar" />
    </Transition>

    <div class="flex flex-col flex-1 relative overflow-hidden">
      
      <div class="absolute inset-0 opacity-[0.03] pointer-events-none">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,_#f97316_1px,transparent_1px)] [background-size:24px_24px] animate-pulse"></div>
      </div>

      <header class="relative bg-gradient-to-r from-brand-600 via-brand-500 to-orange-500 text-white p-4 shadow-2xl z-20">
        <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent"></div>
        
        <div class="relative flex items-center justify-between">
          <div class="flex items-center gap-2">
            <button
              @click="toggleSidebar"
              class="p-2.5 hover:bg-white/10 rounded-xl transition-all duration-300 hover:scale-110 active:scale-95 backdrop-blur-sm"
              title="Toggle History"
            >
              <UIcon 
                :name="showSidebar ? 'i-heroicons-bars-3-bottom-left' : 'i-heroicons-bars-3'" 
                class="w-6 h-6" 
              />
            </button>
            
            <BotaoLimpar />
          </div>

          <div class="flex items-center gap-3">
            <AvatarSupra />
          </div>

          <img 
            src="/logosupra.png" 
            alt="Supranet" 
            class="h-8 brightness-0 invert opacity-90 hover:opacity-100 transition-all duration-300 hover:scale-110" 
          />
        </div>
      </header>

      <main ref="chatContainer" class="flex-1 overflow-y-auto p-6 space-y-6 relative z-10 scroll-smooth">
        
        <div v-if="messages.length === 0" class="flex flex-col items-center justify-center h-full text-center animate-fade-in">
          <div class="w-24 h-24 bg-gradient-to-br from-brand-500 to-orange-500 rounded-3xl flex items-center justify-center mb-6 shadow-2xl animate-bounce-slow">
            <UIcon name="i-heroicons-sparkles" class="w-12 h-12 text-white" />
          </div>
          <h2 class="text-3xl font-bold text-gray-800 dark:text-white mb-3">
            Olá! Sou o Supra 👋
          </h2>
          <p class="text-gray-600 dark:text-gray-400 max-w-md">
            Seu assistente inteligente da Supranet. Como posso ajudar você hoje?
          </p>
          <div class="flex gap-3 mt-8">
            <div class="px-4 py-2 bg-brand-50 dark:bg-brand-900/20 rounded-full text-sm text-brand-600 dark:text-brand-400 border border-brand-200 dark:border-brand-700">
              💡 Velocidade da internet
            </div>
            <div class="px-4 py-2 bg-brand-50 dark:bg-brand-900/20 rounded-full text-sm text-brand-600 dark:text-brand-400 border border-brand-200 dark:border-brand-700">
              📡 Problemas de Wi-Fi
            </div>
          </div>
        </div>

        <div v-if="messages.length > 0" class="flex justify-center my-6 opacity-0 animate-fade-in" style="animation-delay: 0.2s; animation-fill-mode: forwards;">
          <span class="bg-white/80 dark:bg-gray-800/80 text-gray-600 dark:text-gray-400 text-xs px-5 py-2 rounded-full shadow-lg backdrop-blur-md border border-gray-200 dark:border-gray-700 font-medium">
            📅 Hoje
          </span>
        </div>

        <div 
          v-for="(msg, index) in messages" 
          :key="index"
          class="flex w-full items-end gap-3 animate-slide-up"
          :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
        >
         <UAvatar 
            v-if="msg.role === 'assistant'"
            src="/headsupra.png"
            size="sm"
            class="mb-1 border-2 border-white dark:border-gray-700 bg-white shadow-lg ring-2 ring-brand-100 dark:ring-brand-900/30"
          />

          <div 
            class="relative p-4 max-w-[75%] shadow-lg text-sm md:text-base transition-all duration-300 hover:shadow-xl cursor-default group"
            :class="[
              msg.role === 'user' 
                ? 'bg-gradient-to-br from-brand-600 to-brand-500 text-white rounded-2xl rounded-tr-md hover:from-brand-700 hover:to-brand-600' 
                : 'bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 rounded-2xl rounded-tl-md border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-750'
            ]"
          >
            <p v-if="msg.role === 'assistant'" class="text-[10px] font-bold text-brand-600 dark:text-brand-400 mb-2 uppercase tracking-wider flex items-center gap-1.5">
              <UIcon name="i-heroicons-sparkles" class="w-3.5 h-3.5" />
              Supra AI
            </p>
            
            <p class="whitespace-pre-wrap leading-relaxed">{{ msg.content }}</p>
            
            <span 
              class="text-[10px] block text-right mt-2 opacity-60 font-medium" 
              :class="msg.role === 'user' ? 'text-orange-100' : 'text-gray-500 dark:text-gray-400'"
            >
              {{ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) }}
            </span>

            <div 
              v-if="msg.role === 'user'"
              class="absolute -bottom-1 -right-1 w-4 h-4 bg-brand-500 rounded-full opacity-20"
            ></div>
          </div>
        </div>

        <div v-if="isLoading" class="flex justify-start items-end gap-3 animate-slide-up">
          <UAvatar
            src="/headsupra.png" 
            size="sm" 
            class="mb-1 opacity-70 border-2 border-white dark:border-gray-700 shadow-lg" 
            :ui="{ img: 'object-contain h-full w-full' }"     
          />
          <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl rounded-tl-md border border-gray-100 dark:border-gray-700 flex gap-2 items-center shadow-lg">
            <span class="w-2 h-2 bg-brand-500 rounded-full animate-bounce"></span>
            <span class="w-2 h-2 bg-brand-500 rounded-full animate-bounce" style="animation-delay: 0.1s"></span>
            <span class="w-2 h-2 bg-brand-500 rounded-full animate-bounce" style="animation-delay: 0.2s"></span>
          </div>
        </div>
      </main>

      <footer class="relative bg-white/90 dark:bg-gray-900/90 backdrop-blur-xl p-6 border-t border-gray-200 dark:border-gray-800 z-20 shadow-2xl">
        <form @submit.prevent="sendMessage" class="max-w-4xl mx-auto flex gap-3 items-end">

          <UInput
            v-model="currentInput"
            placeholder="Digite sua mensagem..."
            size="xl"
            :disabled="isLoading"
            class="flex-1 transition-all duration-300"
            :ui="{
              rounded: 'rounded-2xl',
              color: { 
                gray: { 
                  outline: 'bg-gray-50 dark:bg-gray-800 shadow-inner border-gray-200 dark:border-gray-700 focus:border-brand-500 dark:focus:border-brand-400' 
                } 
              }
            }"
            variant="outline"
            autofocus
          >
            <template #leading>
              <UIcon name="i-heroicons-chat-bubble-left-ellipsis" class="text-brand-500 dark:text-brand-400" />
            </template>
          </UInput>

          <UButton 
            type="submit"
            icon="i-heroicons-paper-airplane"
            size="xl"
            :disabled="!currentInput.trim() || isLoading"
            :loading="isLoading"
            color="brand" 
            variant="solid"
            class="rounded-2xl w-14 h-14 flex items-center justify-center transition-all duration-300 hover:scale-110 hover:rotate-6 shadow-lg hover:shadow-brand-300/50 hover:shadow-2xl active:scale-95 bg-gradient-to-r from-brand-600 to-brand-500"
          />
          
        </form>
        
        <div class="text-center mt-4 flex justify-center items-center gap-2 text-[11px] text-gray-500 dark:text-gray-400">
          <UIcon name="i-heroicons-lock-closed" class="w-3.5 h-3.5 text-brand-500" />
          <span class="font-medium">Ambiente Seguro</span>
          <span class="text-gray-300 dark:text-gray-600">•</span>
          <span>TI Supranet</span>
        </div>
      </footer>
    </div>
  </div>
</template>

<style scoped>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-fade-in {
  animation: fade-in 0.5s ease-out;
}

.animate-slide-up {
  animation: slide-up 0.4s ease-out;
}

.animate-bounce-slow {
  animation: bounce-slow 2s ease-in-out infinite;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-enter-from {
  transform: translateX(-100%);
}

.slide-leave-to {
  transform: translateX(-100%);
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: #f97316;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #ea580c;
}
</style>
