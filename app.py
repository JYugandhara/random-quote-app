from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    # Motivational
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs", "theme": "Motivational"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius", "theme": "Motivational"},
    {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill", "theme": "Motivational"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt", "theme": "Motivational"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson", "theme": "Motivational"},

    # Programming / Tech
    {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler", "theme": "Programming"},
    {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson", "theme": "Programming"},
    {"text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House", "theme": "Programming"},
    {"text": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Harold Abelson", "theme": "Programming"},
    {"text": "The best error message is the one that never shows up.", "author": "Thomas Fuchs", "theme": "Programming"},

    # Life Wisdom
    {"text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein", "theme": "Life"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon", "theme": "Life"},
    {"text": "The purpose of our lives is to be happy.", "author": "Dalai Lama", "theme": "Life"},
    {"text": "Get busy living or get busy dying.", "author": "Stephen King", "theme": "Life"},
    {"text": "You only live once, but if you do it right, once is enough.", "author": "Mae West", "theme": "Life"},

    # Funny
    {"text": "I choose a lazy person to do a hard job, because a lazy person will find an easy way to do it.", "author": "Bill Gates", "theme": "Funny"},
    {"text": "My software never has bugs. It just develops random features.", "author": "Anonymous", "theme": "Funny"},
    {"text": "Why do programmers prefer dark mode? Because light attracts bugs!", "author": "Anonymous", "theme": "Funny"},
    {"text": "There are only 10 types of people: those who understand binary and those who don't.", "author": "Anonymous", "theme": "Funny"},
    {"text": "A day without sunshine is like, you know, night.", "author": "Steve Martin", "theme": "Funny"},

    # Success
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain", "theme": "Success"},
    {"text": "Don't be afraid to give up the good to go for the great.", "author": "John D. Rockefeller", "theme": "Success"},
    {"text": "I find that the harder I work, the more luck I seem to have.", "author": "Thomas Jefferson", "theme": "Success"},
    {"text": "Opportunities don't happen. You create them.", "author": "Chris Grosser", "theme": "Success"},
    {"text": "Dream big and dare to fail.", "author": "Norman Vaughan", "theme": "Success"},

    # Nature
    {"text": "Look deep into nature, and then you will understand everything better.", "author": "Albert Einstein", "theme": "Nature"},
    {"text": "In every walk with nature, one receives far more than he seeks.", "author": "John Muir", "theme": "Nature"},

    # Leadership
    {"text": "A leader is one who knows the way, goes the way, and shows the way.", "author": "John C. Maxwell", "theme": "Leadership"},
    {"text": "The greatest leader is not necessarily the one who does the greatest things.", "author": "Ronald Reagan", "theme": "Leadership"},

    # Wisdom
    {"text": "The only true wisdom is in knowing you know nothing.", "author": "Socrates", "theme": "Wisdom"},
    {"text": "Turn your wounds into wisdom.", "author": "Oprah Winfrey", "theme": "Wisdom"},
]

@app.route("/")
def index():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/api/quote")
def api_quote():
    quote = random.choice(quotes)
    return {"quote": quote["text"], "author": quote["author"], "theme": quote["theme"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)