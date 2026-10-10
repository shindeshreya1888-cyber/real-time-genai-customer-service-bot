from .conversation_memory import ConversationMemory


memory = ConversationMemory()

memory.add_message(
    "user",
    "What is the refund policy?"
)

memory.add_message(
    "assistant",
    "Customers can request refunds according to the refund policy."
)

memory.add_message(
    "user",
    "How long does it take?"
)

print("=" * 60)
print("CONVERSATION MEMORY TEST")
print("=" * 60)

print("\nStored messages:")
print(memory.get_messages())

print("\nConversation context:")
print(memory.get_context())