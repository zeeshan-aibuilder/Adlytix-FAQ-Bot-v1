# 🤖 Adlytix Smart Support Agent (RAG System v1.0)

> An intelligent, terminal-based FAQ chatbot utilizing local file-based Retrieval-Augmented Generation (RAG) to automate client support.

## 🚀 Overview
The **Adlytix Smart Support Agent** is a Python-based CLI tool engineered to provide instant answers to client queries. It scans a local text-based knowledge base for matching keywords. If a query falls outside its current knowledge, it gracefully falls back, logs the unanswered question as a "missed lead," and provides human contact details. 

## ✨ Core Features
* **🧠 Keyword-Based Retrieval:** Scans user input and matches it against a local database (`adlytix_data.txt`).
* **📝 Automated Lead Logging:** Unanswered questions are automatically appended to `missed_leads.txt` for future training and human follow-up.
* **🛡️ Infinite Loop Protection:** Controlled `while True` loop with safe exit strategies and `try-except` blocks to prevent input crashes.
* **🧹 Data Sanitization:** Utilizes `.lower()`, `.split()`, and `.strip()` for robust string manipulation and accurate matching.
* **🚩 Boolean Flag Logic:** Smart execution flow ensuring responses are printed only once per query without spamming the terminal.

## 🛠️ Architecture Flow
1. **Input:** User asks a question (e.g., "What is the price?").
2. **Process:** System tokenizes the input and iterates through the knowledge base.
3. **Output (Hit):** If a match is found, the specific answer is extracted and displayed.
4. **Output (Miss):** If no match is found, the system logs the exact query and redirects the user to the Adlytix Performance Marketing support line.

## 💻 How to Run
1. Clone this repository:
```bash
   git clone [https://github.com/zeeshan-aibuilder/Adlytix-FAQ-Bot-v1.git](https://github.com/zeeshan-aibuilder/Adlytix-FAQ-Bot-v1.git)
