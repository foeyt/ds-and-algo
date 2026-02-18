import LinkedNode from "../utils/Node"


addToHead = function(head, node) {
    if (head === null) {
        console.log("[FATAL] Head node is null")
        return null
    }
    
    node.next = head
    head = node
    return head
}


addToTail = function(head, node) {
    if (head === null) {
        console.log("[FATAL] Head node is null")
        return null
    }
    let p = head
    while (p.next !== null) {
        p = p.next
    }
    p.next = node
    return p.next
}



