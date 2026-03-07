# plot-localizer

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

(普通はありえないと思いますが) マシンに日本語フォントが一切インストールされていない場合は, マシンに日本語フォントをインストールすることをお勧めします.

例えば Ubuntu OS なら, 以下で Noto をインストールできます (最近の Ubuntu は Noto が標準フォントなので, あまりありえない状況だと思います).

```sh
sudo apt install fonts-noto
```

後述する対応しているフォントであれば, 他のフォントをインストールしても問題ありません.


### uv を使用してインストールする例

```sh
uv add "plot-localizer @ git+https://github.com/Gedevan-Aleksizde/pyplot-localizer"
```

### poetry を使用してインストールする例

```sh
poetry add git+https://git@github.com/Gedevan-Aleksizde/pyplot-localizer.git
```


### pip を使用してインストールする例

```sh
pip install -U git+https://github.com/Gedevan-Aleksizde/pyplot-localizer
```

使用時に以下のようなエラーが発生する場合は, 描画に必要なパッケージが不足しています.

```
Package cairo was not found in the pkg-config search path.
```

必要に応じて `pycairo`, `cairoffi`  もインストールしてください.


## 使い方

### 対応パッケージを読み込む場合

現時点では matplptlib, seaborn, plotnine に対応しています.

これらのパッケージを import する際に, モジュールの先頭に `plot_localizer.` を付けます. 例えば以下のようにしてください.

```python
import plot_localizer.matplotlib.pyplot as plt

import plot_localizer.seaborn as sns

import plot_localizer.plotnine as p9
```

後は通常のインポートと同様に, `plt.plot()` とか `sns.catplot` とかを呼び出せます.

当然ながら, seaborn, plotnine はそれぞれパッケージ本体をインストールする必要があります.


### フォント設定の変更だけをする場合

matplotlib および, matplotlib をバックエンドとしているグラフィックスパッケージを日本語表示させたい場合は, この方法が有効かもしれません. または, 上記の方法を使わずに日本語フォントを設定したい場合にも使えます.

#### 一番簡単だが行儀の良くない方法

以下のいずれかをグラフを描く前に実行すれば, スクリプトの実行中やセッション中は, 設定が維持されます. ただし, 現時点では cairo, pgf の動作が不安定です. 特にこだわりがないなら, `preset_pdf` を使ってください. 

1. 最初にどれかを選んでインポートします
  + PDFモード: ラスタ画像 or フォント埋め込みPDF (**サブセット化なし**)
    ```python
    from plot_localizer.loader import preset_pdf
    ```
  + Cairoモード: ラスタ画像 or フォント埋め込みPDF (サブセット化)
    ```python
    from plot_localizer.loader import preset_cairo
    ```
  + フォント埋め込み (サブセット化) + LaTeX 数式有効
    ```python
    from plot_localizer.loader import preset_pgf
    ```
2. 自動選択されたフォントが表示されます
3. `matplotlib` 依存のグラフを作成します
    * 例えば seaborn も対象です
4. 変更したい場合は別のものを読み込み直します
    + 設定がデフォルトに一番近いのは PDF モードです. フォント名と埋め込み設定以外変えていません


動作確認のためのコピペ用コードです.

```python
import matplotlib.pyplot as plt

from plot_localizer import preset_pdf

plt.plot()
plt.title("ほげほげ")
plt.savefig("test.png")
```

#### unused import を回避する構文

モジュールを import するだけで使わない構文は, 多くのlinterで警告の対象となります. import の行に問題を無視するフラグを付与する方法もありますが, コードの可読性も保守性も損ねます. そこで, 明示的に関数を呼び出す構文も用意しました. 効果は全く同じです.

```python
from plot_localizer.setter import set_graphics_as_pdf


set_graphics_as_pdf()
```

## トラブルシュート

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


## このパッケージに関する技術的な説明

### 対応しているフォント

