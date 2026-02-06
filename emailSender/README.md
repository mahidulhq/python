# Basic Email Sender (lame)

**DEPRECATED** - Uses Less Secure Apps (disabled January 2025).

Simple console-based Gmail sender using SMTP.

## Python Libraries Used

- `smtplib` - SMTP email sending protocol

## SMTP Configuration

- **Server**: `smtp.gmail.com:578`
- **Auth**: Username/password (plain text - insecure)
- **Security**: STARTTLS encryption

## Features

- Interactive email input (recipient + content)
- Basic Gmail SMTP connection
- Send emails from console

## Usage

```bash
python mailSender.py
```

1. Enter recipient email
2. Write email content
3. Sends immediately

## Code Flow

```
Input → SMTP Connect → STARTTLS → Login → Send → Close
```

## Limitations & Security Issues

- Uses deprecated Less Secure Apps method
- Plain text password (hardcoded)
- Non-standard SMTP port (578)
- No error handling
- **Not production-ready**

## Status

**Educational prototype only.** Requires modern alternatives:
- App Passwords (if enabled)
- OAuth2
- Gmail API

***