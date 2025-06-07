'''import speech_recognition as sr
import pyttsx3
import time
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai  # Gemini API library


# Configure the Gemini API with your API key
openai.api_key = "AIzaSyDliTjiJL0o3Gm0wQHerzy1Q5S4vvOG-oY"

# Predefined training data and responses
training_sentences = [
    "hello", "how are you", "who are you", "time", "what is the time",
    "flip a coin", "roll a dice", "attendance tracking", "fee management", "exam performance",
    "AI chatbot", "parent communication", "library management", "cloud system", "role-based access",
    "next cm","AI in education",  "how to update profile", "add course", "manage course", "add subject",
    "add session", "add staff", "view attendance", "date", "whats the date", 
    "today's date", "your name", "what is your name", "what date is it", "what day is it"
]

responses = [
    "Hello! How can I help?",
    "I'm doing great! Thanks for asking.",
    "I'm Webzy, your AI assistant.",
    f"The current time is {time.strftime('%I:%M %p')}",
    "It's " + ("Heads!" if time.time() % 2 > 1 else "Tails!"),
    f"You rolled a {str(int(time.time() % 6) + 1)}",
    "Marks attendance automatically and generates reports.",
    "Allows online payments and sends reminders.",
    "Analyzes student results to improve learning.",
    "Helps students with quick answers and guidance.",
    "Keeps parents updated on student progress.",
    "Helps students find books and study materials online.",
    "Stores data securely and makes access easy anywhere.",
    "Gives different permissions to students, teachers, and admins.",
    "Uses AI to personalize learning and predict student needs.",
    "Thalapathy Vijay Sir.",
    "In the left sidebar, at the top option, click to update your profile.",
    "In the sidebar, select the second option. If you see any sub-options inside, it will show the 'add subject' option.",
    "It is shown inside the course options.",
    "It is shown on the left side in the second option. Select it to add the subject.",
    "It is shown as the third option in the same list. Click to add or manage the session.",
    "It is shown as the fourth option. A person symbol with a plus sign is visible—click it to add staff.",
    "Below the staff and student notify options, a calendar symbol appears. Click it to view attendance.",
    f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "My name is Webzy, your website assistant.",
    "I am Webzy, your website assistant.",
]

# Initialize the vectorizer only once
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)

# Gemini API fallback function
def get_gemini_reply_from_api(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another model like "gpt-3.5-turbo"
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"[ERROR] Error with API: {e}")
        return "Sorry, I couldn't process your request."

# Function to get chatbot's reply
def get_gemini_reply(prompt, threshold=0.6):  # Lowered threshold for better matching
    try:
        print(f"[DEBUG] Received prompt: {prompt}")
        input_vec = vectorizer.transform([prompt])
        similarity_scores = cosine_similarity(input_vec, X)
        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_match_index]

        print(f"[DEBUG] Best match index: {best_match_index}, Score: {best_score}")

        if best_score >= threshold:
            reply = responses[best_match_index]
            print(f"[DEBUG] Returning predefined response: {reply}")
            return reply
        else:
            # If no good match found, fallback to Gemini API
            return get_gemini_reply_from_api(prompt)
    except Exception as e:
        print(f"[ERROR] Exception in get_gemini_reply: {e}")
        return "I'm sorry, I couldn't process your request. Please try again later."

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Processing your input...")
            text = recognizer.recognize_google(audio)
            print(f"[DEBUG] Recognized speech: {text}")
            return text
        except sr.UnknownValueError:
            print("[ERROR] Could not understand the audio.")
            return "Sorry, I couldn't understand your speech."
        except sr.RequestError as e:
            print(f"[ERROR] Could not request results from Google Speech Recognition service; {e}")
            return "Sorry, there was an issue with the speech recognition service."

# Function to speak out the response
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

# Main chatbot function with voice and keyboard input
def chatbot_with_voice_and_keyboard():
    print("Welcome to the Voice-Enabled Chatbot!")
    
    # Initial greeting when page is loaded
    initial_greeting = "Hi, I am Webzy. How can I help you?"
    speak_text(initial_greeting)
    print(initial_greeting)

    while True:
              # Check if Enter key is pressed
            user_input = input("You: ")  # Get text input when Enter is pressed
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Exiting chatbot. Goodbye!")
                break
            response = get_gemini_reply(user_input)
            print(f"Chatbot: {response}")
            speak_text(response)
        
        # Optionally, add the speech recognition here if you want to support both

if __name__ == "__main__":
    chatbot_with_voice_and_keyboard()'''

