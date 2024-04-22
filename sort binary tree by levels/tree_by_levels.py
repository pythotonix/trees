def tree_by_levels(root):
    if root is None:
        return []
    res = []
    def traverse(node, level):
        if node is None:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.value)
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)
    traverse(root, 0)
    return sum(res, [])