""" 
    Kaun Banega Crorepati in DSA (15 questions, 3 stages) 
"""
lst_que = ["What is the time complexity of accessing an element in an array by index?", "Which data structure is best suited for implementing a stack?", "What is the worst-case time complexity of a binary search algorithm?", "Which of the following sorting algorithms has the best average case time complexity?", "In a graph, which algorithm is used to find the shortest path between two nodes in a weighted graph?", "What is the time complexity of inserting an element into a binary search tree in the worst case?", "Which of the following is the correct traversal order for in-order traversal of a binary tree?", "What is the height of an AVL tree with n nodes in terms of time complexity?", "Which data structure is used to detect cycles in a graph?", "Which of the following algorithms is used to solve the longest increasing subsequence problem in O(n log n) time complexity?", "What is the maximum number of edges in a simple undirected graph with n vertices?", "In dynamic programming, which property defines that an optimal solution can be constructed from optimal solutions of its subproblems?", "Which of the following is an NP-complete problem?", "What is the amortized time complexity for insertion into a dynamic array (resizable array)?", "What is the time complexity of solving the 0/1 Knapsack Problem using dynamic programming?"]
lst_ans = [ "C" , "C" , "A" , "C" , "D" , "A", "A" , "A" , "C" , "B" , "A" , "D" , "C" , "A" , "C" ]
lst_opt = ["A) O(n)\tB) O(log n)\nC) O(1)\tD) O(n log n)", "A) Array\tB) Queue\nC) Linked List\tD) Tree", "A) O(log n)\tB) O(n)\nC) O(n log n)\tD) O(1)", "A) Bubble Sort\tB) Selection Sort\nC) Merge Sort\tD) Insertion Sort", "A) DFS (Depth First Search)\tB) BFS (Breadth First Search)\nC) Kruskal's Algorithm\tD) Dijkstra's Algorithm", "A) O(n)\tB) O(log n)\nC) O(n^2)\tD) O(1)", "A) Left, Root, Right\tB) Root, Left, Right\nC) Left, Right, Root\tD) Right, Root, Left", "A) O(log n)\tB) O(n)\nC) O(1)\tD) O(n log n)", "A) Stack\tB) Queue\nC) Union-Find (Disjoint Set)\tD) Linked List", "A) Dynamic Programming with O(n^2)\tB) Binary Search with Dynamic Programming\nC) Merge Sort\tD) Quick Sort", "A) n(n - 1)/2\tB) n(n + 1)/2\nC) n^2\tD) n(n - 2)", "A) Memoization\tB) Overlapping Subproblems\nC) Greedy Choice Property\tD) Optimal Substructure", "A) Sorting\tB) Searching\nC) Travelling Salesman Problem\tD) Binary Search", "A) O(1)\tB) O(log n)\nC) O(n)\tD) O(n^2)", "A) O(n)\tB) O(n log n)\nC) O(nW) (where W is the capacity of the knapsack)\tD) O(n^2)"]
lst_stage = ["Rs. 0", "Rs. 10,000", "Rs. 3,20,000", "Rs. 1 Crore"]
lst_win = ["Rs. 1,000", "Rs. 2,000", "Rs. 3,000", "Rs. 5,000", "Rs. 10,000", "Rs. 20,000",
           "Rs. 40,000", "Rs. 80,000", "Rs. 1,60,000", "Rs. 3,20,000", "Rs. 6,40,000",
           "Rs. 12,50,000", "Rs. 25,00,000", "Rs. 50,00,000", "Rs. 1 Crore"
            ]
print("Be Ready To Play Kaun Banega Crorepati !")
name = input("Enter Your Name :")
K=True
i=0
S=0
while K:
    if S==3 :
        print(f"\nCongratulations {name} :)\nYou Are A CROREPATI Now !!!")
        break
    print(f"\tQuestion for {lst_win[i]}")
    print(lst_que[i])
    print(lst_opt[i])
    if i>5 :
        j=input("Enter the correct option (OR Press 0 to QUIT) : ")
        if j=="0" :
            print(f"Thanks for playing:)\nThe correct option is : {lst_ans[i]}")
            print(f"{name} Wins : {lst_stage[S]}")
            break
    else:
        j=input("Enter the correct option : ")
    j=j.upper()
    if lst_ans[i]==j :
        if lst_win[i] in lst_stage :
            S=S+1
        i=i+1
    else:
        print(f"You Lose:(\nThe correct option is : {lst_ans[i]}")
        print(f"{name} Wins : {lst_stage[S]}")
        break
