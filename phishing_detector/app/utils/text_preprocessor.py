import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# Initialize NLTK stopwords
STOPWORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """
    Cleans and preprocesses text data.

    Args:
        text (str): The input text string.

    Returns:
        str: The cleaned text string.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove HTML tags
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text) # Keep only letters and spaces

    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# Example Usage (for testing purposes)
if __name__ == '__main__':
    sample_html_email = """
    <html>
    <body>
    <p>Hello, this is a <b>test</b> email with some <a href=\"#\">link</a> and numbers like 123.
    <br>
    Please visit our site at example.com!!!</p>
    </body>
    </html>
    """
    sample_plain_email = "This is a sample email. It contains some common words and punctuation! 123."

    print("--- HTML Email Preprocessing ---")
    cleaned_html = clean_text(sample_html_email)
    print(f"Original: {sample_html_email.strip()}")
    print(f"Cleaned: {cleaned_html}")

    print("\n--- Plain Email Preprocessing ---")
    cleaned_plain = clean_text(sample_plain_email)
    print(f"Original: {sample_plain_email.strip()}")
    print(f"Cleaned: {cleaned_plain}")