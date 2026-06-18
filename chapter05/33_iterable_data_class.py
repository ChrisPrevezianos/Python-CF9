class DataCollection:
    def __init__(self, data):
        self.data = data
 
    def __iter__(self):
        return iter(self.data)
   
    def __getitem__(self, index):
        return self.data[index]
   
    def __len__(self):
        return len(self.data)
   
    def __repr__(self):
        return f"DataCollection({self.data})"
 
def main():
    collection = DataCollection([1, 2, 3, 4, 5])
    print(f"DataCollection object: {collection}")
 
    for item in collection:
        print(item)
   
    a, b, c, d, e = collection
    print(a, b, c, d, e)
 
    print(f"Element at index 0: {collection[0]}")
    print(f"Element at index 1: {collection[1]}")
 
    print(f"Length of my collection: {len(collection)}")
 
    print(f"Slice of my collection: {collection[1:3]}")
 
if __name__ == "__main__":
    main()
