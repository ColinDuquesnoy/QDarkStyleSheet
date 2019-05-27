# -*- coding: utf-8 -*-

# Resource object code
#
# Created: seg mai 27 17:43:17 2019
#      by: The Resource Compiler for PySide2 (Qt v5.12.3)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\xba5\
/\
* --------------\
----------------\
----------------\
----------------\
-------------\x0a\x0a \
   Created by th\
e qtsass compile\
r\x0a\x0a    WARNING! \
All changes made\
 in this file wi\
ll be lost!\x0a\x0a---\
----------------\
----------------\
----------------\
----------------\
-------- */\x0a/* Q\
DarkStyleSheet -\
----------------\
----------------\
----------------\
----------\x0a\x0aThis\
 is the main sty\
le sheet, the pa\
lette has eight \
colors.\x0a\x0aIt is b\
ased on three se\
lecting colors, \
three greyish (b\
ackground) color\
s\x0aplus three whi\
tish (foreground\
) colors. Each s\
et of widgets of\
 the same\x0atype h\
ave a header lik\
e this:\x0a\x0a    ---\
---------------\x0a\
    GroupName --\
------\x0a    -----\
-------------\x0a\x0aA\
nd each widget i\
s separated with\
 a header like t\
his:\x0a\x0a    QWidge\
tName ------\x0a\x0aTh\
is makes more ea\
sy to find and c\
hange some css f\
ield. The basic\x0a\
configuration is\
 described bello\
w.\x0a\x0a    BACKGROU\
ND -----------\x0a\x0a\
        Light  #\
4D545B #505F69 (\
unpressed)\x0a     \
   Normal #31363\
B #32414B (borde\
r, disabled, pre\
ssed, checked, t\
oolbars, menus)\x0a\
        Dark   #\
232629 #19232D (\
background)\x0a\x0a   \
 FOREGROUND ----\
-------\x0a\x0a       \
 Light  #EFF0F1 \
#F0F0F0 (texts/l\
abels)\x0a        N\
ormal         #A\
AAAAA (not used \
yet)\x0a        Dar\
k   #505F69 #787\
878 (disabled te\
xts)\x0a\x0a    SELECT\
ION ------------\
\x0a\x0a        Light \
 #179AE0 #148CD2\
 (selection/hove\
r/active)\x0a      \
  Normal #3375A3\
 #1464A0 (select\
ed)\x0a        Dark\
   #18465D #1450\
6E (selected dis\
abled)\x0a\x0aIf a str\
anger configurat\
ion is required \
because of a bug\
fix or anything\x0a\
else, keep the c\
omment on the li\
ne above so nobo\
dy changes it, i\
ncluding the\x0aiss\
ue number.\x0a\x0a*/\x0a/\
*\x0a\x0aSee Qt docume\
ntation:\x0a\x0a  - ht\
tps://doc.qt.io/\
qt-5/stylesheet.\
html\x0a  - https:/\
/doc.qt.io/qt-5/\
stylesheet-refer\
ence.html\x0a  - ht\
tps://doc.qt.io/\
qt-5/stylesheet-\
examples.html\x0a\x0a-\
----------------\
----------------\
----------------\
----------------\
---------- */\x0a/*\
 QWidget -------\
----------------\
----------------\
----------------\
---------\x0a\x0a-----\
----------------\
----------------\
----------------\
----------------\
------ */\x0aQWidge\
t {\x0a  background\
-color: #19232D;\
\x0a  border: 0px s\
olid #32414B;\x0a  \
padding: 0px;\x0a  \
color: #F0F0F0;\x0a\
  selection-back\
ground-color: #1\
464A0;\x0a  selecti\
on-color: #F0F0F\
0;\x0a}\x0a\x0aQWidget:di\
sabled {\x0a  backg\
round-color: #19\
232D;\x0a  color: #\
787878;\x0a  select\
ion-background-c\
olor: #14506E;\x0a \
 selection-color\
: #787878;\x0a}\x0a\x0aQW\
idget::item:sele\
cted {\x0a  backgro\
und-color: #1464\
A0;\x0a}\x0a\x0aQWidget::\
item:hover {\x0a  b\
ackground-color:\
 #148CD2;\x0a  colo\
r: #32414B;\x0a}\x0a\x0a/\
* QMainWindow --\
----------------\
----------------\
----------------\
----------\x0a\x0aThis\
 adjusts the spl\
itter in the doc\
k widget, not qs\
plitter\x0a\x0ahttps:/\
/doc.qt.io/qt-5/\
stylesheet-examp\
les.html#customi\
zing-qmainwindow\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQMainWindow::se\
parator {\x0a  back\
ground-color: #3\
2414B;\x0a  border:\
 0px solid #1923\
2D;\x0a  spacing: 0\
px;\x0a  padding: 2\
px;\x0a}\x0a\x0aQMainWind\
ow::separator:ho\
ver {\x0a  backgrou\
nd-color: #505F6\
9;\x0a  border: 0px\
 solid #148CD2;\x0a\
}\x0a\x0aQMainWindow::\
separator:horizo\
ntal {\x0a  width: \
5px;\x0a  margin-to\
p: 2px;\x0a  margin\
-bottom: 2px;\x0a  \
image: url(\x22:/qs\
s_icons/rc/toolb\
ar_separator_ver\
tical.png\x22);\x0a}\x0a\x0a\
QMainWindow::sep\
arator:vertical \
{\x0a  height: 5px;\
\x0a  margin-left: \
2px;\x0a  margin-ri\
ght: 2px;\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/toolbar_s\
eparator_horizon\
tal.png\x22);\x0a}\x0a\x0a/*\
 QToolTip ------\
----------------\
----------------\
----------------\
---------\x0a\x0ahttps\
://doc.qt.io/qt-\
5/stylesheet-exa\
mples.html#custo\
mizing-qtooltip\x0a\
\x0a---------------\
----------------\
----------------\
----------------\
------------ */\x0a\
QToolTip {\x0a  bac\
kground-color: #\
148CD2;\x0a  border\
: 1px solid #192\
32D;\x0a  color: #1\
9232D;\x0a  /* Remo\
ve padding, for \
fix combo box to\
oltip */\x0a  paddi\
ng: 0px;\x0a  /* Re\
ducing transpare\
ncy to read bett\
er */\x0a  opacity:\
 230;\x0a}\x0a\x0a/* QSta\
tusBar ---------\
----------------\
----------------\
----------------\
----\x0a\x0ahttps://do\
c.qt.io/qt-5/sty\
lesheet-examples\
.html#customizin\
g-qstatusbar\x0a\x0a--\
----------------\
----------------\
----------------\
----------------\
--------- */\x0aQSt\
atusBar {\x0a  bord\
er: 1px solid #3\
2414B;\x0a  /* Fixe\
s Spyder #9120, \
#9121 */\x0a  backg\
round: #32414B;\x0a\
}\x0a\x0aQStatusBar QT\
oolTip {\x0a  backg\
round-color: #14\
8CD2;\x0a  border: \
1px solid #19232\
D;\x0a  color: #192\
32D;\x0a  /* Remove\
 padding, for fi\
x combo box tool\
tip */\x0a  padding\
: 0px;\x0a  /* Redu\
cing transparenc\
y to read better\
 */\x0a  opacity: 2\
30;\x0a}\x0a\x0aQStatusBa\
r QLabel {\x0a  /* \
Fixes Spyder #91\
20, #9121 */\x0a  b\
ackground: trans\
parent;\x0a}\x0a\x0a/* QC\
heckBox --------\
----------------\
----------------\
----------------\
------\x0a\x0ahttps://\
doc.qt.io/qt-5/s\
tylesheet-exampl\
es.html#customiz\
ing-qcheckbox\x0a\x0a-\
----------------\
----------------\
----------------\
----------------\
---------- */\x0aQC\
heckBox {\x0a  back\
ground-color: #1\
9232D;\x0a  color: \
#F0F0F0;\x0a  spaci\
ng: 4px;\x0a  outli\
ne: none;\x0a  padd\
ing-top: 4px;\x0a  \
padding-bottom: \
4px;\x0a}\x0a\x0aQCheckBo\
x:focus {\x0a  bord\
er: none;\x0a}\x0a\x0aQCh\
eckBox QWidget:d\
isabled {\x0a  back\
ground-color: #1\
9232D;\x0a  color: \
#787878;\x0a}\x0a\x0aQChe\
ckBox::indicator\
 {\x0a  margin-left\
: 4px;\x0a  height:\
 16px;\x0a  width: \
16px;\x0a}\x0a\x0aQCheckB\
ox::indicator:un\
checked {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/checkbox_\
unchecked.png\x22);\
\x0a}\x0a\x0aQCheckBox::i\
ndicator:uncheck\
ed:hover, QCheck\
Box::indicator:u\
nchecked:focus, \
QCheckBox::indic\
ator:unchecked:p\
ressed {\x0a  borde\
r: none;\x0a  image\
: url(\x22:/qss_ico\
ns/rc/checkbox_u\
nchecked_focus.p\
ng\x22);\x0a}\x0a\x0aQCheckB\
ox::indicator:un\
checked:disabled\
 {\x0a  image: url(\
\x22:/qss_icons/rc/\
checkbox_uncheck\
ed_disabled.png\x22\
);\x0a}\x0a\x0aQCheckBox:\
:indicator:check\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/checkbox_check\
ed.png\x22);\x0a}\x0a\x0aQCh\
eckBox::indicato\
r:checked:hover,\
 QCheckBox::indi\
