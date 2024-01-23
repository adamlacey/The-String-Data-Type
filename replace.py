# Replacing function changing "!" to " ".
# Replace function replaces all ! for spaces which is executed once printed.

sentence1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence1.replace("!" , " "))

# Upper function capitalising the sentence below.
# Using the upper function changes all letters and capitalises them once printed.

sentence2 = "The quick brown fox jumps over the lazy dog."
print(sentence2.upper())

# Making sentence3 a new variable so it is still capitalised when print function used.
# Using [::-1] changes the sentence and reverses it so the sentence is backwards once printed.

sentence3 = (sentence2.upper())
print(sentence3[::-1])