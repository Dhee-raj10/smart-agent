# main.py
from gmail_agent import get_gmail_service, search_messages, get_message_content

def main():
    print("Connecting to Gmail...")
    service = get_gmail_service()
    print("✅ Gmail connected successfully!\n")

    query = input("Enter Gmail search query (e.g., from:tarun@gmail.com): ")
    results = search_messages(service, query=query)

    if not results:
        print("No messages found.")
        return

    print(f"📩 Found {len(results)} messages.")
    for msg in results[:5]:  # Only show top 5
        content = get_message_content(service, msg['id'])
        if content:
            print("\n📨 Email Content:")
            print("-------------------------")
            print(content)
            print("-------------------------")

if __name__ == "__main__":
    main()
