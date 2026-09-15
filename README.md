# 🛡️ Hindustan Hack

**Hindustan Hack** is a powerful, lightweight CLI suite designed for Termux and Linux, featuring advanced phone number intelligence and OSINT lookup capabilities.

## ✨ Features
- 🔍 **Number Lookup (OSINT):** Query mobile numbers via secure API endpoints with detailed record extraction.
- 📊 **Rich Data Tables:** Formats records, registration info, Aadhaar details, and telecom circles into clean, color-coded tables.
- 📱 **Mobile Friendly:** Designed specifically for Termux and narrow terminal displays.
- ⚡ **Batch Processing:** Support for querying multiple comma-separated numbers simultaneously.
- 🎨 **Terminal UI:** Built using Python's `rich` library and `pyfiglet` for visual headers.

## 🛠️ Prerequisites
Make sure you have Python 3 and Git installed on your system or Termux.

## 📥 Installation & Deployment

```bash
pkg update && upgrade
termux-setup-storage
pkg install python
pkg install git
git clone https://github.com/hindustanhack/HINDUSTAN-HACK
cd HINDUSTAN-HACK
pip install -r requirements.txt
python hindustanosint.py
