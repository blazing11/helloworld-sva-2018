# let the user know what's going on
print ("The following words are adapted from H.P.Lovecraft's fiction The Whisperer in Darkness")
print ("Answer the questions below to see your story.")
print ("-----------------------------------")

# variables containing all of your story info
organ = raw_input("Enter an organ of a human ")
person = raw_input("Enter a person you know but not very clsoe ")
negtiveadverb = raw_input("Enter a negative adverb ")
positiveadjective = raw_input("Enter a positive adjective ")
master = raw_input("Enter a artist you admire")
negativeadjective = raw_input("Enter a negative adjective ")
sound = raw_input("Enter a kind of sound ")
magic_person = raw_input("Enter a magic person you are afriad of ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!
story_1 = "Even now I have my moments of half doubt moments in which I half accept the scepticism of " + "  \n" + \
"those who attribute my whole experience to dream and nerves and delusion." \

story_2 = "These things in the chair were " + negtiveadverb + "clever constructions of their kind, " + "  \n" + \
"and were furnished with " + positiveadjective + " metallic clamps to attach them to organic " + "  \n" +  \
"developments of which I dare not form any conjecture. I hope-developments of "  + "  \n" +  \
"which I dare not form any conjecture. I hope-devoutly hope-that they were the "  + "  \n" +  \
"waxen products of " + master + ", despite what my inmost feats tell me."  + ". \n" +  \
"Great God! That whisperer in darkness with its " + negativeadjective + " odour and " + sound + "!"  + "  \n" +  \
""+ magic_person + ", emissary, changeling, outsider... that hideous repressed buzzing... "  + "  \n" +  \
"and all the time in that fresh, shiny cylinder on the shelf... "  + "  \n" +  \
"poor devil... ""prodigious surgical, biological, chemical, and mechanical skill... """

print (story_1)
print
print (story_2)

raw_input("Press any key to see the rest of the story")

story_3 = "For the things in the chair, prefer to the last, subtle detail of microscopic resemblance"  + "  \n" +  \
"- or identity - were the face and " + organ + " hands of " + person
print
print (story_3)