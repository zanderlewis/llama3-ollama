import ollama

model = 'llama3'

class cli:
    def __init__(self):
        self.model = model
        self.history = []

    def run(self):
        while True:
            message = {'role': 'user', 'content': input('>>> ')}
            if message['content'].lower() == 'exit':
                break
            else:
                print(self.chat(message))
    
    def chat(self, message):
        self.history.append(message)
        response = ollama.chat(model=self.model, messages=self.history)
        self.history.append(response['message'])
        return response['message']['content']


if __name__ == '__main__':
    cli().run()