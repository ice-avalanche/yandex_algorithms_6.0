def solution(a, b, c, d):
    if (a == 0 and c == 0) or (b == 0 and d == 0):
        return "1 1"
    
    elif (a == 0 or b == 0) and (c != 0 or d != 0):
        return f"1 {min(c, d) + 1}" if (a > b and c > d) or (a < b and c < d) else f"1 {max(c, d) + 1}"
    
    elif (a != 0 or b != 0) and (c == 0 or d == 0):
        return f"{min(a, b) + 1} 1" if (a > b and c > d) or (a < b and c < d) else f"{max(a, b) + 1} 1"
    
    elif (a > b and c > d) or (a < b and c < d):
        option1 = min(a, b) + min(c, d) + 2
        option2 = max(a, b) + 2
        option3 = max(c, d) + 2
        if option1 <= min(option2, option3):
            return f"{min(a, b) + 1} {min(c, d) + 1}"
        elif option2 <= option3:
            return f"{max(a, b) + 1} 1"
        else:
            return f"1 {max(c, d) + 1}"
    
    else:
        return f"{max(a, b) + 1} 1" if max(a, b) + 2 <= max(c, d) + 2 else f"1 {max(c, d) + 1}"
    

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(solution(a, b, c, d))
