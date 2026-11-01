# Dunefield Systems - Company IT Handbook


# IT Support Overview

Dunefield Systems IT Support (the "Service Desk") helps all employees and contractors with accounts, devices, software, network access, and security issues.

## How to contact IT Support

| Channel | Details | Best for |
|---|---|---|
| DuneDesk portal | https://portal.dunefield.example | All non-urgent requests and tracking tickets |
| Phone | Extension 4357 (H-E-L-P), or +966 11 555 4357 from outside | Urgent issues, account lockouts |
| Email | it-help@dunefield.example | Requests when you cannot reach the portal |
| Walk-in desk | Riyadh HQ, Floor 2, Room 214 | Hardware pickup, hands-on help |

## Support hours

- **Standard hours:** Sunday to Thursday, 8:00 AM – 5:00 PM (Riyadh time, UTC+3).
- **After-hours on-call:** Available 24/7 for **P1 (Critical)** issues only, by phone at extension 4357. Press 1 for the on-call engineer.
- Requests submitted outside standard hours are handled the next business day unless they are P1.

## Ticket priorities and response times

| Priority | Example | First response | Target resolution |
|---|---|---|---|
| P1 – Critical | Company-wide outage, security breach, ransomware | 15 minutes | 4 hours |
| P2 – High | One team cannot work, VPN down for a department | 1 hour | 1 business day |
| P3 – Medium | One user cannot use an app, printer not working | 4 business hours | 3 business days |
| P4 – Low | New software request, general question | 1 business day | 5 business days |

The Service Desk sets the final priority based on business impact.

## What to include in a ticket

To help us solve your issue faster, include:

1. Your full name and employee ID.
2. Your device's asset tag (the sticker on the bottom of your laptop, starting with `DF-`).
3. A clear description of the problem and when it started.
4. Any error messages (a screenshot is best).
5. What you already tried.

## Self-service first

Many common issues can be solved without a ticket. See the knowledge base articles for password resets, MFA setup, VPN, Wi-Fi, printers, and Outlook problems.

---


# Password Reset and Password Policy

Your Dunefield account (your email address, e.g. `firstname.lastname@dunefield.example`) is used to sign in to your laptop, email, the DuneDesk portal, VPN, and most company apps.

## Password requirements

- Minimum **14 characters**.
- Must include at least three of: uppercase letters, lowercase letters, numbers, symbols.
- Cannot contain your name, username, or the word "Dunefield".
- Cannot reuse any of your last **10** passwords.
- Passwords expire every **180 days**. You will receive email reminders 14, 7, and 1 day before expiry.

**Tip:** Use a passphrase such as `Coffee-Desert-Train-42!`. Long passphrases are easier to remember and harder to crack.

## Reset a forgotten password (self-service)

1. Go to https://reset.dunefield.example from any device (phone or personal computer).
2. Enter your company email address.
3. Verify your identity using your registered MFA method (authenticator app code or SMS).
4. Choose a new password that meets the requirements above.
5. On your laptop, connect to the office network or VPN and lock/unlock your computer (Windows key + L) so the new password syncs.

Self-service reset only works if you have already set up MFA. See "MFA Setup".

## Change your password before it expires

1. Press **Ctrl + Alt + Delete** on your Dunefield laptop.
2. Select **Change a password**.
3. Enter your old password, then the new one twice.

If you are working remotely, connect to the VPN first so your laptop and your account stay in sync.

## After changing your password

Update the password on any device that uses your account, especially your phone's email app. Old passwords saved on phones are the most common cause of account lockouts.

## When to contact IT Support

Call extension 4357 if:

- You never set up MFA and cannot use self-service reset.
- The reset site says your account is disabled.
- You suspect someone else knows your password (this is also a security incident; see "Reporting a Security Incident").

IT staff will **never** ask you for your password by phone, email, or chat.

---


# Multi-Factor Authentication (MFA) Setup

