{"filter":false,"title":"models.py","tooltip":"/blog/models.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":3,"column":0},"end":{"row":16,"column":25},"action":"insert","lines":["class Post(models.Model):","    \"\"\"","    A single Blog post","    \"\"\"","    title = models.CharField(max_length=200)","    content = models.TextField()","    created_date = models.DateTimeField(auto_now_add=True)","    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)","    views = models.IntegerField(default=0)","    tag = models.CharField(max_length=30, blank=True, null=True)","    image = models.ImageField(upload_to=\"img\", blank=True, null=True)","","    def __unicode__(self):","        return self.title"],"id":2}],[{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":4},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["j"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["n"],"id":5},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["g"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["o"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["."]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["u"],"id":6},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["t"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["i"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["l"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":7},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["i"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["m"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["p"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["o"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["r"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":8},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["t"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["i"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["m"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["z"],"id":9},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["o"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["n"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":63},"end":{"row":13,"column":64},"action":"remove","lines":[")"],"id":10},{"start":{"row":13,"column":62},"end":{"row":13,"column":63},"action":"remove","lines":["e"]},{"start":{"row":13,"column":61},"end":{"row":13,"column":62},"action":"remove","lines":["u"]},{"start":{"row":13,"column":60},"end":{"row":13,"column":61},"action":"remove","lines":["r"]},{"start":{"row":13,"column":59},"end":{"row":13,"column":60},"action":"remove","lines":["T"]},{"start":{"row":13,"column":58},"end":{"row":13,"column":59},"action":"remove","lines":["="]},{"start":{"row":13,"column":57},"end":{"row":13,"column":58},"action":"remove","lines":["l"]},{"start":{"row":13,"column":56},"end":{"row":13,"column":57},"action":"remove","lines":["l"]},{"start":{"row":13,"column":55},"end":{"row":13,"column":56},"action":"remove","lines":["u"]},{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"remove","lines":["n"]},{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"remove","lines":[" "]},{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"remove","lines":[","]},{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"remove","lines":["e"]},{"start":{"row":13,"column":50},"end":{"row":13,"column":51},"action":"remove","lines":["u"]},{"start":{"row":13,"column":49},"end":{"row":13,"column":50},"action":"remove","lines":["r"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"remove","lines":["T"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"remove","lines":["="]},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"remove","lines":["k"]},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"remove","lines":["n"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":["a"]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"remove","lines":["l"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":["b"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":[" "]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":[","]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["0"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":["3"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":["="]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["h"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"remove","lines":["t"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"remove","lines":["g"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"remove","lines":["n"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"remove","lines":["e"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":["l"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"remove","lines":["_"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["x"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["a"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["m"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["("]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["d"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["l"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["e"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["i"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["F"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["r"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["a"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["h"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["C"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":["."]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"remove","lines":["s"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"remove","lines":["l"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["d"],"id":11},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["o"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["m"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":[" "]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["="]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":[" "]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["g"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["a"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":68},"end":{"row":14,"column":69},"action":"remove","lines":[")"],"id":12},{"start":{"row":14,"column":67},"end":{"row":14,"column":68},"action":"remove","lines":["e"]},{"start":{"row":14,"column":66},"end":{"row":14,"column":67},"action":"remove","lines":["u"]},{"start":{"row":14,"column":65},"end":{"row":14,"column":66},"action":"remove","lines":["r"]},{"start":{"row":14,"column":64},"end":{"row":14,"column":65},"action":"remove","lines":["T"]},{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"remove","lines":["="]},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"remove","lines":["l"]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"remove","lines":["l"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["u"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["n"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":[" "]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"remove","lines":[","]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"remove","lines":["e"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"remove","lines":["u"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"remove","lines":["r"]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"remove","lines":["T"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"remove","lines":["="]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["k"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["n"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["a"]},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"remove","lines":["l"]},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"remove","lines":["b"]},{"start":{"row":14,"column":46},"end":{"row":14,"column":47},"action":"remove","lines":[" "]},{"start":{"row":14,"column":45},"end":{"row":14,"column":46},"action":"remove","lines":[","]},{"start":{"row":14,"column":44},"end":{"row":14,"column":45},"action":"remove","lines":["\""]},{"start":{"row":14,"column":43},"end":{"row":14,"column":44},"action":"remove","lines":["g"]},{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"remove","lines":["m"]},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":["i"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"remove","lines":["\""]},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"remove","lines":["="]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"remove","lines":["o"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"remove","lines":["t"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"remove","lines":["_"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["d"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["a"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["o"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["l"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["p"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["u"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["("]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["d"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["l"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["e"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["i"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["F"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["e"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["g"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["a"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["m"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["I"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["."]}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["s"],"id":13},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["l"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["e"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["d"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["o"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["m"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":[" "]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["="]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":[" "]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["e"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["g"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["a"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["m"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["i"]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":14},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":42},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":26},"end":{"row":14,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1573898222550,"hash":"bb2ade0b5906d4c34ad5489e26929421fa78ce5e"}