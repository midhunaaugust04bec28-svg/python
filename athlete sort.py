You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.


if __name__ == '__main__':
    n, m = map(int, input().split())
    rows =[]
    for _ in range(n):
        rows.append(list(map(int,input().split())))
    k = int(input())

    rows.sort(key=lambda x: x[k])
    for row in rows:
        print(*row)


