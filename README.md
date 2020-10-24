# msm5232kamata

USAGE: python msm5232kamata.py

OKI MSM5232 サウンドチップの出力波形に似せようとした WaveTable を作成して、Korg Gadget 2 kamata VSTi　用の .kamata_programs 形式のファイルを出力するスクリプトです。  
このスクリプトを実行すると、１個の kamta用の ユーザー定義ファイル（MSM5232likeWaveTable.kamata_programs）が作られます。  
これを kamata にロードすると、MSM5232Tbl-1～Fまでの15種類の波形が読み込まれます。  

このスクリプトは、私自身の python と github の勉強用に作ったものです。特に、実物の MSM5232 と音が違うという点については、あくまで、「MSM5232風」ということでご了解願います。  

Windows PC 上で python 3.8.3 を使用しました。  
まともに動かなかったりファイルが壊れたりしても当方は一切責任を負いません。リスクを承知の上で使ってください。  

波形の作成にあたって、以下のページを参照しました。  
http://sr4.sakura.ne.jp/acsound/taito/taito5232.html  

This script creates 15 wavetables that I tried to imitate OKI MSM5232 sound chip tones and makes a .kamata_programs file for the Korg Gadget 2 kamata VSTi.  
Executing this script creates a single user-defined file for the kamata (The file name is "MSM5232likeWaveTable.kamata_programs").  
When you load this file into the kamata, 15 different wavetables named MSM5232Tbl-1 to F will appear in the instrument.  

I made this script for my python and github studies sake.
I used python 3.8.3 on a Windows PC.  

The following page was consulted in creating the wavetables:
http://sr4.sakura.ne.jp/acsound/taito/taito5232.html  

# Some graphs of wavetables made by this script.

![Figure1](https://user-images.githubusercontent.com/68761912/95644717-75865280-0af3-11eb-9904-3d5cafd55079.png)
![FigureD](https://user-images.githubusercontent.com/68761912/95644721-7c14ca00-0af3-11eb-9322-6987c727499b.png)
![FigureE](https://user-images.githubusercontent.com/68761912/95644728-820aab00-0af3-11eb-9052-a45dc3799389.png)
![FigureF](https://user-images.githubusercontent.com/68761912/95644732-859e3200-0af3-11eb-86ed-d67b512253fd.png)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.   
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