Multi-factor authentication (MFA) is **mandatory** for all Dunefield Systems accounts. When you sign in from a new device or from outside the office, you must confirm your identity with a second factor in addition to your password.

## Approved MFA methods

| Method | Status | Notes |
|---|---|---|
| Authenticator app push notification | **Recommended** | Microsoft Authenticator or Google Authenticator |
| Authenticator app 6-digit code | Approved | Works without internet on your phone |
| Hardware security key (FIDO2) | Approved | Required for IT admins and Finance; request via DuneDesk |
| SMS text message | Backup only | Less secure; use only as a second method |

## Set up MFA for the first time

1. Install an authenticator app on your smartphone.
2. On a computer, go to https://myaccount.dunefield.example/security.
3. Sign in with your Dunefield email and password.
4. Select **Add sign-in method** → **Authenticator app**.
5. Open the app on your phone, tap **Add account** → **Work or school account**, and scan the QR code shown on screen.
6. Approve the test notification.
7. Add a **second method** (SMS or a second device) as a backup.

New employees must complete MFA setup within **3 days** of their start date.

## Getting a new phone

Set up MFA on the new phone **before** you reset or give away the old one:

1. Go to https://myaccount.dunefield.example/security.
2. Add the new phone as a sign-in method.
3. Test it, then remove the old phone.

## Lost or stolen phone

1. Call IT Support immediately at extension 4357 (24/7 for this case).
2. IT will remove the lost device from your account and issue a temporary access pass valid for 8 hours.
3. Use the temporary pass to register your new phone.

## Unexpected MFA prompts

If you receive an MFA prompt you did **not** start, **deny it** and report it right away. It may mean someone has your password. See "Reporting a Security Incident".

---


# Account Lockout

Your Dunefield account is locked automatically after **5 failed sign-in attempts within 15 minutes**. This protects your account from password-guessing attacks.

## How to tell your account is locked

You may see messages such as:

- "The referenced account is currently locked out and may not be logged on to."
- "Your account has been locked. Contact your administrator."
- Repeated password prompts in Outlook or Teams even with the correct password.

## Unlocking your account

- **Automatic unlock:** Accounts unlock on their own after **30 minutes**. Wait, then sign in carefully.
- **Self-service unlock:** Go to https://reset.dunefield.example, choose **Unlock my account**, and verify with MFA. You do not need to change your password.
- **Call IT Support:** Extension 4357 if you need access immediately and cannot use self-service. You will be asked to verify your identity with your employee ID and an MFA prompt.

## Common causes of repeated lockouts

1. **Old password saved on your phone.** Your phone's email app keeps trying the old password after you change it. Update or remove the account on your phone.
2. **Mapped network drives** using saved old credentials. Disconnect and reconnect them.
3. **Saved Wi-Fi password** for the `Dunefield-Corp` network on another device.
4. **Caps Lock** or a different keyboard language (Arabic/English) while typing.
5. Someone else trying to access your account.

## If you keep getting locked out

If your account locks more than twice in one day after fixing the causes above, open a P3 ticket in DuneDesk. IT can check the sign-in logs to find which device is sending the wrong password.

If the logs show sign-in attempts from locations you do not recognize, IT will treat it as a security incident and may require an immediate password change.

---


# Employee Offboarding and Equipment Return

When an employee or contractor leaves Dunefield Systems, IT removes access and collects company equipment to protect company data.

## For managers

Submit an **Offboarding Request** in DuneDesk as soon as the last working day is known, and at least **5 business days** in advance when possible. For urgent or involuntary departures, call IT at extension 4357 so access can be removed immediately.

The request should include:

- Last working day
- Who should receive the employee's files and mailbox access
- Whether an email auto-reply should be set

## What happens on the last day

| Time | Action |
|---|---|
| End of last working day | Account disabled, MFA and VPN access removed |
| Same day | Laptop, badge, and accessories returned |
| After 30 days | Mailbox converted to a shared mailbox for the manager (if requested) |
| After 90 days | Account and personal DuneDrive data permanently deleted |

