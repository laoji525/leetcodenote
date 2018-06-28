/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null || q == null) return q == p;
        if(p.val == q.val)
            return isSameTree(q.left,p.left)&& isSameTree(q.right,p.right);
        return false;
    }
}
