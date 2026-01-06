import tkinter as tk
import random
from tkinter import messagebox

# --- 完整細分資料庫 (已修正漢字誤植) ---
DATA = {
    "平假名_清音": {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so", "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
        "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
        "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "や": "ya", "ゆ": "yu", "よ": "yo", "ら": "ra", "り": "ri",
        "る": "ru", "れ": "re", "ろ": "ro", "わ": "wa", "を": "wo", "ん": "n"
    },
    "平假名_濁音/半濁音": {
        "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
        "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do", "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
        "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"
    },
    "平假名_拗音": {
        "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo", "しゃ": "sha", "しゅ": "shu", "しょ": "sho", "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
        "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
        "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo", "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo", "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
        "びゃ": "bya", "びゅ": "byu", "びょ": "byo", "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"
    },
    "片假名_清音": {
        "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o", "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
        "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so", "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
        "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no", "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
        "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo", "ヤ": "ya", "ユ": "yu", "ヨ": "yo", "ラ": "ra", "リ": "ri",
        "ル": "ru", "レ": "re", "ロ": "ro", "ワ": "wa", "ヲ": "wo", "ン": "n"
    },
    "片假名_濁音/半濁音": {
        "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go", "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
        "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do", "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
        "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"
    },
    "片假名_拗音": {
        "キャ": "kya", "キュ": "kyu", "キョ": "kyo", "シャ": "sha", "シュ": "shu", "ショ": "sho", "チャ": "cha", "チュ": "chu", "チョ": "cho",
        "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo", "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo", "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
        "リャ": "rya", "リュ": "ryu", "リョ": "ryo", "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo", "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
        "ビャ": "bya", "ビュ": "byu", "ビョ": "byo", "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo"
    }
}

class KanaApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        
        # 透明背景設定
        self.bg_magic = "#abcdef"
        self.root.config(bg=self.bg_magic)
        self.root.attributes("-transparentcolor", self.bg_magic)

        self.text_color = "white"
        self.base_size = 45
        self.wrong_history = []
        
        # 預設全選
        self.selected_vars = {name: tk.BooleanVar(value=True) for name in DATA.keys()}
        self.question_pool = []
        
        # UI 元件
        self.label_kana = tk.Label(root, text="", font=("Helvetica", self.base_size, "bold"), 
                                   fg=self.text_color, bg=self.bg_magic, bd=0, highlightthickness=0)
        self.label_kana.pack()

        self.entry = tk.Entry(root, font=("Helvetica", 16), justify='center', width=6, 
                              bd=0, highlightthickness=1, highlightbackground="gray")
        self.entry.pack(pady=2)
        self.entry.bind("<Return>", self.check_answer)
        self.entry.focus_set()

        self.label_feedback = tk.Label(root, text="", font=("Helvetica", 10, "bold"), bg=self.bg_magic, bd=0)
        self.label_feedback.pack()

        # 事件綁定
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.do_move)
        self.root.bind("<MouseWheel>", self.on_zoom)

        # 右鍵選單
        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="查看錯誤列表", command=self.show_wrong_list)
        self.menu.add_separator()
        for name in DATA.keys():
            self.menu.add_checkbutton(label=name, variable=self.selected_vars[name], command=self.refresh_pool)
        self.menu.add_separator()
        self.menu.add_command(label="文字顏色：白色", command=lambda: self.set_color("white"))
        self.menu.add_command(label="文字顏色：黑色", command=lambda: self.set_color("black"))
        self.menu.add_command(label="關閉程式", command=root.quit)
        self.root.bind("<Button-3>", self.show_menu)

        self.refresh_pool()
        self.update_layout()

    def refresh_pool(self):
        """更新題目池"""
        self.question_pool = []
        for name, var in self.selected_vars.items():
            if var.get():
                for k, v in DATA[name].items():
                    self.question_pool.append((k, v, "平假名" if "平假名" in name else "片假名"))
        
        random.shuffle(self.question_pool)
        # 初始刷新不需要跳通知
        self.next_question(is_initial=True)

    def next_question(self, is_initial=False):
        if not self.question_pool:
            if not is_initial:
                messagebox.showinfo("練習完成", "已經作答完一輪了！")
                self.refresh_pool()
            else:
                self.label_kana.config(text="") # 清除文字不顯示"空"
            return

        self.current_kana, self.current_romaji, self.current_type = self.question_pool.pop()
        self.label_kana.config(text=self.current_kana)
        self.entry.delete(0, tk.END)

    def check_answer(self, event=None):
        # 去除所有空白字元（包括不小心按到的空白）
        user_input = self.entry.get().replace(" ", "").strip().lower()
        if not hasattr(self, 'current_romaji'): return # 防止沒題目時報錯

        # 羅馬拼音替代寫法對照表
        romaji_alternatives = {
            'chi': ['chi', 'ti'],
            'shi': ['shi', 'si'],
            'tsu': ['tsu', 'tu'],
            'fu': ['fu', 'hu'],
            'jo': ['jo', 'jyo'],
            'ja': ['ja', 'jya'],
            'ju': ['ju', 'jyu'],
        }
        
        # 建立當前答案的所有可接受寫法
        accepted_answers = [self.current_romaji]
        for standard, alternatives in romaji_alternatives.items():
            if self.current_romaji in alternatives:
                accepted_answers = alternatives
                break
        
        # 檢查答案是否正確
        if user_input in accepted_answers:
            self.label_feedback.config(text="✓", fg="#2ecc71")
            self.root.after(400, lambda: self.next_question())
        else:
            wrong_match = "?"
            search_prefix = self.current_type 
            for name, content in DATA.items():
                if search_prefix in name:
                    for k, v in content.items():
                        if v == user_input:
                            wrong_match = k
                            break
            
            error_text = f"{self.current_kana}({self.current_romaji}) != {wrong_match}({user_input})"
            self.label_feedback.config(text=error_text, fg="#e74c3c")
            
            record = f"{self.current_kana} ({self.current_romaji})"
            if record not in self.wrong_history:
                self.wrong_history.append(record)

    def on_zoom(self, event):
        delta = 2 if event.delta > 0 else -2
        if 15 < self.base_size + delta < 150:
            self.base_size += delta
            self.update_layout()

    def update_layout(self):
        self.label_kana.config(font=("Helvetica", self.base_size, "bold"))
        self.entry.config(font=("Helvetica", int(self.base_size * 0.4)))
        self.label_feedback.config(font=("Helvetica", int(self.base_size * 0.22), "bold"))
        self.root.geometry(f"{int(self.base_size*4)}x{int(self.base_size*3.2)}")

    def start_move(self, event): self.x, self.y = event.x, event.y
    def do_move(self, event): self.root.geometry(f"+{self.root.winfo_x()+(event.x-self.x)}+{self.root.winfo_y()+(event.y-self.y)}")
    def show_menu(self, event): self.menu.post(event.x_root, event.y_root)
    def set_color(self, color): self.text_color = color; self.label_kana.config(fg=color)
    def show_wrong_list(self):
        win = tk.Toplevel(self.root); win.title("錯誤紀錄"); win.attributes("-topmost", True)
        lb = tk.Listbox(win); lb.pack(expand=True, fill="both")
        for item in reversed(self.wrong_history): lb.insert("end", item)

if __name__ == "__main__":
    root = tk.Tk()
    app = KanaApp(root)
    root.mainloop()