## For departing employees

Before your last day:

1. Move work files from personal DuneDrive to your team's shared folder, or ask your manager which files to transfer.
2. Do **not** copy company data to personal devices, USB drives, or personal cloud accounts. This violates company policy.
3. Personal files on your company laptop should be removed before returning it.
4. Return all equipment to the IT Service Desk: laptop, charger, badge, monitor, docking station, headset, and any security key.

Remote employees receive a prepaid return box. Equipment must be shipped within **5 business days** after the last day.

## Unreturned equipment

If equipment is not returned within 10 business days, HR is notified and the cost may be deducted from the final settlement, according to the employment contract.

---


# Software Installation Policy

To keep company devices secure and licensed, employees do **not** have administrator rights on their laptops. Software must be installed from approved sources.

## Option 1: Company Portal (self-service, instant)

Most approved software can be installed without a ticket:

1. Open **Company Portal** from the Start menu.
2. Browse or search for the app.
3. Click **Install**.

Examples available in Company Portal:

- Microsoft Office apps, Teams, OneNote
- Google Chrome, Mozilla Firefox
- Zoom, Adobe Acrobat Reader
- 7-Zip, Notepad++
- Visual Studio Code, Git, Python (for Engineering and Data teams)
- DuneConnect VPN, Dunefield Secure Print

## Option 2: Software request (for anything not in Company Portal)

1. Open DuneDesk → **Software Request**.
2. Enter the software name, version, vendor website, and business reason.
3. Your manager approves the request.
4. IT Security reviews the software (security, privacy, and license).
5. If approved, IT installs it or adds it to Company Portal.

Typical review time: **3–5 business days**. Paid software also needs a budget code from your department.

## Not allowed

- Pirated or "cracked" software, or license keys from unofficial sources.
- Personal VPNs, torrent clients, and remote-control tools not approved by IT.
- Browser extensions that request access to "all websites", unless approved.
- Unofficial AI tools that upload company documents. Use only AI tools listed in Company Portal.

Unapproved software found on company devices is removed automatically, and repeated violations are reported to your manager.

## Temporary admin rights

Engineers who need admin rights for development can request **Privileged Access** in DuneDesk. If approved, admin rights are granted for **4 hours** at a time and every action is logged.

## Software updates

Security updates for Windows and approved apps install automatically. You may be asked to restart; please do not postpone restarts for more than **3 days**. After 7 days, your laptop restarts automatically outside working hours.

---


# Reporting a Security Incident

A security incident is any event that could put company data, systems, or people at risk. **Report it immediately**, even if you are not sure. Reporting quickly reduces the damage. You will not be punished for reporting an honest mistake.

## Examples of security incidents

- You clicked a link or opened an attachment in a suspicious email.
- You entered your password on a website that looked fake.
- You received an MFA prompt you did not start.
- Your laptop, phone, or badge was lost or stolen.
- You sent confidential data to the wrong person.
- Your computer shows ransom messages, or files are suddenly encrypted or renamed.
- Someone you don't recognize asks for your password, MFA code, or access.

## How to report

| Situation | How to report |
|---|---|
| Urgent (ransomware, stolen device, account takeover) | **Call extension 4357, press 2** for the Security team (24/7) |
| Suspicious email | Click **Report Phishing** in Outlook (see "Phishing Emails") |
| Other concerns | Email security@dunefield.example or open a **Security** ticket in DuneDesk |

## What to do right away

1. **Disconnect from the network** if you suspect malware or ransomware: turn off Wi-Fi and unplug the network cable. **Do not shut down** the computer; investigators may need its memory.
2. **Change your password** from a different, trusted device if you entered it on a suspicious site.
3. **Do not delete** the suspicious email, files, or messages. The Security team needs them for investigation.
4. **Write down** what happened and when: what you clicked, what you saw, and any error messages.
5. **Do not try to investigate yourself** or forward suspicious attachments to colleagues.

## What happens next

The Security team will:

