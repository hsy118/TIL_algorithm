"""
def aim_angel(a, b)
def sugu_angle(a, b)

1. 목적구 정하기.
goal_ball1 = True
goal_ball2 = True
면 8번으로 고고

가장 낮은 번호를 구함(기준 (0,0)인가 아닌가)
2. 넣을 구멍 찾기.
코사인 제 2법칙
3. 목적구 -> 구멍 벡터 atan2((x2-x1),(y2-y1))해서
각도 찾기
4. 목적구에서 구멍으로 향한 벡터의 반대로 지름만큼 연장한 좌표 구함
벡터 방향이 3개의 경우
1,4사분면이면 abs(theta)
2 사분면이면 abs(180-theta)
3 사분면이면 abs(theta-180)

경로에 딴공있음 x
수구랑 목적구의 직선공식을 구하고(ax+by+c=0)
점(x1,y1)과 거리의 공식인
d = abs(ax1+by1+c) / (a**2 + b**2) ** (0.5)
if d < 2r이면 x
--> check_ball1 = False
3번공 확인
만약 3번공도 check_ball2 = False면

5. atan으로 수구 각도 정하고 힘설정(1~4사분면나누고).

    dx = gameData.balls[i][0] - gameData.balls[0][0]
    dy = gameData.balls[i][1] - gameData.balls[0][1]
    if dx > 0 and dy >= 0: # 1사분면일 경우
        angle = 90 - math.degrees(math.atan2(dy , dx))
    elif dx > 0 and dy < 0: # 2사분면일 경우
        angle = 360 - math.degrees(math.atan2(dy , dx))
    elif dx < 0 and dy < 0: # 3사분면일 경우
        angle = 90 + abs( math.degrees(math.atan2(dy , dx)) )
    else: # dx < 0 and dy > 0 4사분면일 경우
        angle = 90 + abs( math.degrees(math.atan2(dy , dx)) )

"""
import math
# def cal_angel(x1, a1):
#     dy = a1[1] - x1[1]
#     dx = a1[0] - x1[0]
#     if dx > 0 and dy >= 0: # 1사분면일 경우
#         angle = 90 - math.degrees(math.atan(dy / dx))
#     elif dx > 0 and dy < 0: # 2사분면일 경우
#         angle = 360 - math.degrees(math.atan(dy / dx))
#     elif dx < 0 and dy < 0: # 3사분면일 경우
#         angle = abs (90 + math.degrees(math.atan(dy / dx)) )
#     else: # dx < 0 and dy > 0 4사분면일 경우
#         angle = 90 + abs( math.degrees(math.atan(dy / dx)) )
#
#
# a = (1, 1)
# x =( 0, 0)
# theta = math.atan2(a[1]-x[1], a[0]-x[0])
#
# degree_theta=  abs(math.degrees(theta))
# #
# print(degree_theta)
# cosineX = (1**2 + 2**2 - (3**0.5)**2) / (2 * 1 * 2)
# cosineX = (a**2 + b**2 - c**2) / (2 *a*b)
# print(cosineX)
# result= math.acos(cosineX)
# yy = round(math.degrees(result))
# print(yy)

print(math.sin(51) * 5.72)
