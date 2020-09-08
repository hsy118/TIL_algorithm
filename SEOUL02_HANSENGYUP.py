import socket
import time
import math

# User and Launcher Information
NICKNAME = 'SEOUL02_HANSENGYUP'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s/' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send('%d/%d' % (CODE_REQUEST, CODE_REQUEST).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    angle = 00.0
    power = 00.0

    i = 1
    while i <= 10:
        # 흰공 셋팅
        whiteBall_x = gameData.balls[0][0]
        whiteBall_y = gameData.balls[0][1]
        # 목적구 셋팅
        if i % 2 != 0 and gameData.balls[(i%5)][0] != -1:
            targetBall1_x = gameData.balls[(i%5)][0]
            targetBall1_y = gameData.balls[(i%5)][1]
            pocket = finding_pocket(whiteBall_x, whiteBall_y, targetBall1_x, targetBall1_y)
            site = to_pocket(pocket, targetBall1_x, targetBall1_y)
            shot = shot_to(site, whiteBall_x, whiteBall_y)
            power = shot[0] * 2
            angle = shot[1]

            conn.send(angle, power)

        i += 1
    """
    # 목적구 셋팅
    if gameData.balls[1][0] != -1:
        targetBall1_x = gameData.balls[1][0]
        targetBall1_y = gameData.balls[1][1]
        targetBall1 = [targetBall1_x, targetBall1_y]
    if gameData.balls[2][0] != -1:
        targetBall2_x = gameData.balls[2][0]
        targetBall2_y = gameData.balls[2][1]
        targetBall2 = [targetBall2_x, targetBall2_y]
    if gameData.balls[3][0] != -1:
        targetBall3_x = gameData.balls[3][0]
        targetBall3_y = gameData.balls[3][1]
        targetBall3 = [targetBall3_x, targetBall3_y]
    if gameData.balls[4][0] != -1:
        targetBall4_x = gameData.balls[1][0]
        targetBall4_y = gameData.balls[1][1]
        targetBall4 = [targetBall4_x, targetBall4_y]
    if gameData.balls[5][0] != -1:
        targetBall5_x = gameData.balls[5][0]
        targetBall5_y = gameData.balls[5][1]
        targetBall5 = [targetBall5_x, targetBall5_y]
    """
    # 넣을 구멍 찾기 HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
def finding_pocket(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y):
    # 수구-목적구-구멍의 삼각형을 그려서, 목적구를 중심으로 180도랑 제일 가까운 구멍을 찾는다.


    for i in HOLES:
        pocket_x = i[0]
        pocket_y = i[1]

        # 수구 -목적구 거리
        line1 = ((targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2)**0.5
        # 목적구 - 포켓 거리
        line2 = ((pocket_x - targetBall_x)**2 + (pocket_y - targetBall_y)**2)**0.5
        # 수구- 포켓 거리
        line3 = ((whiteBall_x - pocket_x)**2 + (whiteBall_y - pocket_y)**2)**0.5
         #목적구 각도
        cos_angle = (line1**2 + line2**2 - line3**2) / (2 * line1 * line2)
        angle = math.acos(cos_angle)
        angle = math.degrees(angle)
        if 180-angle < 60:
            break
    pocket = (pocket_x, pocket_y)
    return pocket

def to_pocket(pocket, targetBall_x, targetBall_y):
    pocket_x = pocket[0]
    pocket_y = pocket[1]
    # 목적구에서 구멍까지의 벡터와 각도 theta
    vector_x = (pocket_x - targetBall_x)
    vector_y = (pocket_y - targetBall_y)
    # 목적구에서 구멍으로 향한 벡터의 반대 방향으로 수구의 지름만큼 연장한 좌표를 구함
    if vector_x > 0 and vector_y >0: #1사분면의 벡터
        theta = math.atan2(vector_y, vector_x)
        theta = abs(math.degrees(theta))
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 x
        site_x = round(math.cos(theta) * 5.72, 1)
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 y
        site_y = round(math.sin(theta) * 5.72, 1)
        site_x = targetBall_x - abs(site_x)
        site_y = targetBall_y - abs(site_y)
    elif vector_x < 0 and vector_y >0: #2사분면의 벡터
        theta = math.atan2(vector_y, vector_x)
        theta = abs(180 - math.degrees(theta))
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 x
        site_x = round(math.cos(theta) * 5.72, 1)
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 y
        site_y = round(math.sin(theta) * 5.72, 1)
        site_x = targetBall_x + abs(site_x)
        site_y = targetBall_y - abs(site_y)
    elif vector_x < 0 and vector_y < 0: # 3사분면의 벡터
        theta = math.atan2(vector_y, vector_x)
        theta = abs(math.degrees(theta) - 180)
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 x
        site_x = round(math.cos(theta) * 5.72, 1)
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 y
        site_y = round(math.sin(theta) * 5.72, 1)
        site_x = targetBall_x + abs(site_x)
        site_y = targetBall_y + abs(site_y)
    elif vector_x > 0 and vector_y < 0: #4사분면의 벡터
        theta = math.atan2(vector_y, vector_x)
        theta = abs(math.degrees(theta))
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 x
        site_x = round(math.cos(theta) * 5.72, 1)
        # 벡터의 반대 방향으로 지름만큼 연장한 좌표 y
        site_y = round(math.sin(theta) * 5.72, 1)
        site_x = targetBall_x - abs(site_x)
        site_y = targetBall_y + abs(site_y)

    site = (site_x, site_y)
    return site

def shot_to(site, whiteball_x, whiteball_y):
    # 수구 - to_pocket함수에서 구한 좌표  까지의 거리와 보내는 각도
    site_x = site[0]
    site_y = site[1]
    # 수구 - 목적구의 벡터의 방향을 4분면의 방향중 하나로 나누고, angle을 구함
    dx = site_x - whiteball_x
    dy = site_y - whiteball_y
    if dx > 0 and dy >= 0: # 1사분면일 경우
        angle = 90 - math.degrees(math.atan2(dy , dx))
    elif dx < 0 and dy > 0: # 2사분면일 경우
        angle = 360 - math.degrees(math.atan2(dy , dx))
    elif dx < 0 and dy < 0: # 3사분면일 경우
        angle = 90 + abs( math.degrees(math.atan2(dy , dx)) )
    else: # dx < 0 and dy > 0 4사분면일 경우
        angle = 90 + abs( math.degrees(math.atan2(dy , dx)) )

    distance = (dx**2 + dy**2)**0.5
    shot = (distance, angle)
    return shot


"""
경로에 딴공있음 x
수구랑 목적구의 직선공식을 구하고(ax+by+c=0)
점(x1,y1)과 거리의 공식인
d = abs(ax1+by1+c) / (a**2 + b**2) ** (0.5)
if d < 2r이면 x
--> check_ball1 = False
3번공 확인
만약 3번공도 check_ball2 = False면
"""




def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()
