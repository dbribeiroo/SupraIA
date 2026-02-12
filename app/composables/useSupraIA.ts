export const useSupraIA = () => {
    const messages = useState<any[]>('chat-messages', () => []);
    const currentInput = useState<string>('chat-input', () => '');
    const isLoading = useState<boolean>('chat-loading', () => false);
    const currentConversaId = useState<string>('chat-conversa-id', () => `conversa:${Date.now()}`);

    const clearMessages = () => {
        messages.value = [];
    };

    const createNewConversa = () => {
        messages.value = [];
        currentConversaId.value = `conversa:${Date.now()}`;
    };

    const loadConversa = async (id: string) => {
        try {
            const response = await $fetch(`/api/chat/${id}`);
            if (response.success && response.data) {
                messages.value = response.data.mensagens || [];
                currentConversaId.value = id;
            }
        } catch (error) {
            console.error('Erro ao carregar conversa:', error);
        }
    };

    const deleteConversa = async (id: string) => {
        try {
            await $fetch(`/api/chat/${id}`, { method: 'DELETE' });
            if (currentConversaId.value === id) {
                createNewConversa();
            }
        } catch (error) {
            console.error('Erro ao deletar conversa:', error);
        }
    };

    const sendMessage = async () => {
        if (!currentInput.value.trim()) return;

        messages.value.push({ role: 'user', content: currentInput.value });
        
        const messageToSend = currentInput.value;
        currentInput.value = ''; 
        isLoading.value = true;

        try {
            const response = await $fetch('/api/chat', {
                method: 'POST',
                body: { 
                    messages: messages.value,
                    conversaId: currentConversaId.value
                }
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
        currentConversaId,
        sendMessage,
        clearMessages,
        createNewConversa,
        loadConversa,
        deleteConversa
    };
};
