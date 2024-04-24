"""Function that tests the sort."""

import os
import pytest
from litpack import utils

bs = '''{'first':3, 'last':1}'''

@pytest.fixture()
def setup():
    """Make then delete the bib file."""
    with open("test.bib", "w") as f:
        f.write(bs)
    yield "setup"
    os.unlink("test.bib")


class TestSort:
  """A Test class."""
  def test_sort(self, setup):
    bs = {'first':3, 'last':1}
    """Test function for sorting."""
    sort = utils.sort(bs)
    assert sort == {'last':1, 'first':3}

  def test_get_abstract(self, setup):
    output ={
"The": [
0,
53,
71,
92
],
"problem": [
1,
93
],
"of": [
2,
20,
29,
35,
55,
89,
105,
109,
150,
169
],
"deploying": [
3
],
"sensors": [
4
],
"in": [
5,
13,
60,
74,
96,
100,
117,
154
],
"a": [
6,
26
],
"large": [
7,
27
],
"water": [
8,
166
],
"distribution": [
9,
160,
167
],
"network": [
10
],
"is": [
11,
23,
58,
121,
174
],
"considered,": [
12
],
"order": [
14,
61
],
"to": [
15,
62,
87,
131,
137
],
"detect": [
16
],
"the": [
17,
39,
97,
113,
118,
124,
148,
151
],
"malicious": [
18
],
"introduction": [
19
],
"contaminants.": [
21
],
"It": [
22,
120
],
"shown": [
24,
122
],
"that": [
25
],
"class": [
28
],
"realistic": [
30
],
"objective": [
31
],
"functions—such": [
32
],
"as": [
33
],
"reduction": [
34
],
"detection": [
36
],
"time": [
37
],
"and": [
38,
84,
140,
162
],
"population": [
40
],
"protected": [
41
],
"from": [
42
],
"consuming": [
43
],
"contaminated": [
44
],
"water—exhibits": [
45
],
"an": [
46,
163
],
"important": [
47
],
"diminishing": [
48
],
"returns": [
49
],
"effect": [
50
],
"called": [
51
],
"submodularity.": [
52
],
"submodularity": [
54
],
"these": [
56
],
"objectives": [
57
],
"exploited": [
59
],
"design": [
63
],
"efficient": [
64
],
"placement": [
65
],
"algorithms": [
66,
72
],
"with": [
67
],
"provable": [
68
],
"performance": [
69
],
"guarantees.": [
70
],
"presented": [
73,
99,
126,
153
],
"this": [
75,
101,
155
],
"paper": [
76,
102,
156
],
"do": [
77
],
"not": [
78
],
"rely": [
79
],
"on": [
80,
147,
157
],
"mixed": [
81
],
"integer": [
82
],
"programming,": [
83
],
"scale": [
85
],
"well": [
86
],
"networks": [
88
],
"arbitrary": [
90
],
"size.": [
91
],
"instances": [
94
],
"considered": [
95
],
"approach": [
98
],
"are": [
103
],
"orders": [
104
],
"magnitude": [
106
],
"(a": [
107
],
"factor": [
108
],
"72)": [
110
],
"larger": [
111
],
"than": [
112,
171
],
"largest": [
114
],
"problems": [
115
],
"solved": [
116
],
"literature.": [
119
],
"how": [
123
],
"method": [
125,
152
],
"here": [
127
],
"can": [
128
],
"be": [
129
],
"extended": [
130
],
"multicriteria": [
132
],
"optimization,": [
133
],
"selecting": [
134
],
"placements": [
135
],
"robust": [
136
],
"sensor": [
138
],
"failures": [
139
],
"optimizing": [
141
],
"minimax": [
142
],
"criteria.": [
143
],
"Extensive": [
144
],
"empirical": [
145
],
"evidence": [
146
],
"effectiveness": [
149
],
"two": [
158
],
"benchmark": [
159
],
"networks,": [
161
],
"actual": [
164
],
"drinking": [
165
],
"system": [
168
],
"greater": [
170
],
"21,000": [
172
],
"nodes,": [
173
],
"presented.": [
175
]
}
    assert output == utils.get_abstract('W2145825677')


