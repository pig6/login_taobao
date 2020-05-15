from TSDK.mTop import Client

top = Client()
#获取淘宝二维码，可以通过扫码登录淘宝
umid_token = top.getUmidToken()
res = top.login(umid_token)
print(res.text)
data = json.loads(res.text)
thr = top.checkState(data['lgToken'],umid_token,30)
thr.start()


#设置开放平台的appkey和密钥，然后传递API和配置可以直接获取数据
top.open.config['appkey'] = ''
top.open.config['appsecret'] = ''

res = top.open.execute('taobao.tbk.item.get',{
      'fields':'num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick',
      'q':'女装',
      'cat':'16,18'
  })
print(res.text)

#获取宝贝详情
res = top.H5.execute({
      'api':'mtop.taobao.detail.getdetail',
      'v':'6.0',
      'jsv':'2.4.8',
      'dataType':'json',
      'type':'json',
      'ttid':'2017%40taobao_h5_6.6.0',
      'AntiCreep':'true',
      'data':{
          'itemNumId':'585559878166'
      }
  })
print(res.text)

#API请求日志的记录,SDK对象继承自requests的Session类，可以通过添加hook来获取响应
#请参考requests高级用法：http://docs.python-requests.org/zh_CN/latest/user/advanced.html
def console(res):
  print(res.url)
  print(res.text)

top.H5.hooks['response'] = [console]
