import utils.Node as Utils


def add_to_head(head: Utils.LinkedNode, node: Utils.LinkedNode) -> Utils.LinkedNode | None:
    if head is None:
        print("[FATAL] Head node is None!")
        return None
    
    node.next = head
    head = node
    return head


def add_to_tail(head: Utils.LinkedNode, node: Utils.LinkedNode) -> Utils.LinkedNode | None:
    if head is None:
        print("[FATAL] Head node is None!")
        return None
    
    p = head
    while p.next is not None:
        p = p.next
    p.next = node
    return head


def insert(node: Utils.LinkedNode, nex: Utils.LinkedNode):
    p = node.next
    node.next = nex
    nex.next = p


def remove(head: Utils.LinkedNode, index: int):
    p = head
    for _ in range(0, index - 1):
        p = p.next
    
    q = p.next
    p.next = q.next
    return q.val


def access(head: Utils.LinkedNode, index: int) -> Utils.LinkedNode | None:
    p = head
    for _ in range(0, index - 1):
        if p is None:
            return None
        p = p.next
    return p


def search(head: Utils.LinkedNode, val) -> int:
    p = head
    index = 0
    while p is not None:
        if p.val == val:
            return index
        index += 1
        p = p.next
    return -1

def insert_sort(head: Utils.LinkedNode) -> Utils.LinkedNode:
    dummy = Utils.LinkedNode(-1)
    dummy.next = head
    sorted = head
    cur = head.next
    
    while cur is not None:
        if cur.val < sorted.val:
            pre = dummy
            while pre.next.val <= cur.val:
                pre = pre.next
            sorted.next = cur.next
            cur.next = pre.next
            pre.next = cur
        else:
            sorted = sorted.next
        cur = sorted.next
    return dummy.next


def to_list(head: Utils.LinkedNode) -> list:
    li: list = []
    p = head
    while p is not None:
        li.append(p.val)
        p = p.next

    return li
            