# main_app/gemini_api.py
import pyttsx3
import sys
import time
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import re
import random

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyDliTjiJL0o3Gm0wQHerzy1Q5S4vvOG-oY") 

# Top of your file
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Predefined training data and responses
qa_pairs = {
    # Greetings and Basic Interaction
    "hello": "Hello! How can I help?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "who are you": "I'm Webzy, your AI assistant.",
    "your name": "My name is Webzy, your website assistant.",
    "what is your name": "My name is Webzy, your website assistant.",
    "what can you do": "I can help answer questions, guide you through the website, and provide quick facts.",
    "are you human": "No, I'm a virtual assistant created to help you!",
    "who created you": "I was built by  MGS that means M is Masif , G is Guna , S is Sakthi",
    "who built you":"I was built by  MGS that means M is Masif , G is Guna , S is Sakthi",
    "who made you":"I was built by  MGS that means M is Masif , G is Guna , S is Sakthi",
    "that means":"that's mean M is Masif ,G is Guna and S is Sakthi",
    'what is the full form of MGS':"The Full form of MGS is Masif,Guna,Sakthi",
    "standard of MGS":"The standard of MGS is Masif,Guna and Sakthi",
    'what is the represent of MGS':'The represent of MGS is Masif,Guna and Sakthi',
    'represent of MGS':'The represent of MGS is Masif,Guna and Sakthi', 
       
    

    # Time & Date
    "time": f"The current time is {time.strftime('%I:%M %p')}",
    "what is the time": f"The current time is {time.strftime('%I:%M %p')}",
    "date": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "what is the date": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "whats the date": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "today's date": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "what date is it": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
    "what day is it": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",

    # Student Management Project Related
    # Update profile
    "how to update profile": "In the left sidebar, at the top, click the first option to update your profile.",
    "where is update profile": "In the left sidebar, at the top, click the first option to update your profile.",
    "update my profile": "In the left sidebar, at the top, click the first option to update your profile.",
    "profile update option": "In the left sidebar, at the top, click the first option to update your profile.",
    "edit my profile": "In the left sidebar, at the top, click the first option to update your profile.",

    # Add Course
    "how to add course": "In the sidebar, click the second option. If it expands, you'll see the 'Add Subject' option inside.",
    "where is add course option": "In the sidebar, click the second option. If it expands, you'll see the 'Add Subject' option inside.",
    "add course": "In the sidebar, click the second option. If it expands, you'll see the 'Add Subject' option inside.",
    "course adding option": "In the sidebar, click the second option. If it expands, you'll see the 'Add Subject' option inside.",

    # Manage Student
    "manage student": "You see the left sidebar. Below 'Add Student', it shows 'Manage Student'. Click to manage student records.",
    "how to manage student": "You see the left sidebar. Below 'Add Student', it shows 'Manage Student'. Click to manage student records.",
    "where is manage student": "You see the left sidebar. Below 'Add Student', it shows 'Manage Student'. Click to manage student records.",
    "student management": "You see the left sidebar. Below 'Add Student', it shows 'Manage Student'. Click to manage student records.",

    # Notify Staff
    "notify staff": "It appears below 'Manage Student' in the sidebar with a speaker icon. Click to notify staff.",
    "how to notify staff": "It appears below 'Manage Student' in the sidebar with a speaker icon. Click to notify staff.",
    "where is staff notify option": "It appears below 'Manage Student' in the sidebar with a speaker icon. Click to notify staff.",

    # Notify Student
    "notify student": "It appears below 'Notify Staff' with a speaker icon. Click to notify students.",
    "how to notify student": "It appears below 'Notify Staff' with a speaker icon. Click to notify students.",
    "where is student notify option": "It appears below 'Notify Staff' with a speaker icon. Click to notify students.",

    # View Attendance
    "view attendance": "Below 'Notify Student', it shows 'View Attendance' with a calendar icon.",
    "how to view attendance": "Below 'Notify Student', it shows 'View Attendance' with a calendar icon.",
    "where is attendance view": "Below 'Notify Student', it shows 'View Attendance' with a calendar icon.",

     # Add Student
    "add student": "In the left sidebar, click 'Add Student' to register a new student.",
    "how to add student": "In the left sidebar, click 'Add Student' to register a new student.",
    "where is add student": "In the left sidebar, click 'Add Student' to register a new student.",
    "student registration": "In the left sidebar, click 'Add Student' to register a new student.",

    # Manage Student
    "manage student": "In the sidebar, under 'Add Student', click 'Manage Student' to view and edit student details.",
    "how to manage student": "In the sidebar, under 'Add Student', click 'Manage Student' to view and edit student details.",
    "edit student": "In the sidebar, under 'Add Student', click 'Manage Student' to view and edit student details.",
    "where is manage student": "In the sidebar, under 'Add Student', click 'Manage Student' to view and edit student details.",

    # Notify Staff
    "notify staff": "Under 'Manage Student', click the speaker symbol to notify staff.",
    "how to notify staff": "Under 'Manage Student', click the speaker symbol to notify staff.",
    "send message to staff": "Under 'Manage Student', click the speaker symbol to notify staff.",
    "where is notify staff": "Under 'Manage Student', click the speaker symbol to notify staff.",

    # Notify Student
    "notify student": "Below 'Notify Staff', click the speaker icon to notify students.",
    "how to notify student": "Below 'Notify Staff', click the speaker icon to notify students.",
    "send message to student": "Below 'Notify Staff', click the speaker icon to notify students.",
    "where is notify student": "Below 'Notify Staff', click the speaker icon to notify students.",

    # View Attendance
    "view attendance": "Click the calendar symbol below 'Notify Student' to view attendance.",
    "how to view attendance": "Click the calendar symbol below 'Notify Student' to view attendance.",
    "check attendance": "Click the calendar symbol below 'Notify Student' to view attendance.",
    "where is attendance": "Click the calendar symbol below 'Notify Student' to view attendance.",

    # Update Profile
    "update profile": "You can update your profile from the top option in the left sidebar.",
    "how to update profile": "You can update your profile from the top option in the left sidebar.",
    "where is update profile": "You can update your profile from the top option in the left sidebar.",
    "edit my profile": "You can update your profile from the top option in the left sidebar.",

    # Add Staff
    "add staff": "Click the fourth option in the sidebar with a person symbol and plus sign to add staff.",
    "how to add staff": "Click the fourth option in the sidebar with a person symbol and plus sign to add staff.",
    "register staff": "Click the fourth option in the sidebar with a person symbol and plus sign to add staff.",
    "where is add staff": "Click the fourth option in the sidebar with a person symbol and plus sign to add staff.",

    # Manage Staff
    "manage staff": "Below 'Add Staff', click the option with a table symbol to manage staff.",
    "how to manage staff": "Below 'Add Staff', click the option with a table symbol to manage staff.",
    "edit staff": "Below 'Add Staff', click the option with a table symbol to manage staff.",
    "where is manage staff": "Below 'Add Staff', click the option with a table symbol to manage staff.",

    # Add Course
    "add course": "In the sidebar, select the second option and choose 'Add Course' from the dropdown.",
    "how to add course": "In the sidebar, select the second option and choose 'Add Course' from the dropdown.",
    "where is add course": "In the sidebar, select the second option and choose 'Add Course' from the dropdown.",
    "course addition": "In the sidebar, select the second option and choose 'Add Course' from the dropdown.",

    # Manage Course
    "manage course": "You can find 'Manage Course' under the course options in the sidebar.",
    "how to manage course": "You can find 'Manage Course' under the course options in the sidebar.",
    "edit course": "You can find 'Manage Course' under the course options in the sidebar.",
    "where is manage course": "You can find 'Manage Course' under the course options in the sidebar.",

    # Add Subject
    "add subject": "Select the second option in the sidebar and choose 'Add Subject'.",
    "how to add subject": "Select the second option in the sidebar and choose 'Add Subject'.",
    "where is add subject": "Select the second option in the sidebar and choose 'Add Subject'.",
    "subject addition": "Select the second option in the sidebar and choose 'Add Subject'.",

    # Add Session
    "add session": "Click the third option in the sidebar to add or manage sessions.",
    "how to add session": "Click the third option in the sidebar to add or manage sessions.",
    "where is add session": "Click the third option in the sidebar to add or manage sessions.",
    "create session": "Click the third option in the sidebar to add or manage sessions.",

    # Logout
    "how to logout": "To remove your details from the website, scroll to the last option in the sidebar and click 'Logout'.",
    "logout": "To remove your details from the website, scroll to the last option in the sidebar and click 'Logout'.",
    "where is logout": "To remove your details from the website, scroll to the last option in the sidebar and click 'Logout'.",
    "exit from account": "To remove your details from the website, scroll to the last option in the sidebar and click 'Logout'.",


    # Just for fun
    "flip a coin": "It's " + ("Heads!" if time.time() % 2 > 1 else "Tails!"),
    "roll a dice": f"You rolled a {str(int(time.time() % 6) + 1)}",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "tell me a fun fact": "Did you know? Honey never spoils!",

    "how to manage student": "You see the left sidebar. After 'Add Student', you will find 'Manage Student'. Click it to manage student details.",
    "show manage student": "You see the left sidebar. After 'Add Student', you will find 'Manage Student'. Click it to manage student details.",
    "where is manage student": "You see the left sidebar. After 'Add Student', you will find 'Manage Student'. Click it to manage student details.",

    "how to notify staff": "Notify Staff will appear below Manage Student in the left sidebar. It shows a speaker symbol next to it.",
    "notify staff option": "Notify Staff will appear below Manage Student in the left sidebar. It shows a speaker symbol next to it.",
    "where is notify staff": "Notify Staff will appear below Manage Student in the left sidebar. It shows a speaker symbol next to it.",

    "how to notify student": "Notify Student appears below Notify Staff. It also shows a speaker symbol beside it.",
    "notify student option": "Notify Student appears below Notify Staff. It also shows a speaker symbol beside it.",
    "where is notify student": "Notify Student appears below Notify Staff. It also shows a speaker symbol beside it.",

    "view attendance": "Below Notify Student, you will find View Attendance. It is shown with a calendar icon.",
    "how to check attendance": "Below Notify Student, you will find View Attendance. It is shown with a calendar icon.",
    "attendance with calendar": "Below Notify Student, you will find View Attendance. It is shown with a calendar icon.",

    "student feedback": "Student Feedback is listed below View Attendance in the left sidebar.",
    "how to see student feedback": "Student Feedback is listed below View Attendance in the left sidebar.",

    "staff feedback": "Staff Feedback appears just below Student Feedback in the sidebar menu.",
    "how to check staff feedback": "Staff Feedback appears just below Student Feedback in the sidebar menu.",

    "staff leave": "Staff Leave is shown below Staff Feedback in the sidebar list.",
    "check staff leave": "Staff Leave is shown below Staff Feedback in the sidebar list.",
    "where is staff leave": "Staff Leave is shown below Staff Feedback in the sidebar list.",

    "student leave": "Student Leave comes right below Staff Leave in the sidebar.",
    "check student leave": "Student Leave comes right below Staff Leave in the sidebar.",
    "where is student leave": "Student Leave comes right below Staff Leave in the sidebar.",

    "how to logout": "To logout, click the Logout option at the bottom of the sidebar. It will safely remove your details from the website.",
    "exit website": "To logout, click the Logout option at the bottom of the sidebar. It will safely remove your details from the website.",
    "remove my details": "To logout, click the Logout option at the bottom of the sidebar. It will safely remove your details from the website.",
   

    # Fun, Games, and Misc
    "flip a coin": "It's " + ("Heads!" if time.time() % 2 > 1 else "Tails!"),
    "roll a dice": f"You rolled a {str(int(time.time() % 6) + 1)}",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "tell me a fun fact": "Did you know? Honey never spoils!",
    "write a short poem": "Roses are red, violets are blue, I'm an AI assistant, here to help you!",

    # General Knowledge
    "capital of japan": "The capital of Japan is Tokyo.",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
    "who is the prime minister of india": "As of 2025, the Prime Minister of India is Narendra Modi.",
    "who is the president of usa": "As of 2025, the President of the USA is Joe Biden.",
    "how many continents are there": "There are 7 continents on Earth.",
    "how many days in a year": "There are 365 days in a year (or 366 in a leap year).",
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",

    # Math and Logic
    "what is 2 plus 2": "2 plus 2 is 4.",
    "what is the square root of 16": "The square root of 16 is 4.",
    "is 7 a prime number": "Yes, 7 is a prime number.",

    # Local Personality/Interest
    "next cm": "Thalapathy Vijay Sir.",
    "AI in education": "Uses AI to personalize learning and predict student needs."
}


