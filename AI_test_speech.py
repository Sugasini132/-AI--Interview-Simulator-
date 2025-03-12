import speech_recognition as sr  
import random  
import time  
from textblob import TextBlob  
import nltk  

nltk.download('punkt')  

recognizer = sr.Recognizer()  

# Job roles with specific feedback criteria  
job_roles = {  
    "Software Engineer": "Focus on problem-solving, coding skills, and logic.",  
    "Data Analyst": "Focus on data interpretation, insights, and visualization.",  
    "Marketing Specialist": "Focus on creativity, strategy, and communication."  
}  

# List of interview questions  
interview_questions = [  
    "Tell me about yourself.",  
    "What are your strengths and weaknesses?",  
    "Why do you want this job?",  
    "Describe a challenge you faced and how you handled it.",  
    "Where do you see yourself in five years?"  
]  

# User selects job role  
print("🎯 Select your job role:")  
for idx, role in enumerate(job_roles.keys(), start=1):  
    print(f"{idx}. {role}")  

role_choice = int(input("Enter the number of your job role: "))  
selected_role = list(job_roles.keys())[role_choice - 1]  
print(f"\n📌 You selected: {selected_role}")  

def evaluate_response(response):  
    analysis = TextBlob(response)  
    sentiment_score = analysis.sentiment.polarity  

    print("\n🔍 AI Interview Analysis:")  
    print("✅ Grammar & Clarity Score:", round(analysis.sentiment.subjectivity, 2))  
    print("✅ Confidence Score:", round(sentiment_score, 2))  

    if sentiment_score > 0.2:  
        print("🎯 Your response sounds confident!")  
    else:  
        print("⚠️ Try adding more positivity to your answer.")  

    if len(response.split()) < 5:  
        print("❗ Your answer is too short. Try adding more details.")  

    # Customized feedback  
    print(f"\n💡 Job-Specific Feedback for {selected_role}: {job_roles[selected_role]}")  

with sr.Microphone() as source:  
    print("\n🎤 Welcome to the AI Interview Simulator!")  
    time.sleep(2)  

    for question in interview_questions:  
        print("\n🗣️ Interviewer:", question)  
        time.sleep(1)  

        try:  
            print("🎙️ Listening for your response...")  
            audio = recognizer.listen(source, timeout=10)  
            response = recognizer.recognize_google(audio)  
            print("📝 Your response:", response)  

            evaluate_response(response)  

        except sr.UnknownValueError:  
            print("⚠️ Could not understand your response.")  
        except sr.WaitTimeoutError:  
            print("⏳ No response detected. Let's move to the next question.")
