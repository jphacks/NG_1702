Pythonサーバー用プログラム  
ユーザデータに基づいたおすすめの計算を行う  

# 使用方法
以下のようにcgiサーバを立ち上げ，レコメンドプログラムを立ち上げる．  
@./server_1$ python -m CGIHTTPServer 8000  
@./$ python socket_server.py  

# プログラムの内容
### collaborative_filtering_simple.py
ユーザの履歴に基づいたおすすめを計算
### collaborative_filtering_wvec.py
単語ベクトルを用いてサイトに含まれる単語からそのサイトの特徴を計算．  
深層学習はここで使用する．  
新しくアクセスされたurlに対しても特徴を計算できるため，過去のurlとの類似度を計算可能．  
他のユーザが訪れていなくてもおすすめ度を計算できる．  
### socket_server.py
サーバとやり取りするプログラムとやり取りを行う．
レコメンデーションプログラムもこのプログラムが呼び出す．
### server_1/cgi-bin/sample_1.py
サーバとやり取りを行う  
