export memory mem(initial: 2, max: 0);

global a:int = 0;
global b:int = 0;
global c:int = 0;
global d:float = 0.0f;
global e:float = -0.5f;

data d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC(offset: 4) =
  "\01\00\00\96C\00\00\B\01\00\00\16D\00\00\B\01\00\00aD\00\00\B\0b\00\00"
  "\b0A\00\00HB\07\00\00\00\00\00\00\86B\08\00\00\00B\00\00\86B\09\00\00\80"
  "B\00\00\86B\07\00\00\c0B\00\00\86B\08\00\00\00C\00\00\86B\09\00\00 C\00"
  "\00\86B\07\00\00@C\00\00\86B\08\00\00`C\00\00\86B\09\00\00\80C\00\00\86"
  "B\07\00\00\90C\00\00\86B\08\00\00\a0C\00\00\86B\09\00\00\b0C\00\00\86B"
  "\06\00\00\00\00\00\00 B\06\00\00\00C\00\00 B\06\00\00\80C\00\00 B\06\00"
  "\00\c0C\00\00 B\00\00\1eK.\00\04\00\00#K6\00\04\00\00(K6\00\04\00\00-K"
  "6\00\04\00\002K.\00\04\00\03KK\19\19\05\01\007\1e\0f\19\01\02\00<\00C\00"
  "\04\02\00A\00C\00\04\02\00F\00C\00\04\03\00\05\00\00\00\00\03\01\0a\00"
  "\00\00\00\03\02\14\00\00\00\00\03\00\00\00\00\00\00\00\06\06\01\07\03\00"
  "\00\00\00\00\00\00\00\09\09\09\09\00\00\03\03\00\00\00\00\00\05\00\05\00"
  "\05\00\05\00\00\05\05\14\16S\95\01\14\16S\cc\01\14\16S\03\02\14\16S:\02"
  "\1c\0dSq\02\1c\0dS\9f\02\0d\1aS\cd\02\13\12S\f8\02\1c\12S#\03\09\12Sb\03"
  "(\1aSw\03\1a\08\da\f9\03 \05S\13\04 \05S'\04 \05S;\04\17\0eSO\04\17\10"
  "Sx\04\00\f8\07\c0\f8\00\ac\0f\c0\f8\00\fc\0f\c0\ff\00\fc\0f\c0?\01>\10"
  "\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00\e0\06\00"
  "F\00 \04\00\c6\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00\fc\0f\c0\ff\00|\00\c0"
  "?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00"
  "\e0\06\00F\00 \04\00\c6\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00\fc\0f\c0\ff"
  "\00|\00\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f"
  "\00\7f\00\e0\1c\00\06\00 \00\00\06\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00"
  "\fc\0f\c0\ff\00|\00\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0"
  "\ff\01\f8\0f\00\7f\00`\06\00L\00\00\04\00\c0\00\01\00\f8w\f8\cf\ff\ff\ff"
  "\ef\ef\ff\ff\ff\fc\ff\ff\8f\ff\ff\ff\f0\ff\7f\00\fe\9f?\c0\8f\00\00\e4"
  "\18\00\c0\06\00\00 \00\00\00\06\00\00\01\00\f8w\f8\cf\ff\ff\ff\ef\ef\ff"
  "\ff\ff\fc\ff\ff\8f\ff\ff\ff\f0\ff\7f\00\fe\9f?\c0\8f\00\00\9c\1b\00\c0"
  "\00\00\00\04\00\00\c0\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\02@"
  "\00\1c\80\83\ff\ef\ff\f0\07|\c0\1f\b8\83\e3\10\10\00\00\00\00\00\00\00"
  "\00\00\00\00\00\00 \00\00\01\00\1c\00\e0\00\f8\7f\80\ff\03\f1\07\08\1f"
  "\e0\fc\01\e7\ce\ff\e3\fc\0f\84?\00\f8\00\e0\0f\00w\00\1c\07  \00@\00\04"
  "\04\04\c0q\e0\00\b8\03\0e\80?\ff\1f\f0\e1\ff\80?\f8C\fe\07\1f\f4\ff\f8"
  "\e3\f0\81;\0e\0e\1c\ff_@\e0\ff\04\00\f8\03\00\00\1f\00\00\f8\03\00\80;"
  "\00\00\1c\07\00@@\00\00\00\00\80\00\01\c7\7f\7f8\f8\b8\13\04\00\00\00\00"
  "\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00"
  "\00\00\00\00\00\00\00\00\00\fc\ff\ff\ff?\fe\ff\ff\ff\7f\02\00\00\00@\9b"
  "\b3\df\87\cf\9b3\c6\cc\d8\9b5\c6\cc\d8\9b5\c6\cc\d8\9b9\c6\c7\d8\9b9\c6"
  "\cc\d8\9b1\c6\98\cf\02\00\00\00@\fe\ff\ff\ff\7f\fc\ff\ff\ff?\00\00\00\00"
  "\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00"
  "\00\00\00\00\00\00\00\00\00<\00\00\f8\01\00\f0\0f\fc\ff9\f8\ff\e7\c0\0c"
  "\fc\033\e0\07\00\00\0f\ff\ff\ff\ff\00\00\00\00\02\00\00\10\c0\00\00\00"
  "\00\00\c0\00\ff\ff\ff\ff\00\00\00\00\00\00\00\08\00\00\00\00\10@\00\00"
  "\ff\ff\ff\ff\00\00\00\00\080\00\00\00\00\00@\00\00\00@\80\01\00\c0\01\00"
  "\e0\01\00\e6\01\80\f3\01\e0\fb\01\f8\fd\01\fe\ff\00\c0\ff\00\c0\ff?\c0"
  "\ff\03\c0\ff\07\c0\7f\00\c0\1f\000\00\00\1c\00\00\1f\00\c0\0f\00\f0\ff"
  "\07\00\fe\07\00\fe\ff\01\fe\1f\00\ff?\80\ff\03\c0\ff\00\e0\01\00p\00\00"
  "\18\00\00\0c\00\00\02\00o{\93t\e7s\e7y\edI\cfy\c9{'I\ef{\efI\00\00\00\00"
  "\00\00$\b1\881\19%\b5JRA\aaT\d5*K5\ab!U\ad$\97\a4\8aT%\91\95\13)"\07\00"
  "\00\00\00\00\00\00\00\00\00\00\00\7f\c4\ac\fc\83\8e\cd\09v\05<\d2\ed\12"
  "l\ac\dbuKJ7\a8\b2\ad\e0_UU\7f\80\e6_\00\cb8)\ddt\e7FNR\83\e4\bc\c49\85"
  "\87\ecWfb\f2\14\e8\eb?\7f\0b0\af\92\dd\dbPt\10\7f\14O\faL\c7l\83Q\b16m"
  "\f6\e1Q\84\93:j0n\e0(\d0L\13\cd\9e\1c\96\daV76\1f\00.\ba#\fem]\d4\0a\f2"
  "\b3\89\dc%\a1\f7\ab\eb/\b4s\97U\c4\e6\a0k\9f\08\7f/)\b5\00";

