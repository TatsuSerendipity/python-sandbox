import random

#ランダムの4桁の数字を生成する
def generate_number():
    number = str(random.randint(1000, 9999))
    return number

#ヒットとブローの数を計算
def get_hits_and_blows(guess, number):
    hits = 0
    blows = 0
    for i in range(len(number)):
        if guess[i] == number[i]:
            hits += 1
        elif guess[i] in number:
            blows += 1
    return (hits, blows)

def play_game():
    count = 0
    number = generate_number()
    print("4桁の数字を入力してください(回答はAを入力): ")
    while True:
        guess = input().strip()
        count += 1
        if guess == "A":
            print("正解は　", number, "　です！")
        if len(guess) != 4 or not guess.isdigit():
            print("4桁の数字を入力してください")
            continue
        (hits, blows) = get_hits_and_blows(guess, number)
        if hits == 4:
            print("正解です！", number, ":", count, "回かかりました。")
            break
        print("Hits:", hits, "Blows:", blows)

play_game()