1. Contact you within **15 minutes** for urgent reports.
2. Secure your account (for example, reset your password and sign you out of all sessions).
3. Check your device and may temporarily replace it.
4. Inform you when the incident is closed and share any lessons learned.

Incidents involving personal data may need to be reported to regulators within strict deadlines, which is why fast reporting is essential.

---


# Recognizing and Reporting Phishing Emails

Phishing emails try to trick you into clicking a malicious link, opening an infected attachment, sharing your password, or sending money. Phishing is the most common way attackers break into companies.

## Warning signs

- **Urgency or threats:** "Your account will be deleted in 24 hours", "Pay this invoice today".
- **Unexpected requests** for passwords, MFA codes, gift cards, or bank transfers.
- **Sender address mismatch:** the display name says "IT Support" but the address is `it-support@dunefie1d-help.com`.
- **External warning banner:** Dunefield adds a yellow **[EXTERNAL]** banner to emails from outside the company. Be extra careful when an "internal" request has this banner.
- **Suspicious links:** hover over a link (don't click) to see the real address. Real company sites end in `dunefield.example` or `dunefield.internal`.
- **Unexpected attachments**, especially `.zip`, `.html`, `.exe`, `.iso`, or Office files asking you to "Enable Content".
- Spelling mistakes, unusual greetings, or a tone that doesn't match the sender.

## How to report a phishing email

1. In Outlook, select the email.
2. Click **Report Phishing** on the toolbar (or the **…** menu → **Report** → **Report phishing**).
3. The email is removed from your inbox and sent to the Security team.

Do **not** forward the email to colleagues, reply to it, or click any links "to check".

## If you already clicked or replied

Report it immediately as a security incident: call extension 4357 and press 2. See "Reporting a Security Incident". Acting quickly matters more than anything else.

## Payment and bank change requests

Finance will **never** change a supplier's bank details or approve an urgent payment based only on email. Always verify by calling the person on a phone number you already know, not one provided in the email.

## Phishing simulations

IT Security sends practice phishing emails several times a year. If you report one, you'll see a "Well done" message. If you click one, you'll be asked to complete a short refresher training. These simulations are for learning, not punishment.

---


# Acceptable Use Policy (Summary)

This is a summary of the Dunefield Systems Acceptable Use Policy (AUP). All employees and contractors must read and accept the full policy during onboarding and once a year after that.

## Company devices and accounts

- Company laptops, phones, and accounts are for **business use**. Limited personal use (for example, checking personal news during a break) is allowed if it does not affect work or security.
- Do not share your password, MFA codes, badge, or laptop with anyone, including colleagues and IT staff.
- Lock your screen (Windows key + L) whenever you leave your laptop, even for a short time. Screens lock automatically after **5 minutes** of inactivity.
- Do not disable or bypass security tools such as antivirus, encryption, or device management.

## Data handling

Company data is classified into four levels:

| Level | Examples | Rules |
|---|---|---|
| Public | Marketing website content | Can be shared freely |
| Internal | Org charts, internal announcements | Share only within Dunefield |
| Confidential | Customer data, contracts, financials | Share only with people who need it; use encryption for external sharing |
| Restricted | Passwords, payroll, security reports | Access only with explicit approval |

- Store company files only in approved locations: DuneDrive, department shared folders, or approved business apps.
- Do not upload Confidential or Restricted data to personal email, personal cloud storage, or unapproved AI tools.
- USB storage devices are **blocked** by default. Exceptions require IT Security approval.

## Internet and email

- Do not visit illegal, offensive, or gambling websites. Web filtering blocks many such sites.
- Do not use company email to sign up for personal services.
- Be respectful in all company communications.

## Monitoring

Dunefield Systems monitors company devices, networks, and accounts for security purposes, in line with applicable law. Employees should not expect privacy for personal content stored on company systems.

## Violations

Violations of this policy may lead to loss of access, disciplinary action, or termination, depending on severity. Questions about the policy can be sent to it-help@dunefield.example.

---

