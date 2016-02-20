class notesApplication(object):

    def __init__(self, author, notes_list):

        self.author = author
        self.noteslist = notes_list

    def create(self, notes_content):
        if notes_content == "" or notes_contents == None:
            return "Please enter value"

        self.notelist.append(notes_content)
        return notes_content +" added"


    def list(self):
        count = 0
        for x in self.notelist:
            print("Note ID %d. " %(count))
            print (x)
            print ("By author "+self.author)
            count +=1

    def get(self, note_id):
        return str(self.noteslist[note_id])

    def search(self, search_text):
        textadd = "Search result for \"[<"+search_text+">]\""
        textadd = ""
        count = 0
        for x in self.noteslist:
            if search_text in x:
                textadd +=x +"\n"+"Note ID: %d\n By Author %s" %(count, self.author)
        return str(textadd)

    def delete(self, note_id):
        del self.noteslist[note_id]
        return self.noteslist[note_id]



#test = NotesApplication("Cicy" , ["I am beautiful!"])
#test.create ("Words can't bring me down")
#print(test.get(0))
#print(test.list())
#test.edit(0, "Coding shaaa")
#print(test.list())
#test.delete(0)
#prin(test.list())

    input()
    
