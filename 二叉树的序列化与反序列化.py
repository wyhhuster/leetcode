class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        stack = []
        stack.append(root)
        ans = ''
        while stack and set(stack)!={'NULL'}:
            p = stack.pop(0)
            if p != 'NULL':
                ans += str(p.val) + ','
                if p.left:
                    stack.append(p.left)
                else:
                    stack.append('NULL')
                if p.right:
                    stack.append(p.right)
                else:
                    stack.append('NULL')
            else:
                ans += 'null,'
        return ans.strip(',')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        if len(data)==0:
            return None

        if len(data)==1:
            return TreeNode(data[0])
        data=data.split(',')
        root=TreeNode(data[0])
        stack=[]
        stack.append(root)
        data.pop(0)
        while stack and data:
            p=stack.pop(0)
            if len(data)>=1 and data[0]!='null':
                p.left=TreeNode(data[0])
                stack.append(p.left)
            if len(data)>=2 and data[1]!='null':
                p.right=TreeNode(data[1])
                stack.append(p.right)
            data=data[2:]
        return root