# matplotlib-japreset

`matplotlib` その他の Python グラフィクスパッケージで日本語を自由に表示し保存するための自動設定モジュール

## 機能

* Python グラフィックパッケージで使用するデフォルトのフォントを自動で日本語フォントに変更します. 現在対応しているパッケージは以下です
    * matpliolib
    * plotnine
    * その他, seaborn などバックエンドが matplotlib に依存しているグラフィクスパッケージも対応している可能性があります
* 指定される日本語フォントは, OS ごとにプリインストールされている可能性が高く, なおかつ広く使われているものです
* 以下は試験中です. 環境によっては動作しません 
  + ラスタ画像 or PDF + フォント埋め込み (非Type3)
  + PDF + フォントサブセット化 + LaTeX 数式有効 (要 TeX)
  + SVG + フォント埋め込み


## 要件

* `matplotlib` >= 3.3.1
* (オプション: Cairoモード使用時) `pycairo` >= 1.19.1 or `cairoffi` >= 1.1.0
* (オプション: PGFモード使用時) 最新の TeX
* (オプション) Noto フォント. Debian や Cent OS など Noto がプリインされていない環境の場合: Noto Sans CJK JP のインストール


## インストール方法

各種の標準的な方法でインストールできます.


### 下準備

もしもマシンに日本語フォントが一切インストールされていない場合は, このパッケージでもどうにもできません.

例えば Ubuntu OS なら, 以下で Noto をインストールできます (最近の Ubuntu は Noto が標準フォントなので, あまりありえない状況だと思います).

```sh
sudo apt install fonts-noto
```

後述する対応しているフォントであれば, 他のフォントをインストールしても問題ありません.


### uv を使用する場合 (推奨)

```sh
uv add "matplotlib-japreset @ git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master"
```


### pip を使用する場合 (非推奨)

```sh
pip install -U git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master
```

使用時に以下のようなエラーが発生する場合は, 描画に必要なパッケージが不足しています.

```
Package cairo was not found in the pkg-config search path.
```

必要に応じて `pycairo`, `cairoffi`  もインストールしてください.


## 使い方


### 一番簡単だが行儀の良くない方法

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

from matplotlib_japreset import preset_pdf

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

理論上は, matplotlibrc さえ変えてしまえば, plotnine を除いて, 毎回このパッケージで日本語フォントを設定する必要はありません. しかし, なぜか matplotlib は matplotlibrc をエクスポートする手段をサポートしていません. 自分で作ろうとしましたが複雑すぎて継続的にメンテできる自信がないので, 自動で matplotlibrc を上書きする機能は諦めました.


## Seaborn の場合

Seaborn は matplotlib をバックエンドにしているので, `rcParams` の設定が反映されます. よって, matplotlib と同じ設定をしておけば日本語表示ができます. ただし, Seaborn を使うこと自体を私はおすすめしません.


## Plotnine の場合

Plotnine は matplotlib をバックエンドにしていますが, デフォルトで `rcParams` の設定を上書きしてしまうため, `rcParams` の設定を変更しても日本語フォントを使用してくれません. 昔 pull request を出しましたが, 却下されました. そのため, Plotnine に対応する方法は依然としてやや複雑です. いくつかのクラスを再定義する必要がありました. `ggplot` と, `theme_*` 系のフォントを設定するオブジェクトは, Plotnine ではなくこのパッケージからインポートして使ってください. フォントは matplotlib の場合と同じ方法で決定されます.

```python
import plotnine as p9
import matplotlib_japreset.plotnine as p9jp 

p9jp.ggplot(data, p9.aes(...)) + p9.geom_point()


p9jp.ggplot(data, p9.aes(...)) + p9.geom_line() + p9jp.theme_classic(base_size=18)
```


## カスタマイズ

フォントを手動変更したい場合は, プリセット読み込み後に `rcParams` を上書きします

```python
from matplotlib_japreset import mplj_pdf  # noqa: F401 pylint: disable=W0611
from matplotlib import rcParams
rcParams['font.family'] = 'FONT NAME'
```

使用可能なフォント名一覧が欲しい場合は, 以下を実行してください.

```python
from matplotlib_japreset.utils import show_font_names

show_font_names()
```

UNIX系 (Linux/Mac) ならば, 端末上で `fc-list` を実行して表示される postscript name も有効なはずです.

デフォルトでは `show_font_names` は sans-serif, つまりゴシック体に相当するフォントを設定しますが, matplotlib 本体同様に明朝体に対応する `serif` や等幅フォントに対応する `monospace` も選べます.

```python
from matplotlib_japreset.setter import set_graphics_as_pdf

set_graphics_as_pdf("serif")
```

他の方法では, スタイルを指定する引数が存在しません. 上記の関数では Plotnine にも効果がありません. これらの状況でスタイルを変更するには, Python 呼び出し時に `PYTHONFONTSTYLE` 環境変数に与えておけば, 読込時に対応するスタイルのフォントを選びます.


## 補足

### トラブルシュート

使用時に以下のようなエラーが発生する場合は, 描画に必要なパッケージが不足しています.

```
Package cairo was not found in the pkg-config search path.
```

外部ライブラリがインストールされていない場合もあります.

Ubuntu や Linux 系ならば, 以下を試してください.

```sh
sudo apt install libcairo2-dev libjpeg-dev libgif-dev
```

Mac ならば, 以下を試してください. インストールには Homebrew も必要です.

```sh
brew install cairo
brew install pkg-config
```

### 対応しているフォント

以下のようなフォントがインストールされていれば, このパッケージによってグラフに使用されます. 逆に言えば, これら以外のフォントは日本語用であっても認識されません. グラフで使う意味が思いつかないため, Windows に入っているUI系フォントや非プロポーショナルフォントや等幅フォントなどのカーニングのおかしいフォントは認識しないことが多いです.

* sans-serif と serif 系
    * Noto Sans CJK JP
    * Noto Serif CJK JP
    * ヒラギノ系
    * BIZ UD系
    * メイリオ
    * 游書体
    * Takao系
    * VL系
    * 梅書体
    * IPA系
    * MS系
* 等幅フォント系
    * Ricty系
    * M+, Mgen+


**ただし, OpenType や `.ttc` 形式のフォントは指定しても動作しないことがあります.**

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
    + Plotnine の `theme_xkcd()` はたぶん日本語不可です


## その他

* 追加してほしいフォント名あったら教えてください
  + 隷書とかポップ体とか変わったフォントはめんどくさいので対応しません
* Q. なんでこんなに複雑なの? もっと簡単にサブセット化とかできないの?
  + A. これ以上は matplotlib 側の実装を根本から直さないと無理だと思います
* Q. bokeh や plotly でよくない?
  + A. そうかもね…
