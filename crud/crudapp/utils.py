def check_bad_words(message,bad):
    message = message.split()
    for i in message:
        if i in bad and i !='':
            return True
    return False
