<script setup lang="ts">
const { loadConversa, createNewConversa, deleteConversa, currentConversaId } = useSupraIA()

const conversas = ref<any[]>([])
const isLoading = ref(false)

const fetchConversas = async () => {
  isLoading.value = true
  try {
    const response = await $fetch('/api/chat')
    conversas.value = response.data || []
  } catch (error) {
    console.error('Erro ao carregar conversas:', error)
  } finally {
    isLoading.value = false
  }
}

const handleLoadConversa = async (id: string) => {
  await loadConversa(id)
}

const handleDeleteConversa = async (id: string) => {
  if (confirm('Deseja realmente excluir esta conversa?')) {
    await deleteConversa(id)
    await fetchConversas()
  }
}

const handleNewConversa = () => {
  createNewConversa()
}

onMounted(() => {
  fetchConversas()
})
</script>

<template>
  <aside class="w-80 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 flex flex-col shadow-xl">
    
    <div class="p-4 border-b border-gray-200 dark:border-gray-700">
      <UButton
        icon="i-heroicons-plus"
        label="Nova Conversa"
        color="brand"
        variant="solid"
        block
        @click="handleNewConversa"
        class="mb-3 bg-gradient-to-r from-brand-600 to-brand-500 hover:from-brand-700 hover:to-brand-600"
      />
      
      <div class="flex items-center justify-between">
        <h3 class="text-sm font-bold text-gray-700 dark:text-gray-300 uppercase tracking-wider">
           Histórico
        </h3>
        <UButton
          icon="i-heroicons-arrow-path"
          size="xs"
          color="gray"
          variant="ghost"
          @click="fetchConversas"
          :loading="isLoading"
        />
      </div>
    </div>

    <div class="flex-1 overflow-y-auto p-3 space-y-2">
      
      <div v-if="isLoading" class="flex justify-center py-8">
        <UIcon name="i-heroicons-arrow-path" class="w-6 h-6 animate-spin text-brand-500" />
      </div>

      <div v-else-if="conversas.length === 0" class="text-center py-8 text-gray-500 dark:text-gray-400 text-sm">
        <UIcon name="i-heroicons-chat-bubble-left-ellipsis" class="w-12 h-12 mx-auto mb-2 opacity-30" />
        <p>Nenhuma conversa ainda</p>
      </div>

      <div
        v-else
        v-for="conversa in conversas"
        :key="conversa.id"
        class="group relative p-3 rounded-xl border transition-all duration-200 cursor-pointer hover:shadow-md"
        :class="[
          currentConversaId === conversa.id
            ? 'bg-brand-50 dark:bg-brand-900/20 border-brand-300 dark:border-brand-700'
            : 'bg-gray-50 dark:bg-gray-700/50 border-gray-200 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700'
        ]"
        @click="handleLoadConversa(conversa.id)"
      >
        <div class="flex items-start justify-between gap-2">
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-gray-800 dark:text-gray-200 truncate">
              {{ conversa.titulo }}
            </p>
            <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
              {{ new Date(conversa.firstMessage?.timestamp).toLocaleDateString('pt-BR') }}
            </p>
          </div>
          
          <UButton
            icon="i-heroicons-trash"
            size="xs"
            color="red"
            variant="ghost"
            @click.stop="handleDeleteConversa(conversa.id)"
            class="opacity-0 group-hover:opacity-100 transition-opacity"
          />
        </div>
      </div>
    </div>

    <div class="p-4 border-t border-gray-200 dark:border-gray-700 text-center">
      <p class="text-xs text-gray-500 dark:text-gray-400">
        {{ conversas.length }} conversa(s) ativa(s)
      </p>
    </div>
  </aside>
</template>