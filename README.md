
# SkillSync

**SkillSync** is a terminal-based Python application for managing workshop bookings and one-on-one meetings. Built for flexibility and efficiency, it integrates Firebase for authentication and data storage and leverages the Google Calendar API for seamless scheduling. The app is packaged using `pyinstaller` for easy distribution.

---

## 🚀 Features

### 🔐 Authentication
- **Secure Access**: Firebase Authentication for sign-up and login.
- **User Roles**: Distinct roles such as `mentor` and `peer`.
- **User Data**: Stores name, email, and role.

### 📅 Booking System
- **Mentor Sessions**:
  - Browse available mentors.
  - Request meetings with selected mentors.
- **Peer Sessions**:
  - Search peers by expertise or availability.
  - Schedule one-on-one meetings.

### 🗓 Google Calendar Integration
- **Automatic Scheduling**: Create events for confirmed bookings.
- **Invite Management**: Automatically send calendar invites to participants.
- **Time Constraints**: Meetings allowed only **Monday–Friday, 07:00–17:00**.

### 💻 Command-Line Interface (CLI)
Built with the `click` library for an intuitive terminal experience. Includes:
- `Login`: Authenticate users.
- `View Workshops`: List upcoming sessions and mentors.
- `Request Meeting`: Initiate a mentor or peer session.
- `View Bookings`: Show all confirmed meetings.
- `Cancel Booking`: Remove an existing booking.

---

## 🗄 Database Structure

### Users Collection
```json
{
  "user_id": {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "role": "mentor",
    "expertise": ["Python", "Data Science"]
  }
}
```

### Meetings Collection
```json
{
  "meeting_id": {
    "mentor_id": "...",
    "mentee_id" or "peer_id": "...",
    "time": "YYYY-MM-DDTHH:MM",
    "status": "confirmed"
  }
}
```

### Workshop Requests Collection
```json
{
  "workshop_id": {
    "requestor_id": "...",
    "topic": "Intro to Flask",
    "date_requested": "YYYY-MM-DD"
  }
}
```

---

## 🛠 Tech Stack

- **Backend**: Python
- **CLI Framework**: [`click`](https://click.palletsprojects.com/)
- **Database**: Firebase Realtime Database
- **Auth**: Firebase Authentication
- **Scheduling**: Google Calendar API (`google-api-python-client`)
- **Packaging**: `pyinstaller`

---

## ⏰ Scheduling Constraints

All bookings must strictly fall within:
- **Days**: Monday to Friday
- **Time**: 07:00 – 17:00

Developers must enforce this rule in both data validation and logic.

---

## 🌟 Stretch Features

- 📬 **Email Notifications**: Confirmations & reminders via `smtplib`
- ⭐ **Feedback System**: Rate and review mentors/peers
- 🔍 **Advanced Search**: Filter by expertise or availability

---

## 📦 Packaging & Distribution

Build a distributable version of the app using `pyinstaller`:
```bash
pyinstaller --onefile app.py
```

---

## ✅ Next Steps

1. **Firebase Setup**:
   - Configure Authentication and Database.
2. **Google Calendar Integration**:
   - Enable API and set up OAuth credentials.
3. **CLI Development**:
   - Build commands using `click`.
4. **Testing & Packaging**:
   - Validate all features.
   - Package using `pyinstaller`.
