class Coment:

    def __init__(self, text, upvoutes_qty):
        self.text = text
        self.upvoutes_qty = upvoutes_qty
    
    def edit(self, new_text):
        self.text = new_text

    def display(self):
        return f"{self.upvoutes_qty} upvotes: {self.text}"
    def __eq__(self, other):
        return True if self.text == other.text else False
    
comment_1 = Coment("Good job!", 10)
comment_2 = Coment("Good job!", 5)
print(comment_1 == comment_2)  # True
