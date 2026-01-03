import hashlib

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()
class Block:
    def __init__(self,data,hash,prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class Blockchain:
    def __init__(self):
        hashLast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash')

        genesis = Block('genesis',hashLast,hashStart)
        self.chain = [genesis]

    def addBlock(self,data):
        prev_hash = self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)
bc=Blockchain()
bc.addBlock('1')
bc.addBlock('2')
bc.addBlock('3')

bc.addBlock('4')

for block in bc.chain:
    print(block.__dict__)