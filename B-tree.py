class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        # t là bậc tối thiểu (minimum degree) của cây
        self.root = BTreeNode(True)
        self.t = t 

    def insert(self, k):
        root = self.root
        # Nếu node gốc đã đầy (số lượng key = 2*t - 1)
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # Nếu là node lá, tìm vị trí và chèn key vào
            x.keys.append(None) # Mở rộng mảng
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # Nếu không phải node lá, tìm node con phù hợp
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        
        # Đẩy node mới vào danh sách con của x
        x.child.insert(i + 1, z)
        # Đẩy key ở giữa của y lên node x
        x.keys.insert(i, y.keys[t - 1])
        
        # Chia key của y cho z
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        
        # Chia child của y cho z nếu y không phải node lá
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t]

    def print_tree(self, x, l=0):
        # In ra các key của node hiện tại kèm theo level
        print(f"Level {l} ({len(x.keys)} keys):", end=" ")
        for key in x.keys:
            print(key, end=" ")
        print()
        
        # Đệ quy in các node con
        if len(x.child) > 0:
            for child in x.child:
                self.print_tree(child, l + 1)

# --- Chạy thử nghiệm ---
if __name__ == '__main__':
    B = BTree(3) # Khởi tạo cây B với bậc tối thiểu t = 3

    # Chèn các giá trị vào cây
    for i in [10, 20, 5, 6, 12, 30, 7, 17]:
        B.insert(i)

    print("Cấu trúc của B-Tree:")
    B.print_tree(B.root)