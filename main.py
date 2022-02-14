# 1. 게임시작
# 2. 플레이어2장 컴터1장
# 3. 플레이어 블랙잭 확인 => 블랙잭이면 플레이어 승리
# 4. 플레이어 hit or stay
# 5. 플레이어 hit 시 한장 추가 => 버스터체크
# 6. 플레이어 stay시 컴퓨터 16이하면 계속 한장 받아올것 => 여기서 컴터가 버스터시 플레이어승
# 7. 컴터는 17부터는 그만 가져온다.
# 8. 승패 비교
# 9. 컨티뉴 확인
import random as rd
import replit
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_burst(user):
  return sum(user) > 21

def check_blackjack(user):
  return sum(user) == 21

def draw_card(user):
  card = rd.choice(cards)
  if card != 11:
    user.append(card)
    return
  if card + sum(user) > 21 :
    user.append(1)
  else:
    user.append(11)

def ask_continue():
  continue_msg = "블랙잭 게임을 하시겠습니까?(y/n) >> "
  answer = input(continue_msg).lower() == "y"
  replit.clear()
  return answer

def show_info(player, com, endPhase = False):
  print(f"당신의 패 : {player}, 점수 : {sum(player)}")
  if endPhase:
    print(f"컴퓨터의 패 : {com}, 점수 : {sum(com)}")
  else:
    print(f"컴퓨터의 첫패 : {com[0]}")

# maingame
while ask_continue():
  print(art.logo)
  users = {"player" : [], "com": []}

  # Card Draw
  for _ in range(2):
    draw_card(users["player"])
    draw_card(users["com"])
  show_info(users["player"], users["com"])
  if check_blackjack(users["player"]):
    print("블랙잭! 당신의 승리입니다.")
    continue

  # Player Turn
  while input("카드를 더 받습니까?(y/n) >> ").lower() == "y":
    draw_card(users["player"])
    show_info(users["player"], users["com"])
    if check_blackjack(users["player"]) or check_burst(users["player"]):
      break
  
  show_info(users["player"], users["com"], True)
  if check_blackjack(users["player"]):
    print("블랙잭! 당신의 승리입니다.")
    continue
  if check_burst(users["player"]):
    show_info(users["player"], users["com"], True)
    print("버스트! 당신의 패배입니다.")
    continue
  # Com_Turn
  while sum(users["com"]) < 17:
    draw_card(users["com"])
    show_info(users["player"], users["com"], True)
  
  if check_blackjack(users["com"]):
    print("딜러가 블랙잭 입니다! 당신의 패배입니다.")
  elif check_burst(users["com"]):
    print("딜러가 버스트 입니다! 당신의 승리입니다.")
  elif sum(users["player"]) > sum(users["com"]):
    print("당신이 이겼습니다!")
  elif sum(users["player"]) < sum(users["com"]):
    print("당신의 패배입니다.")
  else:
    print("무승부!")
print("게임 오버")