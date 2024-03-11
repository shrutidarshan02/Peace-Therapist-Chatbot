import tkinter as tk
import re
import random

response = {
    "hello": ["Hello, how can I help you?"],
    "hi": ["Hey there! How can i help you today?"],
    "good morning": ["Good morning, how are you doing today?"],
    "good afternoon": ["Good afternoon! How's your day going so far?"],
    "good evening": ["Good evening to you! How has your day been?"],
    "(.*) hungry": ["Grab a snack!!"],
    "(.*) worried": ["I understand that you're feeling worried. It's natural to have concerns and uncertainties. Is there something specific that's causing worry? I'm here to listen to you and offer support. IF YOU WANT SOME TIPS ON HOW TO NOT GET WORRIED, TYPE WORRY."],
    "worry": ["When it comes to reducing worry, there are a few strategies that can help. One approach is to practice mindfulness and focus on the present moment rather than getting caught up in future uncertainties. Some other ways of dealing with it are:\n\t1. Deep breathing and exercises.\n\t2. Meditation can also be helpful in calming the mind.\nIt's important to remember that worrying is a normal part of life, but these healthy ways to manage it can make a big difference."],
    "(.*) sleep": ["I'm sorry to hear that you're having trouble sleeping. It can be frustrating when sleep eludes us. Here are a few tips that might help you:\n\t1.Try establishing a bedtime routine.\n\t2.Create a comfortable sleep environment.\n\t3.Avoid caffeine and electronics before bed.\n\t4.Consider relaxation techniques like deep breathing or listening to calming music."],
    "good night": ["Good night, dear! I hope you have a restful sleep and wake up refreshed tomorrow. If there's anything on your mind, or if you need someone to talk to, remember that I'm here for you. Take care and have sweet dreams!"],
    "(.*) lonely": ["Loneliness happens when your needs for social interaction and human connection go unmet. It's important to remember that feeling lonely is a valid and common experience, and it's okay to reach out for support.\nIf you're struggling with loneliness, some of the ways of dealing with it are:\n\t1. Consider talking to a trusted friend, family member, or mental health professional.\n\t2. Get engaged in activities you enjoy, join social groups or clubs, and practice self-care.\nThese steps can help alleviate feelings of loneliness."],
    "(.*) die": ["I'm really sorry to hear that you're feeling this way, but I can provide the help that you need. It's important to reach out to someone you trust for support, such as a friend, family member, or a mental health professional.\nSUICIDE HELPLINE NUMBER: 91529-87821"],
    "(.*) suicide": ["I'm really sorry to hear that you're feeling this way, but I can provide the help that you need. It's important to reach out to someone you trust for support, such as a friend, family member, or a mental health professional.\nSUICIDE HELPLINE NUMBER: 91529-87821"],
    "I am feeling (.*)": ["{}?", "How long have you been feeling {}?"],
    "(.*) dead": ["I'm really sorry to hear that you're feeling this way, but I can provide the help that you need. It's important to reach out to someone you trust for support, such as a friend, family member, or a mental health professional.\nSUICIDE HELPLINE NUMBER: 91529-87821"],
    "I'm(.*)": ["Why are you {}?", "How long have you been {}?"],
    "I (.*) you": ["Why do you {} me?", "What makes you think that you {} me?"],
    "I (.*) myself": ["Why do you {} yourself ?", "What make you think you {} yourself"],

    "(.)  sorry (.)": ["There is no need to apologize.", "What are you apologizing for?"],
    "(.) friend (.)": ["Tell me more about your friend.", "How do your friends make you feel?"],
    "yes": ["You seem quite sure.", "Okay, but can you elaborate?"],
    "no": ["Why not?", "Okay, but can you tell me more?"],
    "(.) betrayed (.)": ["I understand that you're feeling betrayed but remember that it's not your fault and you deserve to be surrounded by supportive and trustworthy people in your life."],
    "(.*) move on": ["Moving on can be a challenging process, but it's definitely possible. Here are a few tips that might help you to move on:\n\t1. Allow yourself to feel exposed to the outer world.\n\t2. Seek support: Reach out to your close friends, talk to your close cousins who are frank.\n\t3. Focus on self-care.\nRemember, healing takes time, and everyone's journey is different. Be patient and kind to yourself and trust that you will eventually move forward. You're strong, and I believe in you."],
    "(.*) difficult (.*)": ["I totally get what you're saying. It's completely normal to find it difficult at times. You've got this! Keep pushing forward and remember that you're capable of overcoming challenges."],
    "(.*) difficult": ["I totally get what you're saying. It's completely normal to find it difficult at times. You've got this! Keep pushing forward and remember that you're capable of overcoming challenges."],
    "(.*) toxic (.*)": ["When the people around aren't supportive or positive, remember that you deserve to be surrounded by people who uplift and encourage you. You deserve to be in a positive and healthy environment. Take care of yourself!"],

    "(.*) toxic": ["When the people around aren't supportive or positive, remember that you deserve to be surrounded by people who uplift and encourage you. You deserve to be in a positive and healthy environment. Take care of yourself!"],
    "(.*) tough": ["I totally get what you're saying. It's completely normal to find it tough at times. You've got this! Keep pushing forward and remember that you're capable of overcoming challenges."],
    "(.*) depress": ["I'm really sorry to hear that you're feeling depressed. It's important for you to remember that you don't have to face this alone, I'm here for you. Reach out to someone you trust. DEPRESSION HELPLINE NUMBER: 1800-599-0019."],
    "(.*) sick": ["Oh no, I'm sorry to hear that you're sick. Is there anything I can do to help?"],
    "(.) family (.)": ["I'm really sorry to hear that there are a lot of problems going on in your family. It can be really tough when things get difficult at home. If you want to talk about it or if there's anything specific you need support with, I'm here for you."],
    "(.*) anxiety": ["I'm sorry to hear that you're dealing with anxiety. It can be really tough to manage. (FOR SOME COPING STRATEGIES FOR ANXIETY TYPE ANXIETY."],
    "anxiety": ["Here are a few strategies for coping with anxiety:\n\t1. Eat healthy foods.\n\t2. Make sleep a priority.\n\t3. Quit smoking, alcohol consumption and cut back or quit drinking caffeinated beverages.\nEveryone is different, so it's important to find out what works best for you."],
    "(.*) therapy": ["I'm really sorry to hear that you're feeling this way. It takes a lot of courage to recognize when you need help and reach out to therapy. It's important to prioritize your mental well-being.\nRemember, you don't have to face everything alone. You deserve support and healing."],
    "(.*) stress": ["Stress can be overwhelming, but there are some strategies that can help you reduce it. Follow the following points to reduce your stress:\n\t1. Take breaks and get engaged in activities you enjoy that can help you to relax your mind and body.\n\t2. It's important to prioritize self-care.\n\t3. Maintain a healthy lifestyle."],
   
    "(.) stress (.)": ["Stress can be overwhelming,but there are some strategies that can help you reduce it. Taking breaks and engaging in activities you enjoy can help relax your mind and body.It's important to prioritize self-care, and maintain a healthy lifestyle."],
    "(.*) stressed": ["It can be really tough to deal with stress, but you're not alone. Remember to take some time for yourself and do things that help you relax and unwind. Some other tips for dealing with it are:\n\t1. Meditation,\n\t2. Listening to music,\n\t3. Going for a walk can make a big difference.\nIf you need someone to talk to, I'm here for you. You're strong and you'll get through this!"],
    "(.*) demotivated": ["It's completely normal to have moments of low motivation, especially when facing challenges or difficult situations. Remember to take a step back and remind yourself of your goals and the reason why you're pursuing it. You've got this!"],
    "okay": ["Hey, I'm here for you. If you want to talk about anything, I'm all ears. Remember you don't have to go through tough times alone."],
    "ok": ["Hey, I'm here for you. If you want to talk about anything, I'm all ears. Remember you don't have to go through tough times alone."],
    "(.*) help": ["Of course, I'm here to help! What do you need assistance with? Feel free to share, and I'll do my best to support you."],
    "(.*) low": ["I'm sorry to hear that you're feeling low. It's completely normal to have ups and downs in life. Remember that it's okay to feel low and it's important to take care of yourself during these times."],
    "(.*) irritated": ["I'm sorry to hear that you're feeling irritated. Is there something specific that's been bothering you?"],
    "(.*) irritating": ["I understand how frustrating it can be when things are irritating. Is there something in particular that's been bothering you lately?"],
   
    "(.*) human": ["No, I'm not human. I'm a virtual therapist/friend, here to chat with you and help you with your problems. How can I assist you today?"],
    "(.*) confused": ["I understand, being confused can be overwhelming. Can you tell more about what's causing your confusion? Maybe I can help clarify things for you.\n(IF YOU WANT ANY TIPS FOR REDUCING CONFUSION TYPE'CONFUSE'."],
    "confuse": ["When you're feeling confused, taking a step back, and trying to identify what's causing the confusion may help you a bit. Break things down into smaller parts and ask yourself questions to gain clarity. It's okay to ask for help or seek guidance from someone you trust. Sometimes talking things out can bring more clarity. Remember, it's normal to feel confused at times, and it's a sign that you're seeking understanding."],
    "(.*) confusion": ["I'm sorry to hear that you're feeling confused. It can be tough when things aren't clear. Is there something specific that you're unsure about? I'm here to help!\n(IF YOU WANT ANY TIPS FOR REDUCING CONFUSION TYPE'CONFUSE'."],
    "(.) confused (.)": ["I understand, being confused can be overwhelming. Can you tell more about what's causing your confusion? Maybe I can help clarify things for you.\n(IF YOU WANT ANY TIPS FOR REDUCING CONFUSION TYPE'CONFUSE'."],
    "thank you": ["You're most welcome! If there's anything else you'd like to chat about or if you need any more help, just let me know. I'm here for you!" ],
    "welcome": ["Thank you! I'm here to help and support you. If there's anything specific you'd like to talk about, feel free to share. I'm here to listen and provide assistance. 🤗"],
    "(.*) sad": ["I'm sorry to hear that you're feeling sad. It's completely normal to have ups and downs in life. Remember that it's okay to feel sad and it's important to take care of yourself during these times."],
    "(.*) motivation": ["Finding motivation can be tough sometimes. One thing that can help is setting small, achievable goals for yourself. Celebrate your progress along the way."],

    "(.*) love (.*)": ["Love is a beautiful emotion. It's wonderful that you're experiencing it. What's on your mind about love?"],
    "(.*) heartbroken(.*)": ["I'm sorry to hear that you're feeling heartbroken. Breakups and heartaches can be really tough. Take your time to heal and remember that it's okay to feel sad. If you'd like, we can talk more about it."],
    "(.*) happy": ["I'm glad to hear that you're feeling happy! What's making you feel this way?"],
    "(.*) happy (.*)": ["Wow, that sounds so great 😃"],
    "(.*) excited": ["Excitement is contagious! What's got you feeling so excited?"],

    "(.*) angry (.*)": ["Feeling angry is natural at times. What's causing your anger?"],
    "(.*) tired (.*)": ["It sounds like you're feeling tired. Maybe it's time for a break or a rest."],
    "(.*) stressed (.*)": ["Stress can be tough to deal with. Have you tried any relaxation techniques?"],
    "(.*) grateful (.*)": ["Gratitude is a wonderful feeling. What are you feeling grateful for?"],
    "(.*) lost (.*)": ["Feeling lost is a common experience. Let's talk about how we can find your way."],
    "(.*) confused (.*)": ["Confusion can be frustrating. Let's try to clear things up."],
    "(.*) alone (.*)": ["Feeling alone can be tough. You're not alone; I'm here to chat with you."],
}

def match_response(input_text):
    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.groups())
    return "I'm sorry, I don't understand what you're saying."

def send_message(event=None):
    user_input = entry.get()
    if user_input.lower() == "bye":
        messages_list.insert(tk.END, "Peace: Goodbye 🤗\nHave a nice day ahead!!")
        root.after(2000, root.destroy)  # close the window after 2 seconds
    else:
        messages_list.insert(tk.END, "You: " + user_input)
        messages_list.insert(tk.END, "Peace: " + match_response(user_input))
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Peace, Your Personal Therapist Chatbot")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Vertical scrollbar
scrollbar_y = tk.Scrollbar(frame)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

# Horizontal scrollbar
scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

messages_list = tk.Listbox(frame, width=100, height=20, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, bg="black", fg="white", font=("Arial 18"))
messages_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_y.config(command=messages_list.yview)
scrollbar_x.config(command=messages_list.xview)

entry = tk.Entry(root, font=("Arial 18"))
entry.pack(padx=10, pady=10, fill=tk.X, expand=True)
entry.focus()

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial 16"))
send_button.pack()

root.bind('<Return>', send_message)

root.mainloop()

