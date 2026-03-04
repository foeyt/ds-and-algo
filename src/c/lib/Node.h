#include <stdlib.h>
#ifndef NODE
#define NODE


typedef struct LinkedNode 
{
    int val;
    struct LinkedNode *next;
} LinkedNode;


typedef struct DoubleLinkedNode
{
    int val;
    struct DoubleLinkedNode *prev;
    struct DoubleLinkedNode *next;
} DoubleLinkedNode;


typedef struct TreeNode
{
    int val;
    int height;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;


LinkedNode *newLinkedNode(int val)
{
    LinkedNode *node = (LinkedNode *) malloc(sizeof(LinkedNode));
    node->val = val;
    node->next = NULL;
    return node;
}


DoubleLinkedNode *newDoubleLinkedNode(int val)
{
    DoubleLinkedNode *node = (DoubleLinkedNode *) malloc(sizeof(DoubleLinkedNode));
    node->val = val;
    node->prev = NULL;
    node->next = NULL;
    return node;
}


TreeNode *newTreeNode(int val) 
{
    TreeNode *node = (TreeNode *) malloc(sizeof(TreeNode));
    node->val = val;
    node->height = 0;
    node->left = NULL;
    node->right = NULL;
    return node;
}


LinkedNode *arrToLinkedList(const int *arr, size_t size) 
{
    if (size <= 0)
    {
        return NULL;
    }

    LinkedNode *dummy = newLinkedNode(-1);
    LinkedNode *node = dummy;
    for (int i = 0; i < size; i++)
    {
        node->next = newLinkedNode(arr[i]);
        node = node->next;
    }
    return dummy->next;
}


DoubleLinkedNode *arrToDoubleLinkedList(const int *arr, size_t size) 
{
    if (size <= 0)
    {
        return NULL;
    }

    DoubleLinkedNode *dummy = newDoubleLinkedNode(-1);
    DoubleLinkedNode *node = dummy;
    for (int i = 0; i < size; i++)
    {
        node->next = newDoubleLinkedNode(arr[i]);
        node->next->prev = node;
        node = node->next;
    }
    return dummy->next;
}

// 中序遍历，root->left->right
TreeNode *arrToTreeDFS(const int *arr, size_t size, int i) 
{
    if (i < 0 || i >= size || arr[i] == INT_MAX)
    {
        return NULL;
    }

    TreeNode *root = (TreeNode *) malloc(sizeof(TreeNode));
    root->val = arr[i];
    root->left = arrToTreeDFS(arr, size, 2 * i + 1);
    root->right = arrToTreeDFS(arr, size, 2 * i + 2);
    return root;
}


void treeToArrDFS(TreeNode *root, int i, int *res, int *size)
{
    if (root == NULL)
    {
        return;
    }

    while (i >= *size)
    {
        res = (int *) realloc(res, *(size + 1) * sizeof(int));
        res[*size] = INT_MAX;
        (*size)++;
    }
    res[i] = root->val;
    treeToArrDFS(root->left, 2 * i + 1, res, size);
    treeToArrDFS(root->right, 2 * i + 2, res, size);
}


TreeNode *arrToTree(const int *arr, size_t size)
{
    return arrToTreeDFS(arr, size, 0);
}


int *treeToArr(TreeNode *root, int *size)
{
    *size = 0;
    int *res = NULL;
    treeToArrDFS(root, 0, res, size);
    return res;
}


void freeMemoryLinkedNode(LinkedNode *cur)
{
    if (cur == NULL)
        return;

    LinkedNode *pre;
    while (cur != NULL)
    {
        pre = cur;
        cur = cur->next;
        free(pre);
    }
}


void freeMemoryDoubleLinkedNode(DoubleLinkedNode *cur)
{
    if (cur == NULL)
        return;

    DoubleLinkedNode *pre;
    while (cur != NULL)
    {
        pre = cur;
        cur = cur->next;
        free(pre);
    }
}

// 后序遍历，left->right->root，下面配图分析：回答来自豆包
/*
       A
      / \
     B   C
    / \   \
   D   E   F 
   产生遍历序列 D -> E -> B -> F -> C -> A
   先遍历子树到叶，所有子遍历完后遍历根
 */
void freeMemoryTreeNode(TreeNode *root)
{
    if (root == NULL)
        return;

    freeMemoryTreeNode(root->left);
    freeMemoryTreeNode(root->right);
    free(root);
}


#endif
