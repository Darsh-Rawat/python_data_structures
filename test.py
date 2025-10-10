from data_structures.linkedlist import LinkedList

l1 = LinkedList()
l1.append(2)
print(l1.display(), l1.size())
l1.prepend(1)
print(l1.display(), l1.size())
l1.append(3)
print(l1.display(), l1.size())
l1.insert_at(1,1.5)
print(l1.display(), l1.size())
l1.delete(1.5)
print(l1.display(), l1.size())
print(l1.search(67))
