def solution(board, moves):
    count = 0
    basket = [0]
    turn_board = [list(reversed([i for i in col if i])) for col in zip(*board)]
    for idx in moves:
        if not turn_board[idx-1]:
            continue
        item = turn_board[idx-1].pop()
        if item == basket[-1]:
            basket.pop()
            count += 2
        else:
            basket.append(item)
    return count


# 테스트 코드
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
