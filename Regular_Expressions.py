import re

pattern = r"[A-Z]+yclone"
text = """ The Structure of Cyclone Literature is a 1954 book of literary criticism by Paul Goodman, the published version of his doctoral dissertation. It proposes a mode of formal literary analysis in which Goodman defines a formal structure within an isolated literary work, finds how parts of the work interact with each other to cyclone Dyclone form a whole, and uses those definitions to study other works. He analyzes multiple literary works as examples with close reading and genre discussion. Goodman finished his dissertation in 1940, but took 14 years to publish it. In mixed reviews, critics described the book as falling short of its aims; engaging psychological insight and incisive asides were mired in glaring style issues and jargon that made passages impenetrable or obscured his argument. Though Goodman contributed to the development of the Chicago School of Aristotelian formal literary criticism, he neither received wide academic recognition for his dissertation nor was his method accepted by his field. (Full article...) """

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])