cator:checked:fo\
cus, QCheckBox::\
indicator:checke\
d:pressed {\x0a  bo\
rder: none;\x0a  im\
age: url(\x22:/qss_\
icons/rc/checkbo\
x_checked_focus.\
png\x22);\x0a}\x0a\x0aQCheck\
Box::indicator:c\
hecked:disabled \
{\x0a  image: url(\x22\
:/qss_icons/rc/c\
heckbox_checked_\
disabled.png\x22);\x0a\
}\x0a\x0aQCheckBox::in\
dicator:indeterm\
inate {\x0a  image:\
 url(\x22:/qss_icon\
s/rc/checkbox_in\
determinate.png\x22\
);\x0a}\x0a\x0aQCheckBox:\
:indicator:indet\
erminate:disable\
d {\x0a  image: url\
(\x22:/qss_icons/rc\
/checkbox_indete\
rminate_disabled\
.png\x22);\x0a}\x0a\x0aQChec\
kBox::indicator:\
indeterminate:fo\
cus, QCheckBox::\
indicator:indete\
rminate:hover, Q\
CheckBox::indica\
tor:indeterminat\
e:pressed {\x0a  im\
age: url(\x22:/qss_\
icons/rc/checkbo\
x_indeterminate_\
focus.png\x22);\x0a}\x0a\x0a\
/* QGroupBox ---\
----------------\
----------------\
----------------\
-----------\x0a\x0ahtt\
ps://doc.qt.io/q\
t-5/stylesheet-e\
xamples.html#cus\
tomizing-qgroupb\
ox\x0a\x0a------------\
----------------\
----------------\
----------------\
--------------- \
*/\x0aQGroupBox {\x0a \
 font-weight: bo\
ld;\x0a  border: 1p\
x solid #32414B;\
\x0a  border-radius\
: 4px;\x0a  padding\
: 4px;\x0a  margin-\
top: 16px;\x0a}\x0a\x0aQG\
roupBox::title {\
\x0a  subcontrol-or\
igin: margin;\x0a  \
subcontrol-posit\
ion: top left;\x0a \
 left: 3px;\x0a  pa\
dding-left: 3px;\
\x0a  padding-right\
: 5px;\x0a  padding\
-top: 8px;\x0a  pad\
ding-bottom: 16p\
x;\x0a}\x0a\x0aQGroupBox:\
:indicator {\x0a  m\
argin-left: 2px;\
\x0a  height: 12px;\
\x0a  width: 12px;\x0a\
}\x0a\x0aQGroupBox::in\
dicator:unchecke\
d:hover, QGroupB\
ox::indicator:un\
checked:focus, Q\
GroupBox::indica\
tor:unchecked:pr\
essed {\x0a  border\
: none;\x0a  image:\
 url(\x22:/qss_icon\
s/rc/checkbox_un\
checked_focus.pn\
g\x22);\x0a}\x0a\x0aQGroupBo\
x::indicator:unc\
hecked:disabled \
{\x0a  image: url(\x22\
:/qss_icons/rc/c\
heckbox_unchecke\
d_disabled.png\x22)\
;\x0a}\x0a\x0aQGroupBox::\
indicator:checke\
d:hover, QGroupB\
ox::indicator:ch\
ecked:focus, QGr\
oupBox::indicato\
r:checked:presse\
d {\x0a  border: no\
ne;\x0a  image: url\
(\x22:/qss_icons/rc\
/checkbox_checke\
d_focus.png\x22);\x0a}\
\x0a\x0aQGroupBox::ind\
icator:checked:d\
isabled {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/checkbox_\
checked_disabled\
.png\x22);\x0a}\x0a\x0a/* QR\
adioButton -----\
----------------\
----------------\
----------------\
------\x0a\x0ahttps://\
doc.qt.io/qt-5/s\
tylesheet-exampl\
es.html#customiz\
ing-qradiobutton\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQRadioButton {\x0a\
  background-col\
or: #19232D;\x0a  c\
olor: #F0F0F0;\x0a \
 spacing: 4px;\x0a \
 padding: 0px;\x0a \
 border: none;\x0a \
 outline: none;\x0a\
}\x0a\x0aQRadioButton:\
focus {\x0a  border\
: none;\x0a}\x0a\x0aQRadi\
oButton:disabled\
 {\x0a  background-\
color: #19232D;\x0a\
  color: #787878\
;\x0a  border: none\
;\x0a  outline: non\
e;\x0a}\x0a\x0aQRadioButt\
on QWidget {\x0a  b\
ackground-color:\
 #19232D;\x0a  colo\
r: #F0F0F0;\x0a  sp\
acing: 0px;\x0a  pa\
dding: 0px;\x0a  ou\
tline: none;\x0a  b\
order: none;\x0a}\x0a\x0a\
QRadioButton::in\
dicator {\x0a  bord\
er: none;\x0a  outl\
ine: none;\x0a  mar\
gin-left: 4px;\x0a \
 height: 16px;\x0a \
 width: 16px;\x0a}\x0a\
\x0aQRadioButton::i\
ndicator:uncheck\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/radio_unchecke\
d.png\x22);\x0a}\x0a\x0aQRad\
ioButton::indica\
tor:unchecked:ho\
ver, QRadioButto\
n::indicator:unc\
hecked:focus, QR\
adioButton::indi\
cator:unchecked:\
pressed {\x0a  bord\
er: none;\x0a  outl\
ine: none;\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/radio_un\
checked_focus.pn\
g\x22);\x0a}\x0a\x0aQRadioBu\
tton::indicator:\
unchecked:disabl\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/radio_unchecke\
d_disabled.png\x22)\
;\x0a}\x0a\x0aQRadioButto\
n::indicator:che\
cked {\x0a  border:\
 none;\x0a  outline\
: none;\x0a  image:\
 url(\x22:/qss_icon\
s/rc/radio_check\
ed.png\x22);\x0a}\x0a\x0aQRa\
dioButton::indic\
ator:checked:hov\
er, QRadioButton\
::indicator:chec\
ked:focus, QRadi\
oButton::indicat\
or:checked:press\
ed {\x0a  border: n\
one;\x0a  outline: \
none;\x0a  image: u\
rl(\x22:/qss_icons/\
rc/radio_checked\
_focus.png\x22);\x0a}\x0a\
\x0aQRadioButton::i\
ndicator:checked\
:disabled {\x0a  ou\
tline: none;\x0a  i\
mage: url(\x22:/qss\
_icons/rc/radio_\
checked_disabled\
.png\x22);\x0a}\x0a\x0a/* QM\
enuBar ---------\
----------------\
----------------\
----------------\
------\x0a\x0ahttps://\
doc.qt.io/qt-5/s\
tylesheet-exampl\
es.html#customiz\
ing-qmenubar\x0a\x0a--\
----------------\
----------------\
----------------\
----------------\
--------- */\x0aQMe\
nuBar {\x0a  backgr\
ound-color: #324\
14B;\x0a  padding: \
2px;\x0a  border: 1\
px solid #19232D\
;\x0a  color: #F0F0\
F0;\x0a}\x0a\x0aQMenuBar:\
focus {\x0a  border\
: 1px solid #148\
CD2;\x0a}\x0a\x0aQMenuBar\
::item {\x0a  backg\
round: transpare\
nt;\x0a  padding: 4\
px;\x0a}\x0a\x0aQMenuBar:\
:item:selected {\
\x0a  padding: 4px;\
\x0a  background: t\
ransparent;\x0a  bo\
rder: 0px solid \
#32414B;\x0a}\x0a\x0aQMen\
uBar::item:press\
ed {\x0a  padding: \
4px;\x0a  border: 0\
px solid #32414B\
;\x0a  background-c\
olor: #148CD2;\x0a \
 color: #F0F0F0;\
\x0a  margin-bottom\
: 0px;\x0a  padding\
-bottom: 0px;\x0a}\x0a\
\x0a/* QMenu ------\
----------------\
----------------\
----------------\
------------\x0a\x0aht\
tps://doc.qt.io/\
qt-5/stylesheet-\
examples.html#cu\
stomizing-qmenu\x0a\
\x0a---------------\
----------------\
----------------\
----------------\
------------ */\x0a\
QMenu {\x0a  border\
: 0px solid #324\
14B;\x0a  color: #F\
0F0F0;\x0a  margin:\
 0px;\x0a}\x0a\x0aQMenu::\
separator {\x0a  he\
ight: 5px;\x0a  bac\
kground-color: #\
505F69;\x0a  color:\
 #F0F0F0;\x0a  padd\
ing-left: 4px;\x0a \
 margin-left: 2p\
x;\x0a  margin-righ\
t: 2px;\x0a}\x0a\x0aQMenu\
::icon {\x0a  margi\
n: 0px;\x0a  paddin\
g-left: 4px;\x0a}\x0a\x0a\
QMenu::item {\x0a  \
padding: 4px 24p\
x 4px 24px;\x0a  /*\
 Reserve space f\
or selection bor\
der */\x0a  border:\
 1px transparent\
 #32414B;\x0a}\x0a\x0aQMe\
nu::item:selecte\
d {\x0a  color: #F0\
F0F0;\x0a}\x0a\x0aQMenu::\
indicator {\x0a  wi\
dth: 12px;\x0a  hei\
ght: 12px;\x0a  pad\
ding-left: 6px;\x0a\
  /* non-exclusi\
ve indicator = c\
heck box style i\
ndicator (see QA\
ctionGroup::setE\
xclusive) */\x0a  /\
* exclusive indi\
cator = radio bu\
tton style indic\
ator (see QActio\
nGroup::setExclu\
sive) */\x0a}\x0a\x0aQMen\
u::indicator:non\
-exclusive:unche\
cked {\x0a  image: \
url(\x22:/qss_icons\
/rc/checkbox_unc\
hecked.png\x22);\x0a}\x0a\
\x0aQMenu::indicato\
r:non-exclusive:\
unchecked:select\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/checkbox_unche\
cked_disabled.pn\
g\x22);\x0a}\x0a\x0aQMenu::i\
ndicator:non-exc\
lusive:checked {\
\x0a  image: url(\x22:\
/qss_icons/rc/ch\
eckbox_checked.p\
ng\x22);\x0a}\x0a\x0aQMenu::\
indicator:non-ex\
clusive:checked:\
selected {\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/checkbox\
_checked_disable\
d.png\x22);\x0a}\x0a\x0aQMen\
u::indicator:exc\
lusive:unchecked\
 {\x0a  image: url(\
\x22:/qss_icons/rc/\
radio_unchecked.\
png\x22);\x0a}\x0a\x0aQMenu:\
:indicator:exclu\
sive:unchecked:s\
elected {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/radio_unc\
hecked_disabled.\
png\x22);\x0a}\x0a\x0aQMenu:\
:indicator:exclu\
sive:checked {\x0a \
 image: url(\x22:/q\
ss_icons/rc/radi\
o_checked.png\x22);\
\x0a}\x0a\x0aQMenu::indic\
ator:exclusive:c\
hecked:selected \
{\x0a  image: url(\x22\
:/qss_icons/rc/r\
adio_checked_dis\
abled.png\x22);\x0a}\x0a\x0a\
QMenu::right-arr\
ow {\x0a  margin: 5\
px;\x0a  image: url\
(\x22:/qss_icons/rc\
/arrow_right.png\
\x22);\x0a}\x0a\x0a/* QAbstr\
actItemView ----\
----------------\
----------------\
----------------\
--\x0a\x0ahttps://doc.\
qt.io/qt-5/style\
sheet-examples.h\
tml#customizing-\
qcombobox\x0a\x0a-----\
----------------\
----------------\
----------------\
----------------\
------ */\x0aQAbstr\
actItemView {\x0a  \
alternate-backgr\
ound-color: #192\
32D;\x0a  color: #F\
0F0F0;\x0a  border:\
 1px solid #3241\
4B;\x0a  border-rad\
ius: 4px;\x0a}\x0a\x0aQAb\
stractItemView Q\
LineEdit {\x0a  pad\
ding: 2px;\x0a}\x0a\x0a/*\
 QAbstractScroll\
Area -----------\
----------------\
----------------\
---------\x0a\x0ahttps\
://doc.qt.io/qt-\
5/stylesheet-exa\
mples.html#custo\
mizing-qabstract\
scrollarea\x0a\x0a----\
----------------\
----------------\
----------------\
----------------\
------- */\x0aQAbst\
ractScrollArea {\
\x0a  background-co\
lor: #19232D;\x0a  \
border: 1px soli\
d #32414B;\x0a  bor\
der-radius: 4px;\
\x0a  padding: 4px;\
\x0a  color: #F0F0F\
0;\x0a}\x0a\x0aQAbstractS\
crollArea:disabl\
ed {\x0a  color: #7\
87878;\x0a}\x0a\x0a/* QSc\
rollArea -------\
----------------\
----------------\
----------------\
-----\x0a\x0a---------\
----------------\
----------------\
----------------\
----------------\
-- */\x0aQScrollAre\
a QWidget QWidge\
t:disabled {\x0a  b\
ackground-color:\
 #19232D;\x0a}\x0a\x0a/* \
QScrollBar -----\
----------------\
----------------\
----------------\
--------\x0a\x0ahttps:\
//doc.qt.io/qt-5\
/stylesheet-exam\
ples.html#custom\
izing-qscrollbar\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQScrollBar:hori\
zontal {\x0a  heigh\
t: 16px;\x0a  margi\
n: 2px 16px 2px \
16px;\x0a  border: \
1px solid #32414\
B;\x0a  border-radi\
us: 4px;\x0a  backg\
round-color: #19\
232D;\x0a}\x0a\x0aQScroll\
Bar:vertical {\x0a \
 background-colo\
r: #19232D;\x0a  wi\
dth: 16px;\x0a  mar\
gin: 16px 2px 16\
px 2px;\x0a  border\
: 1px solid #324\
14B;\x0a  border-ra\
dius: 4px;\x0a}\x0a\x0aQS\
crollBar::handle\
:horizontal {\x0a  \
background-color\
: #787878;\x0a  bor\
der: 1px solid #\
32414B;\x0a  border\
-radius: 4px;\x0a  \
min-width: 8px;\x0a\
}\x0a\x0aQScrollBar::h\
andle:horizontal\
:hover {\x0a  backg\
round-color: #14\
8CD2;\x0a  border: \
1px solid #148CD\
2;\x0a  border-radi\
us: 4px;\x0a  min-w\
idth: 8px;\x0a}\x0a\x0aQS\
crollBar::handle\
:vertical {\x0a  ba\
ckground-color: \
#787878;\x0a  borde\
r: 1px solid #32\
414B;\x0a  min-heig\
ht: 8px;\x0a  borde\
r-radius: 4px;\x0a}\
\x0a\x0aQScrollBar::ha\
ndle:vertical:ho\
ver {\x0a  backgrou\
nd-color: #148CD\
2;\x0a  border: 1px\
 solid #148CD2;\x0a\
  border-radius:\
 4px;\x0a  min-heig\
ht: 8px;\x0a}\x0a\x0aQScr\
ollBar::add-line\
:horizontal {\x0a  \
margin: 0px 0px \
0px 0px;\x0a  borde\
r-image: url(\x22:/\
qss_icons/rc/arr\
ow_right_disable\
d.png\x22);\x0a  heigh\
t: 12px;\x0a  width\
: 12px;\x0a  subcon\
trol-position: r\
ight;\x0a  subcontr\
ol-origin: margi\
n;\x0a}\x0a\x0aQScrollBar\
::add-line:horiz\
ontal:hover, QSc\
rollBar::add-lin\
e:horizontal:on \
{\x0a  border-image\
: url(\x22:/qss_ico\
ns/rc/arrow_righ\
t.png\x22);\x0a  heigh\
t: 12px;\x0a  width\
: 12px;\x0a  subcon\
trol-position: r\
ight;\x0a  subcontr\
ol-origin: margi\
n;\x0a}\x0a\x0aQScrollBar\
::add-line:verti\
cal {\x0a  margin: \
3px 0px 3px 0px;\
\x0a  border-image:\
 url(\x22:/qss_icon\
s/rc/arrow_down_\
disabled.png\x22);\x0a\
  height: 12px;\x0a\
  width: 12px;\x0a \
 subcontrol-posi\
tion: bottom;\x0a  \
subcontrol-origi\
n: margin;\x0a}\x0a\x0aQS\
crollBar::add-li\
ne:vertical:hove\
r, QScrollBar::a\
dd-line:vertical\
:on {\x0a  border-i\
mage: url(\x22:/qss\
_icons/rc/arrow_\
down.png\x22);\x0a  he\
ight: 12px;\x0a  wi\
dth: 12px;\x0a  sub\
control-position\
: bottom;\x0a  subc\
ontrol-origin: m\
argin;\x0a}\x0a\x0aQScrol\
lBar::sub-line:h\
orizontal {\x0a  ma\
rgin: 0px 3px 0p\
x 3px;\x0a  border-\
image: url(\x22:/qs\
s_icons/rc/arrow\
_left_disabled.p\
ng\x22);\x0a  height: \
12px;\x0a  width: 1\
2px;\x0a  subcontro\
l-position: left\
;\x0a  subcontrol-o\
rigin: margin;\x0a}\
\x0a\x0aQScrollBar::su\
b-line:horizonta\
l:hover, QScroll\
Bar::sub-line:ho\
rizontal:on {\x0a  \
border-image: ur\
l(\x22:/qss_icons/r\
c/arrow_left.png\
\x22);\x0a  height: 12\
px;\x0a  width: 12p\
x;\x0a  subcontrol-\
position: left;\x0a\
  subcontrol-ori\
gin: margin;\x0a}\x0a\x0a\
QScrollBar::sub-\
line:vertical {\x0a\
  margin: 3px 0p\
x 3px 0px;\x0a  bor\
der-image: url(\x22\
:/qss_icons/rc/a\
rrow_up_disabled\
.png\x22);\x0a  height\
: 12px;\x0a  width:\
 12px;\x0a  subcont\
rol-position: to\
p;\x0a  subcontrol-\
origin: margin;\x0a\
}\x0a\x0aQScrollBar::s\
ub-line:vertical\
:hover, QScrollB\
ar::sub-line:ver\
tical:on {\x0a  bor\
der-image: url(\x22\
:/qss_icons/rc/a\
rrow_up.png\x22);\x0a \
 height: 12px;\x0a \
 width: 12px;\x0a  \
subcontrol-posit\
ion: top;\x0a  subc\
ontrol-origin: m\
argin;\x0a}\x0a\x0aQScrol\
lBar::up-arrow:h\
orizontal, QScro\
llBar::down-arro\
w:horizontal {\x0a \
 background: non\
e;\x0a}\x0a\x0aQScrollBar\
::up-arrow:verti\
cal, QScrollBar:\
:down-arrow:vert\
ical {\x0a  backgro\
und: none;\x0a}\x0a\x0aQS\
crollBar::add-pa\
ge:horizontal, Q\
ScrollBar::sub-p\
age:horizontal {\
\x0a  background: n\
one;\x0a}\x0a\x0aQScrollB\
ar::add-page:ver\
tical, QScrollBa\
r::sub-page:vert\
ical {\x0a  backgro\
und: none;\x0a}\x0a\x0a/*\
 QTextEdit -----\
----------------\
----------------\
----------------\
---------\x0a\x0ahttps\
://doc.qt.io/qt-\
5/stylesheet-exa\
mples.html#custo\
mizing-specific-\
widgets\x0a\x0a-------\
----------------\
----------------\
----------------\
----------------\
---- */\x0aQTextEdi\
t {\x0a  background\
-color: #19232D;\
\x0a  color: #F0F0F\
0;\x0a  border: 1px\
 solid #32414B;\x0a\
}\x0a\x0aQTextEdit:hov\
er {\x0a  border: 1\
px solid #148CD2\
;\x0a  color: #F0F0\
F0;\x0a}\x0a\x0aQTextEdit\
:selected {\x0a  ba\
ckground: #1464A\
0;\x0a  color: #324\
14B;\x0a}\x0a\x0a/* QPlai\
nTextEdit ------\
----------------\
----------------\
----------------\
---\x0a\x0a-----------\
----------------\
----------------\
----------------\
----------------\
 */\x0aQPlainTextEd\
it {\x0a  backgroun\
d-color: #19232D\
;\x0a  color: #F0F0\
F0;\x0a  border-rad\
ius: 4px;\x0a  bord\
er: 1px solid #3\
2414B;\x0a}\x0a\x0aQPlain\
TextEdit:hover {\
\x0a  border: 1px s\
olid #148CD2;\x0a  \
color: #F0F0F0;\x0a\
}\x0a\x0aQPlainTextEdi\
t:selected {\x0a  b\
ackground: #1464\
A0;\x0a  color: #32\
414B;\x0a}\x0a\x0a/* QSiz\
eGrip ----------\
----------------\
----------------\
----------------\
----\x0a\x0ahttps://do\
c.qt.io/qt-5/sty\
lesheet-examples\
.html#customizin\
g-qsizegrip\x0a\x0a---\
----------------\
----------------\
----------------\
----------------\
-------- */\x0aQSiz\
eGrip {\x0a  backgr\
ound: transparen\
t;\x0a  width: 12px\
;\x0a  height: 12px\
;\x0a  image: url(\x22\
:/qss_icons/rc/w\
indow_grip.png\x22)\
;\x0a}\x0a\x0a/* QStacked\
Widget ---------\
----------------\
----------------\
----------------\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQStackedWidget \
{\x0a  padding: 4px\
;\x0a  border: 1px \
solid #32414B;\x0a \
 border: 1px sol\
id #19232D;\x0a}\x0a\x0a/\
* QToolBar -----\
----------------\
----------------\
----------------\
----------\x0a\x0ahttp\
s://doc.qt.io/qt\
-5/stylesheet-ex\
amples.html#cust\
omizing-qtoolbar\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQToolBar {\x0a  ba\
ckground-color: \
#32414B;\x0a  borde\
r-bottom: 1px so\
lid #19232D;\x0a  p\
adding: 2px;\x0a  f\
ont-weight: bold\
;\x0a}\x0a\x0aQToolBar QT\
oolButton {\x0a  ba\
ckground-color: \
#32414B;\x0a}\x0a\x0aQToo\
lBar::handle:hor\
izontal {\x0a  widt\
h: 16px;\x0a  image\
: url(\x22:/qss_ico\
ns/rc/toolbar_mo\
ve_horizontal.pn\
g\x22);\x0a}\x0a\x0aQToolBar\
::handle:vertica\
l {\x0a  height: 16\
px;\x0a  image: url\
(\x22:/qss_icons/rc\
/toolbar_move_ho\
rizontal.png\x22);\x0a\
}\x0a\x0aQToolBar::sep\
arator:horizonta\
l {\x0a  width: 16p\
x;\x0a  image: url(\
\x22:/qss_icons/rc/\
toolbar_separato\
r_horizontal.png\
\x22);\x0a}\x0a\x0aQToolBar:\
:separator:verti\
cal {\x0a  height: \
16px;\x0a  image: u\
rl(\x22:/qss_icons/\
rc/toolbar_separ\
ator_vertical.pn\
g\x22);\x0a}\x0a\x0aQToolBut\
ton#qt_toolbar_e\
xt_button {\x0a  ba\
ckground: #32414\
B;\x0a  border: 0px\
;\x0a  color: #F0F0\
F0;\x0a  image: url\
(\x22:/qss_icons/rc\
/arrow_right.png\
\x22);\x0a}\x0a\x0a/* QAbstr\
actSpinBox -----\
----------------\
----------------\
----------------\
--\x0a\x0a------------\
----------------\
----------------\
----------------\
--------------- \
*/\x0aQAbstractSpin\
Box {\x0a  backgrou\
nd-color: #19232\
D;\x0a  border: 1px\
 solid #32414B;\x0a\
  color: #F0F0F0\
;\x0a  /* This fixe\
s 103, 111 */\x0a  \
padding-top: 2px\
;\x0a  /* This fixe\
s 103, 111 */\x0a  \
padding-bottom: \
2px;\x0a  padding-l\
eft: 4px;\x0a  padd\
ing-right: 4px;\x0a\
  border-radius:\
 4px;\x0a  /* min-w\
idth: 5px; remov\
ed to fix 109 */\
\x0a}\x0a\x0aQAbstractSpi\
nBox:up-button {\
\x0a  background-co\
lor: transparent\
 #19232D;\x0a  subc\
ontrol-origin: b\
order;\x0a  subcont\
rol-position: to\
p right;\x0a  borde\
r-left: 1px soli\
d #32414B;\x0a  mar\
gin: 1px;\x0a}\x0a\x0aQAb\
stractSpinBox::u\
p-arrow, QAbstra\
ctSpinBox::up-ar\
row:disabled, QA\
bstractSpinBox::\
up-arrow:off {\x0a \
 image: url(\x22:/q\
ss_icons/rc/arro\
w_up_disabled.pn\
g\x22);\x0a  height: 1\
2px;\x0a  width: 12\
px;\x0a}\x0a\x0aQAbstract\
SpinBox::up-arro\
w:hover {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/arrow_up.\
png\x22);\x0a}\x0a\x0aQAbstr\
actSpinBox:down-\
button {\x0a  backg\
round-color: tra\
nsparent #19232D\
;\x0a  subcontrol-o\
rigin: border;\x0a \
 subcontrol-posi\
tion: bottom rig\
ht;\x0a  border-lef\
t: 1px solid #32\
414B;\x0a  margin: \
1px;\x0a}\x0a\x0aQAbstrac\
tSpinBox::down-a\
rrow, QAbstractS\
pinBox::down-arr\
ow:disabled, QAb\
stractSpinBox::d\
own-arrow:off {\x0a\
  image: url(\x22:/\
qss_icons/rc/arr\
ow_down_disabled\
.png\x22);\x0a  height\
: 12px;\x0a  width:\
 12px;\x0a}\x0a\x0aQAbstr\
