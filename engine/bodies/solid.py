from ..base.spring import Spring

class Solid:
    """
    Class for a solid of point masses
    Expected input: a square 2d array of points in grid form where each point is given from left to right, bottom to top
    """
    def __init__(self, m, n, pts):
        self.m = m
        self.n = n
        self.pts = pts

        springs = []
        L = 50.0
        k = 0.1
        d = 0.2

        for i in range(m):

            for j in range(n):

                if i < m-1:

                    if j == 0:

                        # First column

                        s1 = Spring(A=pts[i][j], B=pts[i][j+1], L=L, k=k, d=d)
                        s2 = Spring(A=pts[i][j], B=pts[i+1][j+1], L=L, k=k, d=d)
                        s3 = Spring(A=pts[i][j], B=pts[i+1][j], L=L, k=k, d=d)

                        springs.append(s1)
                        springs.append(s2)
                        springs.append(s3)

                    elif j < n-1:

                        # 2nd column - 2nd to last column

                        s1 = Spring(A=pts[i][j], B=pts[i][j+1], L=L, k=k, d=d)
                        s2 = Spring(A=pts[i][j], B=pts[i+1][j+1], L=L, k=k, d=d)
                        s3 = Spring(A=pts[i][j], B=pts[i+1][j], L=L, k=k, d=d)
                        s4 = Spring(A=pts[i][j], B=pts[i+1][j-1], L=L, k=k, d=d)

                        springs.append(s1)
                        springs.append(s2)
                        springs.append(s3)
                        springs.append(s4)

                    else:

                        # Last column
                        s1 = Spring(A=pts[i][j], B=pts[i+1][j], L=L, k=k, d=d)
                        s2 = Spring(A=pts[i][j], B=pts[i+1][j-1], L=L, k=k, d=d)

                        springs.append(s1)
                        springs.append(s2)
                
                else:

                    # Top row
                    if j < n-1:
                        s = Spring(A=pts[i][j], B=pts[i][j+1], L=L, k=k, d=d)
                        springs.append(s)


        self.springs = springs