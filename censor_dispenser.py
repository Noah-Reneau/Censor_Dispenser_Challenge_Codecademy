# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(email, phrase):
    new_email = email.replace(phrase, '[REDACTED]')
    return new_email

#new_email_one = censor(email_one, 'learning algorithms')
#print(new_email_one)

def censor_terms(email, phrases):
    new_email = email
    for phrase in phrases:
        if phrase in email:
            new_email = new_email.replace(phrase.title(), '[REDACTED]')
            new_email = new_email.replace(phrase.lower(), '[REDACTED]')
    return new_email

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#new_email_two = censor_terms(email_two, proprietary_terms)
#print(new_email_two)

#censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as 
# censoring everything from the list from the previous step as well

def censor_negativity(email, phrases, negative_words):
    new_email = censor_terms(email, phrases)
    split_email = new_email.split()
    neg_count = 0
    for word in split_email:
        if word in negative_words:
            neg_count += 1
            if neg_count == 3:
                index = split_email.index(word)
                neg_censor = ' '.join(split_email[index:])
                neg_censored = censor_terms(neg_censor, negative_words)
                censored = ' '.join(split_email[:index])
                positive_email = censored + neg_censored
    return positive_email
                


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
#new_email_three = censor_negativity(email_three, proprietary_terms, negative_words)
#print(new_email_three)

def censor_everything(email, phrases, negative_words):
    new_email = email
    split_email = new_email.split()
    for word in split_email:
        if ((word in phrases) or (word in negative_words)):
            target_index = split_email.index(word)
            split_email[target_index] = '[REDACTED]'
            split_email[target_index + 1] = '[REDACTED]'
            split_email[target_index - 1] = '[REDACTED]'
    newest_email = ' '.join(split_email)
    return newest_email

new_email_four = censor_everything(email_four, proprietary_terms, negative_words)
print(new_email_four)
