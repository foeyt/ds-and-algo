class LinkedNode {
    constructor(val, next) {
        this.val = val
        this.next = (next === undefined ? null : next)
    }
}

class DoubleLinkedNode {
    constructor(val, prev, next) {
        this.val = val
        this.prev = (prev === undefined ? null : prev)
        this.next = (next === undefined ? null : next)
    }
}
