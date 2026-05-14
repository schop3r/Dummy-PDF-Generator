# Dummy PDF Generator

### 💡 Why this exists?
Many document-sharing platforms (such as Scribd or academic repositories) require users to upload a specific number of documents before granting download access. This tool automates the creation of high-quality, professional-looking dummy PDFs, allowing you to meet these requirements instantly without sharing your private or sensitive personal files.

## 🚀 Features
- **Upload-Ready:** Generates unique files that meet the document requirements of online platforms.
- **Contextual Generation:** Uses domain-specific keywords (Quantum Physics, Finance, IoT, etc.) to ensure content variety and realistic structure.
- **Professional Formatting:** Includes bold headers, horizontal dividers, and automated pagination.
- **Clean Directory Management:** Automatically refreshes the output folder before each execution.
- **Modular Architecture:** Easy to extend with custom topics or specific document layouts.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/pdf-dummy-generator.git](https://github.com/yourusername/pdf-dummy-generator.git)
   cd pdf-dummy-generator
   
## 💻 Usage

1. **Simply run the main script to generate a set of unique PDFs:**
   ```bash
   python main.py
   
By default, the output will be stored in the generated_pdfs/ directory.

## 📂 Project Structure

```text
pdf-dummy-generator/
├── src/
│   ├── core.py         # Core PDF generation logic
│   └── constants.py    # Topic pool & keyword definitions
├── main.py             # Script entry point
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation