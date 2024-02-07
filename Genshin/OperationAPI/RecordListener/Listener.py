from RecordListener.CoreDep import *
class Listener:
    def __init__(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click,on_move=self.on_move)
        self.keybd_listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.logmanager = LogManager()
        self.log = self.logmanager.GetLogger("Listener")
        self.is_running = True
        self.prev_x = 0
        self.prev_y = 0
        self.exit_key = keyboard.Key.esc
        self.event_cache = {'event':[]}
        self.filename = input("请设定监听结束后需要写入的操作文件:")
        self.append = self.event_cache['event'].append
        #为了避免程序持续不断的往event_cache添加数据而导致内存泄露,需要做一些限制
        self.max_event_cache = 10000

    def _check_memory(self):
        size = len(self.event_cache['event'])
        if size > self.max_event_cache:
           self._write_to_file(self.filename)
           self.event_cache['event'] = []
           self.log.warning("内存占用到设定极限,已经清理")

    def start(self):
        self.log.info("5秒后开始录制")
        time.sleep(5)
        self.log.info("开始监听键盘鼠标操作")
        self.mouse_listener.start()
        self.keybd_listener.start()
        self.mouse_listener.join()
        self.keybd_listener.join()

    def on_move(self,x,y):
       #这里记录出相对移动量
       dx = x - self.prev_x
       dy = y - self.prev_y
       dict_message = {'type':'mouse','event':'move','dx':dx,'dy':dy,'time':time.time()}
       self.append(dict_message)
       self.prev_x = x
       self.prev_y = y
       self._check_memory()

    def on_press(self,key):
     try:
        message = f"按键被按下：{key}"
        dict_message = {'type':'keyboard','event':'press','key':str(key),'time':time.time()}
        self.append(dict_message)
        self.log.debug(message)
        self._check_memory()
        if key == self.exit_key:
           self.is_running = False
           self.stop()
           self.log.info("监听结束")
     except AttributeError:
        message = f"特殊按键已被按下 {key}"
        if key == self.exit_key:
            self.is_running = False
            self.stop()
            self.log.info("监听结束")
        dict_message = {'type':'keyboard','event':'press','key':str(key),'time':time.time()}
        self.append(dict_message)
        self.log.debug(message)

    def on_release(self,key):
     try:
        message = f"按键被释放：{key}"
        dict_message = {'type':'keyboard','event':'release','key':str(key),'time':time.time()}
        self.append(dict_message)
        self.log.debug(message)
     except AttributeError:
        message = f"特殊按键已被释放 {key}"
        dict_message = {'type':'keyboard','event':'release','key':str(key),'time':time.time()}
        self.append(dict_message)
        self.log.debug(message)

    def on_click(self,x,y,button,pressed):
        message = f"鼠标被点击：{button}"
        dict_message = {'type':'mouse','event':'click','button':str(button),'x':x,'y':y,'pressed':pressed,'time':time.time()}
        self.append(dict_message)
        self.log.debug(message)
        self._check_memory()

    def _write_to_file(self,filename:str):
     try:
        if filename == None or filename == "":
           filename = "event.json"
        with open(filename,'w',encoding='utf-8') as f:
            if self.event_cache == None or self.event_cache == "":
                return
            json.dump(self.event_cache,f,ensure_ascii=False,indent=4)
            self.log.info(f"文件已被写入到:{filename}中")
     except Exception as e:
         self.log.warning(f"写入文件失败：{e}")

    def stop(self):
        self.mouse_listener.stop()
        self.keybd_listener.stop()
        self.log.info("停止监听键盘鼠标操作")
        self._write_to_file(self.filename)
        self.log.info("操作记录完成")

    def validation(self):
       vail.validate()
    
    def Replay(self,filepath:str=None):
        time.sleep(5)
        self.validation()
        self.log.info("开始回放操作记录")
        with open(filepath,'r',encoding='utf-8') as f:
           events = json.loads(f.read())


        start_time = events['event'][0]['time']
        for event in track(events['event'],description="播放进度..."):
            try:
              event_time = event['time']
              time.sleep(event_time - start_time)
              start_time = event_time

              if event['type'] == 'keyboard':
                 if event['event'] == 'press':
                    rep_key = translate.TranslateKey(event['key'])
                    operation.press_key(rep_key)
                 elif event['event'] == 'release':
                    rep_key = translate.TranslateKey(event['key'])
                    operation.release_key(rep_key)
                 else:
                    self.log.warning(f"未知键盘事件：{event['event']}")
              elif event['type'] == 'mouse':
                 if event['event'] == 'move':
                    dx , dy = event['dx'],event['dy']
                    operation.move_mouse(dx * 3,dy * -1)
                 elif event['event'] == 'click':
                    x,y = event['x'],event['y']
                    operation.mouse(Mouse.Left_down,x,y)
                    operation.mouse(Mouse.Left_up,x,y)
                 else:
                    self.log.warning(f"未知鼠标事件：{event['event']}")
              else:
                 self.log.warning(f"未知事件：{event['type']}")
            except Exception as e:
               self.log.warning(f"错误信息: {e}")
               pass
        self.log.info("回放完成")
        
class GUIApp:
    def __init__(self, listener):
        self.listener = listener
        self.root = tk.Tk()
        self.root.title("操作记录与回放")

        # 开始录制按钮
        self.start_btn = tk.Button(self.root, text="开始录制", command=self.start_recording)
        self.start_btn.pack(pady=5)

        # 停止录制按钮
        self.stop_btn = tk.Button(self.root, text="停止并保存录制", command=self.stop_recording, state=tk.DISABLED)
        self.stop_btn.pack(pady=5)

        # 回放录制按钮
        self.replay_btn = tk.Button(self.root, text="回放录制", command=self.replay_recording)
        self.replay_btn.pack(pady=5)

    def start_recording(self):
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.replay_btn.config(state=tk.DISABLED)
        # 在新线程中启动监听，避免阻塞GUI
        Thread(target=self.listener.start, daemon=True).start()

    def stop_recording(self):
        self.listener.is_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.replay_btn.config(state=tk.NORMAL)

    def replay_recording(self):
        filepath = filedialog.askopenfilename(title="选择操作记录文件", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        if filepath:
            try:
                self.listener.Replay(filepath=filepath)
            except Exception as e:
                messagebox.showerror("错误", f"回放失败：{e}")

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
   listener = Listener()
   listener.Replay("operation.json")