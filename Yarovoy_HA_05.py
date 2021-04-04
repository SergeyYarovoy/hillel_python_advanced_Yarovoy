class BadClass:

   def __init__(self, val=0):
       self.val = val
       self.hash_val = val

   def __hash__(self):
       return hash(self.hash_val)

   def __eq__(self, other):
       return self.__class__ == other.__class__ and self.val == other.val


bad = BadClass()

even_worse = { bad }
assert(bad in even_worse)
bad.val += 1
assert(bad in even_worse)
print('yeah, we good!')

still_bad = BadClass(val=bad.val)
assert(still_bad in even_worse)

