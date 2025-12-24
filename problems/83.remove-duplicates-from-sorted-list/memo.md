## step1
何を返せばいい？先頭？
同じNodeで行き先が2つあることとかあるのか？
chatGPTで聞いたら今回はvalで判定するみたい
=> 141や142ではhead = [1,1,2,3,3]はNodeの行き先(next)を表していたのに一貫性がないように感じる

step2
currentのvalとcurrent.nextのvalを比較していきたいが、current.nextがNoneの時にNone.valでエラーが生じるためどこでcurrent.nextがNoneでないかを判定するか迷った
step1ではwhileの中でcurrent.nextがNoneでないことを確認した
=> headがListNodeの型の場合`while current.next:`と書けたと思っている

currentは他の人もよく書いているが、情報がないとの指摘もある
代わりにnodeを使っている人が多い印象
previousを使う場合はcurrentにするのが意図が伝わりやすそう
その場合でもpreviousNodeとか書いたほうが親切かも

他の方のコメントも確認したが概ね差がないように思える