---
layout: post
title: "LeetCode 88. 合并两个有序数组"
date: 2026-02-11 11:00:00
description: 双指针解决有序数组合并问题，支持原地修改和额外空间两种方案
tags: [双指针, LeetCode, 算法]
categories: [算法题解]
---

## 题目描述

给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n`，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0`，应忽略。`nums2` 的长度为 `n`。

## 示例

**示例 1：**

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

## 解题思路

### 方法一：从后向前双指针（原地修改）

由于两个数组均有序，且 `nums1` 后面有足够空间，可以从后向前填充。

**算法步骤**：
1. 使用三个指针：
   - `p1` 指向 `nums1` 的第 m 个元素（最后一个有效元素）
   - `p2` 指向 `nums2` 的第 n 个元素（最后一个元素）
   - `tail` 指向 `nums1` 的最后位置（m + n - 1）
2. 每次比较 `nums1[p1]` 和 `nums2[p2]`，取较大值放到 `nums1[tail]`
3. 移动对应指针，直到所有元素处理完毕

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1, p2 = n - 1;
        int tail = m + n - 1;
        int tar;
        
        while(p1 >= 0 || p2 >= 0){
            if(p1 == -1){ // 如果p1走到终点把p2的搬过来，两个数组均有序，所以可以直接搬
                tar = nums2[p2];
                p2--;
            }else if(p2 == -1){
                tar = nums1[p1]; // 如果p2走到终点把p1的搬过来
                p1--;
            }else if(nums1[p1] > nums2[p2]){
                tar = nums1[p1];
                p1--;
            }else{
                tar = nums2[p2];
                p2--;
            }
            nums1[tail] = tar;
            tail--;
        }
    }
};
```

**复杂度分析**：
- **时间复杂度**：O(m + n)，遍历两个数组各一次
- **空间复杂度**：O(1)，原地修改，只使用常数额外空间

---

### 方法二：使用额外数组

使用额外数组存储合并结果，然后复制回 `nums1`。

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0, j = 0;
        int pos = 0;
        int ans[m+n];
        
        while(i < m || j < n){
            if(i == m){
                ans[pos++] = nums2[j];
                j++;
            }else if(j == n){
                ans[pos++] = nums1[i];
                i++;
            }else if(nums1[i] > nums2[j]){
                ans[pos++] = nums2[j];
                j++;
            }else{
                ans[pos++] = nums1[i];
                i++;
            }
        }
        
        for(int i = 0; i < m + n; i++){
            nums1[i] = ans[i];
        }
    }
};
```

**复杂度分析**：
- **时间复杂度**：O(m + n)
- **空间复杂度**：O(m + n)，使用了额外数组

## 总结

- 方法一更优，实现了 O(1) 空间复杂度的原地修改
- 关键在于利用 `nums1` 后面的空余空间，从后向前填充
- 这种技巧在处理有序数组合并时非常实用
