## step1
```
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    reached = set()
    current = head
    while current:
        if current in reached:
            return current
        reached.add(current)
        current = current.next
    return
```

これでYour returned value is not a ListNode type.になる理由がわからない、、、
ListNodeのclassの定義を無くすと動いた、、、
141では定義をつけたまま動かしていて問題なく回答ができた
一貫性がなく、leetcodeの仕様むずい、、、

## step2

141への指摘でisと＝＝の違いについてレビューを受けた
if cuurent:のコードはよく見るのでこちらの方が多数派だと思う
ただisと==の違いはしっかり理解したい
元々の理解ではNoneとの比較の際はis Noneと書くように暗記していて、他の場面では使わなかった=>原理を理解せず良くなかった
- isは同一オブジェクトかどうか、==は`__eq__`を呼び比較
- Noneは唯一のオブジェクト
- X is not Noneで比較した場合、XはNoneの時以外はTrueにできる
- 一方で、if X:の場合はNone以外にも空の配列や0や空文字列などFalsyな値も含んでしまう 
今後気にしたい

今回の場合return Noneと書くかreturnと書くか迷った
普段ならreturnと書くが他の方のものを見るとreturn Noneが多そうなので合わせる

空間計算量O(1)の解法を考える
- loopするかどうかを考える
  - Floydの循環検出でできそう
- 元の連結リストで最初に出てくるNodeを求める
  - これがわからない
- head → cycle開始点までの距離 = a
- cycleの長さ = b
- 出会い点までの距離（cycle内） = c
- head --a--> [cycle start] --c--> [meeting point]--d-->[cycle start]
- slow / fast が出会ったとき
  - slow が進んだ距離：a + c
  - fast が進んだ距離：2(a + c), a+2c+d, a+c+b*n
- fast は slow より ちょうど cycle を n 周多く回っている
- 2(a+c) = a+2c+d => a = d
- => meeting pointからcycle startまでとheadからcycle startまでの距離は等しい！！！

書き方迷った点
- `if hasLoop != True:`
  - `if not hasLoop`にすべき
- hasLoopが本当に必要か？
- step1とstep2を関数化すればスッキリする？
- Nodeが等しくないことを確かめるにはis notを使うべきなのに!=と書いていた