actSpinBox::down\
-arrow:hover {\x0a \
 image: url(\x22:/q\
ss_icons/rc/arro\
w_down.png\x22);\x0a}\x0a\
\x0aQAbstractSpinBo\
x:hover {\x0a  bord\
er: 1px solid #1\
48CD2;\x0a  color: \
#F0F0F0;\x0a}\x0a\x0aQAbs\
tractSpinBox:sel\
ected {\x0a  backgr\
ound: #1464A0;\x0a \
 color: #32414B;\
\x0a}\x0a\x0a/* ---------\
----------------\
----------------\
----------------\
--------------- \
*/\x0a/* DISPLAYS -\
----------------\
----------------\
----------------\
-------------- *\
/\x0a/* -----------\
----------------\
----------------\
----------------\
------------- */\
\x0a/* QLabel -----\
----------------\
----------------\
----------------\
------------\x0a\x0aht\
tps://doc.qt.io/\
qt-5/stylesheet-\
examples.html#cu\
stomizing-qframe\
\x0a\x0a--------------\
----------------\
----------------\
----------------\
------------- */\
\x0aQLabel {\x0a  back\
ground-color: #1\
9232D;\x0a  border:\
 0px solid #3241\
4B;\x0a  padding: 2\
px;\x0a  margin: 0p\
x;\x0a  color: #F0F\
0F0;\x0a}\x0a\x0aQLabel::\
disabled {\x0a  bac\
kground-color: #\
19232D;\x0a  border\
: 0px solid #324\
14B;\x0a  color: #7\
87878;\x0a}\x0a\x0a/* QTe\
xtBrowser ------\
----------------\
----------------\
----------------\
-----\x0a\x0ahttps://d\
oc.qt.io/qt-5/st\
ylesheet-example\
s.html#customizi\
ng-qabstractscro\
llarea\x0a\x0a--------\
----------------\
----------------\
----------------\
----------------\
--- */\x0aQTextBrow\
ser {\x0a  backgrou\
nd-color: #19232\
D;\x0a  border: 1px\
 solid #32414B;\x0a\
  color: #F0F0F0\
;\x0a  border-radiu\
s: 4px;\x0a}\x0a\x0aQText\
Browser:disabled\
 {\x0a  background-\
color: #19232D;\x0a\
  border: 1px so\
lid #32414B;\x0a  c\
olor: #787878;\x0a \
 border-radius: \
4px;\x0a}\x0a\x0aQTextBro\
wser:hover, QTex\
tBrowser:!hover,\
 QTextBrowser::s\
elected, QTextBr\
owser::pressed {\
\x0a  border: 1px s\
olid #32414B;\x0a}\x0a\
\x0a/* QGraphicsVie\
w --------------\
----------------\
----------------\
------------\x0a\x0a--\
----------------\
----------------\
----------------\
----------------\
--------- */\x0aQGr\
aphicsView {\x0a  b\
ackground-color:\
 #19232D;\x0a  bord\
er: 1px solid #3\
2414B;\x0a  color: \
#F0F0F0;\x0a  borde\
r-radius: 4px;\x0a}\
\x0a\x0aQGraphicsView:\
disabled {\x0a  bac\
kground-color: #\
19232D;\x0a  border\
: 1px solid #324\
14B;\x0a  color: #7\
87878;\x0a  border-\
radius: 4px;\x0a}\x0a\x0a\
QGraphicsView:ho\
ver, QGraphicsVi\
ew:!hover, QGrap\
hicsView::select\
ed, QGraphicsVie\
w::pressed {\x0a  b\
order: 1px solid\
 #32414B;\x0a}\x0a\x0a/* \
QCalendarWidget \
----------------\
----------------\
----------------\
--------\x0a\x0a------\
----------------\
----------------\
----------------\
----------------\
----- */\x0aQCalend\
arWidget {\x0a  bor\
der: 1px solid #\
32414B;\x0a  border\
-radius: 4px;\x0a}\x0a\
\x0aQCalendarWidget\
:disabled {\x0a  ba\
ckground-color: \
#19232D;\x0a  color\
: #787878;\x0a}\x0a\x0a/*\
 QLCDNumber ----\
----------------\
----------------\
----------------\
---------\x0a\x0a-----\
----------------\
----------------\
----------------\
----------------\
------ */\x0aQLCDNu\
mber {\x0a  backgro\
und-color: #1923\
2D;\x0a  color: #F0\
F0F0;\x0a}\x0a\x0aQLCDNum\
ber:disabled {\x0a \
 background-colo\
r: #19232D;\x0a  co\
lor: #787878;\x0a}\x0a\
\x0a/* QProgressBar\
 ---------------\
----------------\
----------------\
------------\x0a\x0aht\
tps://doc.qt.io/\
qt-5/stylesheet-\
examples.html#cu\
stomizing-qprogr\
essbar\x0a\x0a--------\
----------------\
----------------\
----------------\
----------------\
--- */\x0aQProgress\
Bar {\x0a  backgrou\
nd-color: #19232\
D;\x0a  border: 1px\
 solid #32414B;\x0a\
  color: #F0F0F0\
;\x0a  border-radiu\
s: 4px;\x0a  text-a\
lign: center;\x0a}\x0a\
\x0aQProgressBar:di\
sabled {\x0a  backg\
round-color: #19\
232D;\x0a  border: \
1px solid #32414\
B;\x0a  color: #787\
878;\x0a  border-ra\
dius: 4px;\x0a  tex\
t-align: center;\
\x0a}\x0a\x0aQProgressBar\
::chunk {\x0a  back\
ground-color: #1\
464A0;\x0a  color: \
#19232D;\x0a  borde\
r-radius: 4px;\x0a}\
\x0a\x0aQProgressBar::\
chunk:disabled {\
\x0a  background-co\
lor: #14506E;\x0a  \
color: #787878;\x0a\
  border-radius:\
 4px;\x0a}\x0a\x0a/* ----\
----------------\
----------------\
----------------\
----------------\
---- */\x0a/* BUTTO\
NS -------------\
----------------\
----------------\
----------------\
--- */\x0a/* ------\
----------------\
----------------\
----------------\
----------------\
-- */\x0a/* QPushBu\
tton -----------\
----------------\
----------------\
----------------\
-\x0a\x0ahttps://doc.q\
t.io/qt-5/styles\
heet-examples.ht\
ml#customizing-q\
pushbutton\x0a\x0a----\
----------------\
----------------\
----------------\
----------------\
------- */\x0aQPush\
Button {\x0a  backg\
round-color: #50\
5F69;\x0a  border: \
1px solid #32414\
B;\x0a  color: #F0F\
0F0;\x0a  border-ra\
dius: 4px;\x0a  pad\
ding: 3px;\x0a  out\
line: none;\x0a}\x0a\x0aQ\
PushButton:disab\
led {\x0a  backgrou\
nd-color: #32414\
B;\x0a  border: 1px\
 solid #32414B;\x0a\
  color: #787878\
;\x0a  border-radiu\
s: 4px;\x0a  paddin\
g: 3px;\x0a}\x0a\x0aQPush\
Button:checked {\
\x0a  background-co\
lor: #32414B;\x0a  \
border: 1px soli\
d #32414B;\x0a  bor\
der-radius: 4px;\
\x0a  padding: 3px;\
\x0a  outline: none\
;\x0a}\x0a\x0aQPushButton\
:checked:disable\
d {\x0a  background\
-color: #19232D;\
\x0a  border: 1px s\
olid #32414B;\x0a  \
color: #787878;\x0a\
  border-radius:\
 4px;\x0a  padding:\
 3px;\x0a  outline:\
 none;\x0a}\x0a\x0aQPushB\
utton:checked:se\
lected {\x0a  backg\
round: #1464A0;\x0a\
  color: #32414B\
;\x0a}\x0a\x0aQPushButton\
:checked:hover {\
\x0a  border: 1px s\
olid #148CD2;\x0a  \
color: #F0F0F0;\x0a\
}\x0a\x0aQPushButton::\
menu-indicator {\
\x0a  subcontrol-or\
igin: padding;\x0a \
 subcontrol-posi\
tion: bottom rig\
ht;\x0a  bottom: 4p\
x;\x0a}\x0a\x0aQPushButto\
n:pressed {\x0a  ba\
ckground-color: \
#19232D;\x0a  borde\
r: 1px solid #19\
232D;\x0a}\x0a\x0aQPushBu\
tton:pressed:hov\
er {\x0a  border: 1\
px solid #148CD2\
;\x0a}\x0a\x0aQPushButton\
:hover {\x0a  borde\
r: 1px solid #14\
8CD2;\x0a  color: #\
F0F0F0;\x0a}\x0a\x0aQPush\
Button:selected \
{\x0a  background: \
#1464A0;\x0a  color\
: #32414B;\x0a}\x0a\x0a/*\
 QToolButton ---\
----------------\
----------------\
----------------\
---------\x0a\x0ahttps\
://doc.qt.io/qt-\
5/stylesheet-exa\
mples.html#custo\
mizing-qtoolbutt\
on\x0a\x0a------------\
----------------\
----------------\
----------------\
--------------- \
*/\x0aQToolButton {\
\x0a  background-co\
lor: transparent\
;\x0a  border: 1px \
solid #32414B;\x0a \
 border-radius: \
4px;\x0a  margin: 0\
px;\x0a  padding: 2\
px;\x0a  /* The sub\
controls below a\
re used only in \
the MenuButtonPo\
pup mode */\x0a  /*\
 The subcontrol \
below is used on\
ly in the Instan\
tPopup or Delaye\
dPopup mode */\x0a}\
\x0a\x0aQToolButton:ch\
ecked {\x0a  backgr\
ound-color: #192\
32D;\x0a  border: 1\
px solid #19232D\
;\x0a}\x0a\x0aQToolButton\
:checked:hover {\
\x0a  border: 1px s\
olid #148CD2;\x0a}\x0a\
\x0aQToolButton:pre\
ssed {\x0a  backgro\
und-color: #1923\
2D;\x0a  border: 1p\
x solid #19232D;\
\x0a}\x0a\x0aQToolButton:\
pressed:hover {\x0a\
  border: 1px so\
lid #148CD2;\x0a}\x0a\x0a\
QToolButton:disa\
bled {\x0a  border:\
 1px solid #3241\
4B;\x0a}\x0a\x0aQToolButt\
on:hover {\x0a  bor\
der: 1px solid #\
148CD2;\x0a}\x0a\x0aQTool\
Button[popupMode\
=\x221\x22] {\x0a  paddin\
g: 2px;\x0a  /* Onl\
y for MenuButton\
Popup */\x0a  paddi\
ng-right: 12px;\x0a\
  /* Make way fo\
r the popup butt\
on */\x0a  border: \
1px solid #32414\
B;\x0a  border-radi\
us: 4px;\x0a}\x0a\x0aQToo\
lButton[popupMod\
e=\x222\x22] {\x0a  paddi\
ng: 2px;\x0a  /* On\
ly for InstantPo\
pup */\x0a  padding\
-right: 12px;\x0a  \
/* Make way for \
the popup button\
 */\x0a  border: 1p\
x solid #32414B;\
\x0a}\x0a\x0aQToolButton:\
:menu-button {\x0a \
 padding: 2px;\x0a \
 border-radius: \
4px;\x0a  border: 1\
px solid #32414B\
;\x0a  border-top-r\
ight-radius: 4px\
;\x0a  border-botto\
m-right-radius: \
4px;\x0a  /* 16px w\
idth + 4px for b\
order = 20px all\
ocated above */\x0a\
  width: 16px;\x0a \
 outline: none;\x0a\
}\x0a\x0aQToolButton::\
menu-button:hove\
r {\x0a  border: 1p\
x solid #148CD2;\
\x0a}\x0a\x0aQToolButton:\
:menu-button:che\
cked:hover {\x0a  b\
order: 1px solid\
 #148CD2;\x0a}\x0a\x0aQTo\
olButton::menu-i\
ndicator {\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/arrow_do\
wn.png\x22);\x0a  top:\
 -8px;\x0a  /* Shif\
t it a bit */\x0a  \
left: -4px;\x0a  /*\
 Shift it a bit \
*/\x0a}\x0a\x0aQToolButto\
n::menu-arrow {\x0a\
  image: url(\x22:/\
qss_icons/rc/arr\
ow_down.png\x22);\x0a}\
\x0a\x0aQToolButton::m\
enu-arrow:open {\
\x0a  border: 1px s\
olid #32414B;\x0a}\x0a\
\x0a/* QCommandLink\
Button ---------\
----------------\
----------------\
------------\x0a\x0a--\
----------------\
----------------\
----------------\
----------------\
--------- */\x0aQCo\
mmandLinkButton \
{\x0a  background-c\
olor: transparen\
t;\x0a  border: 1px\
 solid #32414B;\x0a\
  color: #F0F0F0\
;\x0a  border-radiu\
s: 4px;\x0a  paddin\
g: 0px;\x0a  margin\
: 0px;\x0a}\x0a\x0aQComma\
ndLinkButton:dis\
abled {\x0a  backgr\
ound-color: tran\
sparent;\x0a  color\
: #787878;\x0a}\x0a\x0a/*\
 ---------------\
----------------\
----------------\
----------------\
--------- */\x0a/* \
INPUTS - NO FIEL\
DS -------------\
----------------\
----------------\
-------- */\x0a/* -\
----------------\
----------------\
----------------\
----------------\
------- */\x0a/* QC\
omboBox --------\
----------------\
----------------\
----------------\
------\x0a\x0ahttps://\
doc.qt.io/qt-5/s\
tylesheet-exampl\
es.html#customiz\
ing-qcombobox\x0a\x0a-\
----------------\
----------------\
----------------\
----------------\
---------- */\x0aQC\
omboBox {\x0a  bord\
er: 1px solid #3\
2414B;\x0a  border-\
radius: 4px;\x0a  s\
election-backgro\
und-color: #1464\
A0;\x0a  padding-le\
ft: 4px;\x0a  paddi\
ng-right: 4px;\x0a \
 /* Fixes #103, \
#111 */\x0a  min-he\
ight: 1.5em;\x0a  /\
* padding-top: 2\
px;     removed \
to fix #132 */\x0a \
 /* padding-bott\
om: 2px;  remove\
d to fix #132 */\
\x0a  /* min-width:\
 75px;      remo\
ved to fix #109 \
*/\x0a  /* Needed t\
o remove indicat\
or - fix #132 */\
\x0a}\x0a\x0aQComboBox QA\
bstractItemView \
{\x0a  background-c\
olor: #19232D;\x0a \
 border-radius: \
4px;\x0a  border: 1\
px solid #32414B\
;\x0a  selection-co\
lor: #148CD2;\x0a  \
selection-backgr\
ound-color: #324\
14B;\x0a}\x0a\x0aQComboBo\
x:disabled {\x0a  b\
ackground-color:\
 #19232D;\x0a  colo\
r: #787878;\x0a}\x0a\x0aQ\
ComboBox:hover {\
\x0a  border: 1px s\
olid #148CD2;\x0a}\x0a\
\x0aQComboBox:on {\x0a\
  selection-back\
ground-color: #1\
9232D;\x0a}\x0a\x0aQCombo\
Box::indicator {\
\x0a  background-co\
lor: transparent\
;\x0a  selection-ba\
ckground-color: \
transparent;\x0a  c\
olor: transparen\
t;\x0a  selection-c\
olor: transparen\
t;\x0a  /* Needed t\
o remove indicat\
or - fix #132 */\
\x0a}\x0a\x0aQComboBox::i\
ndicator:alterna\
te {\x0a  backgroun\
d: #19232D;\x0a}\x0a\x0aQ\
ComboBox::item:a\
lternate {\x0a  bac\
kground: #19232D\
;\x0a}\x0a\x0aQComboBox::\
item:checked {\x0a \
 font-weight: bo\
ld;\x0a}\x0a\x0aQComboBox\
::item:selected \
{\x0a  border: 0px \
solid transparen\
t;\x0a}\x0a\x0aQComboBox:\
:drop-down {\x0a  s\
ubcontrol-origin\
: padding;\x0a  sub\
control-position\
: top right;\x0a  w\
idth: 20px;\x0a  bo\
rder-left-width:\
 0px;\x0a  border-l\
eft-color: #3241\
4B;\x0a  border-lef\
t-style: solid;\x0a\
  border-top-rig\
ht-radius: 3px;\x0a\
  border-bottom-\
right-radius: 3p\
x;\x0a}\x0a\x0aQComboBox:\
:down-arrow {\x0a  \
image: url(\x22:/qs\
s_icons/rc/arrow\
_down_disabled.p\
ng\x22);\x0a  height: \
12px;\x0a  width: 1\
2px;\x0a}\x0a\x0aQComboBo\
x::down-arrow:on\
, QComboBox::dow\
n-arrow:hover, Q\
ComboBox::down-a\
rrow:focus {\x0a  i\
mage: url(\x22:/qss\
_icons/rc/arrow_\
down.png\x22);\x0a}\x0a\x0a/\
* QSlider ------\
----------------\
----------------\
----------------\
----------\x0a\x0ahttp\
s://doc.qt.io/qt\
-5/stylesheet-ex\
amples.html#cust\
omizing-qslider\x0a\
\x0a---------------\
----------------\
----------------\
----------------\
------------ */\x0a\
QSlider:disabled\
 {\x0a  background:\
 #19232D;\x0a}\x0a\x0aQSl\
ider:focus {\x0a  b\
order: none;\x0a}\x0a\x0a\
QSlider::groove:\
horizontal {\x0a  b\
ackground: #3241\
4B;\x0a  border: 1p\
x solid #32414B;\
\x0a  height: 4px;\x0a\
  margin: 0px;\x0a \
 border-radius: \
4px;\x0a}\x0a\x0aQSlider:\
:groove:vertical\
 {\x0a  background:\
 #32414B;\x0a  bord\
er: 1px solid #3\
2414B;\x0a  width: \
4px;\x0a  margin: 0\
px;\x0a  border-rad\
ius: 4px;\x0a}\x0a\x0aQSl\
ider::add-page:v\
ertical {\x0a  back\
ground: #1464A0;\
\x0a  border: 1px s\
olid #32414B;\x0a  \
width: 4px;\x0a  ma\
rgin: 0px;\x0a  bor\
der-radius: 4px;\
\x0a}\x0a\x0aQSlider::add\
-page:vertical :\
disabled {\x0a  bac\
kground: #14506E\
;\x0a}\x0a\x0aQSlider::su\
b-page:horizonta\
l {\x0a  background\
: #1464A0;\x0a  bor\
der: 1px solid #\
32414B;\x0a  height\
: 4px;\x0a  margin:\
 0px;\x0a  border-r\
adius: 4px;\x0a}\x0a\x0aQ\
Slider::sub-page\
:horizontal:disa\
bled {\x0a  backgro\
und: #14506E;\x0a}\x0a\
\x0aQSlider::handle\
:horizontal {\x0a  \
background: #787\
878;\x0a  border: 1\
px solid #32414B\
;\x0a  width: 8px;\x0a\
  height: 8px;\x0a \
 margin: -8px 0p\
x;\x0a  border-radi\
us: 4px;\x0a}\x0a\x0aQSli\
der::handle:hori\
zontal:hover {\x0a \
 background: #14\
8CD2;\x0a  border: \
1px solid #148CD\
2;\x0a}\x0a\x0aQSlider::h\
andle:vertical {\
\x0a  background: #\
787878;\x0a  border\
: 1px solid #324\
14B;\x0a  width: 8p\
x;\x0a  height: 8px\
;\x0a  margin: 0 -8\
px;\x0a  border-rad\
ius: 4px;\x0a}\x0a\x0aQSl\
ider::handle:ver\
tical:hover {\x0a  \
background: #148\
CD2;\x0a  border: 1\
px solid #148CD2\
;\x0a}\x0a\x0a/* QLineEdi\
t --------------\
----------------\
----------------\
----------------\
\x0a\x0ahttps://doc.qt\
.io/qt-5/stylesh\
eet-examples.htm\
l#customizing-ql\
ineedit\x0a\x0a-------\
----------------\
----------------\
----------------\
----------------\
---- */\x0aQLineEdi\
t {\x0a  background\
-color: #19232D;\
\x0a  padding-top: \
2px;\x0a  /* This Q\
LineEdit fix  10\
3, 111 */\x0a  padd\
ing-bottom: 2px;\
\x0a  /* This QLine\
Edit fix  103, 1\
11 */\x0a  padding-\
left: 4px;\x0a  pad\
ding-right: 4px;\
\x0a  border-style:\
 solid;\x0a  border\
: 1px solid #324\
14B;\x0a  border-ra\
dius: 4px;\x0a  col\
or: #F0F0F0;\x0a}\x0a\x0a\
QLineEdit:disabl\
ed {\x0a  backgroun\
d-color: #19232D\
;\x0a  color: #7878\
78;\x0a}\x0a\x0aQLineEdit\
:hover {\x0a  borde\
r: 1px solid #14\
8CD2;\x0a  color: #\
F0F0F0;\x0a}\x0a\x0aQLine\
Edit:selected {\x0a\
  background: #1\
464A0;\x0a  color: \
#32414B;\x0a}\x0a\x0a/* Q\
TabWiget -------\
----------------\
----------------\
----------------\
-------\x0a\x0ahttps:/\
/doc.qt.io/qt-5/\
stylesheet-examp\
les.html#customi\
zing-qtabwidget-\
and-qtabbar\x0a\x0a---\
----------------\
----------------\
----------------\
----------------\
-------- */\x0aQTab\
Widget {\x0a  paddi\
ng: 2px;\x0a  selec\
tion-background-\
color: #32414B;\x0a\
  /* Add wanted \
borders - fix #1\
41, #126, #123 *\
/\x0a}\x0a\x0aQTabWidget \
QWidget {\x0a  bord\
er: 0px solid #3\
2414B;\x0a}\x0a\x0aQTabWi\
dget QWidget QWi\
dget\x0aQTableView,\
\x0aQTabWidget QTre\
eView,\x0aQTabWidge\
t QListView,\x0aQTa\
bWidget QGroupBo\
x,\x0aQTabWidget QL\
ineEdit,\x0aQTabWid\
get QComboBox,\x0aQ\
TabWidget QFontC\
omboBox,\x0aQTabWid\
get QTextEdit,\x0aQ\
TabWidget QSpinB\
ox,\x0aQTabWidget Q\
DoubleSpinBox {\x0a\
  border: 1px so\
lid #32414B;\x0a}\x0a\x0a\
QTabWidget::pane\
 {\x0a  border: 1px\
 solid #32414B;\x0a\
  border-radius:\
 4px;\x0a  margin: \
0px;\x0a  /* Fixes \
double border in\
side pane wit py\
qt5 */\x0a  padding\
: 0px;\x0a}\x0a\x0aQTabWi\
dget::pane:selec\
ted {\x0a  backgrou\
nd-color: #32414\
B;\x0a  border: 1px\
 solid #1464A0;\x0a\
}\x0a\x0a/* QTabBar --\
----------------\
----------------\
----------------\
--------------\x0a\x0a\
https://doc.qt.i\
o/qt-5/styleshee\
t-examples.html#\
customizing-qtab\
widget-and-qtabb\
ar\x0a\x0a------------\
----------------\
----------------\
----------------\
--------------- \
*/\x0aQTabBar {\x0a  q\
property-drawBas\
e: 0;\x0a  border-r\
adius: 4px;\x0a  ma\
rgin: 0px;\x0a  pad\
ding: 2px;\x0a  bor\
der: 0;\x0a  /* lef\
t: 5px; move to \
the right by 5px\
 - removed for f\
ix */\x0a}\x0a\x0aQTabBar\
::close-button {\
\x0a  border: 0;\x0a  \
margin: 2px;\x0a  p\
adding: 2px;\x0a  i\
mage: url(\x22:/qss\
_icons/rc/window\
_close.png\x22);\x0a}\x0a\
\x0aQTabBar::close-\
button:hover {\x0a \
 image: url(\x22:/q\
ss_icons/rc/wind\
ow_close_focus.p\
ng\x22);\x0a}\x0a\x0aQTabBar\
::close-button:p\
ressed {\x0a  image\
: url(\x22:/qss_ico\
ns/rc/window_clo\
se_pressed.png\x22)\
;\x0a}\x0a\x0a/* QTabBar:\
:tab - selected \
----------------\
----------------\
----------------\
\x0a\x0ahttps://doc.qt\
.io/qt-5/stylesh\
eet-examples.htm\
l#customizing-qt\
abwidget-and-qta\
bbar\x0a\x0a----------\
----------------\
----------------\
----------------\
----------------\
- */\x0aQTabBar::ta\
b {\x0a  /* !select\
ed and disabled \
----------------\
----------------\
--------- */\x0a  /\
* selected -----\
----------------\
----------------\
----------------\
-- */\x0a}\x0a\x0aQTabBar\
::tab:top:select\
ed:disabled {\x0a  \
border-bottom: 3\
px solid #14506E\
;\x0a  color: #7878\
78;\x0a  background\
-color: #32414B;\
\x0a}\x0a\x0aQTabBar::tab\
:bottom:selected\
:disabled {\x0a  bo\
rder-top: 3px so\
lid #14506E;\x0a  c\
olor: #787878;\x0a \
 background-colo\
r: #32414B;\x0a}\x0a\x0aQ\
TabBar::tab:left\
:selected:disabl\
ed {\x0a  border-ri\
ght: 3px solid #\
14506E;\x0a  color:\
 #787878;\x0a  back\
ground-color: #3\
2414B;\x0a}\x0a\x0aQTabBa\
r::tab:right:sel\
ected:disabled {\
\x0a  border-left: \
3px solid #14506\
E;\x0a  color: #787\
878;\x0a  backgroun\
d-color: #32414B\
;\x0a}\x0a\x0aQTabBar::ta\
b:top:!selected:\
disabled {\x0a  bor\
der-bottom: 3px \
solid #19232D;\x0a \
 color: #787878;\
\x0a  background-co\
lor: #19232D;\x0a}\x0a\
\x0aQTabBar::tab:bo\
ttom:!selected:d\
isabled {\x0a  bord\
er-top: 3px soli\
d #19232D;\x0a  col\
or: #787878;\x0a  b\
ackground-color:\
 #19232D;\x0a}\x0a\x0aQTa\
bBar::tab:left:!\
selected:disable\
d {\x0a  border-rig\
ht: 3px solid #1\
9232D;\x0a  color: \
#787878;\x0a  backg\
round-color: #19\
232D;\x0a}\x0a\x0aQTabBar\
::tab:right:!sel\
ected:disabled {\
\x0a  border-left: \
3px solid #19232\
D;\x0a  color: #787\
878;\x0a  backgroun\
d-color: #19232D\
;\x0a}\x0a\x0aQTabBar::ta\
b:top:!selected \
{\x0a  border-botto\
m: 2px solid #19\
232D;\x0a  margin-t\
op: 2px;\x0a}\x0a\x0aQTab\
Bar::tab:bottom:\
!selected {\x0a  bo\
rder-top: 2px so\
lid #19232D;\x0a  m\
argin-bottom: 3p\
x;\x0a}\x0a\x0aQTabBar::t\
ab:left:!selecte\
d {\x0a  border-lef\
t: 2px solid #19\
232D;\x0a  margin-r\
ight: 2px;\x0a}\x0a\x0aQT\
abBar::tab:right\
:!selected {\x0a  b\
order-right: 2px\
 solid #19232D;\x0a\
  margin-left: 2\
px;\x0a}\x0a\x0aQTabBar::\
tab:top {\x0a  back\
ground-color: #3\
2414B;\x0a  color: \
#F0F0F0;\x0a  margi\
n-left: 2px;\x0a  p\
adding-left: 4px\
;\x0a  padding-righ\
t: 4px;\x0a  paddin\
g-top: 2px;\x0a  pa\
dding-bottom: 2p\
x;\x0a  min-width: \
5px;\x0a  border-bo\
ttom: 3px solid \
#32414B;\x0a  borde\
r-top-left-radiu\
s: 3px;\x0a  border\
-top-right-radiu\
s: 3px;\x0a}\x0a\x0aQTabB\
ar::tab:top:sele\
cted {\x0a  backgro\
und-color: #505F\
69;\x0a  color: #F0\
F0F0;\x0a  border-b\
ottom: 3px solid\
 #1464A0;\x0a  bord\
er-top-left-radi\
us: 3px;\x0a  borde\
r-top-right-radi\
us: 3px;\x0a}\x0a\x0aQTab\
Bar::tab:top:!se\
lected:hover {\x0a \
 border: 1px sol\
id #148CD2;\x0a  bo\
rder-bottom: 3px\
 solid #148CD2;\x0a\
  padding: 0px;\x0a\
}\x0a\x0aQTabBar::tab:\
bottom {\x0a  color\
: #F0F0F0;\x0a  bor\
der-top: 3px sol\
id #32414B;\x0a  ba\
ckground-color: \
#32414B;\x0a  margi\
n-left: 2px;\x0a  p\
adding-left: 4px\
;\x0a  padding-righ\
t: 4px;\x0a  paddin\
g-top: 2px;\x0a  pa\
dding-bottom: 2p\
x;\x0a  border-bott\
om-left-radius: \
3px;\x0a  border-bo\
ttom-right-radiu\
s: 3px;\x0a  min-wi\
dth: 5px;\x0a}\x0a\x0aQTa\
bBar::tab:bottom\
:selected {\x0a  co\
lor: #F0F0F0;\x0a  \
background-color\
: #505F69;\x0a  bor\
der-top: 3px sol\
id #1464A0;\x0a  bo\
rder-bottom-left\
-radius: 3px;\x0a  \
border-bottom-ri\
ght-radius: 3px;\
\x0a}\x0a\x0aQTabBar::tab\
:bottom:!selecte\
d:hover {\x0a  bord\
er: 1px solid #1\
48CD2;\x0a  border-\
top: 3px solid #\
148CD2;\x0a  paddin\
g: 0px;\x0a}\x0a\x0aQTabB\
ar::tab:left {\x0a \
 color: #F0F0F0;\
\x0a  background-co\
lor: #32414B;\x0a  \
margin-top: 2px;\
\x0a  padding-left:\
 2px;\x0a  padding-\
right: 2px;\x0a  pa\
dding-top: 4px;\x0a\
  padding-bottom\
: 4px;\x0a  border-\
top-left-radius:\
 3px;\x0a  border-b\
ottom-left-radiu\
s: 3px;\x0a  min-he\
ight: 5px;\x0a}\x0a\x0aQT\
abBar::tab:left:\
selected {\x0a  col\
or: #F0F0F0;\x0a  b\
ackground-color:\
 #505F69;\x0a  bord\
er-right: 3px so\
lid #1464A0;\x0a}\x0a\x0a\
QTabBar::tab:lef\
t:!selected:hove\
r {\x0a  border: 1p\
x solid #148CD2;\
\x0a  border-right:\
 3px solid #148C\
D2;\x0a  padding: 0\
px;\x0a}\x0a\x0aQTabBar::\
tab:right {\x0a  co\
lor: #F0F0F0;\x0a  \
background-color\
: #32414B;\x0a  mar\
gin-top: 2px;\x0a  \
padding-left: 2p\
x;\x0a  padding-rig\
ht: 2px;\x0a  paddi\
ng-top: 4px;\x0a  p\
adding-bottom: 4\
px;\x0a  border-top\
-right-radius: 3\
px;\x0a  border-bot\
tom-right-radius\
: 3px;\x0a  min-hei\
ght: 5px;\x0a}\x0a\x0aQTa\
bBar::tab:right:\
selected {\x0a  col\
or: #F0F0F0;\x0a  b\
ackground-color:\
 #505F69;\x0a  bord\
er-left: 3px sol\
id #1464A0;\x0a}\x0a\x0aQ\
TabBar::tab:righ\
t:!selected:hove\
r {\x0a  border: 1p\
x solid #148CD2;\
\x0a  border-left: \
3px solid #148CD\
2;\x0a  padding: 0p\
x;\x0a}\x0a\x0aQTabBar QT\
oolButton {\x0a  /*\
 Fixes #136 */\x0a \
 background-colo\
r: #32414B;\x0a  he\
ight: 12px;\x0a  wi\
dth: 12px;\x0a}\x0a\x0aQT\
abBar QToolButto\
n::left-arrow:en\
abled {\x0a  image:\
 url(\x22:/qss_icon\
s/rc/arrow_left.\
png\x22);\x0a}\x0a\x0aQTabBa\
r QToolButton::l\
eft-arrow:disabl\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/arrow_left_dis\
abled.png\x22);\x0a}\x0a\x0a\
QTabBar QToolBut\
ton::right-arrow\
:enabled {\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/arrow_ri\
ght.png\x22);\x0a}\x0a\x0aQT\
abBar QToolButto\
n::right-arrow:d\
isabled {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/arrow_rig\
ht_disabled.png\x22\
);\x0a}\x0a\x0a/* QDockWi\
get ------------\
----------------\
----------------\
----------------\
-\x0a\x0a-------------\
----------------\
----------------\
----------------\
-------------- *\
/\x0aQDockWidget {\x0a\
  outline: 1px s\
olid #32414B;\x0a  \
background-color\
: #19232D;\x0a  bor\
der: 1px solid #\
32414B;\x0a  border\
-radius: 4px;\x0a  \
titlebar-close-i\
con: url(\x22:/qss_\
icons/rc/window_\
close.png\x22);\x0a  t\
itlebar-normal-i\
con: url(\x22:/qss_\
icons/rc/window_\
undock.png\x22);\x0a}\x0a\
\x0aQDockWidget::ti\
tle {\x0a  /* Bette\
r size for title\
 bar */\x0a  paddin\
g: 6px;\x0a  border\
: none;\x0a  backgr\
ound-color: #324\
14B;\x0a}\x0a\x0aQDockWid\
get::close-butto\
n {\x0a  background\
-color: #32414B;\
\x0a  border-radius\
: 4px;\x0a  border:\
 none;\x0a}\x0a\x0aQDockW\
idget::close-but\
ton:hover {\x0a  im\
age: url(\x22:/qss_\
icons/rc/window_\
close_hover.png\x22\
);\x0a}\x0a\x0aQDockWidge\
t::close-button:\
pressed {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/window_cl\
ose_pressed.png\x22\
);\x0a}\x0a\x0aQDockWidge\
t::float-button \
{\x0a  background-c\
olor: #32414B;\x0a \
 border-radius: \
4px;\x0a  border: n\
one;\x0a}\x0a\x0aQDockWid\
get::float-butto\
n:hover {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/window_un\
dock_focus.png\x22)\
;\x0a}\x0a\x0aQDockWidget\
::float-button:p\
ressed {\x0a  image\
: url(\x22:/qss_ico\
ns/rc/window_und\
ock_pressed.png\x22\
);\x0a}\x0a\x0a/* QTreeVi\
ew QListView QTa\
bleView --------\
----------------\
----------------\
-\x0a\x0ahttps://doc.q\
t.io/qt-5/styles\
heet-examples.ht\
ml#customizing-q\
treeview\x0ahttps:/\
/doc.qt.io/qt-5/\
stylesheet-examp\
les.html#customi\
zing-qlistview\x0ah\
ttps://doc.qt.io\
/qt-5/stylesheet\
-examples.html#c\
ustomizing-qtabl\
eview\x0a\x0a---------\
----------------\
----------------\
----------------\
----------------\
-- */\x0aQTreeView:\
branch:selected,\
 QTreeView:branc\
h:hover {\x0a  back\
ground: url(\x22:/q\
ss_icons/rc/tran\
sparent.png\x22);\x0a}\
\x0a\x0aQTreeView:bran\
ch:has-siblings:\
!adjoins-item {\x0a\
  border-image: \
url(\x22:/qss_icons\
/rc/branch_line.\
png\x22) 0;\x0a}\x0a\x0aQTre\
eView:branch:has\
-siblings:adjoin\
s-item {\x0a  borde\
r-image: url(\x22:/\
qss_icons/rc/bra\
nch_more.png\x22) 0\
;\x0a}\x0a\x0aQTreeView:b\
ranch:!has-child\
ren:!has-sibling\
s:adjoins-item {\
\x0a  border-image:\
 url(\x22:/qss_icon\
s/rc/branch_end.\
png\x22) 0;\x0a}\x0a\x0aQTre\
eView:branch:has\
-children:!has-s\
iblings:closed, \
QTreeView:branch\
:closed:has-chil\
dren:has-sibling\
s {\x0a  border-ima\
ge: none;\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/branch_cl\
osed.png\x22);\x0a}\x0a\x0aQ\
TreeView:branch:\
open:has-childre\
n:!has-siblings,\
 QTreeView:branc\
h:open:has-child\
ren:has-siblings\
 {\x0a  border-imag\
e: none;\x0a  image\
: url(\x22:/qss_ico\
ns/rc/branch_ope\
n.png\x22);\x0a}\x0a\x0aQTre\
eView:branch:has\
-children:!has-s\
iblings:closed:h\
over, QTreeView:\
branch:closed:ha\
s-children:has-s\
iblings:hover {\x0a\
  image: url(\x22:/\
qss_icons/rc/bra\
nch_closed_focus\
.png\x22);\x0a}\x0a\x0aQTree\
View:branch:open\
:has-children:!h\
as-siblings:hove\
r, QTreeView:bra\
nch:open:has-chi\
ldren:has-siblin\
gs:hover {\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/branch_o\
pen_focus.png\x22);\
\x0a}\x0a\x0aQTreeView::i\
ndicator:checked\
,\x0aQListView::ind\
icator:checked {\
\x0a  image: url(\x22:\
/qss_icons/rc/ch\
eckbox_checked.p\
ng\x22);\x0a}\x0a\x0aQTreeVi\
ew::indicator:ch\
ecked:hover, QTr\
eeView::indicato\
r:checked:focus,\
 QTreeView::indi\
cator:checked:pr\
essed,\x0aQListView\
::indicator:chec\
ked:hover,\x0aQList\
View::indicator:\
checked:focus,\x0aQ\
ListView::indica\
tor:checked:pres\
sed {\x0a  image: u\
rl(\x22:/qss_icons/\
rc/checkbox_chec\
ked_focus.png\x22);\
\x0a}\x0a\x0aQTreeView::i\
ndicator:uncheck\
ed,\x0aQListView::i\
ndicator:uncheck\
ed {\x0a  image: ur\
l(\x22:/qss_icons/r\
c/checkbox_unche\
cked.png\x22);\x0a}\x0a\x0aQ\
TreeView::indica\
tor:unchecked:ho\
ver, QTreeView::\
indicator:unchec\
ked:focus, QTree\
View::indicator:\
unchecked:presse\
d,\x0aQListView::in\
dicator:unchecke\
d:hover,\x0aQListVi\
ew::indicator:un\
checked:focus,\x0aQ\
ListView::indica\
tor:unchecked:pr\
essed {\x0a  image:\
 url(\x22:/qss_icon\
s/rc/checkbox_un\
checked_focus.pn\
g\x22);\x0a}\x0a\x0aQTreeVie\
w::indicator:ind\
eterminate,\x0aQLis\
tView::indicator\
:indeterminate {\
\x0a  image: url(\x22:\
/qss_icons/rc/ch\
eckbox_indetermi\
nate.png\x22);\x0a}\x0a\x0aQ\
TreeView::indica\
tor:indeterminat\
e:hover, QTreeVi\
ew::indicator:in\
determinate:focu\
s, QTreeView::in\
dicator:indeterm\
inate:pressed,\x0aQ\
ListView::indica\
tor:indeterminat\
e:hover,\x0aQListVi\
ew::indicator:in\
determinate:focu\
s,\x0aQListView::in\
dicator:indeterm\
inate:pressed {\x0a\
  image: url(\x22:/\
qss_icons/rc/che\
ckbox_indetermin\
ate_focus.png\x22);\
\x0a}\x0a\x0aQTreeView,\x0aQ\
ListView,\x0aQTable\
View,\x0aQColumnVie\
w {\x0a  background\
-color: #19232D;\
\x0a  border: 1px s\
olid #32414B;\x0a  \
color: #F0F0F0;\x0a\
  gridline-color\
: #32414B;\x0a  bor\
der-radius: 4px;\
\x0a}\x0a\x0aQTreeView:di\
sabled,\x0aQListVie\
w:disabled,\x0aQTab\
leView:disabled,\
\x0aQColumnView:dis\
abled {\x0a  backgr\
ound-color: #192\
32D;\x0a  color: #7\
87878;\x0a}\x0a\x0aQTreeV\
iew:selected,\x0aQL\
istView:selected\
,\x0aQTableView:sel\
ected,\x0aQColumnVi\
ew:selected {\x0a  \
background: #146\
4A0;\x0a  color: #3\
2414B;\x0a}\x0a\x0aQTreeV\
iew::hover,\x0aQLis\
tView::hover,\x0aQT\
ableView::hover,\
\x0aQColumnView::ho\
ver {\x0a  backgrou\
nd-color: #19232\
D;\x0a  border: 1px\
 solid #148CD2;\x0a\
}\x0a\x0aQTreeView::it\
em:pressed,\x0aQLis\
tView::item:pres\
sed,\x0aQTableView:\
:item:pressed,\x0aQ\
ColumnView::item\
:pressed {\x0a  bac\
kground-color: #\
1464A0;\x0a}\x0a\x0aQTree\
View::item:selec\
ted:hover,\x0aQList\
View::item:selec\
ted:hover,\x0aQTabl\
eView::item:sele\
cted:hover,\x0aQCol\
umnView::item:se\
lected:hover {\x0a \
 background: #14\
64A0;\x0a  color: #\
19232D;\x0a}\x0a\x0aQTree\
View::item:selec\
ted:active,\x0aQLis\
tView::item:sele\
cted:active,\x0aQTa\
bleView::item:se\
lected:active,\x0aQ\
ColumnView::item\
:selected:active\
 {\x0a  background-\
color: #1464A0;\x0a\
}\x0a\x0aQTreeView::it\
em:!selected:hov\
er,\x0aQListView::i\
tem:!selected:ho\
ver,\x0aQTableView:\
:item:!selected:\
hover,\x0aQColumnVi\
ew::item:!select\
ed:hover {\x0a  out\
line: 0;\x0a  color\
: #148CD2;\x0a  bac\
kground-color: #\
32414B;\x0a}\x0a\x0aQTabl\
eCornerButton::s\
ection {\x0a  backg\
round-color: #19\
232D;\x0a  border: \
1px transparent \
#32414B;\x0a  borde\
r-radius: 0px;\x0a}\
\x0a\x0a/* QHeaderView\
 ---------------\
----------------\
----------------\
-------------\x0a\x0ah\
ttps://doc.qt.io\
/qt-5/stylesheet\
-examples.html#c\
ustomizing-qhead\
erview\x0a\x0a--------\
----------------\
----------------\
----------------\
----------------\
--- */\x0aQHeaderVi\
ew {\x0a  backgroun\
d-color: #32414B\
;\x0a  border: 0px \
transparent #324\
14B;\x0a  padding: \
0px;\x0a  margin: 0\
px;\x0a  border-rad\
ius: 0px;\x0a}\x0a\x0aQHe\
aderView:disable\
d {\x0a  background\
-color: #32414B;\
\x0a  border: 1px t\
ransparent #3241\
4B;\x0a  padding: 2\
px;\x0a}\x0a\x0aQHeaderVi\
ew::section {\x0a  \
background-color\
: #32414B;\x0a  col\
or: #F0F0F0;\x0a  p\
adding: 2px;\x0a  b\
order-radius: 0p\
x;\x0a  text-align:\
 left;\x0a}\x0a\x0aQHeade\
rView::section:c\
hecked {\x0a  color\
: #F0F0F0;\x0a  bac\
kground-color: #\
1464A0;\x0a}\x0a\x0aQHead\
erView::section:\
checked:disabled\
 {\x0a  color: #787\
878;\x0a  backgroun\
d-color: #14506E\
;\x0a}\x0a\x0aQHeaderView\
::section::horiz\
ontal {\x0a  border\
-left: 1px solid\
 #19232D;\x0a}\x0a\x0aQHe\
aderView::sectio\
n::horizontal::f\
irst, QHeaderVie\
w::section::hori\
zontal::only-one\
 {\x0a  border-left\
: 1px solid #324\
14B;\x0a}\x0a\x0aQHeaderV\
iew::section::ho\
rizontal:disable\
d {\x0a  color: #78\
7878;\x0a}\x0a\x0aQHeader\
View::section::v\
ertical {\x0a  bord\
er-top: 1px soli\
d #19232D;\x0a}\x0a\x0aQH\
eaderView::secti\
on::vertical::fi\
rst, QHeaderView\
::section::verti\
cal::only-one {\x0a\
  border-top: 1p\
x solid #32414B;\
\x0a}\x0a\x0aQHeaderView:\
:section::vertic\
al:disabled {\x0a  \
color: #787878;\x0a\
}\x0a\x0aQHeaderView::\
down-arrow {\x0a  /\
* Those settings\
 (border/width/h\
eight/background\
-color) solve bu\
g */\x0a  /* transp\
arent arrow back\
ground and size \
*/\x0a  background-\
color: #32414B;\x0a\
  height: 12px;\x0a\
  width: 12px;\x0a \
 border-right: 1\
px solid #19232D\
;\x0a  image: url(\x22\
:/qss_icons/rc/a\
rrow_down.png\x22);\
\x0a}\x0a\x0aQHeaderView:\
:up-arrow {\x0a  ba\
ckground-color: \
#32414B;\x0a  heigh\
t: 12px;\x0a  width\
: 12px;\x0a  border\
-right: 1px soli\
d #19232D;\x0a  ima\
ge: url(\x22:/qss_i\
cons/rc/arrow_up\
.png\x22);\x0a}\x0a\x0a/* QT\
oolBox ---------\
----------------\
----------------\
----------------\
-----\x0a\x0ahttps://d\
oc.qt.io/qt-5/st\
ylesheet-example\
s.html#customizi\
ng-qtoolbox\x0a\x0a---\
----------------\
----------------\
----------------\
----------------\
-------- */\x0aQToo\
lBox {\x0a  padding\
: 0px;\x0a  border:\
 0px;\x0a  border: \
1px solid #32414\
B;\x0a}\x0a\x0aQToolBox::\
selected {\x0a  pad\
ding: 0px;\x0a  bor\
der: 2px solid #\
1464A0;\x0a}\x0a\x0aQTool\
Box::tab {\x0a  bac\
kground-color: #\
19232D;\x0a  border\
: 1px solid #324\
14B;\x0a  color: #F\
0F0F0;\x0a  border-\
top-left-radius:\
 4px;\x0a  border-t\
op-right-radius:\
 4px;\x0a}\x0a\x0aQToolBo\
x::tab:disabled \
{\x0a  color: #7878\
78;\x0a}\x0a\x0aQToolBox:\
:tab:selected {\x0a\
  background-col\
or: #505F69;\x0a  b\
order-bottom: 2p\
x solid #1464A0;\
\x0a}\x0a\x0aQToolBox::ta\
b:selected:disab\
led {\x0a  backgrou\
nd-color: #32414\
B;\x0a  border-bott\
om: 2px solid #1\
4506E;\x0a}\x0a\x0aQToolB\
ox::tab:!selecte\
d {\x0a  background\
-color: #32414B;\
\x0a  border-bottom\
: 2px solid #324\
14B;\x0a}\x0a\x0aQToolBox\
::tab:!selected:\
disabled {\x0a  bac\
kground-color: #\
19232D;\x0a}\x0a\x0aQTool\
Box::tab:hover {\
\x0a  border-color:\
 #148CD2;\x0a  bord\
er-bottom: 2px s\
olid #148CD2;\x0a}\x0a\
\x0aQToolBox QScrol\
lArea QWidget QW\
idget {\x0a  paddin\
g: 0px;\x0a  border\
: 0px;\x0a  backgro\
und-color: #1923\
2D;\x0a}\x0a\x0a/* QFrame\
 ---------------\
----------------\
----------------\
----------------\
--\x0a\x0ahttps://doc.\
qt.io/qt-5/style\
sheet-examples.h\
tml#customizing-\
qframe\x0a\x0a--------\
----------------\
----------------\
----------------\
----------------\
--- */\x0a.QFrame {\
\x0a  border-radius\
: 4px;\x0a  border:\
 1px solid #3241\
4B;\x0a}\x0a\x0a.QFrame[f\
rameShape=\x220\x22] {\
\x0a  border-radius\
: 4px;\x0a  border:\
 1px transparent\
 #32414B;\x0a}\x0a\x0a.QF\
rame[height=\x223\x22]\
, .QFrame[width=\
\x223\x22] {\x0a  backgro\
und-color: #1923\
2D;\x0a}\x0a\x0a/* QSplit\
ter ------------\
----------------\
----------------\
----------------\
--\x0a\x0ahttps://doc.\
qt.io/qt-5/style\
sheet-examples.h\
tml#customizing-\
qsplitter\x0a\x0a-----\
----------------\
----------------\
----------------\
----------------\
------ */\x0aQSplit\
ter {\x0a  backgrou\
nd-color: #32414\
B;\x0a  spacing: 0p\
x;\x0a  padding: 0p\
x;\x0a  margin: 0px\
;\x0a}\x0a\x0aQSplitter::\
separator {\x0a  ba\
ckground-color: \
#32414B;\x0a  borde\
r: 0px solid #19\
232D;\x0a  spacing:\
 0px;\x0a  padding:\
 1px;\x0a  margin: \
0px;\x0a}\x0a\x0aQSplitte\
r::separator:hov\
er {\x0a  backgroun\
d-color: #787878\
;\x0a}\x0a\x0aQSplitter::\
separator:horizo\
ntal {\x0a  width: \
5px;\x0a  image: ur\
l(\x22:/qss_icons/r\
c/line_vertical.\
png\x22);\x0a}\x0a\x0aQSplit\
ter::separator:v\
ertical {\x0a  heig\
ht: 5px;\x0a  image\
: url(\x22:/qss_ico\
ns/rc/line_horiz\
ontal.png\x22);\x0a}\x0a\x0a\
/* QDateEdit ---\
----------------\
----------------\
----------------\
-----------\x0a\x0a---\
----------------\
----------------\
----------------\
----------------\
-------- */\x0aQDat\
eEdit {\x0a  select\
ion-background-c\
olor: #1464A0;\x0a \
 border-style: s\
olid;\x0a  border: \
1px solid #32414\
B;\x0a  border-radi\
us: 4px;\x0a  /* Th\
is fixes 103, 11\
1 */\x0a  padding-t\
op: 2px;\x0a  /* Th\
is fixes 103, 11\
1 */\x0a  padding-b\
ottom: 2px;\x0a  pa\
dding-left: 4px;\
\x0a  padding-right\
: 4px;\x0a  min-wid\
th: 10px;\x0a}\x0a\x0aQDa\
teEdit:on {\x0a  se\
lection-backgrou\
nd-color: #1464A\
0;\x0a}\x0a\x0aQDateEdit:\
:drop-down {\x0a  s\
ubcontrol-origin\
: padding;\x0a  sub\
control-position\
: top right;\x0a  w\
idth: 20px;\x0a  bo\
rder-top-right-r\
adius: 3px;\x0a  bo\
rder-bottom-righ\
t-radius: 3px;\x0a}\
\x0a\x0aQDateEdit::dow\
n-arrow {\x0a  imag\
e: url(\x22:/qss_ic\
ons/rc/arrow_dow\
n_disabled.png\x22)\
;\x0a  height: 12px\
;\x0a  width: 12px;\
\x0a}\x0a\x0aQDateEdit::d\
own-arrow:on, QD\
ateEdit::down-ar\
row:hover, QDate\
Edit::down-arrow\
:focus {\x0a  image\
: url(\x22:/qss_ico\
ns/rc/arrow_down\
.png\x22);\x0a}\x0a\x0aQDate\
Edit QAbstractIt\
emView {\x0a  backg\
round-color: #19\
232D;\x0a  border-r\
adius: 4px;\x0a  bo\
rder: 1px solid \
#32414B;\x0a  selec\
tion-background-\
color: #1464A0;\x0a\
}\x0a\x0aQAbstractView\
:hover {\x0a  borde\
r: 1px solid #14\
8CD2;\x0a  color: #\
F0F0F0;\x0a}\x0a\x0aQAbst\
ractView:selecte\
d {\x0a  background\
: #1464A0;\x0a  col\
or: #32414B;\x0a}\x0a\x0a\
PlotWidget {\x0a  /\
* Fix cut labels\
 in plots #134 *\
/\x0a  padding: 0px\
;\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x0a\
\x09$M%\
\x00q\
\x00d\x00a\x00r\x00k\x00s\x00t\x00y\x00l\x00e\
\x00\x09\
\x00(\xad#\
\x00s\
\x00t\x00y\x00l\x00e\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
