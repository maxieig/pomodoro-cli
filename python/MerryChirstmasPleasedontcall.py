import tkinter as tk
import math
import random

# ---------------- config ----------------
W, H = 620, 320
# Deep, intimate plum-black background that evokes late-night yearning
BG = "#0D0208"

lyrics = [
    ("To the tempo of your uptight", 0.06, 2.0),
    ("Is the flicker of a street light", 0.06, 2.2),
    ("You know this moment, don't ya?", 0.07, 2.5),
    ("And time is strangely calm now", 0.06, 2.2),
    ("'Cause everybody's gone, it's", 0.06, 1.8),
    ("Just you and your anger", 0.07, 2.8),
    ("So don't tell them what you told me", 0.06, 2.2),
    ("Don't hold me like you know me", 0.06, 2.2),
    ("I would rather burn forever", 0.07, 2.6),
    ("But you should know that I died slow", 0.06, 2.4),
    ("Running through the halls of your haunted home", 0.05, 3.0),
    ("Merry Christmas, please don't call", 0.08, 3.5),
    ("Merry Christmas, I'm not yours at all", 0.08, 3.5),
    ("Please don't call me...", 0.09, 3.0),
]

root = tk.Tk()
root.title("Bleachers - Merry Christmas Please Don't Call")
root.configure(bg=BG)
root.resizable(False, False)

sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{W}x{H}+{(sw - W) // 2}+{(sh - H) // 2}")

canvas = tk.Canvas(root, width=W, height=H, bg=BG, highlightthickness=0)
canvas.pack()

label = tk.Label(root, text="", font=("Helvetica", 20, "bold"),
                 fg="#FFFFFF", bg=BG, wraplength=W - 80, justify="center")
label.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- longing particles ----------------
particles = []


def create_particles(num=130):
    for _ in range(num):
        x = random.randint(0, W)
        y = random.randint(0, H)
        kind = random.choices(
            ["ember", "dust", "star"],
            weights=[40, 45, 15]
        )[0]

        if kind == "ember":
            # Warm rising embers/sparks representing lingering emotion
            size = random.randint(2, 4)
            item = canvas.create_oval(
                x, y, x + size, y + size,
                fill=random.choice(["#E29578", "#FFDDD2", "#E07A5F"]),
                outline=""
            )
            particles.append({"id": item, "kind": kind,
                              "speed": random.uniform(-1.2, -0.4),  # rises upward
                              "drift": random.uniform(-0.3, 0.3)})

        elif kind == "dust":
            # Soft floating dust particles
            size = random.randint(1, 3)
            item = canvas.create_oval(
                x, y, x + size, y + size,
                fill=random.choice(["#6B2D5C", "#4A154B", "#9C4668"]),
                outline=""
            )
            particles.append({"id": item, "kind": kind,
                              "speed": random.uniform(0.2, 0.8),
                              "drift": random.uniform(-0.5, 0.5)})

        else:  # star
            size = random.randint(2, 5)
            item = canvas.create_text(
                x, y, text="✧", font=("Helvetica", size),
                fill=random.choice(["#F4A261", "#E76F51", "#D8E2DC"])
            )
            particles.append({"id": item, "kind": kind,
                              "speed": random.uniform(-0.3, 0.3),
                              "drift": random.uniform(-0.2, 0.2)})


def animate_particles():
    for p in particles:
        item, kind = p["id"], p["kind"]

        canvas.move(item, p["drift"], p["speed"])
        
        # Check boundary depending on direction
        if kind in ("snow", "sparkle", "dust", "star"):
            coords = canvas.coords(item)
            if len(coords) == 2:
                x, y = coords
            else:
                x, y = coords[0], coords[1]

            if y > H + 20:
                canvas.coords(item, random.randint(0, W), -10)
            elif y < -20:
                canvas.coords(item, random.randint(0, W), H + 10)
            elif x < -20:
                canvas.coords(item, W + 20, y)
            elif x > W + 20:
                canvas.coords(item, -20, y)

        elif kind == "ember":
            coords = canvas.coords(item)
            if len(coords) >= 2:
                x, y = coords[0], coords[1]
                if y < -10:
                    canvas.coords(item, random.randint(0, W), H + 10, random.randint(0, W) + 3, H + 13)

    root.after(30, animate_particles)


def twinkle_particles():
    palette = ["#E29578", "#FFDDD2", "#E07A5F", "#9C4668", "#F4A261"]
    for p in particles:
        if p["kind"] in ("ember", "star"):
            if p["kind"] == "star":
                canvas.itemconfig(p["id"], fill=random.choice(palette))
            else:
                canvas.itemconfig(p["id"], fill=random.choice(palette))
    root.after(400, twinkle_particles)


# ---------------- warm melancholic glow ----------------
# Fades between a soft warm white and a deep rose gold/crimson glow
GLOW_A = (255, 235, 224)   # soft warm cream
GLOW_B = (224, 122, 95)    # melancholic terracotta / rose gold


def glow_effect(t=0.0):
    k = (math.sin(t) + 1) / 2
    r, g, b = (int(a + (c - a) * k) for a, c in zip(GLOW_A, GLOW_B))
    label.config(fg=f"#{r:02x}{g:02x}{b:02x}")
    root.after(45, glow_effect, t + 0.06)


# ---------------- typewriter ----------------
def typewriter(loop=True):
    state = {"line": 0, "char": 0, "phase": "typing"}

    def step():
        li = state["line"]
        if li >= len(lyrics):
            if loop:
                state.update(line=0, char=0, phase="typing")
                root.after(1500, step)
            return

        line, char_delay, line_delay = lyrics[li]

        if state["phase"] == "typing":
            state["char"] += 1
            label.config(text=line[:state["char"]])
            if state["char"] >= len(line):
                state["phase"] = "hold"
                root.after(int(line_delay * 1000), step)
            else:
                root.after(int(char_delay * 1000), step)
        else:  # hold finished -> clear and move on
            label.config(text="")
            state.update(line=li + 1, char=0, phase="typing")
            root.after(300, step)

    step()


# ---------------- go ----------------
create_particles(130)
animate_particles()
twinkle_particles()
glow_effect()
root.after(500, typewriter)

root.mainloop()