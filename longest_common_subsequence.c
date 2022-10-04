/**
 * Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

* A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

* For example, "ace" is a subsequence of "abcde".
* A common subsequence of two strings is a subsequence that is common to both strings.
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int max(int a, int b) {
    return a > b ? a : b;
}

int longestCommonSubsequence(char * text1, char * text2) {
    int i, j;
    int l1 = strlen(text1);
    int l2 = strlen(text2);
    int **dp = malloc((l1 + 1) * sizeof(int *));
    for (i = 0; i < l1 + 1; i++) {
        dp[i] = malloc((l2 + 1) * sizeof(int));
    }
    memset(dp[0], 0, (l2 + 1) * sizeof(int));
    for (i = 1; i <= l1; i++) {
        dp[i][0] = 0;
    }

    for (i = 1; i <= l1; i++) {
        for (j = 1; j <= l2; j++) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[l1][l2];
}

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: ./test s1 s2\n");
        exit(-1);
    }

    printf("%d\n", longestCommonSubsequence(argv[1], argv[2]));
    return 0;
}

/**
 * Author : Pythonicboat
 * Objective : Longest common subsequence
 * References : https://leetcode.com/problems/longest-common-subsequence/
 **/
