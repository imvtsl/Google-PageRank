import numpy as np
import scipy


def main():
    matrix = np.array([[0, 0, 1, 0.5], [0.33, 0, 0, 0], [0.33, 0.5, 0, 0.5], [0.33, 0.5, 0, 0]])
    print('The input matrix is:', matrix)

    # calculate eigen vector on input matrix
    values, vectors = scipy.sparse.linalg.eigs(matrix, k=1, sigma=1)
    print('E-value:', values)
    print('E-vector:', vectors)

    # map page to its importance from calculated eigen vector
    page_importance = map_importance(vectors)

    # print pages in decreasing order of importance
    print('Pages in decreasing order of importance:')
    for w in sorted(page_importance, key=page_importance.get, reverse=True):
        print(w)


def map_importance(vectors):
    page_importance = {}
    i = 1
    for vec in vectors:
        page_importance[i] = vec[0]
        i += 1
    print('Importance of pages are:', page_importance)
    return page_importance


if __name__ == "__main__":
    main()