主要なOSおよびLinuxディストリビューションで標準フォントとして採用されているものや, 広く普及している無料フォントを中心に採用しています. 以下のようなフォントがインストールされていれば, このパッケージによってグラフに使用されます. 逆に言えば, これら以外のフォントは日本語用であってもそのままでは認識されません. グラフで使う意味が思いつかないため, Windows に入っているUI系フォントや非プロポーショナルフォントやその他ののカーニングのおかしいフォントは認識しないことが多いです. 非プロポーショナルフォントでは, プログラミング用途に使われるような, 意味のある等幅フォントのみ対応しています.

* sans-serif と serif フォント
    * Noto CJK JP
    * ヒラギノ系
    * BIZ UD系
    * メイリオ
    * 游書体
    * Takao
    * VL
    * 梅書体
    * IPA系
    * MS系
        * MS*フォントのうち名前にUIとついているものは対象としていません.
* 等幅フォント
    * Ricty系
    * M+
    * Mgen+ m


**ただし, OpenType や `.ttc` 形式のフォントは指定しても動作しないことがあります.**

### 永続的にフォントを変更する方法

理論上は, matplotlibrc さえ変えてしまえば, plotnine を除いて, 毎回このパッケージで日本語フォントを設定する必要はありません. しかし, なぜか matplotlib は matplotlibrc をエクスポートする手段をサポートしていません. 自分で作ろうとしましたが複雑すぎて継続的にメンテできる自信がないので, 自動で matplotlibrc を上書きする機能は諦めました.

### Seaborn の場合

Seaborn は matplotlib をバックエンドにしているので, `rcParams` の設定が反映されます. よって, matplotlib と同じ設定をしておけば日本語表示ができます. ただし, Seaborn を使うこと自体を私はおすすめしません.


### Plotnine の場合

Plotnine は matplotlib をバックエンドにしていますが, デフォルトで `rcParams` の設定を上書きしてしまうため, `rcParams` の設定を変更しても日本語フォントを使用してくれません. 昔 pull request を出しましたが, 却下されました. そのため, Plotnine に対応する方法は依然としてやや複雑です. いくつかのクラスを再定義する必要がありました. `ggplot` と, `theme_*` 系のフォントを設定するオブジェクトは, Plotnine ではなくこのパッケージからインポートして使ってください. フォントは matplotlib の場合と同じ方法で決定されます.

```python
import plotnine as p9
import plot_localizer.plotnine as p9jp 

p9jp.ggplot(data, p9.aes(...)) + p9.geom_point()


p9jp.ggplot(data, p9.aes(...)) + p9.geom_line() + p9jp.theme_classic(base_size=18)
```


### カスタマイズ

フォントを手動変更したい場合は, プリセット読み込み後に `rcParams` を上書きします

```python
from plot_localizer import mplj_pdf
from matplotlib import rcParams
rcParams['font.family'] = 'FONT NAME'
```

使用可能なフォント名一覧が欲しい場合は, 以下を実行してください.

```python
from plot_localizer.utils import show_font_names

show_font_names()
```

UNIX系 (Linux/Mac) ならば, 端末上で `fc-list` を実行して表示される postscript name も有効なはずです.

デフォルトでは `show_font_names` は sans-serif, つまりゴシック体に相当するフォントを設定しますが, matplotlib 本体同様に明朝体に対応する `serif` や等幅フォントに対応する `monospace` も選べます.

```python
from plot_localizer.setter import set_graphics_as_pdf

set_graphics_as_pdf("serif")
```

他の方法では, スタイルを指定する引数が存在しません. 上記の関数では Plotnine にも効果がありません. これらの状況でスタイルを変更するには, Python 呼び出し時に `PYTHONFONTSTYLE` 環境変数に与えておけば, 読込時に対応するスタイルのフォントを選びます.


## その他の細かい注意事項

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


## 最後に

* 追加してほしいフォント名あったら教えてください
  + 隷書とかポップ体とか変わったフォントはめんどくさいので対応しません
* Q. なんでこんなに複雑なの? もっと簡単にサブセット化とかできないの?
  + A. これ以上は matplotlib 側の実装を根本から直さないと無理だと思います
* Q. bokeh や plotly でよくない?
  + A. そうかもね…
