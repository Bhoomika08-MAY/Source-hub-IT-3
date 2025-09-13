import tkinter as tk
import pyttsx3
import speech_recognition as sr

# Rule-based responses
def get_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "📋 Admissions open in May. Visit our website or contact the admin office."
    elif "courses" in user_input:
        return "📚 We offer B.E. in AI & ML, Computer Science, Electronics, and more."
    elif "fees" in user_input or "fee" in user_input:
        return "💰 The annual fee for B.E. in AI & ML is ₹85,000."
    elif "placement" in user_input:
        return "💼 Top recruiters include Infosys, TCS, and Wipro. Training starts in 3rd year."
    elif "facilities" in user_input or "campus" in user_input:
        return "🏫 Campus includes hostels, library, labs, Wi-Fi, and sports grounds."
    elif "contact" in user_input:
        return "📞 Reach us at +91-9876543210 or email info@college.edu"
    else:
        return "😕 Sorry, I didn’t understand that. Try asking about courses, fees, or placements."

# Text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice input
def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_chat("🎤 Listening...", "system")
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, user_input)
            send_message()
        except:
            update_chat("😅 Couldn't understand your voice.", "bot")
            speak("Couldn't understand your voice.")

# Update chat log
def update_chat(message, tag):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, message + "\n", tag)
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Send message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    update_chat(f"You: {user_input}", "user")
    response = get_response(user_input)
    update_chat(f"Bot: {response}", "bot")
    speak(response)
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("🎓 College Info Assistant")
root.geometry("800x850")
root.configure(bg="#121212")

# Header content
tk.Label(root, text="College Info Assistant – Your Smart Campus Guide", font=("Helvetica", 18, "bold"), bg="#121212", fg="#ff4081").pack(pady=10)
tk.Label(root, text="Ready to Help with College Information", font=("Segoe UI", 14), bg="#121212", fg="#ffffff").pack()
tk.Label(root, text="Welcome! Ask me about admissions, courses, fees, placements, and more.", wraplength=750, justify="center", font=("Segoe UI", 12), bg="#121212", fg="#ffffff").pack(pady=10)

# Chat log
chat_log = tk.Text(root, height=15, width=90, wrap=tk.WORD, font=("Segoe UI", 12), bg="#1c1c1c", fg="#ffffff", bd=5, relief=tk.FLAT)
chat_log.pack(pady=10)
chat_log.config(state=tk.DISABLED)
chat_log.tag_config("user", foreground="#ffffff", font=("Segoe UI", 12, "bold"))  # White
chat_log.tag_config("bot", foreground="#00bfff", font=("Segoe UI", 12))           # Sky blue
chat_log.tag_config("system", foreground="#757575", font=("Segoe UI", 11, "italic"))

# Button grid (3x2 layout)
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=10)

buttons = [
    ("Admission", "admission"),
    ("Courses", "courses"),
    ("Fees", "fees"),
    ("Placement", "placement"),
    ("Facilities", "facilities"),
    ("Contact", "contact")
]

for i, (label, keyword) in enumerate(buttons):
    btn = tk.Button(button_frame, text=label, font=("Segoe UI", 11, "bold"), width=22, height=2,
                    bg="#212121", fg="#ffffff", relief=tk.RIDGE, bd=4,
                    command=lambda k=keyword: handle_click(k))
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)

# Input + Mic + Send
input_frame = tk.Frame(root, bg="#121212")
input_frame.pack(pady=20)

# Mic icon styled like your image
voice_button = tk.Button(input_frame, text="🎤", font=("Segoe UI", 16, "bold"), bg="#ffffff", fg="#000000",
                         relief=tk.RIDGE, bd=4, width=3, height=1, command=listen_voice)
voice_button.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(input_frame, font=("Segoe UI", 14), width=50, bg="#2e2e2e", fg="#ffffff", relief=tk.FLAT, bd=6, insertbackground="white")
entry.pack(side=tk.LEFT, padx=10, ipady=12)

send_button = tk.Button(input_frame, text="Send 🚀", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#000000", relief=tk.RIDGE, bd=4, command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

def handle_click(keyword):
    update_chat(f"You: {keyword}", "user")
    response = get_response(keyword)
    update_chat(f"Bot: {response}", "bot")
    speak(response)

root.mainloop()
