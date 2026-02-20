#include <iostream>
#include <vector>
#include "Node.hpp"

template<typename T>
LinkedNode<T> *addToHead(LinkedNode<T> *head, LinkedNode<T> *node)
{
    if (head == nullptr)
    {
        std::cout << "[FATAL] Head node is None!" << std::endl;
        return nullptr;
    }
    node->next = head;
    head = node;
    return head;
}


template<typename T>
LinkedNode<T> *addToList(LinkedNode<T> *head, LinkedNode<T> *node)
{
    if (head == nullptr)
    {
        std::cout << "[FATAL] Head node is None!" << std::endl;
        return nullptr;
    }
    
    LinkedNode<T> *p = head;
    while (p->next != nullptr)
    {
        p = p->next
    }
    p->next = node;
    return head;
}


template<typename T>
void insert(LinkedNode<T> *node, LinkedNode<T> *nex)
{
    LinkedNode<T> *p = node->next;
    node->next = nex;
    nex->next = p;
}


template<typename T>
T remove(LinkedNode<T> *head, int index)
{
    LinkedNode<T> *p = head;
    for (int i = 0; i < index - 1; i++)
    {
        if (p == nullptr)
        {
            return NULL;
        }
        p = p->next;
    }
    LinkedNode<T> *q = p->next;
    p->next = q->next;
    T r = q->val;
    delete q;
    return r;
}

template<typename T>
LinkedNode<T> *access(LinkedNode<T> *head, int index)
{
    LinkedNode<T> *p = head;
    for (int i = 0; i < index; i++)
    {
        if (p == nullptr)
        {
            return nullptr;
        }
        p = p->next;
    }
    return p;
}


template<typename T>
int search(LinkedNode<T> *head, T val)
{
    LinkedNode<T> *p = head;
    int index = 0;
    while (p != nullptr)
    {
        if (p->val == val)
        {
            return index;
        }
        p = p->next;
        index++;
    }
    return -1;
}


template<typename T>
LinkedNode<T> *insertSort(LinkedNode<T> *head)
{
    LinkedNode<T> *dummy = new LinkedNode<T>(-1);
    dummy->next = head;
    LinkedNode<T> *sorted = head;
    LinkedNode<T> *cur = head->next;

    while (cur != nullptr)
    {
        if (cur->val < sorted->val)
        {
            LinkedNode<T> *pre = dummy;
            while(pre->next->val <= cur->val)
            {
                pre = pre->next;
            }
            sorted->next = cur->next;
            cur->next = pre->next;
            pre->next = cur;
        }
        else
        {
            sorted = sorted->next;
        }
        cur = cur->next;
    }
    return dummy->next;
}


template<typename T>
std::vector<T> toVector(LinkedNode<T> *head)
{
    LinkedNode<T> *p = head;
    std::vector<T> vec;
    while (p != nullptr)
    {
        vec.push_back(p->val);
        p = p->next;
    }
    return vec;
}


template<typename T>
void toArray(LinkedNode<T> *head, T *array)
{
    LinkedNode<T> *p = head;
    int size = 0;
    while (p != nullptr)
    {
        p = p->next;
        size++;
    }

    array = malloc(size * sizeof(T));
    p = head;
    for (int i = 0; i < size; i++)
    {
        array[i] = p->val;
        p = p->next;
    }
}
