# Lớp đại diện cho một Nút trong cây AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Nút mới thêm vào luôn có chiều cao là 1

class AVLTree:
    # Hàm tiện ích lấy chiều cao của nút
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Lấy hệ số cân bằng (Balance Factor)
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # 1. Phép XOAY PHẢI (Right Rotate)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Thực hiện xoay
        x.right = y
        y.left = T2

        # Cập nhật lại chiều cao
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x # Trả về gốc mới

    # 2. Phép XOAY TRÁI (Left Rotate)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Thực hiện xoay
        y.left = x
        x.right = T2

        # Cập nhật lại chiều cao
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y # Trả về gốc mới

    # Hàm chèn một nút mới vào cây
    def insert(self, root, key):
        # Bước 1: Chèn như cây nhị phân tìm kiếm (BST) bình thường
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root # Không cho phép các khóa trùng lặp

        # Bước 2: Cập nhật chiều cao của nút tổ tiên
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Bước 3: Lấy hệ số cân bằng để kiểm tra trạng thái
        balance = self.get_balance(root)

        # Bước 4: Xử lý 4 trường hợp mất cân bằng
        # Trường hợp 1: Trái Trái
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Trường hợp 2: Phải Phải
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Trường hợp 3: Trái Phải
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Trường hợp 4: Phải Trái
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Hàm in cây theo thứ tự Tiền tố (Pre-order)
    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

# --- Chạy thử nghiệm ---
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Thử chèn các nút khiến cây BST bình thường bị lệch thành đường thẳng
    nodes_to_insert = [10, 20, 30, 40, 50, 25]
    for key in nodes_to_insert:
        root = tree.insert(root, key)

    print("Duyệt cây AVL theo thứ tự Pre-order (Gốc - Trái - Phải):")
    # Kết quả mong đợi: 30 20 10 25 40 50
    tree.pre_order(root)
    print()