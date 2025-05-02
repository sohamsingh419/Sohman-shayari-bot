# Telegram Shayari & Jokes Bot

यह एक सिंपल Telegram बॉट है जो ग्रुप में रैंडम शायरी और जोक्स भेजता है।

## कैसे काम करता है?
- `/start` भेजकर बॉट को शुरू करें।
- बॉट हर 1 घंटे में शायरी और हर 1.5 घंटे में जोक भेजेगा।

## जरूरत:
- Telegram Bot Token (`BOT_TOKEN`)
- ग्रुप Chat ID (`CHAT_ID`)

## डिप्लॉय:
Render पर deploy करने के लिए:
1. Repository को Render से कनेक्ट करें।
2. Environment Variables सेट करें:
   - `BOT_TOKEN` = `<Your Telegram Bot Token>`
   - `CHAT_ID` = `<Your Group Chat ID>`
3. Background Worker सेटअप करें।
4. 
