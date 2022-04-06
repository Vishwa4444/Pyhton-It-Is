import pywhatkit

# using Exception Handling
# to avoid exceptions
try:

    # it plays a random YouTube
    # video of GeeksforGeeks
    pywhatkit.playonyt("")
    print("Playing...")

except:

    # printing the error message
    print("Network Error Occured")