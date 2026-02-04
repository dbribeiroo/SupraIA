

export const useSupraIA = () => {

    const messages = useState<any[]>('chat-messages', () => []);
    const currentInput = useState<string>('chat-input', () => '');
    const isLoading = useState<boolean>('chat-loading', () => false);


    const clearMessages = () => {
        messages.value = [];
    };


    const sendMessage = async () => {
 
        if (!currentInput.value.trim()) return;


        messages.value.push({ role: 'user', content: currentInput.value });
        
      
        currentInput.value = ''; 
        isLoading.value = true;

        try {
            const response = await $fetch('/api/chat', {
                method: 'POST',
                body: { messages: messages.value }
            });

            if (response.message) {
                messages.value.push(response.message);
            }
        } catch (error) {
            messages.value.push({ 
                role: 'assistant', 
                content: 'Ops! Tive um problema de conexão. Tente de novo! 🔌' 
            });
        } finally {
            isLoading.value = false;
        }
    };

 
    return { 
        messages, 
        currentInput, 
        isLoading, 
        sendMessage,
        clearMessages 
    };
};