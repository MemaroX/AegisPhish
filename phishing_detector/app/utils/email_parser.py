import email
from email import policy
from email.parser import BytesParser

def parse_email(raw_email_content: str) -> dict:
    """
    Parses raw email content (string) into a structured dictionary.
    """
    msg = email.message_from_string(raw_email_content, policy=policy.default)

    parsed_email = {
        "headers": {},
        "body": {
            "plain": "",
            "html": ""
        },
        "attachments": []
    }

    # Extract headers
    for header, value in msg.items():
        parsed_email["headers"][header] = value

    # Extract body parts
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdisp = part.get('Content-Disposition')

            if ctype == 'text/plain' and cdisp is None:
                parsed_email["body"]["plain"] = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='ignore')
            elif ctype == 'text/html' and cdisp is None:
                parsed_email["body"]["html"] = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='ignore')
            elif cdisp and cdisp.startswith('attachment'):
                filename = part.get_filename()
                if filename:
                    parsed_email["attachments"].append({
                        "filename": filename,
                        "content_type": ctype,
                        "size": len(part.get_payload(decode=True))
                    })
    else:
        ctype = msg.get_content_type()
        if ctype == 'text/plain':
            parsed_email["body"]["plain"] = msg.get_payload(decode=True).decode(msg.get_content_charset() or 'utf-8', errors='ignore')
        elif ctype == 'text/html':
            parsed_email["body"]["html"] = msg.get_payload(decode=True).decode(msg.get_content_charset() or 'utf-8', errors='ignore')

    return parsed_email

# Example Usage (for testing purposes, not part of the module)
if __name__ == '__main__':
    sample_email = """From: Sender <sender@example.com>
To: Recipient <recipient@example.com>
Subject: Test Email
Content-Type: multipart/alternative; boundary="----=_Part_0_123456789.123456789"

------=_Part_0_123456789.123456789
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

This is the plain text body.

------=_Part_0_123456789.123456789
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

<html><body><p>This is the <b>HTML</b> body.</p></body></html>

------=_Part_0_123456789.123456789--
"""
    parsed = parse_email(sample_email)
    print("Headers:", parsed["headers"])
    print("Plain Body:", parsed["body"]["plain"])
    print("HTML Body:", parsed["body"]["html"])
    print("Attachments:", parsed["attachments"])

    sample_email_with_attachment = """From: Sender <sender@example.com>
To: Recipient <recipient@example.com>
Subject: Email with Attachment
Content-Type: multipart/mixed; boundary="----=_Part_1_987654321.987654321"

------=_Part_1_987654321.987654321
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

This is the main body.

------=_Part_1_987654321.987654321
Content-Type: text/plain; name="attachment.txt"
Content-Disposition: attachment; filename="attachment.txt"
Content-Transfer-Encoding: base64

SGVsbG8sIHRoaXMgZmlsZSBpcyBhbiBhdHRhY2htZW50Lg==

------=_Part_1_987654321.987654321--
"""
    parsed_attach = parse_email(sample_email_with_attachment)
    print("\n--- Email with Attachment ---")
    print("Headers:", parsed_attach["headers"])
    print("Plain Body:", parsed_attach["body"]["plain"])
    print("Attachments:", parsed_attach["attachments"])