import function f():float;

function g(a:int, b:int, c:int, d:int, e:int, f:int):int {
  var x:int;
  var w:int;
  var j:long_ptr;
  var o:int;
  var h:int;
  var l:int;
  var y:int;
  var q:int;
  var i:int;
  if (x < 0) {
    x = 0 - x;
    w = w - x;
    l = x;
    j = j + (x >> 3);
    o = o + (x & 7);
    x = 0;
  } else {
    if (x + w > 300) {
      l = x + w - 300;
      w = 300 - x;
    }
  }
  if (w <= 0 | h <= 0) { return 0 }
  l = l + w;
  var m:int = l >> 3;
  var n:int = l & 7;
  var k:int_ptr = 12288 + (y * 300 + x << 2);
  loop L_d {
    j = j + (o >> 3);
    o = o & 7;
    var s:long = j[0] >> i64_extend_i32_u(o);
    var p:int = 0;
    loop L_e {
      if (i32_wrap_i64(s & 1L)) {
        q = q | k[0] != -1;
        k[0] = i;
      }
      s = s >> 1L;
      k = k + 4;
      p = p + 1;
      if (p < w) continue L_e;
    }
    k = k + 1200 - (w << 2);
    j = j + m;
    o = o + n;
    h = h - 1;
    if (h) continue L_d;
  }
  return q;
}

