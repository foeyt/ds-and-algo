template<typename T>
class LinkedNode 
{
    public:
        T val;
        LinkedNode *next;

        LinkedNode(T val)
        {
            this->val = val;
            this->next = nullptr;
        }
};


template<typename T>
class DoubleLinkedNode
{
    public:
        T val;
        DoubleLinkedNode *prev;
        DoubleLinkedNode *next;

        DoubleLinkedNode(T val)
        {
            this->val = val;
            this->prev = nullptr;
            this->next = nullptr;
        }
};

template<typename T>
void deleteLinkedList(LinkedNode<T> *head) {
     while (*head != nullptr)
     {
        LinkedNode<T> *p = head->next
        delete head;
        head = p;
     }
}