#prepare training data
training_sentences = list(qa_pairs.keys())
responses=list(qa_pairs.values())
# Initialize vectorizer once
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)


# Gemini fallback function
def get_gemini_reply_from_api(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        # Gemini new response structure parsing
        if hasattr(response, 'text') and response.text.strip():
            return response.text.strip()
        
        if hasattr(response, 'candidates') and response.candidates:
            parts = response.candidates[0].content.parts
            if parts and hasattr(parts[0],'text'):
                return parts[0].text.strip()
        
        return "I'm sorry, I couldn't understand your request."
        
    except Exception as e:
        print(f"[ERROR] Error with API: {e}")
        return "Sorry, I couldn't process your request."
    


def clean_text(text):
    # Normalize user input: lowercase, remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text
# Main chatbot reply function
def get_gemini_reply(prompt, threshold=0.75):
    prompt = clean_text(prompt)

    if 'stop' in prompt or 'exit' in prompt:
        speak("Stopping the program. Goodbye!")
        print("Webzy: Stopping the program. Goodbye!")
        return  "the program has stopped.Goodbye"
        sys.exit()
    try:
        #normalized_prompt =prompt.lower().strip()
        input_vec = vectorizer.transform([prompt])
        similarity_scores = cosine_similarity(input_vec, X)
        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_match_index]
        print(f"[DEBUG] Best Match Score: {best_score} for '{training_sentences[best_match_index]}'")
       
        if best_score >= threshold:
            return responses[best_match_index]
        else:
            print(f"[DEBUG] Fallback to Gemini API for '{prompt}'")
            fallback = get_gemini_reply_from_api(prompt)
            if not fallback or fallback.strip() == "":
                return "Sorry, I couldn't find an answer. Please try rephrasing."
            return fallback
            '''try:
                gemini_response = get_gemini_reply_from_api(prompt)
                if not gemini_response or gemini_response.strip() == "":
                    return "I'm sorry, I couldn't find a response. Can you try rephrasing?"
                return gemini_response
            except Exception as api_error:
                print(f"[GEMINI API ERROR] {api_error}")
                return "I'm sorry, I couldn't process your request through the AI service."'''
    except Exception as e:
        print(f"[ERROR] Exception in get_gemini_reply: {e}")
        return "I'm sorry, I couldn't process your request. Please try again later."

