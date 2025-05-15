# 🔐 COMP90082 Software Project Lecture: Security and Vulnerability

👋 **Welcome, Students!**

This week's lecture is designed to give you a **fundamental understanding of cybersecurity** and help you become more aware of potential vulnerabilities when developing your software project.

This repository serves as the **hands-on component** for the second hour of the lecture. It also provides a **template** you can reuse for your **upcoming sprint submission**.

💡 Use this lecture time to brainstorm risks with your team, ask questions, and seek help from teaching staff — completing this activity now will **save you valuable time during your upcoming sprint submission.**

---

## 📚 Lecture Materials & Demo Attacks

* 📄 **Lecture Slides**
  You can access the lecture slides here: \[🔗 *TODO*]

* 🧪 **Security Attack Demos**
  All demo code shown during the lecture is available in the `demo/` folder of this repository.
  Each attack scenario is organized into its own subfolder.

  ✅ Inside each attack folder, you'll find a `demo.txt` file explaining how to run and test it.

* 🧪 **Static Analysis Demos**
  Static analysis demo can be found in the `static_analysis/` folder. 
  To test the static analyzer, use the command:
  ```
  python static_analyzer.py <filename>
  ```

> 💡 **Note:** These examples are intentionally simple to illustrate key concepts.
> Real-world attacks are often more subtle and complex — these demos serve as an accessible starting point to build your security understanding and awareness.
> 
---

## 🛠️ Hands-on Activity: The Risk Evaluation Framework

As every team has different goals, apps, and tech stacks (e.g., web app, mobile app, chatbot), your security concerns will vary.

This framework will guide you to **identify**, **evaluate**, and **document** security risks specific to your project.

### 📋 Risk Evaluation Table Template (Example)
#### You may copy and paste the table to your GitHub Wiki [here](https://github.com/MichaelFu1998-create/cybersecurity_lecture/blob/main/table_template.md?plain=1)

| 🧨 **Risk / Threat**           | 🔁 **Trigger / Cause**                            | 🎲 **Likelihood** | 💥 **Impact**                            | 🛡️ **Contingency Plan**                            |
|-------------------------------|--------------------------------------------------|------------------|------------------------------------------|----------------------------------------------------|
| SQL injection                 | User input is passed directly to SQL query       | Medium           | High (data breach, DB corruption)        | Use input validation, prepared statements          |
| Hardcoded API key             | Developer pushes code with secrets to GitHub     | Low              | High (unauthorized access)               | Use env variables, secret scanners                 |
| No HTTPS                      | API endpoint uses HTTP                           | High             | Medium (data in transit exposed)         | Enforce HTTPS via server config                    |
| Lack of authentication        | Public-facing admin route                        | Medium           | High (unauthorized access)               | Add auth middleware, access control                |

---

### 🧠 Column Explanations

- **Risk / Threat**: A specific vulnerability (e.g., insecure login, exposed data)
- **Trigger / Cause**: What could make this risk happen? (e.g., poor validation, misconfiguration)
- **Likelihood**: How likely is this to occur? *(Low / Medium / High)*
- **Impact**: What harm could it cause? *(Low / Medium / High)*
- **Contingency Plan**: What will your team do to prevent or respond?

---

## 🧭 Where to Start: Identifying Risks in Your Project

### ✅ Hint 1: Common Risk Categories Checklist

* [ ] 🚪 **Authentication & Authorization**
  *e.g., weak login, missing access control*

* [ ] 🛠 **Input Validation**
  *e.g., SQL injection, XSS*

* [ ] 📦 **Secrets Management**
  *e.g., hardcoded API keys, exposed credentials*

* [ ] 📡 **Data in Transit**
  *e.g., HTTP instead of HTTPS*

* [ ] 📁 **Storage Security**
  *e.g., public databases, open file storage*

* [ ] 🤖 **Third-party Components**
  *e.g., outdated libraries, known CVEs*

🧠 *Ask yourself:*  
> “Do any of these apply to our app?”  
> “Where in our code or architecture might this happen?”

---

### 🧱 Hint 2: High-Level – Review the Design of Your Software

Take a step back and look at your **architecture** or **flow diagrams**.

- What are the major components? *(Frontend, backend, APIs, DB, etc.)*  
- How does data move between them?  
- Where are the **trust boundaries**? *(e.g., user ↔ server, server ↔ DB)*  

🔎 *Use existing UML, sequence, or Data Flow Diagrams to look for:*
- Entry points (user input, APIs)
- Sensitive data flows (e.g., credentials, tokens)
- Integration points (e.g., third-party services)

---

### 🧩 Hint 3: Low-Level – Review Specific Code or Functions

Now zoom in 🔬…

- Which features are security-sensitive? *(login, file uploads, admin routes)*  
- Where is user input processed or stored?  
- Which endpoints access your database or external APIs?

---

🧠 Use this repo as both a learning activity **and** a security planning tool for your project.

Happy hacking — and secure coding! 💻🔐
