N = int(input())

result = True
currentT, currentX, currentY = 0, 0, 0
for i in range(N):
    if result is False:
        break
    targetT, targetX, targetY = map(int, input().split())
    diffT = targetT - currentT
    diffX = abs(targetX - currentX)
    diffY = abs(targetY - currentY)

    if (diffT - diffX - diffY) % 2 == 0 and diffT - diffX - diffY >= 0:
        result = True
        currentT, currentX, currentY = targetT, targetX, targetY
    else:
        result = False
print("Yes" if result else "No")
