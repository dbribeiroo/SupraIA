<script setup lang="ts">
const { messages, sendMessage, currentInput, isLoading, clearMessages } = useSupraIA();
const chatContainer = ref<HTMLElement | null>(null);

watch(messages.value, async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTo({
      top: chatContainer.value.scrollHeight,
      behavior: 'smooth'
    });
  }
});


</script>

<template>
  <div class="flex flex-col h-screen bg-gray-50 dark:bg-gray-900 font-sans relative overflow-hidden">
    
    <div class="absolute inset-0 opacity-5 pointer-events-none bg-[radial-gradient(#fb923c_1px,transparent_1px)] [background-size:16px_16px]"></div>

    <header class="bg-gradient-to-r from-brand-600 to-brand-500 text-white p-4 shadow-lg flex items-center justify-between relative z-20">
 
 <BotaoLimpar />     
    
 <AvatarSupra />


      <img src="/logosupra.png" alt="Supranet" class="h-8 brightness-0 invert opacity-80 hidden md:block hover:opacity-100 transition-opacity" />
    </header>

    <main ref="chatContainer" class="flex-1 overflow-y-auto p-4 space-y-6 relative z-10 scroll-smooth">
      
      <div class="flex justify-center my-4 opacity-0 animate-fade-in" style="animation-delay: 0.2s; animation-fill-mode: forwards;">
        <span class="bg-gray-200/80 dark:bg-gray-800/80 text-gray-500 text-xs px-4 py-1.5 rounded-full shadow-sm backdrop-blur-md border border-white/50">
          Hoje
        </span>
      </div>

      <div 
        v-for="(msg, index) in messages" 
        :key="index"
        class="flex w-full items-end gap-2"
        :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
      >
        <UAvatar 
          v-if="msg.role === 'assistant'"
          src="/headsupra.png"
          size="xs"
          class="mb-1 border border-gray-200 bg-white shadow-sm"
        />

        <div 
          class="p-4 max-w-[85%] shadow-sm relative text-sm md:text-base transition-all duration-300 hover:shadow-md cursor-default"
          :class="[
            msg.role === 'user' 
              ? 'bg-brand-600 text-white rounded-2xl rounded-tr-none hover:bg-brand-700' /* Cor Usuário */
              : 'bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 rounded-2xl rounded-tl-none border border-gray-100 dark:border-gray-700 hover:bg-gray-50' /* Cor Supra */
          ]"
        >
          <p v-if="msg.role === 'assistant'" class="text-[10px] font-bold text-brand-500 mb-1 uppercase tracking-wider flex items-center gap-1">
            Supra <UIcon name="i-heroicons-sparkles" class="w-3 h-3" />
          </p>
          
          <p class="whitespace-pre-wrap leading-relaxed">{{ msg.content }}</p>
          
          <span class="text-[10px] block text-right mt-1 opacity-60" :class="msg.role === 'user' ? 'text-orange-100' : 'text-gray-400'">
            {{ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) }}
          </span>
        </div>
      </div>

      <div v-if="isLoading" class="flex justify-start items-end gap-2">
        <UAvatar
         src="/headsupra.png" 
         size="xs" 
         class="mb-1 opacity-70" 
         :ui="{ img: 'object-contain h-full w-full' }"     
      />
        <div class="bg-white dark:bg-gray-800 p-3 rounded-2xl rounded-tl-none border border-gray-100 flex gap-1 items-center h-10 shadow-sm">
          <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce"></span>
          <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce delay-75"></span>
          <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce delay-150"></span>
        </div>
      </div>
    </main>

    <footer class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-lg p-4 border-t border-gray-200 dark:border-gray-800 relative z-20">
      <form @submit.prevent="sendMessage" class="max-w-4xl mx-auto flex gap-3 items-end">
        
        <UInput
          v-model="currentInput"
          placeholder="Digite sua dúvida..."
          size="xl"
          :disabled="isLoading"
          class="flex-1 transition-all duration-300"
          :ui="{
            rounded: 'rounded-3xl',
            color: { gray: { outline: 'bg-gray-50 shadow-inner' } }
          }"
          variant="outline"
          autofocus
        >
          <template #leading>
            <UIcon name="i-heroicons-chat-bubble-left-ellipsis" class="text-gray-400" />
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
          class="rounded-full w-12 h-12 flex items-center justify-center transition-all duration-300 hover:scale-110 hover:rotate-6 hover:shadow-orange-300/50 hover:shadow-lg active:scale-95"
        />
        
      </form>
      
      <div class="text-center mt-3 flex justify-center items-center gap-1 text-[10px] text-gray-400">
        <UIcon name="i-heroicons-lock-closed" class="w-3 h-3" />
        Ambiente Seguro | TI Supranet
      </div>
    </footer>
  </div>
</template>

<style scoped>

@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>