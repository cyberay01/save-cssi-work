template = "The {0[0]} jumped over a {2} {0[1]}. Then the {0[1]} had {1[0]} and the {0[0]} {1[1]} the {0[1]}"

nouns = ["",""]
verbs = ["",""]
adj = ""

for index in range(len(verbs)):
    nouns[index] = raw_input("Enter a noun.\n")

for index in range(len(verbs)):
    verbs[index] = raw_input("Enter a verb in its past tense.\n")

adj = raw_input("Enter an adjective.\n")

madlib = template.format(nouns, verbs, adj)

print(madlib)