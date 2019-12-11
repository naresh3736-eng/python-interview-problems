def prinnt_max_size_sub_matrix(M):
    R = len(M)
    C = len(M[0])
    #S = [0][0]

    # for i in range(R):
    #     S[i][0] = M[i][0]
    #
    # for j in range(C):
    #     S[0][j] = M[0][j]

    S = [[0 for i in range(R)] for j in range(C)]


    for i in range(1, R):
        for j in range(1, C):
            if M[i][j] == 1:
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            else:
                S[i][j] = 0


    max_of_s = S[0][0]
    max_i = 0
    max_j = 0

    for i in range(R):
        for j in range(C):
            if S[i][j] > max_of_s:
                max_of_s = S[i][j]
                max_i = i
                max_j = j


    for i in range(max_j, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j],)
        print(" ")
