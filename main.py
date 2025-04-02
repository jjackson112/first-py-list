websites = [
    "www.google.com", "www.youtube.com", "www.dropbox.com", "www.quora.com",
    "www.reddit.com", "www.instagram.com"
]
websites.pop(2)
websites.insert(2, "www.yahoo.com")
websites.append("refinery29.com")
print(websites)

villains = [
    "Shan Yu", "Ursula", "Gaston", "Jafar", "Maleficent", "Scar",
    "Mother Gothel", "Cruella", "Lady Tremaine", "Queen of Hearts", "Hades",
    "Dr. Facilier", "Ratigan", "Hans", "Yzma", "Captain Hook", "Frollo",
    "Syndrome", "Screenslaver", "Tamatoa"
]

first_four = villains[0:4]
print(first_four)

last_four = villains[16:20]
print(last_four)

middle_four = villains[10:13]
print(middle_four)

only_one = villains[9]
print(only_one)