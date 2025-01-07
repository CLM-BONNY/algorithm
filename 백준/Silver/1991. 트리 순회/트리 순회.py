# 트리 저장 딕셔너리 초기화
tree = {}

# 전위 순회 (Preorder Traversal)
def preorder(node):
    if node == '.':
        return
    print(node, end='')  # 루트 출력
    preorder(tree[node][0])  # 왼쪽 자식 탐색
    preorder(tree[node][1])  # 오른쪽 자식 탐색

# 중위 순회 (Inorder Traversal)
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])  # 왼쪽 자식 탐색
    print(node, end='')  # 루트 출력
    inorder(tree[node][1])  # 오른쪽 자식 탐색

# 후위 순회 (Postorder Traversal)
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # 왼쪽 자식 탐색
    postorder(tree[node][1])  # 오른쪽 자식 탐색
    print(node, end='')  # 루트 출력

# 입력 받기
n = int(input())
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

# 순회 결과 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
