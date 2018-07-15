class Codec:
    import string
    import random

    def __init__(self):
        self.hashmap = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        set = string.ascii_letters + string.digits
        short = "https://tinyurl.com/".join(random.choice(set) for _ in range(6))
        self.hashmap[short] = longUrl
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.hashmap.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
