# Dunefield Systems - Service Desk Runbook


# VPN Setup (DuneConnect)

DuneConnect is Dunefield Systems' VPN. It creates a secure, encrypted connection from your laptop to the company network when you work outside the office.

## When you need the VPN

You **must** use the VPN to access:

- Internal websites ending in `.dunefield.internal`
- Shared network drives (S: and P: drives)
- The ERP and finance systems
- Remote desktop to office computers

You **do not** need the VPN for email, Teams, the DuneDesk portal, or DuneDrive cloud storage. These work from anywhere with MFA.

## Installing DuneConnect

DuneConnect is preinstalled on all company laptops. If it is missing:

1. Open **Company Portal** from the Start menu.
2. Search for **DuneConnect VPN**.
3. Click **Install** and wait for the installation to finish.
4. Restart your laptop.

Personal devices are **not** allowed to connect to the VPN.

## Connecting

1. Click the DuneConnect icon (a shield) in the system tray, near the clock.
2. Select the gateway closest to you:
   - `vpn-riy.dunefield.example` – Riyadh (default)
   - `vpn-dxb.dunefield.example` – Dubai
   - `vpn-eu.dunefield.example` – Europe (for travel)
3. Click **Connect**.
4. Sign in with your Dunefield email and password.
5. Approve the MFA prompt on your phone.
6. The icon turns green when connected.

## Rules for VPN use

- Disconnect from the VPN when you no longer need internal resources.
- Sessions disconnect automatically after **12 hours**.
- Do not use the VPN on public computers or share your VPN session.
- Streaming video and personal downloads over the VPN are not allowed.

If you cannot connect, see "VPN Troubleshooting".

---


# VPN Troubleshooting

Use this guide if DuneConnect VPN will not connect, keeps disconnecting, or is very slow.

## Before you start

1. Check that your internet works without the VPN (open any public website).
2. Make sure your laptop's date and time are correct. Wrong time settings cause certificate errors.
3. Restart your laptop. This fixes many VPN issues.

## Common errors and fixes

### "Authentication failed"

- Check your password. If you changed it recently, use the new one.
- Make sure you approved the MFA prompt within 60 seconds.
- Your account may be locked. See "Account Lockout".

### "Unable to reach gateway" or connection timeout

- Try a different gateway (for example `vpn-dxb.dunefield.example` instead of `vpn-riy`).
- Some hotel and public Wi-Fi networks block VPN traffic. Try your phone's hotspot.
- Check the DuneDesk portal status page for any VPN outage.

### "Certificate error" or "Untrusted server"

- Check your laptop's date, time, and time zone.
- Do **not** click "Continue anyway". Contact IT Support; this could indicate a security problem.

### VPN connects but internal sites do not load

1. Disconnect and reconnect the VPN.
2. Open Command Prompt and run `ipconfig /flushdns`.
3. Try opening the site by its full name, e.g. `https://intranet.dunefield.internal`.

### VPN disconnects frequently

- Use a wired connection or move closer to your Wi-Fi router.
- Turn off "power saving" for your Wi-Fi adapter.
- Sessions automatically end after 12 hours; this is expected.

### VPN is very slow

- Connect to the nearest gateway.
- Pause large personal downloads or video streaming on your home network.
- Close cloud sync apps temporarily if uploading large files.

## Collecting logs for IT Support

If the problem continues, open a ticket and attach the VPN log:

1. Right-click the DuneConnect icon → **Diagnostics** → **Export logs**.
2. Save the ZIP file and attach it to your DuneDesk ticket.

Include the gateway you used, your location, and the exact error message.

---


# Office Wi-Fi Networks

Dunefield Systems offices have three Wi-Fi networks. Use the correct one for your device.

| Network name | Who can use it | Sign-in | Access |
|---|---|---|---|
| `Dunefield-Corp` | Company laptops only | Automatic (device certificate) | Full internal network |
| `Dunefield-BYOD` | Employees' personal phones and tablets | Dunefield email + password + MFA | Internet, email, Teams only |
| `Dunefield-Guest` | Visitors | Daily code from reception | Internet only, 8-hour limit |

## Company laptops

Company laptops connect to `Dunefield-Corp` **automatically** using a security certificate. You do not need to type a password.

If your laptop does not connect:

1. Make sure Wi-Fi is turned on (check airplane mode).
2. Click the Wi-Fi icon, select `Dunefield-Corp`, and click **Connect**.
3. If it still fails, restart your laptop while in the office.
4. If you see "Can't connect to this network", your device certificate may have expired. Plug into a wired network port (blue cable on your desk) and restart; the certificate renews automatically. If that fails, contact IT Support.

## Personal devices

1. Select `Dunefield-BYOD`.
2. Enter your Dunefield email and password.
3. Approve the MFA prompt.
4. Accept the "Acceptable Use" notice.

Personal devices cannot reach internal systems, shared drives, or printers.

## Guest access

Visitors should ask reception for the daily guest code. Employees must **not** share their own credentials with visitors.

## Slow or unstable Wi-Fi in the office

- Move closer to an access point (white device on the ceiling).
- Meeting rooms on Floor 3 have weaker coverage; use the wired port on the table for video calls.
- Report persistent dead zones to IT with the room number and floor so the network team can investigate.

---


# Email and Outlook Problems

Dunefield Systems uses Microsoft Outlook for email and calendars. You can use the Outlook desktop app on your laptop, Outlook on the web at https://mail.dunefield.example, or the Outlook mobile app.

## Mailbox limits

- Mailbox size: **50 GB** per user.
- Maximum attachment size: **25 MB**. For larger files, share a DuneDrive link instead.
- Emails to more than **200 recipients** require approval from Internal Communications.

## Outlook is not sending or receiving

1. Check the bottom of the Outlook window. If it says **Working Offline**, go to **Send/Receive** → click **Work Offline** to turn it off.
2. Check that you are connected to the internet.
3. Close Outlook completely and reopen it.
4. Try Outlook on the web. If it works there, the problem is with the desktop app.

## Outlook keeps asking for your password

- You probably changed your password recently. Enter the new one and check **Remember my credentials**.
- If prompts continue, sign out of Outlook (**File** → **Office Account** → **Sign out**), restart, and sign in again.
- Check your phone's email app for an old saved password, which can lock your account.

## Outlook is slow or freezes

- Restart Outlook and your laptop.
- Archive old email: **File** → **Tools** → **Mailbox Cleanup**.
- Turn off add-ins you do not use: **File** → **Options** → **Add-ins** → **Go**.

## Missing emails

- Check the **Junk Email** folder and the **Other** tab (if Focused Inbox is on).
- Search all folders using the search box with "All Mailboxes" selected.
- Emails flagged as suspicious by the security system are held in **quarantine**. You receive a daily quarantine digest at 9:00 AM; release legitimate emails from there.

## Shared mailboxes

To get access to a shared mailbox (for example `sales@dunefield.example`), your manager must request it through the DuneDesk portal under **Access Requests** → **Shared Mailbox**. Access appears in Outlook automatically within 2 hours after approval.

## Out of office replies

In Outlook desktop: **File** → **Automatic Replies**. Please include your return date and a colleague's contact for urgent matters.

---


# Printer Setup and Secure Printing

Dunefield Systems uses **secure "follow-me" printing**. You send your document to one shared print queue, then release it at any office printer by tapping your employee badge. This saves paper and keeps confidential documents private.

## Adding the printer to your laptop

The printer is usually installed automatically. If it is missing:

1. Connect to the office network (`Dunefield-Corp` Wi-Fi or wired) or the VPN.
2. Open **Company Portal** from the Start menu.
3. Search for **Dunefield Secure Print** and click **Install**.
4. The printer `DF-SecurePrint` appears in your printer list.

Personal devices cannot print to office printers.

## Printing a document

1. Print as usual and choose **DF-SecurePrint** as the printer.
2. Walk to any office printer.
3. Tap your employee badge on the card reader.
4. Select your document on the screen and press **Print**.

Documents waiting in the queue are **deleted after 24 hours** if not printed.

## Printer locations (Riyadh HQ)

| Floor | Location | Color printing |
|---|---|---|
| 1 | Near reception | No |
| 2 | Next to the IT Service Desk, Room 214 | Yes |
| 3 | Kitchen area | Yes |
| 4 | Finance wing (badge access required) | Yes |

## Printing rules

- Default setting is **black and white, double-sided**. Change it in the print dialog if needed.
- Color printing is limited to **200 pages per month** per person.
- Do not print confidential documents and leave them unattended. Secure printing helps prevent this.

## Badge not recognized at the printer

The first time you use a printer, you may need to register your badge:

1. Tap your badge.
2. When prompted, sign in with your Dunefield email and password on the printer screen.
3. Your badge is now linked and will work at all printers.

For printing problems, see "Printer Troubleshooting".

---


# Printer Troubleshooting

Use this guide when printing does not work. For first-time setup, see "Printer Setup and Secure Printing".

## My document does not appear at the printer

1. Make sure you printed to **DF-SecurePrint**, not another printer such as "Microsoft Print to PDF".
2. Check that your laptop is on the office network or VPN when you click Print.
3. Wait one minute. Large documents take time to reach the queue.
4. Remember that documents are deleted after **24 hours** in the queue.
5. Open the print queue on your laptop (**Settings** → **Bluetooth & devices** → **Printers & scanners** → **DF-SecurePrint** → **Open print queue**). If the job shows "Error", cancel it and print again.

## The printer shows an error

| Message on screen | What to do |
|---|---|
| Paper jam | Follow the animation on the screen to open the correct tray. Remove the paper gently. Do not use tools. |
| Load paper / Tray empty | Paper is in the cabinet under each printer. Use A4 only. |
| Toner low | You can keep printing. Facilities replaces toner automatically. |
| Toner empty / Replace cartridge | Report it in DuneDesk under **Printers** with the printer's floor and location. |
| Offline / Not responding | Use another printer and report the issue. |

## Badge does not work at the printer

- Make sure you registered your badge (first-time use requires signing in on the printer screen).
- If you recently received a new badge, register it again.
- If your badge also fails at door readers, contact Facilities, not IT.

## Print quality problems (lines, faded text, smudges)

Try printing on a different printer. If the problem only happens on one printer, report that printer in DuneDesk with a photo of the printed page.

## Printing in color is blocked

You may have reached the monthly color limit of **200 pages**. Color quota resets on the 1st of each month. Managers can request a temporary increase for business needs through DuneDesk.

## Reporting a printer problem

Open a P3 ticket in DuneDesk under **Printers & Devices** and include:

- Floor and location of the printer
- The exact error message (photo if possible)
- Whether other people are affected

---


# Laptop Requests, Replacement, and Repairs

All Dunefield Systems employees receive a company laptop. Laptops are company property and must be returned when you leave.

## Standard laptop models

| Role | Model | Specs |
|---|---|---|
| Standard (most employees) | Dell Latitude 14 | 16 GB RAM, 512 GB SSD |
| Engineering & Data | Dell Precision 16 | 32 GB RAM, 1 TB SSD, dedicated GPU |
| Design | Apple MacBook Pro 14 | 32 GB RAM, 1 TB SSD |

Non-standard models require approval from your department head and the IT Manager.

## Requesting a new laptop

1. Your manager submits a **Hardware Request** in the DuneDesk portal.
2. IT confirms the model based on your role.
3. Delivery time: **3 business days** if in stock, up to **15 business days** if it must be ordered.
4. You collect the laptop from the IT Service Desk (Floor 2, Room 214) or it is shipped to remote employees.

## Replacement cycle

Laptops are replaced every **4 years**. IT will contact you about 2 months before your laptop is due. You do not need to request it.

## Broken laptop or hardware problem

