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

