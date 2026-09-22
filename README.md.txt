# Rule-Based AI Chatbot

**Project 1 — DecodeLabs Industrial Training Kit (Batch 2026)**

A simple rule-based chatbot built in Python that responds to predefined user
inputs using dictionary-based lookup logic, running in a continuous loop.

## Features

- **Continuous input loop** — keeps the conversation running until the user exits
- **Input sanitization** — handles case and whitespace differences
- **Dictionary-based knowledge base** — maps recognized intents to responses using O(1) lookup instead of a long if-elif chain
- **Fallback response** — gracefully handles unrecognized input
- **Clean exit strategy** — ends the chat on `bye`, `exit`, or `quit`

## How to Run

\`\`\`bash
python rule_based_chatbot.py
\`\`\`

## Example

\`\`\`
Chatbot: Hello! I'm your rule-based assistant.
Chatbot: Type 'bye', 'exit', or 'quit' anytime to end the chat.

You: hi
Chatbot: Hello there!
You: bye
Chatbot: Goodbye! Have a great day!
\`\`\`

## Concepts Practiced

- Control flow (`while`, `if`/`in`)
- Dictionaries as lookup tables (`.get()` with a fallback)
- Basic rule-based AI system design

## Author

[Your Name] — DecodeLabs Intern, Batch 2026