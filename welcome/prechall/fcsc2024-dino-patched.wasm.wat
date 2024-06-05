(module
  (type (;0;) (func (result f32)))
  (type (;1;) (func (param i32 i32 i32 i32 i32 i32) (result i32)))
  (type (;2;) (func (param i32 i32 i32)))
  (type (;3;) (func))
  (import "Math" "random" (func $f (type 0)))
  (func $g (type 1) (param $x i32) (param $y i32) (param $w i32) (param $h i32) (param $i i32) (param $j i32) (result i32)
    (local $k i32) (local $l i32) (local $m i32) (local $n i32) (local $o i32) (local $p i32) (local $q i32) (local $r i32) (local $s i64)
    local.get $x
    i32.const 0
    i32.lt_s
    if  ;; label = @1
      i32.const 0
      local.get $x
      i32.sub
      local.set $x
      local.get $w
      local.get $x
      i32.sub
      local.set $w
      local.get $x
      local.set $l
      local.get $j
      local.get $x
      i32.const 3
      i32.shr_u
      i32.add
      local.set $j
      local.get $o
      local.get $x
      i32.const 7
      i32.and
      i32.add
      local.set $o
      i32.const 0
      local.set $x
    else
      local.get $x
      local.get $w
      i32.add
      i32.const 300
      i32.gt_s
      if  ;; label = @2
        local.get $x
        local.get $w
        i32.add
        i32.const 300
        i32.sub
        local.set $l
        i32.const 300
        local.get $x
        i32.sub
        local.set $w
      end
    end
    local.get $w
    i32.const 0
    i32.le_s
    local.get $h
    i32.const 0
    i32.le_s
    i32.or
    if  ;; label = @1
      i32.const 0
      return
    end
    local.get $l
    local.get $w
    i32.add
    local.set $l
    local.get $l
    i32.const 3
    i32.shr_u
    local.set $m
    local.get $l
    i32.const 7
    i32.and
    local.set $n
    i32.const 12288
    local.get $y
    i32.const 300
    i32.mul
    local.get $x
    i32.add
    i32.const 2
    i32.shl
    i32.add
    local.set $k
    loop  ;; label = @1
      local.get $j
      local.get $o
      i32.const 3
      i32.shr_u
      i32.add
      local.set $j
      local.get $o
      i32.const 7
      i32.and
      local.set $o
      local.get $j
      i64.load
      local.get $o
      i64.extend_i32_u
      i64.shr_u
      local.set $s
      i32.const 0
      local.set $p
      loop  ;; label = @2
        local.get $s
        i64.const 1
        i64.and
        i32.wrap_i64
        if  ;; label = @3
          local.get $q
          local.get $k
          i32.load
          i32.const -1
          i32.ne
          i32.or
          local.set $q
          local.get $k
          local.get $i
          i32.store
        end
        local.get $s
        i64.const 1
        i64.shr_u
        local.set $s
        local.get $k
        i32.const 4
        i32.add
        local.set $k
        local.get $p
        i32.const 1
        i32.add
        local.tee $p
        local.get $w
        i32.lt_s
        br_if 0 (;@2;)
      end
      local.get $k
      i32.const 1200
      i32.add
      local.get $w
      i32.const 2
      i32.shl
      i32.sub
      local.set $k
      local.get $j
      local.get $m
      i32.add
      local.set $j
      local.get $o
      local.get $n
      i32.add
      local.set $o
      local.get $h
      i32.const 1
      i32.sub
      local.tee $h
      br_if 0 (;@1;)
    end
    local.get $q)
  (func $h (type 2) (param $num i32) (param $x i32) (param $y i32)
    loop  ;; label = @1
      local.get $x
      i32.const 4
      i32.sub
      local.tee $x
      local.get $y
      i32.const 3
      i32.const 5
      i32.const -1409286144
      i32.const 1190
      local.get $num
      i32.const 10
      i32.rem_u
      i32.const 1
      i32.shl
      i32.add
      call $g
      drop
      local.get $num
      i32.const 10
      i32.div_u
      local.tee $num
      br_if 0 (;@1;)
    end)
  (func (;3;) (type 3)
    (local $i i32) (local $i1 i32) (local $input i32) (local $z5 i32) (local $kind i32) (local $i2 i32) (local $i5 i32) (local $i3 i32) (local $rand_info i32) (local $x f32) (local $y f32)
    loop  ;; label = @1
      local.get $i
      i64.const -1
      i64.store offset=12288
      local.get $i
      i32.const 8
      i32.add
      local.tee $i
      i32.const 90000
      i32.lt_s
      br_if 0 (;@1;)
    end
    global.get $a
    i32.const 1
    i32.add
    global.set $a
    global.get $e
    f32.const 0x1p-9 (;=0.00195312;)
    f32.sub
    f32.const -0x1p+0 (;=-1;)
    f32.max
    global.set $e
    i32.const 0
    i32.load8_u
    local.set $input
    i32.const 36
    f32.load
    local.set $y
    block  ;; label = @1
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              block  ;; label = @6
                global.get $c
                br_table 1 (;@5;) 2 (;@4;) 3 (;@3;) 0 (;@6;)
              end
              i32.const 13
              local.set $z5
              f32.const 0x0p+0 (;=0;)
              global.set $e
              i32.const 125
              i32.const 33
              i32.const 50
              i32.const 8
              i32.const -1409286144
              i32.const 1210
              call $g
              local.get $input
              i32.const 0
              i32.ne
              global.get $a
              global.get $b
              i32.sub
              i32.const 20
              i32.gt_u
              i32.and
              if  ;; label = @6
                i32.const 0
                global.set $b
                i32.const 0
                global.set $a
                i32.const 0
                global.set $c
                f32.const 0x0p+0 (;=0;)
                global.set $d
                f32.const -0x1p-1 (;=-0.5;)
                global.set $e
                i32.const 11
                local.set $z5
                f32.const 0x1.9p+5 (;=50;)
                local.set $y
                i32.const 4
                i64.const 6629298941768761345
                i64.store
                i32.const 12
                i64.const 74861279969602
                i64.store
                i32.const 20
                i64.const 19246951044301404
                i64.store
                i32.const 28
                i32.const 188898304
                i32.store
              end
              br 4 (;@1;)
            end
            i32.const 12
            i32.const 11
            local.get $input
            i32.const 2
            i32.eq
            select
            local.set $z5
            local.get $input
            i32.const 1
            i32.eq
            if  ;; label = @5
              i32.const 1
              global.set $c
              f32.const -0x1.8p+2 (;=-6;)
              global.set $d
            end
            br 2 (;@2;)
          end
          local.get $input
          i32.const 1
          i32.ne
          local.get $y
          f32.const 0x1.ep+4 (;=30;)
          f32.lt
          i32.and
          local.get $y
          f32.const 0x1.4p+3 (;=10;)
          f32.lt
          i32.or
          if  ;; label = @4
            i32.const 2
            global.set $c
            f32.const -0x1p+0 (;=-1;)
            global.set $d
          end
        end
        i32.const 10
        local.set $z5
        local.get $y
        global.get $d
        f32.add
        local.set $y
        global.get $d
        f32.const 0x1.99999ap-2 (;=0.4;)
        f32.add
        global.set $d
        local.get $y
        f32.const 0x1.9p+5 (;=50;)
        f32.gt
        if  ;; label = @3
          i32.const 0
          global.set $c
          f32.const 0x1.9p+5 (;=50;)
          local.set $y
          f32.const 0x0p+0 (;=0;)
          global.set $d
        end
      end
      global.get $b
      i32.const 1
      i32.add
      global.set $b
    end
    i32.const 31
    local.get $z5
    i32.store8
    i32.const 36
    local.get $y
    f32.store
    i32.const 4
    local.set $i1
    loop  ;; label = @1
      local.get $i1
      f32.load offset=1
      i32.trunc_f32_s
      local.get $i1
      f32.load offset=5
      i32.trunc_f32_s
      local.get $i1
      i32.load8_u
      local.tee $kind
      i32.const 7
      i32.mul
      local.tee $i3
      i32.load8_u offset=185
      i32.const 2
      i32.shl
      global.get $a
      i32.const 15
      i32.and
      i32.const 2
      i32.shr_u
      i32.add
      local.tee $i2
      i32.load8_u offset=288
      i32.add
      local.get $i3
      i32.load8_u offset=186
      local.get $i2
      i32.load8_u offset=304
      i32.add
      local.tee $i5
      i32.load8_u offset=320
      local.get $i5
      i32.load8_u offset=321
      i32.const 255
      local.get $i5
      i32.load8_u offset=322
      i32.sub
      i32.const 24
      i32.shl
      local.get $i5
      i32.load16_u offset=323
      call $g
      local.get $kind
      i32.const 10
      i32.ge_u
      i32.and
      if  ;; label = @2
		i32.const 3
        global.set $c
      end
      local.get $i1
      f32.load offset=1
      local.get $i3
      i32.load8_u offset=190
      f32.convert_i32_u
      global.get $e
      f32.mul
      f32.add
      local.tee $x
      f32.const -0x1p+5 (;=-32;)
      f32.lt
      if  ;; label = @2
        local.get $i1
        call $f
        local.get $i3
        i32.load8_u offset=184
        i32.const 1
        i32.shl
        local.tee $rand_info
        i32.load8_u offset=283
        f32.convert_i32_u
        f32.mul
        i32.trunc_f32_s
        local.get $rand_info
        i32.load8_u offset=282
        i32.add
        local.tee $i3
        i32.store8
        local.get $x
        f32.const 0x1.6p+8 (;=352;)
        f32.add
        local.get $i3
        i32.const 7
        i32.mul
        local.tee $kind
        i32.load8_u offset=187
        i32.const 3
        i32.shl
        f32.convert_i32_u
        f32.add
        local.set $x
        local.get $i1
        local.get $kind
        i32.load8_u offset=188
        f32.convert_i32_u
        call $f
        local.get $kind
        i32.load8_u offset=189
        f32.convert_i32_u
        f32.mul
        f32.add
        f32.store offset=5
      end
      local.get $i1
      local.get $x
      f32.store offset=1
      local.get $i1
      i32.const 9
      i32.add
      local.tee $i1
      i32.const 184
      i32.lt_s
      br_if 0 (;@1;)
    end
    global.get $b
    i32.const 300
    i32.const 4
    call $h
    i32.const 500000000
    global.get $b
    i32.lt_u
    if  ;; label = @1
      i32.const 5
      i32.const 5
      i32.const 33
      i32.const 33
      i32.const -1409286144
      i32.const 1260
      call $g
      drop
    end)
  (memory (;0;) 2)
  (global $a (mut i32) (i32.const 0))
  (global $b (mut i32) (i32.const 500000000))
  (global $c (mut i32) (i32.const 0))
  (global $d (mut f32) (f32.const 0x0p+0 (;=0;)))
  (global $e (mut f32) (f32.const -0x1p-1 (;=-0.5;)))
  (export "mem" (memory 0))
  (export "run" (func 3))
  (data (;0;) (i32.const 4) "\01\00\00\96C\00\00\5cB\01\00\00\16D\00\00\5cB\01\00\00aD\00\00\5cB\0b\00\00\b0A\00\00HB\07\00\00\00\00\00\00\86B\08\00\00\00B\00\00\86B\09\00\00\80B\00\00\86B\07\00\00\c0B\00\00\86B\08\00\00\00C\00\00\86B\09\00\00 C\00\00\86B\07\00\00@C\00\00\86B\08\00\00`C\00\00\86B\09\00\00\80C\00\00\86B\07\00\00\90C\00\00\86B\08\00\00\a0C\00\00\86B\09\00\00\b0C\00\00\86B\06\00\00\00\00\00\00 B\06\00\00\00C\00\00 B\06\00\00\80C\00\00 B\06\00\00\c0C\00\00 B\00\00\1eK.\00\04\00\00#K6\00\04\00\00(K6\00\04\00\00-K6\00\04\00\002K.\00\04\00\03KK\19\19\05\01\007\1e\0f\19\01\02\00<\00C\00\04\02\00A\00C\00\04\02\00F\00C\00\04\03\00\05\00\00\00\00\03\01\0a\00\00\00\00\03\02\14\00\00\00\00\03\00\00\00\00\00\00\00\06\06\01\07\03\00\00\00\00\00\00\00\00\09\09\09\09\00\00\03\03\00\00\00\00\00\05\00\05\00\05\00\05\00\00\05\05\14\16S\95\01\14\16S\cc\01\14\16S\03\02\14\16S:\02\1c\0dSq\02\1c\0dS\9f\02\0d\1aS\cd\02\13\12S\f8\02\1c\12S#\03\09\12Sb\03(\1aSw\03\1a\08\da\f9\03 \05S\13\04 \05S'\04 \05S;\04\17\0eSO\04\17\10Sx\04\00\f8\07\c0\f8\00\ac\0f\c0\f8\00\fc\0f\c0\ff\00\fc\0f\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00\e0\06\00F\00 \04\00\c6\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00\fc\0f\c0\ff\00|\00\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00\e0\06\00F\00 \04\00\c6\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00\fc\0f\c0\ff\00|\00\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00\e0\1c\00\06\00 \00\00\06\00\00\f8\07\c0\ff\00\ec\0f\c0\ff\00\fc\0f\c0\ff\00|\00\c0?\01>\10\f0\03\c3\ffp\fe\0b\ff?\f0\ff\03\fe\1f\c0\ff\01\f8\0f\00\7f\00`\06\00L\00\00\04\00\c0\00\01\00\f8w\f8\cf\ff\ff\ff\ef\ef\ff\ff\ff\fc\ff\ff\8f\ff\ff\ff\f0\ff\7f\00\fe\9f?\c0\8f\00\00\e4\18\00\c0\06\00\00 \00\00\00\06\00\00\01\00\f8w\f8\cf\ff\ff\ff\ef\ef\ff\ff\ff\fc\ff\ff\8f\ff\ff\ff\f0\ff\7f\00\fe\9f?\c0\8f\00\00\9c\1b\00\c0\00\00\00\04\00\00\c0\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\02@\00\1c\80\83\ff\ef\ff\f0\07|\c0\1f\b8\83\e3\10\10\00\00\00\00\00\00\00\00\00\00\00\00\00 \00\00\01\00\1c\00\e0\00\f8\7f\80\ff\03\f1\07\08\1f\e0\fc\01\e7\ce\ff\e3\fc\0f\84?\00\f8\00\e0\0f\00w\00\1c\07  \00@\00\04\04\04\c0q\e0\00\b8\03\0e\80?\ff\1f\f0\e1\ff\80?\f8C\fe\07\1f\f4\ff\f8\e3\f0\81;\0e\0e\1c\ff_@\e0\ff\04\00\f8\03\00\00\1f\00\00\f8\03\00\80;\00\00\1c\07\00@@\00\00\00\00\80\00\01\c7\7f\7f8\f8\b8\13\04\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\fc\ff\ff\ff?\fe\ff\ff\ff\7f\02\00\00\00@\9b\b3\df\87\cf\9b3\c6\cc\d8\9b5\c6\cc\d8\9b5\c6\cc\d8\9b9\c6\c7\d8\9b9\c6\cc\d8\9b1\c6\98\cf\02\00\00\00@\fe\ff\ff\ff\7f\fc\ff\ff\ff?\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00<\00\00\f8\01\00\f0\0f\fc\ff9\f8\ff\e7\c0\0c\fc\033\e0\07\00\00\0f\ff\ff\ff\ff\00\00\00\00\02\00\00\10\c0\00\00\00\00\00\c0\00\ff\ff\ff\ff\00\00\00\00\00\00\00\08\00\00\00\00\10@\00\00\ff\ff\ff\ff\00\00\00\00\080\00\00\00\00\00@\00\00\00@\80\01\00\c0\01\00\e0\01\00\e6\01\80\f3\01\e0\fb\01\f8\fd\01\fe\ff\00\c0\ff\00\c0\ff?\c0\ff\03\c0\ff\07\c0\7f\00\c0\1f\000\00\00\1c\00\00\1f\00\c0\0f\00\f0\ff\07\00\fe\07\00\fe\ff\01\fe\1f\00\ff?\80\ff\03\c0\ff\00\e0\01\00p\00\00\18\00\00\0c\00\00\02\00o{\93t\e7s\e7y\edI\cfy\c9{'I\ef{\efI\00\00\00\00\00\00$\b1\881\19%\b5JRA\aaT\d5*K5\ab!U\ad$\97\a4\8aT%\91\95\13)\22\07\00\00\00\00\00\00\00\00\00\00\00\00\7f\c4\ac\fc\83\8e\cd\09v\05<\d2\ed\12l\ac\dbuKJ7\a8\b2\ad\e0_UU\7f\80\e6_\00\cb8)\ddt\e7FNR\83\e4\bc\c49\85\87\ecWfb\f2\14\e8\eb?\7f\0b0\af\92\dd\dbPt\10\7f\14O\faL\c7l\83Q\b16m\f6\e1Q\84\93:j0n\e0(\d0L\13\cd\9e\1c\96\daV76\1f\00.\ba#\fem]\d4\0a\f2\b3\89\dc%\a1\f7\ab\eb/\b4s\97U\c4\e6\a0k\9f\08\7f/)\b5\00"))
