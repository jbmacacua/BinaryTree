print("\n============  Introduction to Binary Tree with Exercises  ============")
print("************************************************************************\n")
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

#======================Exercise Number 4 P1========================

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

#======================Exercise Number 5 P1========================

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

#======================Exercise Number 1 P1========================

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

#======================Exercise Number 2 P1========================

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

#======================Exercise Number 3 P1========================

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

#==================================================================

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("-------------------------------------------")
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print("-------------------------------------------\n")

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    numbers_tree1 = build_tree([2, 5, 9, 23, 88])
    numbers_tree1.delete(88)
    print("After deleting 88 ",numbers_tree1.in_order_traversal())

#--------------------------------------------------------------
    #Binary tree using the letters of my name
    print("_________________________________________________________________________\n")
    my_name = ["J", "O", "N", "A", "S",
               "B", "R", "I", "A", "N",
               "R",
               "M", "A", "C", "A", "C", "U", "A"]
    name_tree = build_tree(my_name)
    print("Is letter J in my name? : ", name_tree.search("J"))
    print("Is letter Q in my name? : ", name_tree.search("Q"))
    print("_________________________________________________________________________\n")

    numbers_tree1 = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree1.delete(9)
    print("After deleting 9 ", numbers_tree1.in_order_traversal())
    print("_________________________________________________________________________\n")

#--------------------------------------------------------------

#*************Print Area for the Exercise part 1**************
    print("                <=== Exercises Output Part 1===>\n")

    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())