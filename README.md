# matplotlib-japreset

`matplotlib` で日本語を自由に表示し保存するための自動設定モジュール

**Linuxでしか動作確認していない**

```sh
pip install -U git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master
```

## 機能

* Python グラフィックパッケージで使用するデフォルトのフォントを自動で日本語フォントに変更します. 現在対応しているパッケージは以下です
    * matpliolib
    * plotnine
    * その他, seaborn などバックエンドが matplotlib に依存しているグラフィクスパッケージも対応している可能性があります
* 指定される日本語フォントは, OS ごとにプリインストールされている可能性が高く, なおかつ広く使われているものです
* (試験中) 用途ごとに選択できます
  + ラスタ画像 or PDF + フォント埋め込み (非Type3)
  + PDF + フォントサブセット化 + LaTeX 数式有効 (要 TeX)
  + SVG + フォント埋め込み
* どれも不要, 日本語表示できれば**文字通り**なんでもいいと言う人は japanize-matplotlib でも良いでしょう

## 要件

* `matplotlib` >= 3.3.1
* (オプション: Cairoモード使用時) `pycairo` >= 1.19.1 or `cairoffi` >= 1.1.0
* (オプション: PGFモード使用時) 最新の TeX
* (オプション) Noto フォント. Debian や Cent OS など Noto がプリインされていない環境の場合: Noto Sans CJK JP のインストール


## インストール方法

各種の標準的な方法でインストールできます.


### 下準備

もしもNotoをインストールしていない場合,

```
sudo dnf install 
```

さらに, `pycairo`, `cairoffi` も必要に応じてインストールしてください.



### uv add を使用する場合

```sh
uv add "matplotlib-japreset @ git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master"
```


### pip を使用する場合

```sh
pip install -U git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master
```

必要に応じて依存パッケージも追加してください.


```sh
pip install pycairo cairoffi
```

使用時に以下のようなエラーが発生する場合は, 描画に必要なパッケージが不足しています.

```
Package cairo was not found in the pkg-config search path.
```


### 補足

使用時に以下のようなエラーが発生する場合は, 描画に必要なパッケージが不足しています.

```
Package cairo was not found in the pkg-config search path.
```


必要に応じて `pycairo`, `cairffi` を追加してください.

外部ライブラリがインストールされていない場合もあります.

Ubuntu や Linux 系ならば, 以下を試してください.

```sh
sudo apt install libcairo2-dev libjpeg-dev libgif-dev
```

Mac ならば, 以下を試してください.

```sh
brew install cairo
brew install pkg-config
```


## 使い方

### 毎回設定する方法

以下のいずれかをグラフを描く前に実行すれば, スクリプトの実行中やセッション中は, 設定が維持されます. ただし, 現時点では cairo, pgf の動作が不安定です. 特にこだわりがないなら, `preset_pdf` を使ってください. 

1. 最初にどれかを選んでインポートします
  + PDFモード: ラスタ画像 or フォント埋め込みPDF (**サブセット化なし**)
    ```python
    from matplotlib_japreset.loader import preset_pdf  # noqa: F401 pylint: disable=W0611
    ```
  + Cairoモード: ラスタ画像 or フォント埋め込みPDF (サブセット化)
    ```python
    from matplotlib_japreset.loader import preset_cairo
    ```
  + フォント埋め込み (サブセット化) + LaTeX 数式有効
    ```python
    from matplotlib_japreset.loader import preset_pgf
    ```
2. 自動選択されたフォントが表示されます
3. `matplotlib` 依存のグラフを作成します (cf. `plotnine`, `seaborn` でも有効)
4. 変更したい場合は別のものを読み込み直します
    + 設定がデフォルトに一番近いのは PDF モードです. フォント名と埋め込み設定以外変えていません


動作確認のためのコピペ用コードです.

```python
import matplotlib.pyplot as plt

from matplotlib_japreset import mplj_pdf

plt.plot()
plt.title("ほげほげ")
plt.savefig("test.png")
```

#### unused import を回避する構文

モジュールを import するだけで使わない構文は, 多くのlinterで警告の対象となります. import の行に問題を無視するフラグを付与する方法もありますが, コードの可読性も保守性も損ねます. そこで, 明示的に関数を呼び出す構文も用意しました. 効果は全く同じです.

```python
from matplotlib_japreset.setter import set_graphics_as_pdf


set_graphics_as_pdf()
```


### 永続的に変更する方法

理論上は, matplotlibrc さえ変えてしまえば毎回日本語フォントを設定する必要はありません. しかし, なぜか matplotlib は matplotlibrc をエクスポートする手段をサポートしていません. 自分で作ろうとしましたが複雑すぎて継続的にメンテできる自信がないので諦めました.


## カスタマイズ

フォントを手動変更したい場合は, プリセット読み込み後に `rcParams` を上書きします

```python
from matplotlib_japreset import mplj_pdf  # noqa: F401 pylint: disable=W0611
from matplotlib import rcParams
rcParams['font.family'] = 'FONT NAME'
```

または, 

使用可能なフォント名一覧が欲しい場合は, 以下を実行してください.

```python
from matplotlib_japreset.utils import show_font_names

show_font_names()
```

または UNIX系 (Linux/Mac) ならば, 端末上で `fc-list` を実行して表示される postscript name も有効なはずです.

## 注意事項

* Windows OSで新たにフォントをインストールして使用したい場合は, 全ユーザーが使えるようにインストールする必要があるかもしれません.
* PDF は一番環境制約が少ないですが, 埋め込みフォントをサブセット化できません
    + `ghostscript` を使ったり `.tex` ファイルに埋め込んでまとめてサブセット化してしまうと言う手もあります
    + しかしそんな手順を踏むならそもそも本モジュールは効率化に寄与できません
* 実用的な PDF が欲しい場合は (名前に反して) PDF モードより Cairo モードのほうが簡単です. しかしやや字が太くなります
* PGFモードはLaTeX が必要です. **数式以外も TeX として評価**されます. つまり, タイトルや軸ラベルの `_` や `$` をエスケープする必要があります
* PGFモードでは Jupyter 上で表示するにはマジックコマンド `%maplotlib inline` が必要です
* ~~`plotnine` で `theme_*()` を使う場合, デフォルト値にオーバーライドされてしまうため `base_family=None` の指定が必要です (PR済み)~~
    * PRが却下されてしまったので無理やり上書きする実装になりました
    + `theme_xkcd()` は日本語不可 (たぶん)

## その他

* 追加してほしいフォント名あったら教えてください
  + 隷書とかポップ体とか変わったフォントはめんどくさいので対応しません
* Q. なんでこんなに複雑なの? もっと簡単にサブセット化とかできないの?
  + A. これ以上は matplotlib 側の実装を根本から直さないと無理だと思います
* Q. bokeh や plotly でよくない?
  + A. そうかもね…
