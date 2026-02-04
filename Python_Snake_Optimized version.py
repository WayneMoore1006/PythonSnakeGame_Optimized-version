import turtle
import time
import random

tick_gap = 0.1

# 分數
current_pts = 0
best_pts = 0

# 螢幕設定
stage = turtle.Screen()
stage.title("貪食蛇")
stage.bgcolor("green")
stage.setup(width=600, height=600)
stage.tracer(0)

# 蛇本體
head_unit = turtle.Turtle()
head_unit.speed(0)
head_unit.shape("square")
head_unit.color("black")
head_unit.penup()
head_unit.goto(0, 0)
head_unit.face = "stop"

# 蛇的食物
bait = turtle.Turtle()
bait.speed(0)
bait.shape("circle")
bait.color("red")
bait.penup()
bait.goto(0, 100)

body_chain = []  # 身體串列

# 計分板
score_panel = turtle.Turtle()
score_panel.speed(0)
score_panel.shape("square")
score_panel.color("white")
score_panel.penup()
score_panel.hideturtle()
score_panel.goto(0, 260)
score_panel.write(
    "本局分數: 0  歷史最高分: 0",
    align="center",
    font=("Courier", 24, "normal")
)


class GameController:
    def redraw_score(self):
        score_panel.clear()
        score_panel.write(
            "本局分數: {}  歷史最高分: {}".format(current_pts, best_pts),
            align="center",
            font=("Courier", 24, "normal")
        )

    def clear_body(self):
        # 把身體給隱藏
        for part in body_chain:
            part.goto(1000, 1000)

    def restart_round(self):
        global current_pts, tick_gap
        time.sleep(1)

        head_unit.goto(0, 0)
        head_unit.face = "stop"

        self.clear_body()

        # 清除身體串列
        body_chain.clear()

        # 重置分數
        current_pts = 0

        # 重置時的延遲時間
        tick_gap = 0.1

        self.redraw_score()

    def drop_food(self):
        # 將下一次食物隨機傳送到其他點位
        bait.goto(
            random.randint(-290, 290),
            random.randint(-290, 290)
        )

    def extend_body(self):
        # 增加身體長度
        node = turtle.Turtle()
        node.speed(0)
        node.shape("square")
        node.color("grey")
        node.penup()
        body_chain.append(node)

    def shift_head(self):
        if head_unit.face == "stop":
            return

        x, y = head_unit.xcor(), head_unit.ycor()

        if head_unit.face == "up":
            y += 20
        elif head_unit.face == "down":
            y -= 20
        elif head_unit.face == "left":
            x -= 20
        elif head_unit.face == "right":
            x += 20

        head_unit.goto(x, y)

    def drag_body(self):
        # 當下達迴轉指令時，將串列首尾互換
        if not body_chain:
            return

        trail = [(head_unit.xcor(), head_unit.ycor())]
        trail += [(p.xcor(), p.ycor()) for p in body_chain[:-1]]

        for part, pos in zip(body_chain, trail):
            part.goto(pos)

    def hit_border(self):
        # 如果撞到牆壁的話
        return (
            head_unit.xcor() > 290 or head_unit.xcor() < -290 or
            head_unit.ycor() > 290 or head_unit.ycor() < -290
        )

    def bite_self(self):
        # 當撞到自己身體時重置
        for part in body_chain:
            if part.distance(head_unit) < 20:
                return True
        return False

    def eat_check(self):
        return head_unit.distance(bait) < 20

    def game_tick(self):
        global current_pts, best_pts, tick_gap

        stage.update()

        if self.hit_border():
            self.restart_round()
            return self.schedule_next()

        if self.eat_check():
            self.drop_food()
            self.extend_body()

            # 縮短時延遲
            tick_gap -= 0.001

            # 吃到食物增加的分數
            current_pts += 10
            if current_pts > best_pts:
                best_pts = current_pts

            self.redraw_score()

        self.drag_body()
        self.shift_head()

        if self.bite_self():
            self.restart_round()

        self.schedule_next()

    def schedule_next(self):
        delay_ms = int(max(0.01, tick_gap) * 1000)
        stage.ontimer(self.game_tick, delay_ms)


controller = GameController()

# 行動函數
def cmd_up():
    if head_unit.face != "down":
        head_unit.face = "up"

def cmd_down():
    if head_unit.face != "up":
        head_unit.face = "down"

def cmd_left():
    if head_unit.face != "right":
        head_unit.face = "left"

def cmd_right():
    if head_unit.face != "left":
        head_unit.face = "right"

# 鍵盤上下左右
stage.listen()
stage.onkeypress(cmd_up, "w")
stage.onkeypress(cmd_down, "s")
stage.onkeypress(cmd_left, "a")
stage.onkeypress(cmd_right, "d")

# 主要程式
controller.game_tick()
stage.mainloop()
