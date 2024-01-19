
class Node:
    def __init__(self,item):
        self.item = item#将值存放进item
        self.next = None#不赋予下一个结点
class SingleLinkList:
    def __init__(self):#创建链表
        self.head = None

    def is_empty(self):#判断链表是否为空
        return self.haed is None

    def add(self,item):#头插法
        node = Node(item)
        node.next = self.head
        self.head = node

    def change(self,item,t):#改变指定元素
        cur = self.head
        while cur is not None:
            if cur.item == item:
                cur.item = t
            else:
                cur = cur.next

    def remove(self,item):#移除指定元素
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item :
                if not pre:#第一个就是要删除的结点
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self,item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

linklist=SingleLinkList()
linklist.add(4)
linklist.add(6)
linklist.add(15)
linklist.remove(6)
linklist.change(4,14)
print(linklist.find(14))