1. Open a ticket in DuneDesk under **Hardware** and describe the problem (screen damage, keyboard, battery, won't turn on).
2. Back up anything not already in DuneDrive (see "File Storage and Backup").
3. Bring the laptop to the IT Service Desk. Remote employees receive a prepaid shipping box.
4. If repair takes more than one day, you receive a **loaner laptop**.

## Accidental damage, loss, or theft

- **Accidental damage** (drops, spills): Report within 24 hours. Repairs are covered by the company the first time; repeated damage may require manager review.
- **Lost or stolen laptop:** Report **immediately** by phone (extension 4357, available 24/7 for this). IT will remotely lock and wipe the device. For theft, also file a police report and attach it to the ticket.

## Accessories

Standard accessories (mouse, keyboard, headset, laptop bag, USB-C dock) can be requested in DuneDesk under **Accessories** without manager approval. Monitors and docking stations for home require manager approval (see "Remote Work Equipment").

---


# New Employee IT Onboarding

Welcome to Dunefield Systems! This guide explains how to get your IT accounts and equipment ready in your first week.

## Before your first day

Your manager submits an **Onboarding Request** in DuneDesk at least **5 business days** before your start date. This creates your account, orders your laptop, and assigns your software and access.

## Day 1 checklist

1. **Collect your laptop and badge** from the IT Service Desk (Floor 2, Room 214) at 9:00 AM. Remote employees receive the laptop by courier before day 1.
2. **Sign in** with the temporary password from your welcome email. You will be asked to create a new password (see "Password Reset and Password Policy").
3. **Set up MFA** on your phone (see "Multi-Factor Authentication Setup"). This must be done within 3 days.
4. **Open Outlook and Teams** to confirm email and chat work.
5. **Register your badge** at a printer (see "Printer Setup").

## First week checklist

- Complete the **Security Awareness Training** in the learning portal (about 45 minutes). This is required within **7 days**; your access may be limited until it is finished.
- Read and accept the **Acceptable Use Policy**.
- Install the DuneConnect VPN if you work remotely (preinstalled on most laptops).
- Request any additional software through Company Portal or DuneDesk (see "Software Installation Policy").
- Join the `#it-announcements` Teams channel for outage and maintenance notices.

## What access you get by default

| System | Default access |
|---|---|
| Email, Teams, calendar | Yes |
| DuneDrive personal storage (1 TB) | Yes |
| Department shared folder | Yes |
| ERP / Finance systems | Only if your role requires it |
| Admin rights on laptop | No (see "Software Installation Policy") |

Anything else must be requested by your manager through **Access Requests** in DuneDesk.

## Need help?

Visit the IT Service Desk or call extension 4357. New employees can also book a 30-minute "IT welcome session" in DuneDesk.

---


# File Storage, Sharing, and Backup

Save company files in approved storage so they are backed up and accessible from any device. Files saved only on your laptop's local drive are **not backed up**.

## Where to save files

| Location | Use for | Size | Backed up |
|---|---|---|---|
| **DuneDrive** (personal) | Your own work files and drafts | 1 TB | Yes |
| **Team shared folders** (in DuneDrive) | Files your team works on together | 5 TB per team | Yes |
| **S: drive** (legacy network share) | Older department files; being retired by June 2027 | Varies | Yes |
| Laptop local drive (C:) | Temporary files only | — | **No** |

Your Desktop, Documents, and Pictures folders are automatically synced to DuneDrive on company laptops.

## Sharing files

- **Inside Dunefield:** Share a link with "People in Dunefield Systems" or specific colleagues.
- **Outside Dunefield:** Share with specific external email addresses only. "Anyone with the link" sharing is disabled for Confidential data.
- External sharing links expire after **30 days** by default.
- Avoid sending large attachments by email; share a DuneDrive link instead.

## Recovering deleted or older files

- **Deleted files:** Go to DuneDrive on the web → **Recycle bin**. Files can be restored for **93 days**.
- **Previous versions:** Right-click a file → **Version history** to restore an older version. DuneDrive keeps up to 500 versions.
- **Whole folder restore** (for example after ransomware or mass deletion): Contact IT Support. Backups are kept for **1 year**.

## Sync problems

If the DuneDrive icon in the system tray shows a red X or a pause symbol:

1. Click the icon and read the error.
2. Make sure you are signed in and have internet access.
3. Check for file names with unsupported characters (such as `"`, `*`, `:`, `<`, `>`, `?`) or paths longer than 400 characters.
4. Click **Resume syncing** if paused.
5. If the problem continues, restart your laptop, then contact IT Support.

## Storage full

If your DuneDrive is almost full, delete old files you no longer need or move team files to the team shared folder. Storage increases beyond 1 TB require manager approval.

---


# Remote Work IT Guidelines and Home Equipment

Dunefield Systems supports hybrid and remote work. These guidelines help you work securely and productively from home or while traveling.

## Home network

- Use a private home Wi-Fi network protected with **WPA2 or WPA3** and a strong password.
- Change the default admin password on your home router.
- Avoid public Wi-Fi (cafés, airports) for confidential work. If you must use it, connect to the DuneConnect VPN immediately, or use your phone's hotspot.

## Working securely

- Lock your laptop when you step away, even at home.
- Do not let family members or friends use your company laptop.
- Use headphones for calls that discuss confidential information.
- Do not print confidential documents on home printers.
- Keep your laptop with you when traveling. Never leave it in a car.

## Home office equipment

Remote and hybrid employees can request the following through DuneDesk → **Remote Work Equipment**:

| Item | Approval needed | Notes |
|---|---|---|
| Headset, mouse, keyboard | No | Shipped within 5 business days |
| External monitor (24") | Manager | One per employee |
| USB-C docking station | Manager | Recommended with a monitor |
| Second monitor | Manager + department head | For roles that need it |
| Office chair or desk | HR (not IT) | Request through the HR portal |

All equipment remains company property and must be returned when you leave.

## Internet costs

Dunefield does not provide home internet. A monthly remote work allowance is paid through payroll for eligible employees; contact HR for details.

## Working from abroad

Working from another country for more than **14 days** requires approval from your manager, HR, and IT Security, because some countries restrict VPN use or data transfer. Submit the request at least **10 business days** before travel.

## Getting help remotely

IT Support can connect to your laptop with remote assistance. When asked, open **Quick Assist** from the Start menu and enter the code the technician gives you. Only accept remote sessions that **you** requested through DuneDesk or by calling extension 4357.

---


# Slow Computer Troubleshooting

If your company laptop is slow, freezes, or takes a long time to start, try these steps in order before opening a ticket.

## 1. Restart your laptop

Many people only close the lid instead of restarting. Laptops that have not restarted in days become slow and miss security updates.

Click **Start** → **Power** → **Restart** (not "Shut down"). Restart at least **once a week**.

## 2. Install pending updates

1. Go to **Settings** → **Windows Update**.
2. Click **Check for updates** and install everything.
3. Restart when asked.

## 3. Close programs you aren't using

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Click the **Memory** or **CPU** column to sort.
3. Close apps you don't need (for example, dozens of browser tabs). Do not end processes you don't recognize; some are security tools.

Browsers with many tabs are the most common cause of slowness. Use fewer tabs or enable "Memory Saver" in your browser settings.

## 4. Check your disk space

1. Open **File Explorer** → **This PC**.
2. If the C: drive is almost full (red bar), free up space:
   - Empty the Recycle Bin.
   - Delete old files in **Downloads**.
   - Run **Disk Cleanup** from the Start menu.
   - Set DuneDrive files to **Free up space** (right-click a folder → Free up space) so they stay in the cloud.

## 5. Check your charger and power mode

Laptops run slower on battery saver.

- Plug in the original charger.
- Go to **Settings** → **System** → **Power & battery** and set Power mode to **Balanced** or **Best performance**.

## When to contact IT Support

Open a P3 ticket in DuneDesk if:

- The laptop is still slow after all the steps above.
- You hear unusual noises, or the laptop gets very hot.
- The laptop restarts on its own or shows blue screen errors (note the error code shown).
- It is more than 4 years old (it may be due for replacement; see "Laptop Requests, Replacement, and Repairs").

If your laptop suddenly becomes slow **and** you see pop-ups, unknown programs, or renamed files, treat it as a possible security incident and call extension 4357, press 2.

---


# Meeting Rooms and Video Calls

Dunefield Systems uses Microsoft Teams for chat, video calls, and online meetings. Most meeting rooms have a Teams Room system with a screen, camera, and microphone.

## Booking a meeting room

1. In Outlook, create a new meeting.
2. Click **Room Finder** (or **Add a room**).
3. Choose the building and floor, then pick an available room.
4. Send the invite. The room accepts automatically if it is free.

Rooms not checked in within **10 minutes** of the start time are released automatically for others. Check in on the screen outside the room.

## Meeting room sizes (Riyadh HQ)

| Room type | Capacity | Equipment |
|---|---|---|
| Focus room | 1–2 | Screen with HDMI/USB-C cable |
| Small meeting room | 4–6 | Teams Room, camera, speaker |
| Large meeting room | 10–14 | Teams Room, dual screens, ceiling microphones |
| Boardroom (Floor 4) | 20 | Requires approval from the Executive Office |

## Joining a Teams meeting from a meeting room

1. Tap **Join** on the touch panel on the table. Teams meetings booked with the room appear automatically.
2. For a meeting not booked with the room, tap **Join with an ID** and enter the meeting ID and passcode from the invite.

## Sharing your screen in a meeting room

- **Wireless:** Join the meeting from your laptop with audio turned **off** (choose "Don't use audio"), then click **Share**.
- **Wired:** Connect the HDMI or USB-C cable on the table. Your screen appears automatically.

## Common problems

| Problem | Fix |
|---|---|
| Others can't hear you | Check the microphone isn't muted on the touch panel or the ceiling mic indicator is green |
| Echo or feedback | Someone in the room joined with laptop audio on; ask them to mute their laptop |
| Screen shows "No signal" | Unplug and reconnect the cable, or select the correct input on the touch panel |
| Camera not showing | Tap the camera icon on the touch panel to turn video on |
| Room panel frozen | Restart it: touch panel **Settings** → **Restart**. Report it if it happens again |

## Getting help during a meeting

For urgent meeting room problems before an important meeting, call extension 4357 and say it is a meeting room issue. IT will try to send someone within 15 minutes during business hours. For executive and customer meetings, request **meeting support** in DuneDesk at least **1 business day** in advance.

---


# IT Frequently Asked Questions

Quick answers to the most common questions received by the Dunefield Systems IT Service Desk.

## Accounts and passwords

**How often do I need to change my password?**
Every 180 days. You get reminders 14, 7, and 1 day before it expires.

**I forgot my password. What do I do?**
Use self-service reset at https://reset.dunefield.example. You need MFA set up first.

**Why does my account keep locking?**
Usually an old password saved on your phone or another device. See "Account Lockout".

## Devices

**Can I use my personal laptop for work?**
No. Only company laptops can access internal systems, the VPN, and shared drives. Personal phones can use email and Teams through the `Dunefield-BYOD` Wi-Fi and the mobile apps with MFA.

**Can I get admin rights on my laptop?**
No, not permanently. Install software from Company Portal or submit a Software Request. Engineers can request temporary 4-hour admin access.

**How long does it take to get a new laptop?**
3 business days if in stock, up to 15 business days if ordered.

**My laptop was stolen. What should I do?**
Call extension 4357 immediately (24/7). IT will lock and wipe it. File a police report and attach it to your ticket.

## Network and remote work

**Do I need the VPN for email or Teams?**
No. You only need the VPN for internal websites, shared network drives, ERP/finance systems, and remote desktop.

**What is the guest Wi-Fi password?**
Visitors get a daily code from reception. Do not share your own credentials.

## Files and email

**What's the maximum email attachment size?**
25 MB. For larger files, share a DuneDrive link.

**I deleted a file by mistake. Can I get it back?**
Yes. Check the DuneDrive Recycle bin (kept for 93 days), or use Version history. For larger restores, contact IT Support.

**Can I use a USB flash drive?**
USB storage is blocked by default. Use DuneDrive to share files. Exceptions need IT Security approval.

## Security

**I clicked a link in a suspicious email. What now?**
Call extension 4357 and press 2 right away. You won't be punished for reporting.

**I got an MFA prompt I didn't request.**
Deny it and report it immediately. Someone may know your password.

**Can I use AI tools like chatbots for work?**
Only AI tools listed in Company Portal. Never paste Confidential or Restricted data into unapproved AI tools.

## Contacting IT

**What are IT Support hours?**
Sunday to Thursday, 8:00 AM – 5:00 PM (Riyadh time). Critical (P1) issues are handled 24/7 by phone at extension 4357.

**How do I check the status of my ticket?**
Log in to the DuneDesk portal at https://portal.dunefield.example → **My Tickets**.

---

