# Customer Support Agent – Demo Script

## 1. Introduction

Hello everyone!

Today, we are presenting our Customer Support Agent, an AI-powered support assistant designed to deliver continuous and personalised customer support using persistent memory.

Unlike traditional chatbots that primarily focus on the current conversation, our agent can retain relevant customer information and recall previous interactions, even when a customer starts a completely new chat session.

## 2. The Problem

One of the biggest challenges in customer support is the lack of continuity between conversations.

Customers often have to explain their technical environment, repeat previously reported issues, and describe troubleshooting steps they have already completed.

This results in repetitive communication, wasted time, and a frustrating support experience.

Our project addresses this problem through persistent AI memory.

## 3. Meet the Customer – Sarah

For our demonstration, let's consider Sarah, a Lead Engineer working with a Node.js backend hosted on AWS infrastructure.

Sarah has previously contacted technical support for three issues:

- **TKT-1001 – API Authentication Failure:** Revoked API keys caused authentication errors. The issue was resolved by generating new API keys and updating AWS environment variables.
- **TKT-1042 – Outbound API Timeout:** Restrictive AWS security group rules affected outbound connectivity. The issue was resolved by correcting the required network rules.
- **TKT-1087 – Webhook Timeout:** Sarah reported a continuing webhook timeout issue, which is still under investigation.

This information forms Sarah's customer support history.

## 4. Session 1 – Initial Interaction

Sarah starts a conversation with the AI support agent.

**Sarah:** Hi, my payment webhook keeps timing out. We're receiving 504 errors.

**AI Agent:** I'm sorry you're experiencing this. Could you tell me about your technical environment?

**Sarah:** Our backend is built using Node.js and hosted on AWS.

**AI Agent:** Have you already tried any troubleshooting steps?

**Sarah:** Yes, we've checked our AWS firewall rules and rotated our production API keys, but the issue is still happening.

**AI Agent:** Understood. I'll keep your environment and troubleshooting history in mind. Could you share the latest request ID and relevant server logs so we can investigate further?

During this interaction, the system uses Hindsight to retain relevant customer information and support context.

## 5. Session 2 – The Memory Demonstration

Now imagine Sarah returns one week later and starts a completely new chat session.

**Sarah:** Hi, my webhook is still timing out. Can you help me?

**AI Agent:** Welcome back, Sarah! I remember that you're using a Node.js backend hosted on AWS. You previously investigated authentication failures and outbound connectivity issues. Your earlier firewall checks and API key rotation have already been attempted.

Let's continue investigating the webhook timeout without repeating those troubleshooting steps.

**Sarah:** Yes! That's exactly what we discussed last time.

**AI Agent:** Great! Let's focus on the remaining issue. Could you share your latest request ID and Node.js server logs so we can identify whether the delay is occurring within your application or during network communication?

This demonstrates how the agent can retrieve relevant historical context instead of treating Sarah as a completely new customer.

## 6. How Hindsight Powers the System

Our architecture combines four major components:

1. **Frontend:** Provides an interactive customer support chat interface using HTML, CSS and JavaScript.
2. **FastAPI:** Handles communication between the frontend, AI model and memory system.
3. **Groq:** Processes customer queries and generates contextual responses.
4. **Hindsight:** Retains and retrieves relevant customer information across separate interactions.

The workflow follows five stages:

- Recall previous customer memories.
- Understand the current customer query.
- Generate a contextual response using Groq.
- Retain relevant new interaction information.
- Return the response to the frontend.

## 7. Key Benefits

- Persistent customer context across separate sessions.
- Reduced repetition of previously attempted troubleshooting.
- More personalised support interactions.
- Better continuity in ongoing technical investigations.
- Improved customer support efficiency.

## 8. Conclusion

Our Customer Support Agent demonstrates how persistent memory can transform a conventional chatbot into a context-aware support assistant.

By combining AI-powered responses with long-term customer memory, our system aims to make support interactions more continuous, efficient and personalised.

Instead of making customers start from zero every time, our agent remembers where the conversation left off.

Thank you!
