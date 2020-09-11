import pickle


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        # 收到建立websocket连接消息
        if event['type'] == 'websocket.connect':
            # pickle.dump(scope, open('scope.pkl', 'wb'))
            # data = pickle.load(open('file_path', 'rb'))
            print(scope)
            # scope['path'] = '/'
            # scope['raw_path'] = '/'
            # scope['query_string'] = b''
            # scope['client'] = ('127.0.0.1', 61849)

            # print(scope)
            # print(receive)
            # print(send)
            await send({
                'type': 'websocket.accept'
            })
        # 收到中断websocket连接消息
        if event['type'] == 'websocket.disconnect':
            break
        # 其他情况，正常的webSocket的消息
        if event['type'] == 'websocket.receive':
            print(event['text'] )
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })