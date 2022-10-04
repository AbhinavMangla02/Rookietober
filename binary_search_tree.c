/**
* Definition for a binary tree node
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *Right;
};
**/

struct TreeNode* bstFromPreorder(int* preorder, int preordersize) {
    struct TreeNode *node;
    int mid;

    if (preordersize == 0) return NULL;

    node = malloc(sizeof(struct TreeNode));
    node->val = preorder[0];

    mid = 1;
    while (mid < preordersize && preoder[mid] < node->val) {
        mid ++;
    }
    node->left = bstFromPreorder(&preorder[1], mid - 1);
    node->right = bstFromPreorder(&preorder[mid], preorderSize - mid);

    return node;
}

/**
 * Author : Pythonicboat
 * Objective : Construct Binary search tree from preorder traversal
 * References : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
 **/
