#### 1. [SettingWithCopy warning](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy)
- 가끔씩 `SettingWithCopy` Warning이 뜬다.
- 목적은 Multi-Indexing된 column에 접근할 때 `df['a']['b]`식의 접근보다 `df.loc[:, ('a','b')]` 접근을 강력히 권장하기 위함이다.
- 의도치 않게 이런 Warning이 뜨는 경우가 있는데 DataFrame을 이미 한 번 복사해서 사용하는 경우다. (추측이 X, 페이지에 써있는 내용)
