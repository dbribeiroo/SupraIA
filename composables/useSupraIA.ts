import { useState } from "nuxt/app"

export const useSupraIA = () => {
    const messages = useState<any[]>('chat-messages', () => []);
    const currentInput = useState<string>('chat-input', () => '');
    const isLoading = useState<boolean>('chat-loading', () => false);
    const sendMessage = async () => {
        if (!currentInput.value.trim()) return;

    const userMsg = { role: 'user', content: currentInput.value };
    messages.value.push(userMsg);
    const textToSend = currentInput.value;
    currentInput.value = ''; 
    isLoading.value = true;

    try {
        const response = await $fetch('/api/chat', {
        method: 'POST',
        body: {
            messages: messages.value 
        }
      });

      if (response.message) {
        messages.value.push(response.message);
      }

    } catch (error) {
        messages.value.push({ 
        role: 'assistant', 
        content: 'Ops! Acabei cochilando um pouco. Tente de novo! 🔌' 
      });
    } finally {
        isLoading.value = false;
    }
  };
  return { 
    messages, 
    currentInput, 
    isLoading, 
    sendMessage 
  };
};
