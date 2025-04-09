# Aɴɪᴍᴇ Lᴏʀᴅ - Telegram Bot

**A powerful, feature-rich Telegram bot for file sharing, user management, channel control, and automation. Fully deployable on platforms like Koyeb.**

---

## ✦ Core Features

1. **Admin Access Management** - Control who can access admin features.
2. **Link Password Protection** - Secure links with custom passwords.
3. **File Expiration System** - Auto-delete files after specific time.
4. **Bulk File Sharing** - Upload and share multiple files at once.
5. **File Deletion** - Delete any uploaded content with ease.
6. **Upload Size Limits** - Set size restrictions for uploads.

---

## ✦ Channel Control

7. **Forced Channel Subscription** - Ensure users join your channel before using bot.
8. **Custom Subscription Messages** - Show personalized messages for unsubscribed users.
9. **Auto-posting to Channels** - Automatically forward content to configured channels.

---

## ✦ User Management

10. **User List Viewing** - Get list of all users using the bot.
11. **Broadcast Messaging** - Send announcements to all users.
12. **User Activity Tracking** - Track when and how users interact with the bot.

---

## ✦ Automation & Logs

13. **Auto-post Configuration** - Setup automation rules.
14. **Activity Logging** - Log all critical actions and activities.
15. **Log Clearing** - Clear old logs to maintain performance.

---

## ✦ Security & Maintenance

16. **Database Backups** - Backup user and file data.
17. **Data Restoration** - Restore from backup if needed.
18. **Emergency Reset** - Reset bot in case of failure or breach.

---

## ✦ Advanced Features

19. **Custom Button Creation** - Create inline keyboard buttons dynamically.
20. **Automatic Channel Logging** - Logs messages/events in specific channels.
21. **Anime Lord Styling** - Stylish responses using Anime-themed fonts.

---

## Deployment (Koyeb Ready)

**Required Files:**

- `runtime.txt`
- `requirements.txt`
- `Procfile`
- `config.py`
- `bot.py`
- `handlers/`
- `utils/`
- `database/`
- `templates/`

**Deploy on Koyeb:**

1. Upload this project to GitHub.
2. Link GitHub repo to Koyeb.
3. Deploy with Python build settings.
4. Ensure config variables are set in Koyeb environment settings.

---

## Installation (Locally)

```bash
[git clone https://github.com/yourusername/animelord-bot.git](https://github.com/whoami847/Anime-Lord)
cd animelord-bot
pip install -r requirements.txt
python bot.py
