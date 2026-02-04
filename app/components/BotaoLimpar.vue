<script setup lang="ts">
const { clearMessages } = useSupraIA();
</script>

<template>
    <UButton 
  icon="i-heroicons-trash"
  label="Limpar conversa"
  color="white"
  variant="ghost"
  size="sm"
  @click="clearMessages"
  class="transition-all duration-300 hover:bg-white/20 hover:scale-105 hover:shadow-sm active:scale-95"
  :ui="{ 
    label: 'hidden md:inline font-semibold', 
    icon: { base: 'w-5 h-5' } 
  }"
/> 
</template>