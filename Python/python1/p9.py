import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

    # sending message to receiver
    # using pywhatkit
    pywhatkit.sendwhatmsg("+91 9148549116",
                          "Hello from dubai",
                           13,46)
    print("Successfully Sent!")

except:

    # handling exception
    # and printing error message
    print("An Unexpected Error!")
