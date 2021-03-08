# UnionFind implementation adapted from java example by @williamfiset on Github:
# https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java

class UnionFind:

    def __init__(self, size):
        # The number of elements in this union find
        self.size = self.numComponents = size

        # Used to track the size of each of the component
        self.sz = [1 for i in range(size)]

        # id[i] points to the parent of i, if id[i] = i then i is a root node
        self.id = [i for i in range(size)]


    # Find which component/set 'p' belongs to, takes amortized constant time.s
    def find(self, p):

        # Find the root of the component/set
        root = p

        # since we are using a compressed union path approach this will be almost O(1)
        while (root != self.id[root]):
            root = self.id[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while (p != root):
            next = self.id[p]
            self.id[p] = root
            p = next

        return root


    # Return whether or not the elements 'p' and
    # 'q' are in the same components/set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)


    # Return the size of the components/set 'p' belongs to
    def componentSize(self, p):
        return self.sz[self.find(p)]


    # Return the number of elements in this UnionFind/Disjoint set
    #def size(self):
    #    return self.size


    # Returns the number of remaining components/sets
    def components(self):
        return self.numComponents


    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):

        # These elements are already in the same group!
        if (self.connected(p, q)):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        # Merge smaller component/set into the larger one.
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        # Since the roots found are different we know that the
        # number of components/sets has decreased by one
        self.numComponents -= 1
