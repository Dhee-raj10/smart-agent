# Smart Gmail Agent

A Python-based smart agent that connects to your Gmail account, fetches recent emails based on custom queries, and displays them in a clean and accessible format — all without using OpenAI. Perfect for developers looking to automate their inbox workflows or integrate email parsing into other systems.

---

## What It Does

-  Authenticates securely with your Gmail using OAuth2.
-  Searches and filters emails using Gmail's powerful search queries (`from:`, `subject:`, etc.).
-  Fetches the **latest 5 messages** (or more if modified).
-  Extracts and displays:
  - Sender name and email
  - Subject
  - Snippet of the message

---

##  Tech Stack

- **Python 3.10+**
- `google-api-python-client`
- `google-auth-oauthlib`
- `gmail API`
- No OpenAI or LLM dependencies

---

## Project Structure

    smart-agent/
    │
    ├── gmail_agent.py 
    ├── main.py 
    ├── credentials/ 
    │ └── credentials.json
    ├── token.json # Created automatically after first successful auth
    ├── .gitignore 
    └── README.md 


---

## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Dhee-raj10/smart-agent.git
   cd smart-agent
2.Set up your Gmail API:

  Go to: Google Cloud Console

  Create OAuth 2.0 credentials

  Download credentials.json and place it in the credentials/ folder.

3.Install dependencies:
          
    pip install -r requirements.txt
    
4.Run the agent:
     
    python main.py

### Sample Output
  Connecting to Gmail...
  Fetching messages...
  
  From: Dheeraj (dheerajbachi@gmail.com)
  Subject: Final Report Submission
  Snippet: Hi, please find attached the final report due for submission...
  