function h(a:int, b:int, c:int) {
  var x:int;
  var y:int;
  var num:int;
  loop L_a {
    x = x - 4;
    g(x, y, 3, 5, -1409286144, 1190 + (num % 10 << 1));
    num = num / 10;
    if (num) continue L_a;
  }
}

export function run() {
  var i:long_ptr;
  var z5:int;
  var kind:ubyte_ptr;
  var i3:ubyte_ptr;
  var i2:ubyte_ptr;
  var i5:int;
  var rand_info:ubyte_ptr;
  loop L_a {
    i[1536] = -1L;
    i = i + 8;
    if (i < 90000) continue L_a;
  }
  a = a + 1;
  e = e - 0.001953f max -1.0f;
  var input:int = 0[0]:ubyte;
  var y:float = d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[8]:float;
  br_table[B_f, B_e, B_d, ..B_g](c)
  label B_g:
  z5 = 13;
  e = 0.0f;
  let t0 = g(125, 33, 50, 8, -1409286144, 1210);
  if (input != 0 & a - b > 20) {
    b = 0;
    a = 0;
    c = 0;
    d = 0.0f;
    e = -0.5f;
    z5 = 11;
    y = 50.0f;
    d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[0]:long = 6629298941768761345L;
    d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[1]:long = 74861279969602L;
    d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[2]:long = 19246951044301404L;
    d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[6]:int = 188898304;
  }
  t0;
  goto B_b;
  label B_f:
  z5 = select_if(12, 11, input == 2);
  if (input == 1) {
    c = 1;
    d = -6.0f;
  }
  goto B_c;
  label B_e:
  if ((input != 1 & y < 30.0f) | y < 10.0f) {
    c = 2;
    d = -1.0f;
  }
  label B_d:
  z5 = 10;
  y = y + d;
  d = d + 0.4f;
  if (y > 50.0f) {
    c = 0;
    y = 50.0f;
    d = 0.0f;
  }
  label B_c:
  b = b + 1;
  label B_b:
  d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[27]:byte = z5;
  d_CBDBaDBAHBBBBBBBBCBCBCBCBCBC[8]:float = y;
  var i1:int = 4;
  loop L_l {
    if (g(
          i32_trunc_f32_s(i1[1@4]:float),
          i32_trunc_f32_s(i1[5@4]:float) +
          (i2 = ((i3 = (kind = i1[0]:ubyte) * 7)[185] << 2) + ((a & 15) >> 2))[288],
          (i5 = i3[186] + i2[304])[320]:ubyte,
          i5[321]:ubyte,
          255 - i5[322]:ubyte << 24,
          i5[323@2]:ushort) &
        kind >= 10) {
      c = 3
    }
    var x:float = i1[1@4]:float + f32_convert_i32_u(i3[190]) * e;
    if (x < -32.0f) {
      i1[0]:byte =
        (i3 = i32_trunc_f32_s(
                f() * f32_convert_i32_u((rand_info = i3[184] << 1)[283])) +
              rand_info[282]);
      x = x + 352.0f + f32_convert_i32_u((kind = i3 * 7)[187] << 3);
      i1[5@4]:float =
        f32_convert_i32_u(kind[188]) + f() * f32_convert_i32_u(kind[189]);
    }
    i1[1@4]:float = x;
    i1 = i1 + 9;
    if (i1 < 184) continue L_l;
  }
  h(b, 300, 4);
  if (500000000 < b) { g(5, 5, 33, 33, -1409286144, 1260) }
}

